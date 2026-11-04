<div align="center">

# HANDOVER.md

**Convention for every agent working with this `HANDOVER.md`:**

Instructions for the **start of a session** can be found under _`## Shift Handoff` in [AGENTS.md](AGENTS.md)_.

**At the end of a session**, carefully read the instructions under _`## Shift Handoff` in [AGENTS.md](AGENTS.md)_ and use the template under _`## Template for a HANDOVER.md-Entry` in [AGENTS.md](AGENTS.md)_ to create a new entry in this file.

**Important:** Do not delete old entries, because they represent the history, like a git log, but in narrative form. If the file becomes too long, move the oldest entries to [HANDOVER_ARCHIVE.md](HANDOVER_ARCHIVE.md) (once there are more than 50 entries).

</div>

---

## 2026-11-04 - GPT-6: Implement Phase 1 assessment notebook

### Session Summary
- Implemented `src/notebooks/001_f_phase_1.ipynb` as a self-contained 25-cell Phase 1 workflow with explicit example configuration, instructions, five required output sections and backlog mapping.
- Implemented all currently feasible code; empirical Phase 1 findings, domain confirmations and P1.18 remain pending populated inputs and researcher review.
- All 16 embedded synthetic checks passed. Isolated code-cell workflows passed for empty sources, populated synthetic sources with exports, populated sources without general exports, and conflicting headers that must block analysis.

### Changes & Findings
- Added field/type/null/key/relationship audits, order-header consistency checks, structural date/code/value reports and an optional price-feasibility screen.
- Added customer-level evidence assignment/exposure tracking, durable pre-exploration role freeze, explicit 24-month/eligibility gates, coverage-aware monthly/quarterly profiles, history/population assessments, focused plots and partial-rejection sensitivity.
- Added decision/open-issue registers, completion review, reproducibility metadata and verified CSV-to-Parquet exports preserving identifiers and missing values.
- Added implementation plan at `docs/superpowers/plans/2026-11-04-phase-1-notebook.md`; no dependency/configuration changes.
- Independent read-only review identified false inactivity after quarantining uncertain orders and role persistence after exploration; both were corrected with regressions.

### End-Session Status
- Branch: `feat/phase-1-data-understanding`; HEAD: `87d2b5d`. No commit or push performed.
- Source notebook remains untracked and has no saved outputs/execution counts. Pre-existing `.gitkeep` deletion and eight untracked Parquet inputs were preserved.
- Notebook schema/code syntax checks and `git diff --check` passed. No project-wide test suite exists. No real extract notebook execution, bootstrap, production access or mirror regeneration occurred.
- Verification used the existing project interpreter and invented fixtures under `/tmp/erp-phase1-work/`; fixture raw-file hashes remained unchanged.

### Next Step
- User reviews notebook settings, supplies populated extracts in their own environment, confirms extraction metadata/coverage, parsing/identifier semantics, eligible reason codes/currency and evidence-use plan, then restarts the kernel and runs the notebook.
- Review generated evidence, enter evidence-linked preparation recommendations and assess all Phase 1 completion criteria before marking P1.18 complete.

### Important Decisions with Justification
- Unknown coverage leaves primary measures undefined; recorded counts/values remain separate. Excluding uncertain headers must not imply zero purchasing, so unresolved development order attribution/eligibility blocks analysis.
- Confirmed analysis persists CSV/Parquet evidence roles before behavioural calculations even when general exports are disabled: later splits cannot silently reserve previously explored customers.
- Scoped export reads CSV fields as strings through DuckDB, restores the explicit Arrow schema and verifies the round trip. The general converter's inferred types could lose leading zeros or reinterpret null-like strings. Seconds-resolution dates are stored losslessly as nanoseconds because Parquet lacks timestamp[s].
- Only P1.01 and P1.02 are checked complete; implementation/synthetic verification of remaining tasks is distinguished from empirical results and private-environment reproduction.

### Gotchas and Pitfalls
- Default settings intentionally block behavioural analysis until dates, currency, reason eligibility, identifier semantics and evidence/exposure confirmations are supplied. General exports default off; a confirmed analysis still writes the mandatory evidence manifest under the configured interim directory.
- Filenames in `SOURCES` and explicit parsing formats must match the user's extracts; changing the config import changes roots, not filenames or ERP semantics.
- Product keys must be unique/non-null before joins. Missing amounts/items/classifications leave affected measures undefined; no annual order-count minimum or automatic currency/unit conversion is imposed.
- Notebook Python mirrors remain user-managed and were not inspected or modified.

### Modified and new Memories
- Updated `core` with the Phase 1 source location and current implementation boundary.
- Updated `conventions` with pre-exploration evidence persistence, unresolved-order gating and schema-preserving export guidance.

### Open or Unresolved
- Data-dependent P1.03–P1.18 outputs, actual extraction coverage, final temporal/suitability rules and Phase 2 recommendations remain pending.
- Discount assignment/overlap/unit feasibility and optional subgroup/quantity exploration remain deferred unless justified by an explicit analytical question.

## 2026-11-04 - GPT-6: Phase 1 feasibility review

### Session Summary
- Reviewed AGENTS.md, the plan, FUUCCE framework, Phase 1 backlog, data documentation, configuration and relevant Serena memories.
- Confirmed that all eight example CSV/Parquet pairs contain zero records and documented columns; the requested notebook is a zero-byte file.
- Implementation is feasible from the schema, but empirical Phase 1 completion requires populated data and user review. User requested assessment first and a pause before implementation.

### Changes & Findings
- No notebook, data, configuration or mirror changes. Added this handover and a Phase 1 backlog status note.
- Empty Parquet fields are strings: future parsing must validate dates/numbers explicitly and preserve identifier semantics.
- Exact observation dates, extraction coverage/filters, prior evidence exposure and unresolved eligibility treatments require explicit inputs or pending decisions.

### End-Session Status
- Branch: `feat/phase-1-data-understanding`; HEAD: `87d2b5d`. No commit or push performed.
- Pre-existing work: deleted notebook `.gitkeep`, untracked empty target notebook and eight untracked Parquet files; preserved.
- Read-only schema/row-count inspection used the project interpreter. No notebook execution or build performed.

### Next Step
- Await the user's response before implementing `src/notebooks/001_f_phase_1.ipynb` against P1.01–P1.18.

### Important Decisions with Justification
- Distinguish complete notebook implementation from empirical phase completion: header-only files cannot establish behavioural findings or preparation recommendations.
- Use `from config.example import CONFIG` with an explanatory comment and configured paths; private production execution remains user-managed.
- Preserve evaluation boundaries before behavioural exploration; do not invent extraction coverage or eligibility semantics.

### Gotchas and Pitfalls
- Missing coverage must not become zero activity; repeated header amounts must be counted once per consistent order, and currencies kept compatible.
- Monthly aggregation and two-to-four annual orders are exploratory orientations, not fixed inclusion requirements.

### Modified and new Memories
- Updated `core` to remove the stale claim that public notebook directories contain only `.gitkeep` placeholders.

### Open or Unresolved
- No Phase 1 checklist task marked complete. Empirical assessment, metadata clarification and final Phase 2 recommendations remain pending.

