# Infra & Deploy Gotchas

Purpose: operational knowledge for the OCI server and deploy pipeline that keeps
getting re-learned the hard way.

**Status:** active · **Last-verified:** 2026-08-09

- Server: OCI 130.61.219.74, SSH key `~/Downloads/ssh-key-2026-03-18.key`, container
  `financial-research-mas`, DB `/data/mas.db`. Staging container shares the prod bot
  token — must run `TELEGRAM_ENABLED=false`.
- **SSH drops during long docker builds** (connection reset by peer, repeatedly).
  Always: `-o ServerAliveInterval=15`, and run rebuilds detached on the server:
  `nohup bash -c 'cd ~/financial-research-mas && docker compose up -d --build' > /tmp/log 2>&1 &`.
- **Interrupted compose recreates leave container-name conflicts**
  ("name already in use by …"). Fix: `docker rm -f` the STALE leftover — check
  `docker ps -a` first; on 2026-07-15 the freshly-started container was removed by
  mistake (brief outage). The conflicting name in the error is not always the one
  to delete.
- `deploy.sh` = rsync (local `.env` OVERWRITES server `.env`) + remote rebuild.
  Never add keys server-side only. deploy.sh can hang silently — targeted
  `scp` of changed files + detached rebuild is the reliable fallback.
- **Langfuse prompts override local code prompts** (`app/prompts.py` edits do nothing
  until pushed via `scripts/push_prompts_to_langfuse.py`, docker cp'd in). Inline
  prompts (e.g. `_DECISION_SYSTEM` in earnings_research.py) are NOT Langfuse-managed —
  safe to edit directly.
- An auto-commit hook commits local repo changes periodically ("auto: <timestamp>") —
  don't be surprised by a clean tree.
- Views (`signals`, `signal_features`) are dropped/recreated on every boot — VIEW
  definition changes need only a container restart, no data migration.
- Kasm Workspaces 1.15.0 also runs on this box (port 8443, Caddy-proxied via
  stillcasting.app:8443) plus GDM — unrelated to MAS but shares resources.
- **Image size:** plain `pip install torch` on aarch64 (torch>=2.4 wheels) pulls
  ~3.5GB of nvidia/triton GPU libs this GPU-less box can't use — was 60% of the
  ~6GB image (2 MAS images = 73% of all image space on the box). Fixed 2026-08-09:
  Dockerfile installs torch from `https://download.pytorch.org/whl/cpu` first.
  The requirements.txt comment "aarch64 wheels are CPU-only" is OBSOLETE — don't
  trust it. HF model cache is volume-mounted (`HF_HOME=/data/hf-cache`) — model
  weights are NOT in the image and survive recreates. Result (2026-08-28): both
  images 1.96GB (layers shared), 11.72GB pruned.
- **Staging compose had `container_name: financial-research-mas`** (same as prod!)
  and NO `TELEGRAM_ENABLED=false` in its .env (flag defaults True → it was polling
  with the prod bot token). Both fixed 2026-08-28: renamed to
  financial-research-mas-staging in its docker-compose.yml, flag appended to .env,
  verified "silent mode" in boot logs. If a staging recreate ever errors with a
  name conflict on the PROD name, check this first.

Related: [[signal-quality]], [[earnings-scoring]]
