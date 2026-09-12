<!-- aistudio:start -->
# AI Studio

- This project was scaffolded with `aistudio`.
- For AI Studio artifact work, use the bundled `aistudio` skill in `.codex/skills/aistudio`.
- Treat `aistudio` prompt output, command help, generated artifact files, and checked-in project examples as the source of truth for artifact structure and supported operations.
- Treat concrete IDs or sample parameter values shown in CLI help, prompts, tests, or checked-in project examples as syntax illustrations only, not as reusable live data.
- Do not inspect unrelated AI Studio framework/app source code, bundled implementation files, or minified assets to infer hidden contracts unless the user explicitly asks for source-level investigation.
- If the CLI and current project files do not make the contract clear, stop and ask instead of reverse-engineering internals.
- Use `aistudio --help` and `aistudio <command> --help` for command syntax.
- Use `aistudio list-workflow-families` and `aistudio list-workflow-products --family <family>` to discover valid workflow create values.
- Use `aistudio do-create-workflow` to create new workflow files.
- Use `aistudio do-save-workflow --file <workflow-file>` only when the user explicitly asks to save/push the workflow to the remote draft. Do not save automatically after local edits. It looks up an existing draft by `workflowCode`, creates it when absent, and patches it when present.
- Use `aistudio do-create-app` to create new local app files.
- Use `aistudio do-save-app --file <app-file>` only when the user explicitly asks to save/push the app to the remote draft application. Do not save automatically after local edits. It looks up an existing draft by `code`, creates it when absent, and patches it when present.
- Use `aistudio do-create-bo` to create new local Business Object files.
- Use `aistudio do-save-bo --file <bo-file>` only when the user explicitly asks to save/push the Business Object to the remote draft. Do not save automatically after local edits. It looks up an existing BO by `objectCode`, creates it when absent, and patches it when present.
- If `aistudio do-save-bo` fails, report the backend error plainly and stop. Do not auto-search for other BOs, speculate about conflicts, or retarget the save unless the user explicitly asks for deeper investigation.
- Use `aistudio get-bo-function-example-guidance` and `aistudio prepare-bo-function-example-inputs` before `aistudio do-fetch-bo-function-example-sample` when a BO GET example needs user-provided values.
- For Business Object GET example/sample fetches, ask the user for required sample input values unless they already provided them explicitly.
- Do not reuse sample parameter values from CLI help, tests, prompts, or checked-in examples.
- Only attempt live discovery of Business Object sample IDs when the user explicitly asks for discovery.
- If `aistudio validate-bo` only reports BO example-input or example-payload issues, do not invent a payload to make validation pass. Ask the user for the missing values instead.
- Only use `illustrative=true` on BO example payload commands when the user explicitly asks for a manual illustrative example.
- When app work references a known local workflow file, prefer reading the local `.wf` from disk for metadata/context instead of saving the workflow just to make it discoverable.
- Do not save a workflow to the server merely to confirm app-side agent metadata when the workflow file is already known locally.
- Use remote workflow search/discovery only when the task truly depends on server-side search results or the user explicitly wants remote discoverability.
- Do not assume `aistudio do-save-workflow` makes a workflow app-searchable. Many app-side workflow discovery paths only return remote `PUBLISHED` workflows with `aiAppsCompatibleFlag = true`.
- For workflow/debugger mutation commands, use `aistudio <command> ... --dry-run` first only when the user wants approval on the exact file diff before writing.
- After approval, rerun the same command without `--dry-run` to apply the change.
- Do not run mutating `aistudio` commands in parallel against the same `.app`, `.wf`, or `.bo` file.
- For a given artifact file, apply mutations serially so each step sees the latest on-disk state. Parallelism is fine only for read-only commands or mutations against different files.
- After each mutating app or workflow command, treat the updated artifact file as the source of truth before issuing the next mutating command.
- For JSON-valued CLI options such as `--metadata-patch`, `--inputs-patch`, and `--changes`, do not inline JSON in a double-quoted shell argument.
- Prefer `@file` JSON input for payloads that contain code, escaped quotes, backslashes, or `$context` references.
- If inline JSON is unavoidable, wrap the full JSON payload in single quotes so embedded `\"\"` and `$...` survive shell parsing.
- When invoking `aistudio` from Python or Node, pass an argv array and avoid shell string construction.
- After workflow mutations that update code-bearing metadata, verify the stored value with `aistudio get-nodes-metadata-by-code`.
- After material workflow changes, run `aistudio validate-workflow --file <workflow-file>` and fix reported issues before considering the workflow done.
- After material app changes, run `aistudio validate-app --file <app-file>` and fix reported issues before considering the app done.
- After material Business Object changes, run `aistudio validate-bo --file <bo-file>` and fix reported issues before considering the Business Object done.
- After material workflow changes, use `aistudio do-modify-workflow-metadata` to keep the workflow name, description, family, product, and `aiAppsCompatibleFlag` current.
- Workflow files live under `src/workflows/*.wf`, one workflow per file.
- App files live under `src/apps/*.app`, one app per file.
- Business Object files live under `src/businessObjects/*.bo`, one BO per file.
- New workflow files default to the lowercased workflow code plus `.wf`, but filenames do not need to match `workflowCode`.
- New app files default to the lowercased app code plus `.app`, but filenames do not need to match `code`.
- New Business Object files default to the lowercased object code plus `.bo`, but filenames do not need to match `objectCode`.
- Do not modify workflow files directly when the CLI supports the operation. Use `aistudio` commands to inspect and change workflows.
- Do not modify app files directly when the CLI supports the operation. Use `aistudio` commands to inspect and change apps.
- Do not modify Business Object files directly when the CLI supports the operation. Use `aistudio` commands to inspect and change Business Objects.
- The on-disk workflow `specification` is JSON, not a JSON string.
- The on-disk app `specification` is JSON, not a JSON string.
- The on-disk Business Object `specification.objectProperties` is JSON, not a JSON string.
- App Builder prompt assets are available through `aistudio get-prompt --name app-vibe-master|app-vibe-plan|app-vibe-actions|app-vibe-templates|app-vibe-widgets`.
- App Builder tool parity commands use the same command names as the App Builder vibe tools and operate on local `.app` files via `--file <app-file>`.
- Debugger sidecars live under `.debug/`.
<!-- aistudio:end -->

## Local Team Memory

- For Confluence access in this workspace, use the `confluence-browser-access` skill and its browser-backed workflow. Do not use Confluence MCP tools.
- When the user refers to `@kh05 team`, use the roster stored in `.codex/memory/kh05-team.md`.
- For KH05 ticket assignment, use `.codex/memory/kh05-repo-ownership-weights.md` and `.codex/memory/kh05-repo-ownership-weights.json` as the local repo ownership model.
- For KH05 product owner, DM, and component ownership lookups, use `.codex/memory/kh05-product-owners.json`; use `.codex/memory/team_ownership_cache.json` when another OFS team lookup is needed.
