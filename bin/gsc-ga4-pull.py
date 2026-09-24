#!/usr/bin/env python3
"""Pull Search Console + GA4 data for stillcasting.app into JSON files.
Usage: python3 gsc-ga4-pull.py OUT_DIR   (needs google-auth + requests; key from wiki/.secrets)
"""
import json, sys, os, datetime as dt, requests, google.auth.transport.requests
from google.oauth2 import service_account
K=os.path.expanduser('~/Documents/wiki/.secrets/gsc-ga4-service-account.json')
SITE='sc-domain:stillcasting.app'; PROP='365602077'
OUT=sys.argv[1]; os.makedirs(OUT, exist_ok=True)
cred=service_account.Credentials.from_service_account_file(K, scopes=['https://www.googleapis.com/auth/webmasters.readonly','https://www.googleapis.com/auth/analytics.readonly'])
cred.refresh(google.auth.transport.requests.Request()); H={'Authorization':'Bearer '+cred.token}
today=dt.date.today(); end=(today-dt.timedelta(days=2)).isoformat(); start='2026-06-01'
def gsc(name, body):
    rows=[]; body=dict(body); body.setdefault('rowLimit',25000); body['startRow']=0
    while True:
        r=requests.post(f'https://www.googleapis.com/webmasters/v3/sites/{SITE}/searchAnalytics/query', headers=H, json=body, timeout=60); r.raise_for_status()
        got=r.json().get('rows',[]); rows+=got
        if len(got)<body['rowLimit']: break
        body['startRow']+=body['rowLimit']
    json.dump(rows, open(f'{OUT}/gsc_{name}.json','w')); print(f'gsc_{name}: {len(rows)} rows'); return rows
gsc('daily', {'startDate':start,'endDate':end,'dimensions':['date']})
gsc('daily_by_device', {'startDate':start,'endDate':end,'dimensions':['date','device']})
gsc('pages_before', {'startDate':'2026-06-20','endDate':'2026-07-13','dimensions':['page']})
gsc('pages_after',  {'startDate':'2026-07-14','endDate':'2026-08-10','dimensions':['page']})
gsc('pages_recent', {'startDate':'2026-08-25','endDate':end,'dimensions':['page']})
gsc('queries_before', {'startDate':'2026-06-20','endDate':'2026-07-13','dimensions':['query']})
gsc('queries_after',  {'startDate':'2026-07-14','endDate':'2026-08-10','dimensions':['query']})
gsc('queries_recent', {'startDate':'2026-08-25','endDate':end,'dimensions':['query']})
gsc('country_before', {'startDate':'2026-06-20','endDate':'2026-07-13','dimensions':['country']})
gsc('country_after',  {'startDate':'2026-07-14','endDate':'2026-08-10','dimensions':['country']})
gsc('page_date', {'startDate':start,'endDate':end,'dimensions':['date','page']})
for t in ('image','video','news','discover'):
    try: gsc(f'daily_{t}', {'startDate':start,'endDate':end,'dimensions':['date'],'type':t})
    except Exception as e: print(f'daily_{t}: {e}')
r=requests.get(f'https://www.googleapis.com/webmasters/v3/sites/{SITE}/sitemaps', headers=H, timeout=60); json.dump(r.json(), open(f'{OUT}/gsc_sitemaps.json','w')); print('sitemaps:', r.status_code)
for i,u in enumerate(['https://stillcasting.app/','https://stillcasting.app/legends','https://stillcasting.app/persons/sylvester-stallone','https://stillcasting.app/titles/the-godfather-1972-movie','https://stillcasting.app/died-this-week']):
    r=requests.post('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect', headers=H, json={'inspectionUrl':u,'siteUrl':SITE}, timeout=60)
    json.dump({'url':u,'status':r.status_code,'body':r.json()}, open(f'{OUT}/gsc_inspect_{i}.json','w')); print('inspect', u, r.status_code)
def ga(name, body):
    r=requests.post(f'https://analyticsdata.googleapis.com/v1beta/properties/{PROP}:runReport', headers=H, json=dict(body, limit=100000), timeout=60); r.raise_for_status()
    d=r.json(); json.dump(d, open(f'{OUT}/ga_{name}.json','w')); print(f'ga_{name}: {d.get("rowCount",0)} rows'); return d
R=[{'startDate':start,'endDate':'yesterday'}]
ga('daily_channel', {'dateRanges':R,'dimensions':[{'name':'date'},{'name':'sessionDefaultChannelGroup'}],'metrics':[{'name':'activeUsers'},{'name':'sessions'},{'name':'newUsers'},{'name':'engagedSessions'},{'name':'averageSessionDuration'}]})
ga('source_medium', {'dateRanges':R,'dimensions':[{'name':'sessionSource'},{'name':'sessionMedium'}],'metrics':[{'name':'activeUsers'},{'name':'sessions'},{'name':'engagedSessions'},{'name':'averageSessionDuration'}]})
ga('hostname', {'dateRanges':R,'dimensions':[{'name':'hostName'}],'metrics':[{'name':'activeUsers'},{'name':'sessions'}]})
ga('direct_profile', {'dateRanges':R,'dimensions':[{'name':'country'},{'name':'deviceCategory'},{'name':'browser'}],'metrics':[{'name':'activeUsers'},{'name':'sessions'},{'name':'engagedSessions'},{'name':'averageSessionDuration'}],'dimensionFilter':{'filter':{'fieldName':'sessionDefaultChannelGroup','stringFilter':{'value':'Direct'}}}})
ga('organic_landing', {'dateRanges':R,'dimensions':[{'name':'landingPage'},{'name':'sessionSource'}],'metrics':[{'name':'sessions'},{'name':'engagedSessions'}],'dimensionFilter':{'filter':{'fieldName':'sessionDefaultChannelGroup','stringFilter':{'value':'Organic Search'}}}})
ga('direct_landing', {'dateRanges':R,'dimensions':[{'name':'landingPage'}],'metrics':[{'name':'sessions'},{'name':'engagedSessions'}],'dimensionFilter':{'filter':{'fieldName':'sessionDefaultChannelGroup','stringFilter':{'value':'Direct'}}}})
ga('pages_top', {'dateRanges':R,'dimensions':[{'name':'pagePath'}],'metrics':[{'name':'screenPageViews'},{'name':'activeUsers'}]})
print('done', OUT)
