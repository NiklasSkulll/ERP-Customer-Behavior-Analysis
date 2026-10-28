<!-- MANUAL -->
<div align="center">

# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

**Instructions for AI agents working on this project:** Keep it brief and follow conventions. See [BACKLOG.md](BACKLOG.md) for open tasks.

## Shift Handoff (ALWAYS read this first)

**Before each new session:** _First_, read this `AGENTS.md`. _Afterward_, read [HANDOVER.md](HANDOVER.md) (the top entry) in its entirety. It contains the status of the last session, the next planned step, decisions made along with their rationale and potential pitfalls. _After that_, consult the [BACKLOG.md](BACKLOG.md) (Task Status) and MCP Serena-Memory files (in [.serena/](.serena/)).

> **Important notes for development:**
>- For notebook-related changes, _edit only_ the source notebooks in [src/notebooks/](src/notebooks/). Python files in [src/raw-notebooks/](src/raw-notebooks/) are _read-only mirrors_ of notebook code. Use them for navigation and inspection only. Never edit, overwrite, regenerate, delete or synchronize these mirror files. Their generation is handled separately by the user. If a mirror differs from its source notebook, treat the notebook as authoritative and report the mismatch.
>- Never inspect, load, search, execute against or modify production data located [src/.notebooks/](src/.notebooks/), [data/data-prd/](data/data-prd/) and [outputs/.exports/](outputs/.exports/). Do not copy production information into chat responses, code examples, documentation, handovers or Serena memories. If a task requires production access, stop and request a synthetic reproduction or data-free specification.

**At the end of the session:** _First_, add a new entry at the top of [HANDOVER.md](HANDOVER.md). A template is provided at the bottom of this `AGENTS.md`. _Afterward_, update the [BACKLOG.md](BACKLOG.md). _At the end_, update relevant Serena memories using its memory operations. Run onboarding only for initial setup or when a deliberate refresh is needed.

</div>

<!-- END MANUAL -->

---

<!-- AUTO-MANAGED: project-description -->
## Overview

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: build-commands -->
## Build & Development Commands

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: architecture -->
## Architecture

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: conventions -->
## Code Conventions

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: patterns -->
## Detected Patterns

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: git-insights -->
## Git Insights

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: best-practices -->
## Best Practices

<!-- END AUTO-MANAGED -->

<!-- MANUAL -->
## Template for a HANDOVER.md-Entry

Copy and paste this template below for the next entry in [HANDOVER.md](HANDOVER.md).

```markdown
## YYYY-MM-DD - <AI model name>: <Short Overview-Title>

### Session Summary
- 2–4 bullets summarizing the goal, outcome, and overall state of the session.

### Changes & Findings
- Implemented ...
- Refactored ...
- Commit `abc1234`: ...
- Investigated X and determined that ...
- Discovered that Y depends on ...

### End-Session Status
- Branch / Push Status / HEAD Hash
- Working Tree Status
- Build Status
- App launchability
- Other conditions relevant to the next session

### Next Step
- Specific, with reference to the backlog or code location.

### Important Decisions with Justification
- What was decided + WHY.
- The "why" is the most important part. The "what" can be read by the successor in the code.

### Gotchas and Pitfalls
- What had to be worked around?
- What else might come as a surprise?

### Modified and new Memories
- Serena / Auto-Memory, with a brief explanation of why it was saved.

### Open or Unresolved
- What's in the backlog, what remains a question mark, what was deliberately postponed.
```
<!-- END MANUAL -->
