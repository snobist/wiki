# OFS repos (local checkouts)

`~/Documents/OFS_REPOS/` — `Last-verified: 2026-09-12` (listing only; contents not yet ingested).
- `app_server` — core C++ app server (`src/app_server`, `mod_app`); main owner Oleksiy Tymofiev.
- `web` — largest tree (50 entries); web frontend.
- `platform-lcm`, `db-updater`, `db-maintenance` (have `AGENTS.md`), `daily-extract`, `daily-extract-scheduler`,
  `content-delivery`, `mobile-data-interface`.
- `cmdb` appears in ownership weights but is not checked out here.
Each has a `README.md`; `db-updater` and `db-maintenance` also carry `AGENTS.md` — read those before touching them.
The daily repo report automation used Git working copies of 10 OFS repos (see [[ofs-automations]]).
Related: [[kh05-team]].
