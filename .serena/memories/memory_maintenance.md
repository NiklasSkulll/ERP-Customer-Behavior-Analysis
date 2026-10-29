# Memory maintenance
- Progressive discovery: `mem:core` is the entry point and links focused memories. Its domain references should explain what information each target provides.
- Keep the existing compact graph for this repository: core, tech_stack, suggested_commands, conventions and task_completion. Add topic folders only when a distinct module needs them.
- References must use a mem: prefix inside backticks, e.g. `mem:tech_stack`. Put discovery guidance in the referring memory, not instructions about when to read a memory inside its own contents.
- Write dense agent notes containing stable, non-obvious facts and invariants that prevent rediscovery. Avoid generic framework advice, quick-read facts, task-local decisions, transient installed-version snapshots and duplicate explanations.
- Verify against authoritative source files and tool configuration. Generated docs/docsite/ pages may contain stale copies of memories or session notes; do not treat them as authoritative evidence.
- Preserve production-data and read-only-mirror boundaries while collecting evidence. Source map and boundaries: `mem:core`.
- Keep session history in HANDOVER.md and task status in BACKLOG.md under the repository workflow, subject to explicit user overrides; do not duplicate them in memory.
- Use Serena memory operations for writes/renames. Renaming updates references; deletion requires explicit authorization. Verify the active project on the specific MCP connection before writing.
- After changes run serena memories check and inspect the report for dangling references; exit status alone is insufficient.
