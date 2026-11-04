<div align="center">

# Backlog

This backlog turns the six-phase FUUCCE workflow into ordered, trackable tasks for completing the bachelor's thesis investigation. The project plan defines the scope and evaluation commitments; the framework defines the procedures, required outputs and phase-completion criteria.

</div>

---

Use the [project plan](docs/project/bachelor_thesis_project_plan.md) as the source of truth, the [FUUCCE framework](docs/framework/fuucce_framework.md) as the detailed workflow, and the [data description](docs/project/data_description.md) for source fields and relationships.

Work through the core tasks in order. Task IDs support progress references; check an item only when its output and verification are available. Development may return to earlier phases, but affected decisions and outputs must then be revised and regenerated. Optional refinements are not phase-completion requirements and must not delay the complete core workflow and its evaluation.

Agents implement and verify with fully synthetic fixtures and public source notebooks. Production-dependent inspection, execution and real-case review are user-managed work in the private environment. Do not record production data, derived findings or private case identifiers in this public backlog. Use `CONFIG.data_dir` and `CONFIG.output_dir`, preserve original extracts, and follow the framework's CSV-to-Parquet workflow for reusable tables.

---

## Phase 1 - Familiarise yourself with the data and assess its suitability

**Status (2026-11-04):** Implemented the Phase 1 workflow in `src/notebooks/001_f_phase_1.ipynb`, including empty-input handling, structural audits, fixed evidence roles, provisional profiles, focused exploration, decisions and verified exports. All 16 embedded synthetic checks and four isolated empty/populated/export/conflict workflows passed. P1.01 and P1.02 are complete; P1.03–P1.17 have implementation support but remain unchecked where empirical outputs or actual-input reproduction require populated extracts and review. P1.18 remains pending. The eight example CSV/Parquet pairs still contain no records.

### Inspect the datasets and verify their meaning

- [x] **P1.01** Review the plan, framework and existing data description; confirm the research questions, core measures, 24-month scope and information still needed from the extraction process.
- [x] **P1.02** Create a reproducible source notebook in `src/notebooks/` with the explicit example configuration and synthetic fixtures; establish Parquet loading and configured artifact paths without changing original extracts.
- [ ] **P1.03** Record the available tables, extraction dates, filters, coverage, row/column counts and the entity represented by each row; distinguish documented facts, observed properties, assumptions and unresolved questions.
- [ ] **P1.04** Verify required fields, data types, identifiers, leading-zero semantics, duplicate candidate keys and missing-value placeholders against the data description.
- [ ] **P1.05** Verify table relationships and the distinction between order-level and item-level fields, including how `TOTALNETAMOUNT` can be counted once per order after joins.
- [ ] **P1.06** Assess dates and extraction gaps, order types, processing/rejection statuses, currencies, quantity units and product-group coverage; record unusual values as investigation flags rather than automatically excluding them.

### Reserve evaluation evidence before behavioural exploration

- [ ] **P1.07** Define and document development and final-evaluation boundaries before examining individual behavioural patterns. Start with customer-level separation; justify any temporal alternative and address overlapping observations/windows.
- [ ] **P1.08** Record the evidence assigned to each role, prior exposure and independence limitations. Restrict behavioural exploration and feature, threshold and type decisions to development evidence.

### Assess histories and explore candidate measures

- [ ] **P1.09** Examine development customers' distinct order counts, active periods, first/last observed orders, ordering intervals, inactivity periods, incomplete periods and uncertain extraction coverage within the 24-month window.
- [ ] **P1.10** Propose analytical suitability criteria from comparison support. Treat two to four annual orders only as exploratory orientation; do not impose separate annual minimums or infer acquisition/coverage from first and last orders.
- [ ] **P1.11** Assess feasibility and interpretation of `ORDERCOUNT`, `TOTALORDERVALUE`, `AVGORDERVALUE`, `DISTINCTPRODUCTCOUNT` and `DISTINCTPRODUCTGROUPCOUNT`; identify missingness and dependencies between measures.
- [ ] **P1.12** Build reusable provisional customer-period views using documented eligibility principles; assess monthly aggregation as an initial option rather than a fixed requirement, and record unresolved status-code treatments.
- [ ] **P1.13** Produce focused tables and graphics addressing comparison support, temporal resolution, measure validity, individual large orders and sensitivity to consequential preparation choices; include ordinary and difficult development histories.

### Consolidate outputs and complete the phase

- [ ] **P1.14** Document proposed order/item selection, missing/duplicate-record treatment, candidate measures, temporal representation and customer suitability. Record evidence, rationale and status for each consequential decision.
- [ ] **P1.15** Identify blockers to a trustworthy core analysis and give each a concrete next action; defer unresolved optional requirements explicitly. Keep exploratory patterns distinct from automatic detections and established types.
- [ ] **P1.16** Consolidate the required notebook sections: data assessment, customer-history assessment, focused exploratory findings, preparation decisions/open issues, and the evidence-use record. Save supporting public synthetic artifacts through the example configuration.
- [ ] **P1.17** Verify that the notebook can be reproduced from its declared inputs and that joins, conversions and provisional selection rules are traceable; keep reusable preparation code ready for Phase 2.
- [ ] **P1.18 — Completion check:** Confirm that core data meaning/relationships, quality/coverage limits, measure feasibility, proposed temporal/suitability rules and evaluation boundaries are documented, with explicit preparation recommendations for Phase 2.

### Optional refinements after the core assessment

- [ ] **P1.O1 — Optional:** Assess discount feasibility, including price-condition assignment, validity, quantity compatibility and coverage, without making full discount integration a core requirement.
- [ ] **P1.O2 — Optional:** Explore product-group incidence, compatible quantity measures or customer subgroups only where they answer a specific unresolved analytical question.

---

## Phase 2 - Use ERP data to prepare customer profiles

### Finalise and apply preparation rules

- [ ] **P2.01** Reuse Phase 1 loading/preparation code and resolve blockers affecting core measure meanings; confirm that development/evaluation boundaries remain applicable to the preparation procedure.
- [ ] **P2.02** Fix the exact 24-month start/end dates using `SALESORDERDATE` and document treatment of incomplete periods.
- [ ] **P2.03** Specify eligible combinations of `SALESORDERTYPE`, `OVERALLSDPROCESSSTATUS`, `SDDOCUMENTREASON` and `OVERALLSDDOCUMENTREJECTIONSTS`; exclude fully rejected orders and clarify partial rejection and recorded amounts. Do not reject open orders solely because processing is incomplete.
- [ ] **P2.04** Implement justified treatments for identifiers, dates, duplicates, missing placeholders, currencies and categories. Separate technical corrections from analytical exclusions, preserve leading zeros and retain large orders unless a documented rule excludes them.
- [ ] **P2.05** Record preparation rules, rationale, affected record/customer counts and remaining limitations. Do not infer project-order status from order size or attempt an unsupported project/routine classification.

### Integrate tables and specify measures

- [ ] **P2.06** Construct eligible order-level and item-level views using verified keys; check uniqueness/cardinality, unmatched records, row-count changes and order-count/monetary reconciliation for each consequential join.
- [ ] **P2.07** Retain `TOTALNETAMOUNT` once per eligible `SALESORDER`; aggregate item information before combining levels where needed and use a documented consistent currency basis.
- [ ] **P2.08** Define consistent item eligibility for assortment measures, including rejected items and missing product classifications; retain classification-coverage information.
- [ ] **P2.09** Select a compact feasible set of core measures and maintain a feature specification with meanings, source fields, formulas, units, aggregation bases, missing-value treatments and interpretation limits. Do not require every catalogue measure as a detection input.
- [ ] **P2.10** Implement and check distinct order counts, once-per-order net totals, average order value and selected product/product-group breadth measures. Record mathematical dependencies and avoid interpreting order values as realised revenue.

### Construct profiles and confirm suitability

- [ ] **P2.11** Justify the temporal resolution using Phase 1 evidence and construct one profile row per `CUSTOMERID` and `PERIODSTART`, deriving the customer identifier from `SOLDTOPARTY`.
- [ ] **P2.12** Represent zero counts/totals only where coverage supports observed inactivity; preserve unknown coverage as missing and leave averages/shares undefined when denominators are zero.
- [ ] **P2.13** Retain original units and indicators for partial periods, missing classifications and other consequential quality restrictions. Fit any necessary data-derived transformations on development evidence only.
- [ ] **P2.14** Reassess suitability after preparation; document included/excluded customers, restricted periods/measures and reasons. Allow partial assessability and avoid separate annual minimums or recent-activity requirements that suppress declining histories.

### Verify outputs and complete the phase

- [ ] **P2.15** Verify unique customer-period identifiers, source-to-profile order counts and net totals, feature formulas, missing values and the expected effects of joins/exclusions; inspect selected development profiles against their underlying orders.
- [ ] **P2.16** Export profiles and eligibility/coverage tables as CSV, convert the selected `interim` or `processed` folder with `--folder` (and `--update` when refreshing), and retain/reload Parquet versions. Verify schema, identifiers, missing values and round-trip consistency.
- [ ] **P2.17** Document output schemas, encoding, delimiter, decimal/missing-value representations, input references and configuration; verify reproducible regeneration without altering the original extracts.
- [ ] **P2.18** Consolidate the required deliverables: prepared profiles, eligibility/coverage information, preparation/feature specification, verification results and reproducible preparation code. Resolve discrepancies or record explicit core blockers.
- [ ] **P2.19 — Completion check:** Confirm explicit preparation rules, verified joins/aggregates, documented measures, correct inactivity/missing/undefined distinctions, recorded suitability and reproducible outputs ready for window comparisons.

### Optional refinements after the core dataset

- [ ] **P2.O1 — Optional:** Add product-group order shares, days since last order or compatible-unit quantities where justified; retain appropriate denominators and distinguish unknown preceding history from inactivity.
- [ ] **P2.O2 — Optional:** Integrate discounts only after verifying customer/price-group assignment, validity, price bases and quantity compatibility; retain unmaintained prices as missing and report calculable-item coverage. Preserve a runnable core dataset.

---

## Phase 3 - Uncover and characterise changes

### Specify the comparison design

- [ ] **P3.01** Confirm the prepared profiles, eligibility/coverage restrictions and feature definitions; select development histories and keep reserved evaluation histories out of calibration and detailed inspection.
- [ ] **P3.02** Specify target patterns, detection inputs and additional descriptive measures. Retain time-window profile comparison as the main approach; document any justified replacement and align SQ1 wording if the main approach changes.
- [ ] **P3.03** Define reference/subsequent window lengths, movement, boundaries and incomplete-window treatment. Start with adjacent non-overlapping reference/subsequent windows, and account for dependence between successive rolling comparisons.
- [ ] **P3.04** Define minimum observation, order-activity and coverage support per measure; document restrictions arising from recurring patterns, isolated large orders and changing coverage.

### Implement and calibrate detection

- [ ] **P3.05** Implement comparable feature summaries, using appropriate averages or rates where unequal window lengths would make totals misleading.
- [ ] **P3.06** Specify each measure's comparison statistic, representation of usual variability, minimum change magnitude, evidence requirements and unavailable-comparison treatment. Define whether one dimension or a stated combination triggers a candidate.
- [ ] **P3.07** Handle dependent measures and incompatible units explicitly; justify any scaling, weighting or combined score. Do not count order count, total value and average value as independent corroboration.
- [ ] **P3.08** Calibrate windows and criteria using development cases and, where helpful, separate pilot scenarios. Record parameters and rationale; do not target a desired number of events/types or imply hypothesis-test significance.

### Detect, consolidate and characterise candidates

- [ ] **P3.09** Apply the detector reproducibly and account for qualifying, assessable non-qualifying and unassessable comparisons, retaining reasons and processing counts.
- [ ] **P3.10** Define and implement consolidation of repeated nearby detections, event timing and the comparison windows supplying evidence; preserve original detections and their event links without merging distinct changes merely because they affect the same measure.
- [ ] **P3.11** Create the candidate-event register with stable event/customer identifiers, configuration, reference/subsequent periods, boundary or transition interval, detection criteria, support information and review status.
- [ ] **P3.12** Retain linked before/after values, units, absolute differences and meaningful relative differences; distinguish percentage points from relative percentages and flag zero/small-reference ratios as undefined or unstable.
- [ ] **P3.13** Specify persistence and follow-up assessment, recording observed duration only where supported. Preserve observation boundaries and avoid presenting period-level timing as an exact transaction-level change date.

### Review development evidence and complete the phase

- [ ] **P3.14** Review selected candidates against their orders and development histories for large-order dominance, recurring patterns, incomplete periods, classification/preparation effects, weak support and unclear event boundaries.
- [ ] **P3.15** Run limited development sensitivity checks where they resolve consequential design questions; record decisions separately from the final sensitivity analysis.
- [ ] **P3.16** Assemble a manageable taxonomy-development collection spanning dimensions, directions, magnitudes, combinations, ambiguous cases and selected histories without detections; record selection rationale and event/customer counts.
- [ ] **P3.17** Keep manual observations separate from automatic detections, avoid domination by repeated events from one customer, and retain candidates that do not fit anticipated types. A non-detection is not verified stability.
- [ ] **P3.18** Export/reload the detection specification, candidate register, feature-change evidence, processing summary and development-case collection with enough configuration and provenance to reproduce each event.
- [ ] **P3.19 — Completion check:** Confirm explicit comparison/significance rules, reproducible development execution, consistent handling of unavailable/repeated comparisons, traceable candidate evidence and sufficient or explicitly restricted taxonomy-development material. Revisit earlier decisions if defensible comparisons are impossible.

### Optional refinements after the main detector

- [ ] **P3.O1 — Optional:** Add a behavioural dimension, alternative window design or second detector only for a specific justified limitation and with time for evaluation; preserve disagreements and applicability differences between methods.

---

## Phase 4 - Construct the change taxonomy

### Establish the perspective and review development evidence

- [ ] **P4.01** Confirm the development-event register, feature evidence, manual provenance, quality restrictions, literature and reserved-evidence boundaries; reuse the Phase 3 case collection.
- [ ] **P4.02** Document the taxonomy's purpose, intended readers and organising perspective: observable event-level purchasing changes at the focal wholesaler, rather than permanent customer labels or behavioural causes.
- [ ] **P4.03** Check case coverage across dimensions, directions, combined changes, magnitudes, temporal evidence, activity levels, borderline cases and detector omissions; document selection reasons and event/customer counts without fixing a target type/case count.

### Develop and revise the type structure

- [ ] **P4.04** Propose initial distinctions from supported measures, the organising perspective and conceptual/domain-informed literature; keep dimensions, types, supporting descriptors and evidence statuses separate.
- [ ] **P4.05** Review manageable case batches against histories and before/after evidence; record provisional matches, non-matches, uncertainty and coverage gaps without treating manually observed patterns as automatic detections.
- [ ] **P4.06** Revise redundant, missing or unclear distinctions with documented reasons and reassess affected earlier cases. Keep magnitude, timing and duration as descriptors unless categorical distinctions are justified.
- [ ] **P4.07** Define compatible labels and logical exclusions; add a composite type only for a distinct interpretation with explicit criteria, not for every possible label combination. Specify denominators/representation if composition changes are included.

### Specify the codebook and operational criteria

- [ ] **P4.08** Create each retained type's stable identifier, neutral name, conceptual definition, relevant measures/units/windows, minimum evidence and applicability restrictions.
- [ ] **P4.09** Specify executable assignment conditions, comparison operators, threshold-boundary behaviour, parameters and rationale; keep detection criteria distinct from assignment criteria.
- [ ] **P4.10** Record examples, counterexamples, conceptual sources, compatible/conflicting relationships and limitations. Define met, not-met, insufficient-evidence and not-applicable outcomes without turning evidence statuses into behavioural types.
- [ ] **P4.11** Reuse Phase 3 measurements unless a justified revision is needed; update earlier specifications and regenerate affected evidence when definitions or measurements change. Keep event-level quality concerns separate from numerical type matches.
- [ ] **P4.12** Resolve parameters using development evidence or document narrowly defined Phase 5 calibration tasks and their development-only selection procedure; do not adopt illustrative percentages or durations as established thresholds.

### Check coherence and prepare implementation

- [ ] **P4.13** Review scope, interpretability, measurable distinctions, evidence requirements, rule consistency, compatible combinations and terminology; investigate conceptual gaps separately from missing evidence and out-of-scope patterns.
- [ ] **P4.14** Perform a final development review and resolve conceptual contradictions; retain documented unrepresented cases rather than forcing labels or creating an undefined "other" type. Identify unsupported conceptual extensions separately.
- [ ] **P4.15** Consolidate the taxonomy overview, codebook, development-case record and decision/revision history; export reusable tables with stable links between types, events and revisions.
- [ ] **P4.16** Freeze and version the Phase 5 handover, including codebook/data versions, parameters and bounded calibration tasks; document any remaining provisional scope or evidence restrictions.
- [ ] **P4.17 — Completion check:** Confirm a coherent purpose, clear assessable type definitions, explicit combinations/conflicts, documented insufficient/unrepresented cases and an implementation-ready version. Completion does not require full coverage or a fixed number of types.

### Optional refinements after the core taxonomy

- [ ] **P4.O1 — Optional:** Obtain targeted domain feedback, inspect additional development cases or use exploratory clustering for a specific unresolved question; interpret any groups against the taxonomy purpose before adopting them as types.

---

## Phase 5 - Classify and explain changes

### Confirm the operational specification

- [ ] **P5.01** Load the versioned codebook, event/feature evidence, definitions, coverage restrictions and development examples; confirm the relevant data versions and reserved-evidence boundary.
- [ ] **P5.02** Check identifiers, applicability, evidence, conditions/operators, boundary values, thresholds and label relationships for every type. Resolve specification ambiguities explicitly rather than hiding assumptions in code.
- [ ] **P5.03** Complete only the bounded development calibration tasks from Phase 4 and record settings/rationale; treat changes to type meaning as codebook revisions and reconsider affected development cases.

### Implement and apply assignment rules

- [ ] **P5.04** Implement explicit assignment functions and a documented configuration. For each event/type, check applicability, usable evidence and conditions, then record the result; a general-purpose rule engine or learned classifier is not required.
- [ ] **P5.05** Preserve the four outcomes: criteria met, criteria not met, indeterminate and not applicable. Keep execution failures and unresolved specifications separate from ordinary non-matches.
- [ ] **P5.06** Evaluate all applicable types, retain compatible simultaneous labels and detect conflicting matches before accepting assignments. Make decisions at recorded numerical precision and round only for presentation.
- [ ] **P5.07** Apply the rules to the declared development-event set and account for every event, including partial assessability and withheld assignments with explicit reasons.
- [ ] **P5.08** Record decisive measurements, units, operators, thresholds, compound-condition structure and satisfied alternative branches. Preserve Phase 3 review statuses and keep manual corrections separate from automatic outputs.

### Generate evidence-based descriptions

- [ ] **P5.09** Define structured description records containing event/customer references, comparison periods, before/after measurements, direction/magnitude, assigned types, supporting conditions, limitations and data/taxonomy/configuration references.
- [ ] **P5.10** Implement short standardised templates for temporal context/types, observed differences, assignment rationale and consequential limitations; derive all factual statements and values from the evidence records.
- [ ] **P5.11** Distinguish assignment-driving measures from descriptive context; handle unassigned/partly assessable cases without implying stability, avoid cross-unit importance rankings and causal claims, and require evidence for persistence statements.
- [ ] **P5.12** Reuse suitable before/after tables and history plots; preserve uncertainty and observation boundaries and add graphics only where they answer an interpretive question.

### Verify implementation and freeze the evaluation configuration

- [ ] **P5.13** Derive expected outcomes independently of the implementation and verify clear matches, non-matches, threshold boundaries, unsuitable denominators, missing evidence, applicability restrictions and compatible label combinations.
- [ ] **P5.14** Check codebook conformity, rule traces, conflicting combinations, technical failures, event accounting and deterministic reproduction; investigate differences from provisional Phase 4 assignments rather than assuming those assignments are correct.
- [ ] **P5.15** Verify description values, units, directions, reasons and limitations against actual rule execution and evidence. Resolve implementation errors before evaluating performance.
- [ ] **P5.16** Export/reload classification code/configuration references, assignment records, supporting rule evidence, structured/rendered descriptions and selected displays; keep production-derived outputs exclusively in private configured locations.
- [ ] **P5.17** Document verification, corrections and restrictions, then freeze preparation/detection versions, measures, codebook, parameters, classification code and templates before reserved evidence is processed in Phase 6.
- [ ] **P5.18 — Completion check:** Confirm consistent rules and resolved calibration, explicit multiple/withheld assignments, complete event accounting, accurate evidence-based descriptions, passing meaningful checks and a reproducible fixed evaluation configuration.

### Optional refinements after correct core outputs

- [ ] **P5.O1 — Optional:** Add templates, focused domain feedback or improved graphics for identified limitations. Introduce a learned classifier or extra explanation technique only for a distinct purpose with its own evaluation.

---

## Phase 6 - Evaluate and discuss findings

### Finalise the evaluation protocol before inspecting results

- [ ] **P6.01** Confirm the frozen preparation/detection procedure, taxonomy, assignment code, parameters, templates and verification results; review the development-exposure record and availability of genuinely reserved evidence.
- [ ] **P6.02** Specify claims, case-selection rules, reference information, fixed versions, scenario/pilot separation, review instructions and evidence required for each conclusion; address customer-level and overlapping-window dependence.
- [ ] **P6.03** Predefine event representation, temporal tolerance, one-to-one matching, metrics/denominators, undefined-result handling and sensitivity settings. Justify any acceptance criterion before viewing results; do not impose an arbitrary success threshold.
- [ ] **P6.04** Define the description-review checklist, factual-claim boundaries, numerical tolerances and required content per case; plan blinded assignment review before automatic labels/descriptions are revealed.

### Evaluate change detection on controlled cases

- [ ] **P6.05** Construct a compact benchmark with independently known changes and no-change controls containing ordinary variability; cover core dimensions, magnitudes, activity levels and selected simultaneous changes.
- [ ] **P6.06** Preserve dependencies between generated measures, document scenario definitions/repetitions/seeds and keep final realisations distinct from pilots. Use profile-level generation where sufficient; a full ERP simulator is not required.
- [ ] **P6.07** Apply the fixed detector and consolidation procedure. Implement maximum-cardinality one-to-one event matching within tolerance, resolving competing matches deterministically by timing distance.
- [ ] **P6.08** Report TP, FP and FN counts, precision, recall, F1 and duration-normalised false-alarm frequency on known no-change controls; retain scenario-specific results, undefined ratios, repetitions/variability and excluded, unassessable or failed histories.
- [ ] **P6.09** Document reference limitations: real histories are not automatically no-change controls, and extra detections in injected real backgrounds cannot automatically count as false positives. Restrict scores where reference information is insufficient.

### Assess taxonomy applicability on held-out real cases

- [ ] **P6.10** Select and document held-out cases spanning straightforward, combined, borderline, insufficient-evidence and unassigned patterns; record selection rationale and customer/event counts without using the cases to tune the taxonomy.
- [ ] **P6.11** Review representational coverage, clarity of distinctions, coherent combinations and inadequately represented dimensions; distinguish conceptual gaps, missing evidence, out-of-scope patterns and assessable non-matches.
- [ ] **P6.12** Record supporting cases and counterexamples. Do not equate assignment rate with taxonomy quality or interpret purposively sampled type frequencies as population prevalence.

### Evaluate automatic type assignment separately

- [ ] **P6.13** Supply reference events directly to the classifier to separate assignment errors from detection errors. Establish reference labels from independent scenario expectations or blinded manual examination of evidence/codebook, not from classification code.
- [ ] **P6.14** Record initial reference assessments before revealing automatic labels/descriptions; retain uncertainty and any later adjudication separately, and acknowledge reviewer dependence if only the thesis author reviews cases.
- [ ] **P6.15** Compute exact-match ratio and per-type precision/recall with underlying counts and reference frequencies; report unassigned/ambiguous proportions and reasons for withheld assignments.
- [ ] **P6.16** Document denominator treatment for non-matches, indeterminate/not-applicable outcomes and uncertain reference cases. Retain abstentions where a definite reference exists; separate automatic results from overrides and implementation conformity from taxonomy validity.

### Evaluate generated descriptions

- [ ] **P6.17** Check descriptions against measurements and executed assignment conditions using the predefined checklist, covering temporal context, measures, direction/magnitude, rationale and applicable limitations.
- [ ] **P6.18** Calculate factual correctness and completeness from assessed claims and required information items; report description/claim counts, supporting error evidence, denominator treatment and missing-description failures.
- [ ] **P6.19** Identify wrong values/units, unsupported duration or causal statements, omitted uncertainty and rule-inconsistent explanations. State that these project-specific checks are not the original FineSurE evaluator or proof of user comprehensibility/usefulness.

### Assess the complete workflow and planned sensitivities

- [ ] **P6.20** Process selected held-out histories through detection, assignment and description generation, reusing the real-case collection where suitable and completing blinded reference review before revealing corresponding outputs.
- [ ] **P6.21** Analyse propagation of errors/uncertainty into assignments and descriptions; report missed changes or false detections only where independent reference evidence supports the judgement.
- [ ] **P6.22** Run the predefined limited sensitivity analysis for consequential windows, detection thresholds or assignment thresholds; compare event timing, labels, assessability and description content while preserving primary results.
- [ ] **P6.23** Hold event evidence fixed for assignment-threshold comparisons where feasible, otherwise distinguish changed-window effects from rule effects. Label post-result tuning as further development; retain original results and document revisions and evidence reuse.

### Answer the research questions and complete the phase

- [ ] **P6.24** Answer SQ1 using detection performance and failure conditions, SQ2 using supported taxonomy distinctions/combinations/gaps, SQ3 using assignment agreement/errors/abstentions, and SQ4 using description correctness/completeness/traceability.
- [ ] **P6.25** Answer the main research question, separating the developed taxonomy, implemented procedure and empirical findings. Discuss the 24-month scope, selection, sparse activity, data quality, scenario assumptions, reviewer availability and single-company context, including negative/inconclusive results.
- [ ] **P6.26** Consolidate the required evaluation protocol, controlled benchmark results, real-case assessment, complete-workflow/sensitivity findings and research-question assessment; preserve versioned provenance, CSV/Parquet tables and configured figures without publishing production-derived content.
- [ ] **P6.27 — Completion check:** Confirm that core assessments are performed or infeasibility/consequences explained; counts, denominators and reference limits are interpretable; taxonomy validity and user usefulness are not overstated; revisions remain distinguishable; and every research question has an evidence-based answer.

### Optional refinements after the core evaluation

- [ ] **P6.O1 — Optional:** Add an independent reviewer or targeted reader-comprehension tasks only where resources permit and the additional evidence supports a clearly specified claim.
- [ ] **P6.O2 — Optional:** Extend controlled scenarios or evaluate an optional second detector only after the core assessment, documenting the separate purpose, reference evidence and proportionate conclusions.
