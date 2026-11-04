# Phase 1 Notebook Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline implementation. User authorised implementation after the feasibility assessment; do not add another approval gate or commit/push.

**Goal:** Implement everything currently possible for P1.01–P1.18 in `src/notebooks/001_f_phase_1.ipynb`, distinguishing executable implementation from empirical completion.

**Architecture:** One authoritative notebook with pure reusable assessment/profile functions, explicit parameters, read-only Parquet sources, structural diagnostics, customer-level evidence separation before exploration, synthetic verification, and configured exports. No raw-notebook mirrors or production inputs are touched. Empty sources are a supported pending state, never fabricated findings.

**Tech Stack:** Existing Python 3.12 environment, pandas, PyArrow, DuckDB, matplotlib, Jupyter notebook format.

**Spec:** `docs/framework/fuucce_framework.md` Phase 1; `docs/project/bachelor_thesis_project_plan.md`; `docs/project/data_description.md`; `BACKLOG.md` P1.01–P1.18 and optional feasibility items; accepted feasibility assessment in HANDOVER.md.

## Global Constraints

- Start with commented `from config.example import CONFIG`; use configured roots. Production execution is user-managed in private copies.
- Edit only source notebooks for notebook implementation. Preserve original extracts and mirrors.
- No annual order-count exclusion, inferred coverage, currency summation across currencies, or repeated order-header amounts.
- Explicit 24-month bounds and evidence-use confirmation precede behavioural exploration. Exposed customers cannot be reserved as untouched evidence.
- Retain unknown/invalid evidence and selection reasons; report provisional rules and incomplete measures.
- Export reusable tables as CSV then Parquet, retaining both and checking values, nulls, identifiers and schema. Use an explicit schema rather than unverified CSV inference.
- Tests use only explicitly generated synthetic fixtures in temporary directories. Saved notebook outputs remain empty.

## Review Focus

- Empty files and malformed/missing columns must yield diagnostics, not false completion.
- Conflicting order headers or duplicate master keys must not multiply order values.
- Missing values and unobserved coverage must not become zero purchasing activity.
- Held-out/exposed evidence and changed split settings must not silently contaminate evaluation.
- Date/numeric parsing, zero-padded identifiers, mixed currencies and CSV null/text ambiguity must remain visible.

### Task 1: Input contract and structural assessment

**Files:** Source notebook; isolated temporary verification harness.

**Interfaces:** `normalise_table(frame, table_name)`, `structural_assessment(tables)`, `order_views(orders)` provide typed data, audits and consistent order/item views.

- [x] Write and run failing synthetic expectations for schema validation, parsing failures, repeated headers, conflicting keys and many-to-one relationships.
- [x] Implement commented config import, input manifest/metadata parameters, explicit parsing, structural diagnostics and order/item integrity.
- [x] Verify empty inputs, leading zeros, invalid values and deduplicated headers against hand-derived expectations.

### Task 2: Evidence boundaries, profiles and exploration

**Interfaces:** Consumes Task 1 typed tables. `assign_evidence`, `select_orders`, `build_profiles`, `history_assessment` return role records, selection audit, customer-period measures and comparison support.

- [x] Write and run failing expectations for customer isolation, known inactivity vs unknown coverage, missing amount/product evidence and mixed currencies.
- [x] Implement explicit 24-month settings, persistent evidence manifest, prior-exposure handling, provisional eligibility, coverage-aware monthly/quarterly profiles, histories and focused displays.
- [x] Verify hand-derived measures, ordering gaps, boundary months, exclusion reasons and sensitivity comparisons on fully synthetic fixtures.

### Task 3: Decisions, export, verification and handover

**Interfaces:** Consumes all prior outputs; `export_table` performs a schema-preserving CSV-to-Parquet round trip; synthetic verification cell exercises the public functions.

- [x] Write failing expectations for round-trip identifiers/nulls and behavioural gating.
- [x] Implement five required output sections, decision/open-issue registers, optional discount feasibility diagnostics, evidence-use record, reproducibility metadata and P1 task mapping.
- [x] Verify code-cell syntax and notebook schema; run isolated empty and populated synthetic workflows plus meaningful regression checks; review the final notebook.
- [x] Update HANDOVER.md first, BACKLOG.md second, relevant Serena memories last. Check only tasks with available evidence; retain empirical completion as pending.

## Execution record

- User requested work in the existing empty notebook on the current feature branch. Work in place to preserve their untracked Parquet inputs and notebook; no setup, dependency or Git configuration changes.
- Temporary verification artifacts and task ledger: `/tmp/erp-phase1-work/`; durable outcomes belong in HANDOVER.md/BACKLOG.md.

## Verification outcome

- 16 embedded synthetic regression checks passed. All notebook code cells passed isolated empty-input, populated/export-enabled, populated/general-exports-disabled and conflicting-header workflows. Raw fixture hashes were unchanged.
- Notebook format/schema and cell syntax are valid; saved outputs/execution counts remain empty. No actual dataset notebook execution or project-wide suite was claimed.
- Independent review found two high-priority issues (false inactivity after header quarantine and late optional evidence persistence). Both were corrected and covered by synthetic checks.
- Empirical suitability, extraction completeness, domain eligibility, final sampling adequacy and discount assignment were not judged because they require later evidence.
