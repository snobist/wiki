#!/usr/bin/env python3
"""GA4 human-traffic summary for stillcasting.app (growth runbook, step 3).

Usage: stillcasting-ga-human.py START END [OUT.json]   (dates YYYY-MM-DD, inclusive)

A session row (channel x country x source x device x browser) is BOT and dropped when:
  1. channel Direct from China / Hong Kong / Singapore (JS-executing scrapers), or
  2. average session duration < 1 s, or
  3. (added 2026-11-04) channel Direct with >= 10 sessions in the row and engagement rate < 10 %
     — real Direct visitors are a handful per country and engage ~50 %; 2026-11-04 Iran 78 / Russia 25
     desktop-Chrome sessions at 1.1–1.6 s with 1 engaged session slipped past rule 2.
"""
import json, sys, collections
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

KEY = '/Users/alexgrtsenko/Documents/wiki/.secrets/gsc-ga4-service-account.json'
PROP = '365602077'
BOT_DIRECT_COUNTRIES = {'China', 'Hong Kong', 'Singapore'}

def is_bot(ch, country, sessions, engaged, dur):
    if ch == 'Direct' and country in BOT_DIRECT_COUNTRIES: return 'direct_cn_hk_sg'
    if dur < 1: return 'under_1s'
    if ch == 'Direct' and sessions >= 10 and engaged / sessions < 0.10: return 'direct_low_engagement'
    return None

def main():
    start, end = sys.argv[1], sys.argv[2]
    s = AuthorizedSession(service_account.Credentials.from_service_account_file(
        KEY, scopes=['https://www.googleapis.com/auth/analytics.readonly']))
    body = {'dateRanges': [{'startDate': start, 'endDate': end}],
            'dimensions': [{'name': n} for n in ['sessionDefaultChannelGroup', 'country', 'sessionSource', 'deviceCategory', 'browser']],
            'metrics': [{'name': n} for n in ['sessions', 'engagedSessions', 'activeUsers', 'averageSessionDuration']],
            'limit': 100000}
    r = s.post(f'https://analyticsdata.googleapis.com/v1beta/properties/{PROP}:runReport', json=body, timeout=60)
    r.raise_for_status(); d = r.json()
    if len(sys.argv) > 3: json.dump(d, open(sys.argv[3], 'w'))
    total = 0; sess = collections.Counter(); eng = collections.Counter(); users = 0
    organic = collections.Counter(); dropped = collections.Counter()
    for row in d.get('rows', []):
        ch, country, src, dev, br = [x['value'] for x in row['dimensionValues']]
        se, en, us, du = [float(x['value']) for x in row['metricValues']]
        total += se
        why = is_bot(ch, country, se, en, du)
        if why: dropped[why] += se; continue
        sess[ch] += se; eng[ch] += en; users += us
        if ch == 'Organic Search': organic[src] += se
    human = sum(sess.values())
    print(f'{start}..{end}  total {int(total)}  human {int(human)}  engaged {int(sum(eng.values()))}  users {int(users)}  bot share {100*(1-human/total if total else 0):.1f} %')
    print('channels (sessions, engaged):', {k: (int(sess[k]), int(eng[k])) for k in sorted(sess, key=lambda k: -sess[k])})
    print('organic by source:', dict(organic.most_common()))
    print('dropped by rule:', {k: int(v) for k, v in dropped.items()})

if __name__ == '__main__':
    main()
