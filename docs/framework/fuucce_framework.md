<div align="center">

# Framework for analysing and typing customer purchasing changes

[![Phase 1](https://img.shields.io/badge/Phase%201-Familiarise%20and%20assess-%23352898?style=flat&labelColor=%2315934E)](#phase-1---familiarise-yourself-with-the-data-and-assess-its-suitability)
[![Phase 2](https://img.shields.io/badge/Phase%202-Use%20data%20and%20prepare%20profiles-%23352898?style=flat&labelColor=%2315934E)](#phase-2---use-erp-data-to-prepare-customer-profiles)
[![Phase 3](https://img.shields.io/badge/Phase%203-Uncover%20and%20characterise-%23352898?style=flat&labelColor=%2315934E)](#phase-3---uncover-and-characterise-changes)
[![Phase 4](https://img.shields.io/badge/Phase%204-Construct%20the%20taxonomy-%23352898?style=flat&labelColor=%2315934E)](#phase-4---construct-the-change-taxonomy)
[![Phase 5](https://img.shields.io/badge/Phase%205-Classify%20and%20explain-%23352898?style=flat&labelColor=%2315934E)](#phase-5---classify-and-explain-changes)
[![Phase 6](https://img.shields.io/badge/Phase%206-Evaluate%20and%20discuss-%23352898?style=flat&labelColor=%2315934E)](#phase-6---evaluate-and-discuss-findings)

</div>

## Table of Contents

- [Overview of the FUUCCE framework](#overview-of-the-fuucce-framework)
- [Data formats and file workflow](#data-formats-and-file-workflow)
- [Phase 1 - Familiarise yourself with the data and assess its suitability](#phase-1---familiarise-yourself-with-the-data-and-assess-its-suitability)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Inputs](#12-inputs)
    - [1.3 Core procedure](#13-core-procedure)
        - [1.3.1 Inspect the datasets and verify their meaning](#131-inspect-the-datasets-and-verify-their-meaning)
        - [1.3.2 Establish development and evaluation boundaries](#132-establish-development-and-evaluation-boundaries)
        - [1.3.3 Assess customer histories and ordering activity](#133-assess-customer-histories-and-ordering-activity)
        - [1.3.4 Explore a small set of candidate measures](#134-explore-a-small-set-of-candidate-measures)
        - [1.3.5 Consolidate preparation and analysis decisions](#135-consolidate-preparation-and-analysis-decisions)
    - [1.4 Required outputs](#14-required-outputs)
    - [1.5 Completion criteria](#15-completion-criteria)
    - [1.6 Optional refinements](#16-optional-refinements)
- [Phase 2 - Use ERP data to prepare customer profiles](#phase-2---use-erp-data-to-prepare-customer-profiles)
    - [2.1 Purpose](#21-purpose)
    - [2.2 Inputs](#22-inputs)
    - [2.3 Core procedure](#23-core-procedure)
        - [2.3.1 Finalise and apply preparation rules](#231-finalise-and-apply-preparation-rules)
        - [2.3.2 Integrate the relevant tables](#232-integrate-the-relevant-tables)
        - [2.3.3 Calculate the selected core measures](#233-calculate-the-selected-core-measures)
        - [2.3.4 Construct customer-period histories](#234-construct-customer-period-histories)
        - [2.3.5 Confirm suitability and verify the dataset](#235-confirm-suitability-and-verify-the-dataset)
    - [2.4 Required outputs](#24-required-outputs)
    - [2.5 Completion criteria](#25-completion-criteria)
    - [2.6 Optional refinements](#26-optional-refinements)
- [Phase 3 - Uncover and characterise changes](#phase-3---uncover-and-characterise-changes)
    - [3.1 Purpose](#31-purpose)
    - [3.2 Inputs](#32-inputs)
    - [3.3 Core procedure](#33-core-procedure)
        - [3.3.1 Specify the comparison design](#331-specify-the-comparison-design)
        - [3.3.2 Implement and calibrate the comparison rules](#332-implement-and-calibrate-the-comparison-rules)
        - [3.3.3 Identify and consolidate candidate events](#333-identify-and-consolidate-candidate-events)
        - [3.3.4 Characterise each candidate](#334-characterise-each-candidate)
        - [3.3.5 Review development cases and prepare taxonomy evidence](#335-review-development-cases-and-prepare-taxonomy-evidence)
    - [3.4 Required outputs](#34-required-outputs)
    - [3.5 Completion criteria](#35-completion-criteria)
    - [3.6 Optional refinements](#36-optional-refinements)
- [Phase 4 - Construct the change taxonomy](#phase-4---construct-the-change-taxonomy)
    - [4.1 Purpose](#41-purpose)
    - [4.2 Inputs](#42-inputs)
    - [4.3 Core procedure](#43-core-procedure)
        - [4.3.1 Establish the organising perspective](#431-establish-the-organising-perspective)
        - [4.3.2 Review and select development evidence](#432-review-and-select-development-evidence)
        - [4.3.3 Develop and revise the type structure](#433-develop-and-revise-the-type-structure)
        - [4.3.4 Specify definitions and assignment criteria](#434-specify-definitions-and-assignment-criteria)
        - [4.3.5 Check coherence and prepare the handover](#435-check-coherence-and-prepare-the-handover)
    - [4.4 Required outputs](#44-required-outputs)
    - [4.5 Completion criteria](#45-completion-criteria)
    - [4.6 Optional refinements](#46-optional-refinements)
- [Phase 5 - Classify and explain changes](#phase-5---classify-and-explain-changes)
    - [5.1 Purpose](#51-purpose)
    - [5.2 Inputs](#52-inputs)
    - [5.3 Core procedure](#53-core-procedure)
        - [5.3.1 Confirm the operational specification](#531-confirm-the-operational-specification)
        - [5.3.2 Implement the assignment rules](#532-implement-the-assignment-rules)
        - [5.3.3 Apply the rules and retain assignment evidence](#533-apply-the-rules-and-retain-assignment-evidence)
        - [5.3.4 Generate evidence-based descriptions](#534-generate-evidence-based-descriptions)
        - [5.3.5 Verify the implementation and prepare evaluation](#535-verify-the-implementation-and-prepare-evaluation)
    - [5.4 Required outputs](#54-required-outputs)
    - [5.5 Completion criteria](#55-completion-criteria)
    - [5.6 Optional refinements](#56-optional-refinements)
- [Phase 6 - Evaluate and discuss findings](#phase-6---evaluate-and-discuss-findings)
    - [6.1 Purpose](#61-purpose)
    - [6.2 Inputs](#62-inputs)
    - [6.3 Core procedure](#63-core-procedure)
        - [6.3.1 Finalise the evaluation protocol](#631-finalise-the-evaluation-protocol)
        - [6.3.2 Evaluate change detection](#632-evaluate-change-detection)
        - [6.3.3 Assess taxonomy applicability](#633-assess-taxonomy-applicability)
        - [6.3.4 Evaluate automatic type assignment](#634-evaluate-automatic-type-assignment)
        - [6.3.5 Evaluate generated descriptions](#635-evaluate-generated-descriptions)
        - [6.3.6 Examine the complete workflow and sensitivity](#636-examine-the-complete-workflow-and-sensitivity)
        - [6.3.7 Answer the research questions](#637-answer-the-research-questions)
    - [6.4 Required outputs](#64-required-outputs)
    - [6.5 Completion criteria](#65-completion-criteria)
    - [6.6 Optional refinements](#66-optional-refinements)
- [Bibliography](#bibliography)

---

## Overview of the FUUCCE framework

The **FUUCCE framework** operationalises the thesis project plan through six phases: familiarising with and assessing the data, preparing customer profiles, uncovering and characterising changes, constructing a change taxonomy, classifying and explaining events, and evaluating the findings.

It defines the core activities, expected outputs and completion criteria for a reproducible workflow, prioritising a complete core analysis before optional extensions. Development proceeds iteratively, while the final evaluation uses separate evidence to assess the individual components and the complete workflow.

---

## Data formats and file workflow

Parquet is the standard input format for loading, processing and analysing tabular datasets throughout the framework.

**The file workflow is:**
1. **Load:** Read the required datasets from their Parquet files.
2. **Analyse:** Perform preparation, calculations and analyses in the relevant notebook or script.
3. **Export:** Save newly created or updated datasets as CSV.
4. **Convert:** Convert the exported CSV files to Parquet using [setup/csv_to_parquet.py](setup/csv_to_parquet.py), retaining both formats.
5. **Reuse:** Load the resulting Parquet files in subsequent processing steps or phases.

After conversion, verify that both files represent the same dataset and that the Parquet version preserves the intended schema and missing values. Regenerate the corresponding Parquet file whenever an exported CSV dataset changes.

Use the configured data and output directories consistently and preserve the original extracts.

---

## Phase 1 - Familiarise yourself with the data and assess its suitability

### 1.1 Purpose

Establish whether the available ERP data can support the planned investigation and identify the preparation and analytical decisions needed for the core workflow.

This phase combines technical inspection with focused exploration of customer histories. It examines data quality, observation coverage, ordering activity and the feasibility of candidate measures. Existing source documentation provides the starting point and is verified against the actual extracts rather than recreated.

The main output is a documented assessment of suitable data, promising behavioural measures and preparation requirements. Final cleaning, systematic profile construction and change detection follow in subsequent phases.

> **Methodological basis:** This phase adapts the inspection and exploration activities of CRISP-DM's data-understanding phase (IBM, n.d.) and exploratory data-analysis principles (Heckert & Filliben, 2003). The ERP-specific checks, analytical priorities and suitability decisions are project-specific operational choices.

### 1.2 Inputs

- The final project plan, including the research questions, scope and candidate measures.
- Available ERP extracts and information about their extraction date, filters and coverage.
- Existing data descriptions, field definitions and relevant business-code explanations.

Record missing information and its consequences. Distinguish documented facts, observations from the extracts, provisional assumptions and unresolved questions.

### 1.3 Core procedure

#### 1.3.1 Inspect the datasets and verify their meaning

Load the relevant extracts reproducibly and compare their contents with the existing data documentation.

**Check:**
- the size of each table, including its row and column counts.
- what each table and row represent.
- required fields, observed data types and missing-value placeholders.
- identifiers, duplicate candidate keys and relationships between tables.
- date coverage, record counts and apparent extraction gaps.
- order types, processing and rejection statuses.
- monetary currencies, quantity units and product-group coverage.

Verify the distinction between order-level and item-level information. In particular, establish how order amounts can be retained once per order when item information is joined.

Unusual values are initially recorded as investigation flags. Exclusions or corrections require evidence and a documented rationale.

#### 1.3.2 Establish development and evaluation boundaries

Define how evidence will be reserved for the final evaluation before inspecting individual behavioural patterns or using cases to develop analytical rules.

The separation must reflect the intended evaluation claim. Customer-level separation is the starting option for assessing the approach on additional customers. If a temporal separation is chosen, overlapping observations and comparison windows must be addressed.

General structural checks may cover the extracts, but behavioural exploration and decisions about features, thresholds or types must use the declared development evidence. Record any prior exposure that limits the independence of reserved cases.

#### 1.3.3 Assess customer histories and ordering activity

**Within the agreed 24-month observation window, examine:**
- distinct order counts and active periods per customer.
- first and last observed order dates.
- intervals between orders and periods without recorded activity.
- incomplete observation periods and uncertain coverage.
- the effects of relevant data-quality issues on potential comparisons.

Distinguish extraction coverage from observed purchasing activity. A first-to-last order span does not establish continuous coverage, and the first recorded order does not necessarily identify a newly acquired customer.

The project's orientation of approximately two to four orders per year is not an inclusion rule. Assess whether histories contain enough information for the intended comparisons without requiring a minimum number of orders separately in each year.

#### 1.3.4 Explore a small set of candidate measures

Prioritise ordering activity, net order value and assortment. Examine whether the documented fields support order count, total and average net order value, and product or product-group breadth.

Create provisional customer-period views where needed. Use the project plan's order-eligibility principles, documenting unresolved status-code decisions and any restrictions they impose on interpretation. Monthly aggregation may serve as an initial exploratory view. Its suitability must be assessed against ordering activity. It is not a fixed requirement.

**Use a small number of tables and graphics to answer specific questions:**

| **Question**                                                   | **Suggested evidence**                                                            |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Which histories provide usable comparison support?**         | Order-count, active-period and ordering-interval summaries.                       |
| **Is the proposed temporal resolution informative?**           | Selected customer histories and the proportion of periods without orders.         |
| **Are core measures calculable and interpretable?**            | Missingness, formula checks, value distributions and product-group coverage.      |
| **Could individual orders dominate apparent differences?**     | Selected histories shown alongside their underlying orders.                       |
| **Do preparation decisions materially affect interpretation?** | Targeted comparisons of plausible treatments for consequential unresolved issues. |

Select development examples with varied activity and history characteristics. Include ordinary and difficult cases, rather than only conspicuous changes.

Exploratory transformations and provisional profiles should use reusable code that can be completed in Phase 2. Preserve original extracts and record the effects of joins, conversions and temporary selection rules.

#### 1.3.5 Consolidate preparation and analysis decisions

**Translate findings into recommendations for:**
- order and item selection.
- treatment of missing, duplicate or questionable records.
- candidate measures and their interpretation limits.
- temporal aggregation and customer suitability.
- issues that require clarification before the core analysis can proceed.

**For each consequential decision, record the evidence, rationale and status:** adopted for exploration, proposed for preparation or unresolved.

Apparent changes observed during exploration remain development findings. They are not automatically detected events or established taxonomy types.

### 1.4 Required outputs

**Maintain one reproducible notebook containing:**
1. **Data assessment:** Verified source definitions, key relationships and relevant quality findings.
2. **Customer-history assessment:** Coverage, activity and provisional analytical suitability.
3. **Focused exploratory findings:** Selected summaries and graphics linked to the questions they answer.
4. **Preparation decisions and open issues:** Recommended treatments, candidate measures, temporal representation and outstanding dependencies.
5. **Evidence-use record:** Development cases, reserved evaluation evidence and any prior exposure.

These outputs may be sections or tables within the same notebook. Separate files are only necessary where they support reuse in later phases. Export figures and tables to the directory specified by the project configuration in [src/config](src/config). The default export directory is [outputs/exports](outputs/exports). Outputs derived from production data must use [outputs/.exports](outputs/.exports). Use the configured path consistently throughout the notebook.

### 1.5 Completion criteria

**Phase 1 is complete when:**
- the meaning and relationships of the core data are sufficiently understood.
- relevant quality and coverage limitations are documented.
- the feasibility of the core candidate measures has been assessed.
- customer activity has been examined sufficiently to propose a temporal representation and suitability criteria.
- development and evaluation boundaries are documented.
- Phase 2 can proceed using explicit preparation recommendations.

Exhaustive exploration is not required. Unresolved issues affecting optional extensions may be deferred. Issues preventing a trustworthy core analysis must be identified as blockers with a specified next action.

### 1.6 Optional refinements

After the core assessment, additional exploration may examine discount feasibility, product-group incidence patterns, compatible quantity measures or customer subgroups.

Undertake these refinements only when they address a specific analytical question or support an agreed extension. They must not delay preparation of the core dataset merely to complete every possible descriptive analysis.

---

## Phase 2 - Use ERP data to prepare customer profiles

### 2.1 Purpose

Transform the available ERP extracts into reproducible customer-period profiles suitable for the core change analysis.

This phase implements and verifies the preparation decisions developed in Phase 1. It establishes consistent order selection, validated table relationships, explicit feature definitions and a justified temporal representation.

The main output is an analytical dataset accompanied by eligibility information and the documentation needed to interpret and regenerate it. Provisional preparation code from Phase 1 is refined and reused.

> **Methodological basis:** This phase adapts CRISP-DM's data-selection, cleaning, integration, construction and formatting activities (IBM, n.d.), supported by tidy-data principles for organising observations and variables (Wickham, 2014). The separation of development and evaluation evidence informs the treatment of fitted transformations and empirically selected rules (Kapoor & Narayanan, 2023). ERP-specific selection rules, feature definitions and aggregation choices are project-specific decisions requiring justification.

### 2.2 Inputs

- Original ERP extracts and reproducible loading code.
- Verified field definitions and table relationships.
- Phase 1 quality findings, customer-history assessment and preparation recommendations.
- The project plan's observation window, order-eligibility principles and candidate measures.
- The documented separation between development and final evaluation evidence.

Resolve issues affecting the meaning or calculation of core measures before constructing the corresponding profiles. Unresolved requirements for optional measures may remain deferred.

### 2.3 Core procedure

#### 2.3.1 Finalise and apply preparation rules

Specify the exact boundaries of the agreed 24-month observation window using `SALESORDERDATE`. Document the treatment of incomplete periods.

**Translate the project's requirement for valid, non-cancelled orders into explicit rules using the documented meanings of:**
- `SALESORDERTYPE`
- `OVERALLSDPROCESSSTATUS`
- `SDDOCUMENTREASON`
- `OVERALLSDDOCUMENTREJECTIONSTS`

Exclude fully rejected orders. Clarify partially rejected orders and the meaning of their recorded amounts before including them in affected measures. Open or in-progress orders are not excluded solely because processing is incomplete.

Apply documented treatments for identifiers, dates, duplicate representations, missing-value placeholders, currencies and categories. Preserve identifier semantics, including leading zeros.

Separate technical corrections from analytical exclusions. Large orders remain included unless a justified rule requires otherwise. Their size alone is not evidence of an error or project-order status.

Record consequential rules with their rationale, affected record and customer counts, and remaining limitations.

#### 2.3.2 Integrate the relevant tables

Construct validated order-level and item-level views using the relationships verified in Phase 1.

**For each consequential join, check:**
- expected key uniqueness and relationship cardinality.
- unmatched records and their treatment.
- changes in row counts.
- consistency of relevant order counts and monetary totals.

Retain `TOTALNETAMOUNT` once per eligible `SALESORDER`. Where necessary, aggregate item-level information before combining it with order-level measures.

Apply consistent item eligibility when calculating assortment measures, including the treatment of rejected items within otherwise eligible orders. Record missing product classifications rather than silently removing their effect from the analysis.

#### 2.3.3 Calculate the selected core measures

Use the candidate catalogue in the project plan to select a compact set of feasible measures covering ordering activity, net order value and assortment.

Maintain one feature specification containing each selected measure's meaning, source fields, formula, unit, aggregation basis, missing-value treatment and interpretation limits.

| **Candidate measure**                                   | **Preparation requirement**                                                                            |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Order count - `ORDERCOUNT`**                          | Count distinct eligible orders per customer and period.                                                |
| **Total net order value - `TOTALORDERVALUE`**           | Sum eligible order-level net amounts once per order on a consistent currency basis.                    |
| **Average net order value - `AVGORDERVALUE`**           | Divide total net order value by the corresponding order count. Leave undefined when the count is zero. |
| **Product breadth - `DISTINCTPRODUCTCOUNT`**            | Count distinct eligible products within the period.                                                    |
| **Product-group breadth - `DISTINCTPRODUCTGROUPCOUNT`** | Count distinct assigned product groups and report classification coverage.                             |

The table does not require every candidate to become a detection input. Document dependencies between measures and distinguish selected detection inputs from additional descriptive measures when that decision is made.

#### 2.3.4 Construct customer-period histories

Select the temporal resolution using Phase 1 evidence. Document why it provides useful comparison support for the intended customers.

Create the principal profile table with one row per customer and aggregation period, identified by `CUSTOMERID`, derived from `SOLDTOPARTY`, and `PERIODSTART`.

**Apply the following rules:**
- Represent periods without orders only within a justified observation interval.
- Use zero counts and totals where complete observation supports inactivity.
- Preserve unknown coverage and missing measurements as missing.
- Leave averages and shares undefined when their denominators are zero.
- Retain indicators for partial periods, missing classifications and other consequential quality restrictions.
- Preserve measures in their original units.

Optional scaling or other method-specific transformations may be deferred until required. Parameters estimated from data must use the declared development evidence and then be applied consistently to evaluation data.

#### 2.3.5 Confirm suitability and verify the dataset

Reassess customer suitability after cleaning and selection, because these operations may change usable activity and history.

Record eligibility and restrictions for the intended analysis, including whether particular periods or measures are unassessable. A customer may support some comparisons but not others. Do not impose a minimum order count separately in each year or require recent activity merely to qualify. Document the reasons for exclusions and their consequences for the analysed population.

**Verify:**
- uniqueness of customer-period identifiers.
- agreement of order counts and monetary totals with eligible source records.
- correct feature calculations and missing-value handling.
- expected effects of joins and exclusions.
- selected profiles against their underlying orders.
- successful regeneration and reloading of the saved outputs.

Investigate discrepancies before using affected profiles for detection.

### 2.4 Required outputs

**Produce:**
1. **Prepared customer profiles:** Selected measures, period identifiers and relevant quality indicators.
2. **Eligibility and coverage information:** Included customers, restricted comparisons and exclusion reasons.
3. **Preparation and feature specification:** Applied rules, formulas and consequential decisions.
4. **Verification results:** Reconciliation checks, identified discrepancies and their resolution.
5. **Reproducible preparation code:** Input references, configuration and output schemas.

**Export the prepared analytical datasets according to the [shared data-format workflow](#data-formats-and-file-workflow):** save them as CSV, convert them to Parquet and use the Parquet versions in subsequent phases. Document the CSV encoding, delimiter, decimal notation and missing-value representation. Retain additional intermediate datasets where they support verification or reuse, and preserve the original extracts.

### 2.5 Completion criteria

**Phase 2 is complete when:**
- core selection and preparation rules are explicit.
- joins and aggregates have been verified.
- selected measures have documented definitions.
- customer-period profiles distinguish inactivity, missing evidence and undefined values.
- analytical suitability and restrictions are recorded.
- outputs can be regenerated and reloaded correctly.
- the profiles are ready for the planned window comparisons.

Remaining optional preparation tasks do not block completion. Unresolved issues affecting core measures or trustworthy comparisons must be recorded as blockers.

### 2.6 Optional refinements

Additional preparation may support product-group order shares, days since the last order, discount measures or quantities within compatible units.

Discount integration requires verified price-condition assignment, validity periods, price bases and quantities. Missing or unmaintained prices remain missing, and discount coverage must accompany aggregate results.

Introduce these refinements only when justified by the investigation. Preserve a reproducible core dataset so that optional additions do not prevent execution of the main workflow.

---

## Phase 3 - Uncover and characterise changes

### 3.1 Purpose

Identify and characterise candidate purchasing changes using the customer-period profiles prepared in Phase 2.

Time-window-based profile comparison is the main detection approach. It compares a customer's behaviour in a reference period with behaviour in a subsequent period, applying explicit criteria for deviation from usual variability, change magnitude and sufficient evidence.

The unit of analysis is a change event within a customer's history. A customer may contribute several events, and an event may involve several behavioural dimensions.

The main output is a reproducible collection of change candidates with before-and-after measurements and relevant limitations. These development cases support taxonomy construction in Phase 4. Final type assignment follows in Phase 5, while independent performance evaluation belongs to Phase 6.

> **Methodological basis:** This phase adapts window-based comparison principles from retrospective change-point detection methodology (Truong et al., 2020). The window design, comparison measures, significance criteria and event-consolidation rules are project-specific choices requiring justification.

### 3.2 Inputs

- Prepared customer-period profiles and feature definitions from Phase 2.
- Customer eligibility, observation coverage and relevant quality indicators.
- Phase 1 exploratory findings and documented preparation decisions.
- The project's operational definition of significant purchasing behaviour changes.
- Records identifying development data and evidence reserved for final evaluation.

Method selection, calibration and detailed case inspection in this phase use development evidence. Reserved evaluation histories are processed later using the fixed configuration.

### 3.3 Core procedure

#### 3.3.1 Specify the comparison design

Define a compact analysis configuration before systematically detecting events.

| **Decision**                | **Required specification**                                                                                                        |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Target patterns**         | State which changes the initial approach addresses, such as changes in ordering frequency, net order value or assortment breadth. |
| **Detection inputs**        | Identify the selected measures and distinguish them from additional descriptive measures.                                         |
| **Comparison windows**      | Define reference and subsequent window lengths, movement, boundary conventions and treatment of incomplete windows.               |
| **Comparison support**      | Specify the observations, order activity and coverage needed to assess each measure.                                              |
| **Change criteria**         | Define how deviation from usual variability, minimum magnitude and sufficient evidence are assessed.                              |
| **Contextual restrictions** | Specify how recurring patterns, isolated large orders and coverage changes affect interpretation or assessability.                |

Use adjacent, non-overlapping reference and subsequent windows as the initial comparison design unless another arrangement is justified. Successive rolling comparisons may overlap. Their dependence must be considered when consolidating events and separating development from evaluation evidence.

Window lengths and minimum-support rules are selected using development evidence. They are not assumed to be universally suitable for every customer.

#### 3.3.2 Implement and calibrate the comparison rules

Calculate comparable feature summaries for each eligible pair of windows. Use period averages or rates where unequal window lengths would make totals misleading.

**Begin with interpretable, feature-specific comparisons. Document:**
- the comparison statistic for each selected measure.
- how usual variability is represented and estimated.
- the required magnitude of a change.
- evidence requirements and treatment of unavailable comparisons.
- whether any qualifying dimension can trigger an event or whether a specified combination is required.

Keep variability assessment and magnitude requirements explicit, even where they are incorporated into one decision rule. If the available history cannot support the required assessment, record the comparison as unassessable. Any combined score requires a justified treatment of units, scaling, weighting and dependencies between measures. Order count, total order value and average order value must not be treated as independent corroborating signals merely because all three change.

Calibrate settings using development cases and, where useful, separate pilot scenarios. Do not select thresholds simply to obtain a desired number of events or anticipated types.

Meeting the operational criteria identifies a change candidate. It does not establish statistical significance through hypothesis testing, a behavioural cause or membership in a taxonomy type.

#### 3.3.3 Identify and consolidate candidate events

Apply the specified procedure to eligible development histories.

**Account for comparisons that:**
- satisfy the candidate-selection criteria.
- are assessable but do not satisfy those criteria.
- cannot be assessed because required evidence is missing or insufficient.

An assessable comparison without a detection is not proof that the customer's behaviour is stable.

Rolling comparisons may repeatedly flag the same underlying pattern. Define when nearby detections should be consolidated into one candidate event, how its timing is represented and which comparison windows provide its descriptive evidence.

Preserve the original detections and their links to consolidated events. Do not merge temporally distinct changes solely because they affect the same feature.

#### 3.3.4 Characterise each candidate

Create an event register and linked feature-level descriptions.

| **Component**            | **Required information**                                                                                               |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Identity**             | Event identifier, customer identifier and analysis configuration.                                                      |
| **Temporal context**     | Reference and subsequent periods, together with the reported boundary or transition interval.                          |
| **Observed differences** | Before-and-after values, affected measures, direction and magnitude.                                                   |
| **Detection basis**      | Criteria satisfied, relevant comparison statistics and applied settings.                                               |
| **Supporting evidence**  | Available observations, order counts and consequential coverage or quality restrictions.                               |
| **Temporal extent**      | Observed duration or follow-up where assessable. Otherwise an explicit limitation.                                     |
| **Review status**        | Candidate without identified concerns, ambiguous case, insufficient evidence or suspected data artefact, with reasons. |

Report absolute differences and relative differences where meaningful. Distinguish percentage-point changes from relative percentage changes. If the reference value is zero or too small for a meaningful relative comparison, retain the absolute difference and mark the relative result as undefined or unstable.

Persistence requires an explicit assessment rule. The length of a comparison window alone does not demonstrate sustained change. If follow-up ends before the pattern resolves, report the observation boundary rather than a completed duration.

An event's period-level timing does not establish an exact transaction-level change date.

#### 3.3.5 Review development cases and prepare taxonomy evidence

Inspect selected candidates against their underlying orders and full available development histories.

**Prioritise checks for:**
- changes dominated by individual large orders.
- recurring patterns or incomplete observation periods.
- missing classifications or other preparation effects.
- insufficient comparison support.
- repeated detections and unclear event boundaries.

Use a limited set of alternative settings where needed to understand consequential sensitivities. These are development checks. Final sensitivity reporting follows the evaluation protocol.

Assemble a manageable case collection covering different dimensions, directions, magnitudes, combined changes and ambiguous outcomes. Include selected histories without automatic detections to inspect possible omissions. Record the case-selection rationale and both event and customer counts. Avoid allowing numerous similar events from one customer to dominate taxonomy development.

Manually noticed patterns retain their manual provenance. They must not be presented as automatic detections, and candidates must not be removed merely because they do not fit an anticipated type.

### 3.4 Required outputs

**Produce:**
1. **Detection specification:** Selected measures, windows, criteria, calibration rationale and consolidation rules.
2. **Candidate-event register:** Event timing, detection evidence, review status and links to original detections.
3. **Feature-change evidence:** Before-and-after values, differences, units and support information.
4. **Processing summary:** Assessed and unassessable histories or comparisons, with reasons.
5. **Taxonomy-development case collection:** Selected cases, supporting displays and selection rationale.

These outputs may be linked tables within a small number of datasets and notebooks. Preserve enough configuration and provenance information to reproduce each event.

### 3.5 Completion criteria

**Phase 3 is complete when:**
- the comparison procedure and operational significance criteria are explicit.
- the procedure runs reproducibly on the declared development data.
- unassessable comparisons and repeated detections are handled consistently.
- candidates have traceable measurements and interpretation limits.
- consequential development checks are documented.
- sufficient usable evidence is available to begin taxonomy development, or its limitations are explicitly identified.

Completion does not require a predetermined number of events or favourable detection performance. If the available evidence cannot support defensible comparisons or taxonomy development, record the restriction and revisit the relevant preparation or analysis decisions.

### 3.6 Optional refinements

Possible refinements include additional behavioural dimensions, alternative window designs or a second detection method such as change-point segmentation.

Introduce an extension only when it addresses a specific limitation or research-relevant question and sufficient time remains for its assessment. Method disagreements and applicability differences must be retained if multiple approaches are compared.

The initial priority is a functioning, interpretable profile-comparison approach with usable event descriptions for the subsequent taxonomy phase.

---

## Phase 4 - Construct the change taxonomy

### 4.1 Purpose

Develop a compact, interpretable taxonomy of purchasing behaviour changes using the development evidence assembled in Phase 3 and relevant conceptual and domain knowledge.

The classified object is a change event within a customer's history. The taxonomy describes observable purchasing patterns at the focal wholesaler. It does not classify customers permanently or establish the causes of their behaviour.

Taxonomy development is researcher-led and systematic. Provisional application to development cases helps refine the definitions before their automatic implementation in Phase 5. Independent evaluation of the resulting taxonomy belongs to Phase 6.

> **Methodological basis:** This phase adapts the iterative conceptual-to-empirical and empirical-to-conceptual approach of Nickerson et al. (2013). The specification of the taxonomy's purpose and the distinction between development checks and subsequent evaluation follow the guidance of Kundisch et al. (2022). The retained types, assignment criteria and development-case selection are project-specific decisions requiring justification.

### 4.2 Inputs

- The Phase 3 candidate-event register and linked feature-change evidence.
- Selected development cases, including combined changes, ambiguous events and separately documented manual observations.
- Feature definitions, comparison rules and relevant data-quality restrictions.
- The project plan's research objectives, scope and operational significance definition.
- Relevant scientific literature and available business definitions.
- Records distinguishing development evidence from cases reserved for final evaluation.

Use development evidence to construct and revise the taxonomy. Reserved evaluation cases must not inform type definitions or parameter choices.

### 4.3 Core procedure

#### 4.3.1 Establish the organising perspective

**Use the following organising perspective to guide which distinctions belong in the taxonomy:**

> Observable changes within a customer's purchasing behaviour at the focal wholesaler, represented through differences in behavioural dimensions between documented reference and subsequent periods.

Define the intended use as consistent classification and interpretation of change events. The initial users are the researcher and readers examining the findings.

Begin with the behavioural dimensions supported by the prepared measures. Include increases, decreases and other relevant patterns where the representation permits them. A calculated feature does not automatically require a separate type. Retain a distinction when it has a clear interpretation, can be measured defensibly and contributes to describing the observed events. Keep magnitude, timing and observed duration as supporting descriptors unless categorical distinctions are justified by the taxonomy's purpose.

#### 4.3.2 Review and select development evidence

Reuse the Phase 3 development-case collection rather than assembling a separate, disconnected set of examples.

**Check whether it includes:**
- different behavioural dimensions and directions.
- single-dimension and combined changes.
- varied magnitudes and available temporal evidence.
- customers with different activity levels.
- borderline cases and relevant data limitations.
- patterns that the current detection approach may not capture adequately.

Record case-selection reasons and both event and customer counts. Numerous similar events from one customer should not dominate the development process.

Manually identified patterns retain their provenance and require a documented event description before being used as examples. Histories without automatic detections are not automatically verified no-change cases. The number of reviewed cases is guided by pattern coverage, unresolved questions and the available workload. No fixed number of cases or types is required.

#### 4.3.3 Develop and revise the type structure

**Combine conceptual reasoning with systematic comparison of development cases:**
1. Propose initial distinctions from the organising perspective, behavioural measures and relevant literature.
2. Examine a manageable batch of cases using their original histories and before-and-after evidence.
3. Apply the provisional definitions and record matches, non-matches and uncertainty.
4. Identify missing, redundant or unclear distinctions.
5. Revise the definitions with documented reasons.
6. Revisit earlier cases affected by the revision.

**Preserve the distinction between:**
- **behavioural dimensions**, such as ordering frequency.
- **change types**, such as a qualifying decrease in ordering frequency.
- **supporting descriptors**, such as magnitude or observed duration.
- **evidence statuses**, such as insufficient comparison support.

The examples above illustrate the structure. They do not establish final empirical types. Compatible types may coexist within one event. Define logical exclusions where necessary, but do not create a separate named type for every possible combination. A composite type requires a distinct interpretation and explicit criteria.

For composition changes, define the representation and denominator rather than applying a generic increase/decrease label to the entire mix.

#### 4.3.4 Specify definitions and assignment criteria

Maintain a concise type codebook that can be translated into executable rules in Phase 5.

| **Field**                    | **Required content**                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| **Identity and meaning**     | Stable identifier, neutral name and conceptual definition.                            |
| **Required evidence**        | Relevant measures, units, comparison periods and minimum data support.                |
| **Assignment conditions**    | Explicit conditions, comparison operators and treatment of boundary values.           |
| **Parameters**               | Adopted thresholds, their rationale and any remaining calibration tasks.              |
| **Relationships**            | Compatible types, exclusions and justified composite relationships.                   |
| **Limitations and examples** | Applicability restrictions, supporting cases, counterexamples and conceptual sources. |

Reuse the Phase 3 comparison evidence unless a revision is justified. Changes to measurements or event descriptions require updating the relevant earlier phase and regenerating affected results.

Distinguish detection criteria from type-assignment criteria, even where they use the same measurements or numerical thresholds. Detection identifies candidates. The codebook specifies which patterns those candidates satisfy.

Use development evidence to justify parameter choices. Do not adopt illustrative percentages or durations as established thresholds. If calibration is deferred to Phase 5, identify the parameter and development-only selection procedure explicitly. Distinguish cases where criteria are met, criteria are not met, evidence is insufficient or the type is not applicable. These outcomes are not additional behavioural types.

Preserve event-level quality concerns separately. A numerical match must not conceal a suspected data artefact or resolve an ambiguity unsupported by the evidence.

#### 4.3.5 Check coherence and prepare the handover

**Review the proposed taxonomy for:**
- alignment with its purpose and analytical scope.
- clear distinctions without unnecessary proliferation of types.
- feasible measurements and explicit evidence requirements.
- consistent rules and compatible label combinations.
- representation of development cases and documented reasons for non-coverage.
- terminology that describes observations without unsupported causal claims.

Investigate whether an unrepresented case reflects insufficient evidence, an excluded pattern or a genuine gap in the taxonomy. Do not force every event into a type or introduce an undefined "other" category. Record revisions and their effects on previously examined cases. Complete a final development pass over the retained definitions and affected examples.

Freeze the codebook version handed to Phase 5. Subsequent changes to type meaning require a documented revision. These development checks establish readiness for implementation. They do not replace the evaluation in Phase 6.

### 4.4 Required outputs

**Produce:**
1. **Taxonomy overview:** Retained dimensions, types, relationships and supporting descriptors.
2. **Type codebook:** Definitions and operational assignment criteria.
3. **Development-case record:** Cases examined, provisional outcomes and supporting evidence.
4. **Decision and revision record:** Reasons for additions, combinations, removals and parameter choices.
5. **Phase 5 handover:** The codebook version, applicable data versions and any bounded calibration tasks.

These outputs may be maintained in one specification document and linked tables. Use stable identifiers to connect types, events and revisions. Export reusable tabular datasets according to the [shared CSV-to-Parquet workflow](#data-formats-and-file-workflow). Qualitative reasoning remains documented in the notebook or accompanying specification.

### 4.5 Completion criteria

**Phase 4 is complete when:**
- the taxonomy's purpose and organising perspective are explicit.
- retained types have clear meanings and assessable assignment criteria.
- compatible combinations and conflicting outcomes are addressed.
- insufficient evidence and unrepresented cases have documented treatment.
- a final development review identifies no unresolved conceptual contradictions in the retained definitions.
- the implementation handover is versioned and sufficiently specific for Phase 5.

Completion does not require a predetermined number of types, complete coverage or a label for every candidate. Conceptual extensions without empirical examples must be identified separately. If the available cases cannot support defensible distinctions, report the taxonomy as provisional or restricted and identify the necessary follow-up.

### 4.6 Optional refinements

Optional refinements include targeted domain feedback, additional development cases addressing specific coverage gaps or exploratory clustering to investigate an unresolved grouping question.

Clustering does not independently establish meaningful change types. Any resulting groups require interpretation and assessment against the taxonomy's purpose.

Prioritise a coherent, implementable taxonomy for the core measures before adding further dimensions or more detailed subtypes.

---

## Phase 5 - Classify and explain changes

### 5.1 Purpose

Implement the taxonomy developed in Phase 4 as executable rules and generate descriptions that connect observed purchasing changes with their type assignments. Each change event may receive several compatible types, remain partly assessable or receive no type. The implementation preserves these outcomes and their reasons.

Descriptions explain what changed and why the documented assignment criteria were satisfied or could not be assessed. They do not establish the causes of customer behaviour.

The main output is a reproducible classification and description procedure, verified on development cases and prepared for the independent evaluation in Phase 6.

> **Methodological basis:** Direct implementation of explicit assignment rules is informed by the distinction between interpretable decision procedures and post-hoc explanations discussed by Rudin (2019). Description generation adapts data-to-text principles for selecting, organising and expressing structured evidence (Gatt & Krahmer, 2018). The rule implementation, outcome handling and text templates are project-specific design choices.

### 5.2 Inputs

- The versioned taxonomy and type codebook from Phase 4.
- Adopted parameters and any explicitly deferred calibration tasks.
- Phase 3 event records and feature-change evidence.
- Relevant feature definitions, coverage information and quality restrictions.
- Development examples, counterexamples and provisional assignments.
- Records identifying development evidence and reserved evaluation cases.

Load tabular inputs from their Parquet versions according to the [shared file workflow](#data-formats-and-file-workflow). Keep the final evaluation cases reserved for Phase 6.

### 5.3 Core procedure

#### 5.3.1 Confirm the operational specification

**Check that every retained type has:**
- an identifier and clear definition.
- required measurements and applicability conditions.
- explicit assignment conditions and comparison operators.
- documented thresholds and treatment of boundary values.
- rules for insufficient evidence.
- compatible labels and relevant exclusions.

Complete any deferred calibration using the development evidence and procedure specified in Phase 4. Record the selected settings and their rationale.

Distinguish changes to parameter values from changes to a type's meaning. A conceptual change requires a documented taxonomy revision and reconsideration of affected development cases.

Do not resolve an unclear definition through an undocumented coding assumption.

#### 5.3.2 Implement the assignment rules

Translate the codebook into explicit functions and a documented parameter configuration. A general-purpose rule engine or learned classifier is not required.

**For each event and relevant type:**
1. Determine whether the type is applicable.
2. Check whether the required evidence is available and usable.
3. Evaluate the assignment conditions.
4. Record the outcome and supporting evidence.

**Use the following outcomes consistently:**

| **Outcome**          | **Meaning**                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| **Criteria met**     | The required evidence is assessable and satisfies the type definition.       |
| **Criteria not met** | The evidence is assessable but does not satisfy the definition.              |
| **Indeterminate**    | Missing, insufficient or unreliable evidence prevents a defensible decision. |
| **Not applicable**   | The event falls outside the type's documented applicability conditions.      |

An unresolved definition is a specification issue requiring revision. An execution failure is a technical issue. Neither should be silently recorded as an ordinary non-match.

Evaluate all applicable types rather than stopping after the first match. Assign compatible labels together. If conflicting labels satisfy their rules, preserve the diagnostic results and resolve the inconsistency before accepting the affected assignment. Use the recorded numerical precision for decisions and round only for presentation. Preserve the distinctions between absolute differences, relative changes and percentage-point changes.

#### 5.3.3 Apply the rules and retain assignment evidence

Apply the implementation to a declared development-event set and account for every input event.

Maintain a concise rule trace containing the decisive measurements, operators, thresholds and condition outcomes. For compound conditions, preserve the relationship between the conditions and identify the satisfied branch where alternatives are allowed. Keep the event's Phase 3 review status separate from its type assignments. Meeting a numerical rule does not resolve an underlying data-quality concern.

An event with no assigned type must retain the reason, such as assessable non-matches, insufficient evidence or applicability restrictions. Partial assessability may permit some assignments while preventing others.

Record manual corrections separately from automatic results. Do not silently replace algorithmic outputs with researcher judgements.

#### 5.3.4 Generate evidence-based descriptions

Create a structured description record before rendering text.

| **Component**       | **Required content**                                                                         |
| ------------------- | -------------------------------------------------------------------------------------------- |
| **Event context**   | Customer and event references, comparison periods and relevant event status.                 |
| **Observed change** | Affected measures, before-and-after values, units, direction and magnitude.                  |
| **Type assignment** | Assigned labels and the conditions supporting them.                                          |
| **Limitations**     | Consequential uncertainty, missing evidence, coverage restrictions or unavailable follow-up. |
| **Traceability**    | References to the event evidence, taxonomy version and parameter configuration.              |

**Use short, standardised templates to present:**
1. the comparison periods and assigned types.
2. the corresponding observed differences.
3. the reasons for the assignments.
4. limitations that materially affect interpretation.

Generate values and factual statements from the recorded evidence. Avoid maintaining separate manually entered numbers in the narrative.

Distinguish measures that determine an assignment from additional descriptive context. Do not rank differences expressed in incompatible units as if they shared a common importance scale. For unassigned or partly assessable events, explain the relevant limitation. A non-match must not be described as proof that no behavioural change occurred.

Only describe a change as sustained when the documented persistence criterion is supported. Preserve the observation boundary where the available follow-up ends.

Reuse suitable before-and-after tables and customer-history plots from Phase 3. Additional graphics should answer a specific interpretive question.

#### 5.3.5 Verify the implementation and prepare evaluation

Check the procedure using expected outcomes derived separately from the implementation. Include clear matches, non-matches, threshold boundaries, unsuitable denominators, missing evidence and compatible label combinations.

**Verify that:**
- implemented conditions match the codebook.
- rule outcomes correspond to the recorded measurements.
- conflicting combinations and execution failures are identified.
- descriptions contain correct values, units, directions and assignment reasons.
- consequential limitations remain visible.
- all input events are accounted for.
- fixed inputs and settings reproduce the same outputs.

Investigate differences from Phase 4 provisional assignments rather than automatically treating those assignments as correct. These checks establish implementation conformity and readiness for evaluation. They do not independently establish the taxonomy's validity or classification performance.

Freeze the relevant taxonomy, parameters, code and templates before processing reserved evaluation evidence in Phase 6. Document subsequent changes and their effects on the status of the evaluation.

### 5.4 Required outputs

**Produce:**
1. **Classification code and configuration:** Executable rules, adopted parameters and taxonomy version.
2. **Assignment records:** Event-level labels, per-type outcomes and reasons for withheld assignments.
3. **Supporting rule evidence:** Measurements and conditions sufficient to reconstruct each decision.
4. **Generated descriptions:** Structured records, rendered text and selected supporting displays.
5. **Verification and handover record:** Checks, corrections, unresolved restrictions and the fixed configuration for Phase 6.

Use linked tables where useful without requiring a separate file for every output. Export reusable tabular datasets as CSV, convert them to Parquet and use the Parquet versions subsequently.

Export figures and tables to the configured directories. Outputs derived from production data must follow the project's production-output configuration.

### 5.5 Completion criteria

**Phase 5 is complete when:**
- retained type definitions are implemented consistently.
- required calibration tasks are resolved.
- multiple assignments, non-matches and insufficient evidence are handled explicitly.
- every input event has a recorded processing outcome.
- descriptions correspond to the evidence and actual assignment conditions.
- meaningful verification checks pass.
- outputs are reproducible and the evaluation configuration is fixed.

Completion does not require a label for every event or the elimination of uncertainty. Unresolved specification problems or implementation errors that prevent trustworthy results must be corrected or explicitly restrict the affected scope.

### 5.6 Optional refinements

Optional refinements include additional text templates, targeted domain feedback or improved visual presentation where these address an identified limitation.

A learned classifier, surrogate model or additional explanation technique requires a distinct purpose and further evaluation. Such methods are not necessary for implementing the documented rules.

Prioritise correct assignments and accurate, complete descriptions before adding presentation complexity or alternative modelling approaches.

---

## Phase 6 - Evaluate and discuss findings

### 6.1 Purpose

Evaluate change detection, taxonomy applicability, automatic type assignment and generated descriptions using the procedures established in the project plan.

The evaluation combines controlled cases, held-out real customer histories and a limited sensitivity analysis. It examines the components separately and their interaction within the complete workflow.

The main output is an evidence-based assessment of the research questions, including successful results, errors, uncertainty and limitations. Evaluation does not require favourable findings or complete assignment coverage.

> **Methodological basis:** Detection evaluation draws on Truong et al. (2020), while controlled scenario design is informed by Morris et al. (2019). Taxonomy assessment follows Kundisch et al. (2022). Classification measures draw on Zhang and Zhou (2014) and Opitz (2024). Description assessment adapts the distinction between faithfulness and completeness in Song et al. (2024). Sampling, matching rules and review criteria are project-specific operational decisions.

### 6.2 Inputs

- The fixed detection procedure, preparation rules and feature definitions.
- The versioned taxonomy, assignment implementation and parameter configuration.
- Description templates and verification results from Phase 5.
- Controlled evaluation scenarios and reserved real customer histories.
- Records of development exposure and case-selection procedures.
- The main research question, four sub-questions and agreed evaluation scope.

Load tabular inputs from their Parquet versions. Cases previously used to revise the approach cannot subsequently be described as untouched evaluation evidence.

### 6.3 Core procedure

#### 6.3.1 Finalise the evaluation protocol

**Before inspecting evaluation results, record:**
- the claim assessed by each evaluation component.
- case-selection rules and available reference information.
- fixed versions of the data, code, taxonomy, parameters and templates.
- controlled scenarios and their separation from pilot scenarios or realisations.
- event-matching rules and temporal tolerance.
- metrics, denominators and treatment of undefined results.
- review instructions and planned sensitivity settings.

Use the development–evaluation boundaries established earlier. Address dependence between events from the same customer and overlapping observation windows. Specify the evidence required for each conclusion. If suitable reference information is unavailable, restrict the corresponding claim rather than substitute an unsupported score.

No universal accuracy target is imposed. Any acceptance criterion must be justified before examining the final results.

#### 6.3.2 Evaluate change detection

Use a compact controlled benchmark containing known changes and known no-change controls. Define reference events through the scenario construction independently of the detector's output.

Cover the core behavioural dimensions and selected variations in change magnitude, ordering activity and simultaneous changes. No-change controls should contain ordinary variation rather than only constant signals.

Preserve dependencies between generated measures. For example, total order value, order count and average order value must remain consistent. A profile-level generator is sufficient where the evaluation claim concerns detection from prepared profiles. A complete ERP simulator is not required.

Document the scenarios, repetitions and random seeds. Report variability across repeated realisations where used. The scenario specification and number of repetitions should reflect the intended assessment and available resources.

Apply the fixed detection and event-consolidation procedure. Match detected and reference events one-to-one within a predefined temporal tolerance. Maximise the number of valid matches and use timing distance to resolve competing matches deterministically. Count matched pairs as true positives, unmatched detections as false positives and unmatched reference events as false negatives.

| **Metric**                | **Definition**                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Precision**             | `TP / (TP + FP)`                                                                        |
| **Recall**                | `TP / (TP + FN)`                                                                        |
| **F1-score**              | `2 × TP / (2 × TP + FP + FN)`                                                           |
| **False-alarm frequency** | Detections in known no-change controls divided by their evaluated observation duration. |

Report undefined ratios explicitly when their denominators are zero. Accompany scores with counts, scenario characteristics and the numbers of excluded, unassessable or technically failed histories.

Do not automatically treat real histories as no-change controls. If changes are injected into real backgrounds, additional detections may reflect pre-existing changes. Only calculate precision or false-alarm measures where the reference information supports those judgements.

#### 6.3.3 Assess taxonomy applicability

Examine a documented selection of held-out real cases against the fixed taxonomy. Include straightforward patterns, combined changes, borderline cases and events with insufficient evidence or no assignment. Record the selection rationale and both customer and event counts.

**Assess:**
- whether the observed patterns can be represented within the declared scope.
- whether definitions and assignment criteria provide clear distinctions.
- whether combinations are coherent.
- which patterns remain inadequately represented.

Distinguish a conceptual gap from missing evidence, an out-of-scope pattern or criteria that are assessable but not met. An event receiving one label may still be inadequately represented in another dimension.

Report case evidence and counterexamples. A high assignment rate alone does not establish taxonomy quality, and frequencies in a purposive case collection do not estimate population prevalence.

#### 6.3.4 Evaluate automatic type assignment

First supply reference events directly to the classification component so that assignment errors can be examined separately from detection errors. Establish expected assignments from documented scenario expectations or manual examination of the evidence and codebook. Hide automatic assignments and generated descriptions during the initial manual assessment.

The reference must not be produced by the classification code being evaluated.

| **Measure**                              | **Required assessment**                                                                    |
| ---------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Exact-match ratio**                    | Proportion of evaluable events whose predicted type set exactly matches the reference set. |
| **Precision and recall per type**        | Incorrect and missed assignments for each type, with underlying counts.                    |
| **Unassigned and ambiguous proportions** | Frequency of withheld or unresolved assignments, with reasons.                             |

Retain distinctions between criteria not met, indeterminate and not applicable. Specify how these outcomes affect metric denominators. Do not silently exclude system abstentions where a definite reference assignment exists.

Investigate disagreements and preserve initial assessments separately from subsequent adjudication. Report automatic results separately from manual overrides. Where the thesis author performs the reference assessment alone, acknowledge reviewer dependence. Agreement with the codebook supports consistent application of the specified taxonomy; it does not independently establish an objectively correct behavioural classification.

#### 6.3.5 Evaluate generated descriptions

Check descriptions against their underlying measurements and the assignment conditions actually executed. Use a predefined checklist specifying factual-claim boundaries, numerical tolerances and the information required for each case.

| **Measure**             | **Project-specific calculation**                                                                          |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **Factual correctness** | Correct, source-supported factual claims divided by all assessed factual claims.                          |
| **Completeness**        | Correctly communicated required information items divided by all information items required for the case. |

Required information includes temporal context, affected measures, direction, magnitude, assignment rationale and applicable limitations.

Check for incorrect values, misleading units, unsupported persistence claims, omitted uncertainty and explanations inconsistent with the rules. Unsupported causal statements count as defects.

Record errors with their supporting evidence and report the numbers of descriptions and claims assessed. Missing descriptions remain recorded as output failures.

These measures adapt the evaluation dimensions discussed by Song et al. (2024). They do not constitute an implementation of the original FineSurE evaluator. Without a suitable user study, the findings do not establish comprehensibility or usefulness for sales staff.

#### 6.3.6 Examine the complete workflow and sensitivity

Process selected held-out customer histories through detection, automatic assignment and description generation. Reuse the real-case collection where appropriate. Complete any blinded assignment review before revealing the corresponding automatic results.

Examine how earlier errors or uncertainty affect later outputs. Include missed changes or false detections only where the reference evidence supports those judgements. Perform a limited sensitivity analysis using the alternatives specified in the protocol. Prioritise consequential choices such as comparison-window length, detection thresholds or assignment thresholds.

**Distinguish changes in:**
- detected events and their timing.
- type assignments.
- assessability and unresolved outcomes.
- description content.

Hold event evidence fixed when examining assignment thresholds where feasible. Otherwise, distinguish effects caused by changed event windows from effects caused by the assignment rules.

Preserve the primary configuration. Settings selected after inspecting evaluation outcomes represent further development and must not be presented as having been fixed in advance.

#### 6.3.7 Answer the research questions

Connect each sub-question to its findings, supporting evidence and limitations.

| **Sub-question**         | **Evaluation contribution**                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **SQ1 - Detection**      | Detection performance and failure conditions under the evaluated scenarios and available real-case evidence. |
| **SQ2 - Taxonomy**       | Supported distinctions, combinations, representational gaps and scope restrictions.                          |
| **SQ3 - Classification** | Agreement with reference assignments, type-specific errors and unresolved outcomes.                          |
| **SQ4 - Descriptions**   | Factual correctness, completeness and traceability to measurements and assignment criteria.                  |

Use these findings to answer the main research question. Distinguish the developed taxonomy, implemented procedure and empirical results. Discuss limitations arising from the observation window, customer selection, sparse activity, data quality, scenario assumptions, reviewer availability and the single-company context.

If evaluation prompts a correction, preserve the original results and document the revision. Reassessment using the same cases is development-informed. An independent reassessment requires suitable unused evidence.

### 6.4 Required outputs

**Produce:**
1. **Evaluation protocol:** Claims, evidence roles, sampling, matching, metrics and fixed configurations.
2. **Controlled benchmark results:** Scenario definitions, reference events, scores and relevant uncertainty.
3. **Real-case assessment:** Taxonomy findings, assignment comparisons and description checks.
4. **Complete-workflow and sensitivity findings:** Error propagation, alternative-setting results and failure cases.
5. **Research-question assessment:** Supported conclusions, limitations and unresolved questions.

Keep results traceable to their input data and configuration. Export reusable tabular datasets according to the [shared CSV-to-Parquet workflow](#data-formats-and-file-workflow) and save figures and tables in the configured directories.

### 6.5 Completion criteria

**Phase 6 is complete when:**
- the planned core assessments have been performed or their infeasibility and consequences are explained.
- results include interpretable counts, denominators and reference limitations.
- taxonomy applicability is distinguished from implementation conformity.
- description quality is distinguished from demonstrated user usefulness.
- the complete workflow and selected sensitivities have been examined.
- development-informed revisions remain distinguishable from the original evaluation.
- each research question has an evidence-based answer, including negative or inconclusive findings.

Completion does not require meeting an arbitrary performance threshold. Unsupported or unevaluated capabilities remain explicit limitations.

### 6.6 Optional refinements

Optional extensions include an additional reviewer, targeted reader-comprehension tasks, additional controlled scenarios or evaluation of an optional second detection method.

Undertake these extensions only after completing the core assessment and when they address a specific unresolved question.

Any additional claims must remain proportionate to the evidence collected.

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
