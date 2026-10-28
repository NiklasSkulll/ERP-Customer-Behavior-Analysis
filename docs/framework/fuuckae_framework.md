<div align="center">

# Framework for analysing and typing customer purchasing changes

[![Phase 1](https://img.shields.io/badge/Phase%201-Frame%20and%20inspect-%23352898?style=flat&labelColor=%2315934E)](#phase-1---frame-the-analysis-and-inspect-the-data)
[![Phase 2](https://img.shields.io/badge/Phase%202-Understand-%23352898?style=flat&labelColor=%2315934E)](#phase-2---understand-customer-histories-and-purchasing-patterns)
[![Phase 3](https://img.shields.io/badge/Phase%203-Unify%20and%20construct-%23352898?style=flat&labelColor=%2315934E)](#phase-3---unify-the-data-and-construct-reliable-customer-time-series)
[![Phase 4](https://img.shields.io/badge/Phase%204-Compare%20and%20characterise-%23352898?style=flat&labelColor=%2315934E)](#phase-4---compare-purchasing-profiles-and-characterise-candidate-changes)
[![Phase 5](https://img.shields.io/badge/Phase%205-Knowledge%20synthesis-%23352898?style=flat&labelColor=%2315934E)](#phase-5---knowledge-synthesis-develop-the-purchasing-change-taxonomy)
[![Phase 6](https://img.shields.io/badge/Phase%206-Apply%20and%20explain-%23352898?style=flat&labelColor=%2315934E)](#phase-6---apply-the-taxonomy-and-explain-assignment-outcomes)
[![Phase 7](https://img.shields.io/badge/Phase%207-Evaluate%20and%20reflect-%23352898?style=flat&labelColor=%2315934E)](#phase-7---evaluate-the-framework-and-reflect-on-findings)

</div>

## Table of Contents

- [Overview of the FUUCKAE framework](#overview-of-the-fuuckae-framework)
- [Phase 1 - Frame the analysis and inspect the data](#phase-1---frame-the-analysis-and-inspect-the-data)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Inputs and objectives](#12-inputs-and-objectives)
    - [1.3 Procedure](#13-procedure)
        - [1.3.1 Dataset and column documentation](#131-dataset-and-column-documentation)
        - [1.3.2 Coverage and quality checks](#132-coverage-and-quality-checks)
    - [1.4 Interpretation and boundaries](#14-interpretation-and-boundaries)
    - [1.5 Documentation and outputs](#15-documentation-and-outputs)
    - [1.6 Completion criteria](#16-completion-criteria)
- [Phase 2 - Understand customer histories and purchasing patterns](#phase-2---understand-customer-histories-and-purchasing-patterns)
    - [2.1 Purpose](#21-purpose)
    - [2.2 Inputs and objectives](#22-inputs-and-objectives)
    - [2.3 Procedure](#23-procedure)
        - [2.3.1 Customer assessment](#231-customer-assessment)
        - [2.3.2 Monthly profile definitions](#232-monthly-profile-definitions)
    - [2.4 Recommended tables and graphics](#24-recommended-tables-and-graphics)
    - [2.5 Interpretation and boundaries](#25-interpretation-and-boundaries)
    - [2.6 Documentation and outputs](#26-documentation-and-outputs)
    - [2.7 Completion criteria](#27-completion-criteria)
- [Phase 3 - Unify the data and construct reliable customer time series](#phase-3---unify-the-data-and-construct-reliable-customer-time-series)
    - [3.1 Purpose](#31-purpose)
    - [3.2 Inputs and objectives](#32-inputs-and-objectives)
    - [3.3 Procedure](#33-procedure)
        - [3.3.1 Preparation decision table](#331-preparation-decision-table)
        - [3.3.2 Cleaning and selection rules](#332-cleaning-and-selection-rules)
    - [3.4 Feature and time-series construction](#34-feature-and-time-series-construction)
    - [3.5 Verification tables and graphics](#35-verification-tables-and-graphics)
    - [3.6 Interpretation and boundaries](#36-interpretation-and-boundaries)
    - [3.7 Documentation and outputs](#37-documentation-and-outputs)
    - [3.8 Completion criteria](#38-completion-criteria)
- [Phase 4 - Compare purchasing profiles and characterise candidate changes](#phase-4---compare-purchasing-profiles-and-characterise-candidate-changes)
    - [4.1 Purpose](#41-purpose)
    - [4.2 Inputs and objectives](#42-inputs-and-objectives)
    - [4.3 Procedure](#43-procedure)
        - [4.3.1 Analysis specification](#431-analysis-specification)
        - [4.3.2 Detection approaches](#432-detection-approaches)
    - [4.4 Event and feature descriptions](#44-event-and-feature-descriptions)
    - [4.5 Review and sensitivity checks](#45-review-and-sensitivity-checks)
    - [4.6 Recommended tables and graphics](#46-recommended-tables-and-graphics)
    - [4.7 Evidence for taxonomy development](#47-evidence-for-taxonomy-development)
    - [4.8 Interpretation and boundaries](#48-interpretation-and-boundaries)
    - [4.9 Documentation and outputs](#49-documentation-and-outputs)
    - [4.10 Completion criteria](#410-completion-criteria)
- [Phase 5 - Knowledge synthesis: Develop the purchasing-change taxonomy](#phase-5---knowledge-synthesis-develop-the-purchasing-change-taxonomy)
    - [5.1 Purpose](#51-purpose)
    - [5.2 Inputs and objectives](#52-inputs-and-objectives)
    - [5.3 Procedure](#53-procedure)
        - [5.3.1 Taxonomy purpose, scope and organising perspective](#531-taxonomy-purpose-scope-and-organising-perspective)
        - [5.3.2 Development evidence and case selection](#532-development-evidence-and-case-selection)
        - [5.3.3 Iterative development and revision](#533-iterative-development-and-revision)
    - [5.4 Taxonomy structure and type definitions](#54-taxonomy-structure-and-type-definitions)
        - [5.4.1 Dimensions, characteristics and overlapping types](#541-dimensions-characteristics-and-overlapping-types)
        - [5.4.2 Proposed assignment criteria and parameter decisions](#542-proposed-assignment-criteria-and-parameter-decisions)
        - [5.4.3 Ambiguous cases and insufficient evidence](#543-ambiguous-cases-and-insufficient-evidence)
    - [5.5 Development checks and revision record](#55-development-checks-and-revision-record)
    - [5.6 Interpretation and boundaries](#56-interpretation-and-boundaries)
    - [5.7 Documentation and outputs](#57-documentation-and-outputs)
    - [5.8 Completion criteria](#58-completion-criteria)
- [Phase 6 - Apply the taxonomy and explain assignment outcomes](#phase-6---apply-the-taxonomy-and-explain-assignment-outcomes)
    - [6.1 Purpose](#61-purpose)
    - [6.2 Inputs and objectives](#62-inputs-and-objectives)
    - [6.3 Procedure](#63-procedure)
        - [6.3.1 Operational specification and deferred calibration](#631-operational-specification-and-deferred-calibration)
        - [6.3.2 Rule implementation and verification](#632-rule-implementation-and-verification)
        - [6.3.3 Systematic assignment and unresolved outcomes](#633-systematic-assignment-and-unresolved-outcomes)
    - [6.4 Explanation construction](#64-explanation-construction)
        - [6.4.1 Observed differences and assignment reasons](#641-observed-differences-and-assignment-reasons)
        - [6.4.2 Structured evidence and text templates](#642-structured-evidence-and-text-templates)
        - [6.4.3 Supporting tables and graphics](#643-supporting-tables-and-graphics)
    - [6.5 Verification and evaluation handover](#65-verification-and-evaluation-handover)
    - [6.6 Interpretation and boundaries](#66-interpretation-and-boundaries)
    - [6.7 Documentation and outputs](#67-documentation-and-outputs)
    - [6.8 Completion criteria](#68-completion-criteria)
- [Phase 7 - Evaluate the framework and reflect on findings](#phase-7---evaluate-the-framework-and-reflect-on-findings)
    - [7.1 Purpose](#71-purpose)
    - [7.2 Inputs and prerequisites](#72-inputs-and-prerequisites)
    - [7.3 Procedure](#73-procedure)
        - [7.3.1 Specify evaluation claims and evidence roles](#731-specify-evaluation-claims-and-evidence-roles)
        - [7.3.2 Freeze the evaluation configuration](#732-freeze-the-evaluation-configuration)
        - [7.3.3 Evaluate change detection](#733-evaluate-change-detection)
            - [7.3.3.1 Controlled benchmark design](#7331-controlled-benchmark-design)
            - [7.3.3.2 Reference matching](#7332-reference-matching)
            - [7.3.3.3 Performance reporting](#7333-performance-reporting)
            - [7.3.3.4 Supplementary semi-synthetic and real-data evidence](#7334-supplementary-semi-synthetic-and-real-data-evidence)
        - [7.3.4 Evaluate taxonomy applicability](#734-evaluate-taxonomy-applicability)
        - [7.3.5 Evaluate assignment consistency](#735-evaluate-assignment-consistency)
        - [7.3.6 Evaluate explanation quality](#736-evaluate-explanation-quality)
        - [7.3.7 Assess sensitivity and failure cases](#737-assess-sensitivity-and-failure-cases)
        - [7.3.8 Reflect on findings and research questions](#738-reflect-on-findings-and-research-questions)
    - [7.4 Outputs](#74-outputs)
    - [7.5 Completion criteria](#75-completion-criteria)
    - [7.6 Limitations and interpretation](#76-limitations-and-interpretation)
- [Bibliography](#bibliography)

---

## Overview of the FUUCKAE framework

The **FUUCKAE framework** sets out a _seven-phase workflow_ for retrospectively analysing purchasing changes among B2B wholesale customers using ERP data. It connects data understanding and preparation with candidate-change detection, taxonomy development, type assignment and evaluation. Its purpose is to produce traceable descriptions of observable purchasing changes and explain their classification under explicit rules.

**Phases 1–3** establish the analytical context, explore customer histories and construct reproducible customer-period datasets. **Phase 4** identifies candidate change events and describes their timing, affected dimensions, magnitude and observed persistence. **Phase 5** combines conceptual foundations with development cases to define a purchasing-change taxonomy. **Phase 6** applies this taxonomy and explains assignment outcomes using recorded evidence and executed rules. **Phase 7** evaluates detection, taxonomy applicability, assignment consistency, explanation quality and sensitivity, then relates the findings to the research questions.

**The workflow is iterative:** findings may require documented revisions to earlier phases. Each phase specifies its inputs, activities, outputs and completion criteria, while preserving uncertainty and known data limitations. Development evidence is distinguished from evidence reserved for evaluation. Conclusions remain restricted to purchasing observed with the focal wholesaler and to the capabilities supported by the assessment.

---

## Phase 1 - Frame the analysis and inspect the data

### 1.1 Purpose

**Phase 1** frames the analysis around the thesis research question and establishes a documented understanding of the ERP datasets, their structure, meaning, relationships, coverage and initial quality. It assesses their potential to support the detection, typing and explainable description of purchasing changes among B2B wholesale customers.

The resulting dataset inventory, preliminary data dictionary and readiness assessment guide customer-history exploration in Phase 2 and data preparation in Phase 3. Expected tables and fields remain requirements to verify against the received extracts, while inspection findings remain provisional and unresolved limitations require documented follow-up.

> **Methodological basis:** This phase adapts the dataset-description and data-quality assessment activities of CRISP-DM's data-understanding phase (IBM, n.d., pp. 13–16). The ERP-specific inspection checks, field requirements and readiness criteria are project-specific decisions requiring justification.

### 1.2 Inputs and objectives

**Inputs:**
- The thesis research question and defined scope.
- Available ERP extracts and their extraction information, once received.
- Available field descriptions, business definitions and data-source documentation.

Missing inputs are recorded explicitly. Their absence may restrict execution but does not prevent defining the procedure.

**Objectives:**
- Identify what each dataset and row represent.
- Establish which required fields are present and what they mean.
- Assess whether datasets can be linked without unintended duplication or loss.
- Describe temporal coverage and the distribution of customer activity.
- Identify initial quality concerns and questions requiring further investigation.

### 1.3 Procedure

| **Activity**                         | **Checks and decisions**                                                                                                                                                                                                                                           | **Recorded output**                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **1. Frame the analysis**            | Record the research objective, scope, expected purchasing dimensions and intended observation levels: order, order line, customer and customer-period. Distinguish documented information from assumptions.                                                        | Analysis context and assumptions                              |
| **2. Inventory and load datasets**   | Record source, extraction date, file format and documented extraction filters. Check loading success, parsing settings, row and column counts and sample records. Compare received tables with the expected order header, order line, product and customer tables. | Dataset inventory and loading issues                          |
| **3. Inspect structure and meaning** | Record column names, technical types, example values, units and semantic roles. Verify the meaning of dates, quantities, monetary amounts, discounts and status fields against available documentation.                                                            | Preliminary data dictionary and field-availability assessment |
| **4. Check keys and relationships**  | Check missing and duplicate candidate keys, expected relationship cardinalities and unmatched references between tables. Distinguish exact duplicate rows from legitimate repeated business records.                                                               | Relationship map and integrity flags                          |
| **5. Scan coverage and quality**     | Apply the checks below to relevant tables and fields. Use descriptive summaries and selected graphics to identify issues requiring investigation.                                                                                                                  | Initial quality and coverage profile                          |
| **6. Assess readiness**              | Summarize available evidence, unresolved meanings, missing requirements and preparation needs. Specify which subsequent analyses can proceed and which are restricted.                                                                                             | Readiness assessment and issue register                       |

#### 1.3.1 Dataset and column documentation

- _Dataset description:_ 1–2 sentences explaining what each dataset contains and what one row represents.
- _Column description:_ 1–2 sentences per column explaining its meaning, including units or business codes where relevant.
- _Data type:_ the observed technical type and, where different, the intended type.
- _Definition status:_ whether the meaning is documented, assumed or unresolved.

#### 1.3.2 Coverage and quality checks

| **Area**                       | **Minimum assessment**                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **Field availability**         | Required fields present, absent or available through another table. Meaning confirmed or unresolved.                     |
| **Missing values**             | Counts and percentages per relevant field, including documented placeholder values.                                      |
| **Identifiers and duplicates** | Missing identifiers, repeated candidate keys, exact duplicate rows and unmatched join references.                        |
| **Time coverage**              | Earliest and latest dates, records per period, apparent gaps and first-to-last observed order span per customer.         |
| **Customer activity**          | Number of observed customers and distributions of orders and active periods per customer.                                |
| **Numerical plausibility**     | Selected summary statistics, zero and negative values, non-finite values, extreme values, currencies and quantity units. |
| **Categories and statuses**    | Distinct values and frequencies, inconsistent labels, product-group coverage and observed order-status categories.       |

**Suitable orientation graphics _(only when informative)_:**
- Missing-value percentages by field.
- Number of orders or records per month, with the counting unit stated.
- Distribution of order counts or observed history spans per customer.

An observed history span does not establish continuous data coverage. Similarly, a period without recorded orders may reflect inactivity or missing records. Phase 1 flags the ambiguity rather than resolving it automatically.

### 1.4 Interpretation and boundaries

- Preserve the original extracts. Document parsing and any temporary transformations required for inspection.
- Treat unusual values as flags, not automatic errors. Do not delete, impute or exclude records solely because they are missing, duplicated, zero, negative or extreme.
- Treat proposed business filters, such as excluding open orders, as decisions requiring justification against the intended measurement.
- Perform relationship checks without creating an unverified merged analysis table. In particular, joining headers to multiple order lines can duplicate order-level amounts.
- Keep conclusions descriptive and provisional. Detailed pattern analysis, final cleaning rules, feature construction, detection and typing are outside this phase.

### 1.5 Documentation and outputs

**Record the inspection in one reproducible notebook or equivalent scripted report containing:**
1. Analysis context and dataset inventory.
2. Preliminary data dictionary and relationship map.
3. Quality and coverage summaries, with selected graphics.
4. Issue register and readiness assessment.

For each issue, record the affected table or field, observed evidence, potential analytical consequence and required follow-up. Distinguish **observed**, **documented**, **assumed** and **unresolved** information. Record the input version, inspection code and relevant execution settings.

### 1.6 Completion criteria

Phase 1 is complete when applicable checks have been performed, their outputs recorded and unresolved issues assigned a follow-up action. The readiness assessment must distinguish analyses that can proceed from those requiring clarification or additional data.

Complete or error-free data is not a completion requirement. However, if access or loading prevents the core inspection, record the phase as **blocked or partially completed**, rather than claiming that the data has been assessed.

---

## Phase 2 - Understand customer histories and purchasing patterns

### 2.1 Purpose

**Phase 2** builds on the initial inspection to examine customer histories, record usability and purchasing patterns. It uses provisional customer-period profiles, initially monthly, to investigate activity, temporal variation, relationships between purchasing measures and differences between customer groups. Exploration addresses explicit questions while allowing additional questions to emerge from the findings.

The resulting customer assessments, descriptive findings and preparation recommendations inform eligibility rules, feature definitions and data preparation in Phase 3, as well as the analysis design in Phase 4. Findings remain provisional: apparent changes and associations require further investigation, while formal detection, taxonomy development and independent evaluation belong to subsequent phases.

> **Methodological basis:** This phase adapts the exploration activities of CRISP-DM's data-understanding phase (IBM, n.d., pp. 13–16), informed by exploratory data-analysis principles (Heckert & Filliben, 2003, Section 1.1.1). Limited preparation and renewed investigation are consistent with CRISP-DM's recognition that exploration may require prior processing and movement between phases (IBM, n.d., p. 15). The customer assessments, proposed observation window, provisional profile definitions, temporal aggregation and selected analyses are project-specific decisions requiring justification.

### 2.2 Inputs and objectives

**Inputs:**
- Original ERP extracts and reproducible loading code.
- Phase 1 inventory, data dictionary, relationship checks and quality findings.
- The thesis research question and unresolved-issue register.

**Objectives:**
- Assess customer histories, purchasing activity and record usability.
- Construct provisional monthly purchasing profiles with explicit definitions.
- Explore distributions, temporal patterns, relationships and customer-group differences.
- Investigate issues that could distort interpretation.
- Recommend preparation rules, customer eligibility criteria and suitable analytical representations.

No data availability, sufficiency threshold or cleaning rule is assumed in advance. Analyses dependent on unresolved issues remain restricted or provisional.

### 2.3 Procedure

| **Activity**                                      | **Checks and decisions**                                                                                                                                                                                                            | **Recorded output**                                         |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **1. Assess customer histories and suitability**  | Examine the proposed two-year window, customer activity and record-level concerns. Distinguish extraction coverage, observed purchasing history and suitability for a particular analysis.                                          | Customer assessment table and unresolved coverage questions |
| **2. Prepare exploratory views**                  | Apply necessary documented conversions, verified joins and justified corrections to working copies. Check row counts, unmatched records and relevant totals before and after transformations.                                       | Reproducible working views and transformation log           |
| **3. Build provisional monthly profiles**         | Define the date, order-counting unit, monetary measure and record treatment before aggregation. Summarize each assessable customer by month. Flag restricted profiles and uncertain periods.                                        | Customer-month table and profile definitions                |
| **4. Explore patterns and relationships**         | Examine distributions, order intervals, temporal variation, product mix and relationships among available measures. Compare existing customer groups and varied individual histories. Extend exploration where new questions arise. | Tables, graphics and exploratory findings                   |
| **5. Investigate quality consequences**           | Examine whether missing or questionable records concentrate in particular periods or groups. Where useful, compare plausible treatments without silently adopting a final rule.                                                     | Issue-specific evidence and proposed treatments             |
| **6. Recommend preparation and analysis choices** | Consolidate evidence for eligibility, record treatment, measures and temporal aggregation. Record alternatives, limitations and questions requiring follow-up.                                                                      | Decision register and preparation recommendations           |

Activities may be revisited. If a problem prevents trustworthy interpretation, address it or restrict the affected analysis before proceeding.

#### 2.3.1 Customer assessment

**Create one row per customer containing, where measurable:**
- Customer identifier and existing business group, if available.
- First and last observed order dates in the extract and activity within the assessment window.
- Distinct order count, active-month count and distribution of intervals between orders.
- Periods without recorded orders, with coverage uncertainty distinguished from inactivity.
- Counts and proportions of records affected by relevant quality issues.
- Provisional suitability for the intended analysis, reasons and required follow-up.

Specify the assessment window's start and end dates, preferably using complete calendar months. **Twenty-four months is a proposed window, not proof of sufficient information.** A first-to-last order span does not establish continuous coverage.

> **Require neither a purchase every month nor recent activity merely to qualify:** such rules could remove declining or inactive customers of research interest. Distinguish customers first observed recently from customers confirmed to be newly acquired.

#### 2.3.2 Monthly profile definitions

| **Measure**                   | **Definition to establish before interpretation**                                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Order count**               | Count distinct orders using the verified key and selected order date. Do not count order lines as separate orders.                                          |
| **Purchasing value**          | Specify the monetary field, currency, aggregation level and treatment of cancellations, returns and credits. Avoid duplicating header amounts across lines. |
| **Product mix**               | Specify product groups and whether composition is measured by value, order incidence or another interpretable basis. State the denominator.                 |
| **Quantity, when meaningful** | Aggregate only compatible units or documented conversions. Do not sum heterogeneous quantities without justification.                                       |

For each measure, distinguish an observed zero from an unknown or unobserved value. Zero-fill only when coverage, customer observation and record definitions support that interpretation. Flag partial months. Monthly aggregation is an initial exploratory representation. Compare alternatives if sparse or irregular activity makes it uninformative.

### 2.4 Recommended tables and graphics

Select displays to answer questions. This is a recommendation set, not a requirement to produce every chart for every field or customer.

| **Question**                                                    | **Recommended table or graphic**                                                                        | **Interpretation focus**                                                                                                             |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Which customer histories are assessable?**                    | Customer assessment table. Summary counts by provisional suitability and reason.                        | Coverage, activity and quality are separate dimensions.                                                                              |
| **How much activity and history do customers have?**            | Histograms of order counts, active months and observed history spans.                                   | Heterogeneity and sparsity. Show the population and window.                                                                          |
| **Where are inactive or uncertain periods?**                    | Customer-by-month activity heatmap for a documented sample, sorted by activity or group.                | Distinguish zero activity from unknown coverage visually.                                                                            |
| **What do individual monthly histories look like?**             | Small-multiple line charts or monthly bars for order count and purchasing value.                        | Use separate panels. Retain gaps for unknown values and comparable scales where comparison is intended.                              |
| **Are patterns shared across time?**                            | Monthly total and active-customer-count plots. Calendar-month comparisons if sufficient history exists. | Changing customer composition and incomplete months may affect totals. Two years provides limited evidence of recurring seasonality. |
| **How do purchasing measures vary and relate?**                 | Distribution plots. Selected scatterplots, such as order count versus purchasing value.                 | State whether points represent customers, orders or customer-months. Association does not establish cause.                           |
| **Do existing customer groups differ?**                         | Group summary table with sample sizes, medians and quartiles. Boxplots.                                 | Compare activity, purchasing value and history while acknowledging unequal coverage.                                                 |
| **How does product mix differ or change?**                      | Ranked product-group bars. Selected composition charts across periods.                                  | Show the share denominator. Handle negative values before interpreting percentage composition.                                       |
| **Where do data issues concentrate, and do treatments matter?** | Missingness or issue-rate tables by period/group. Side-by-side summaries under plausible rules.         | Show counts, denominators and consequences for records, customers and profiles.                                                      |

Document how example customers are selected. Include varied activity levels, values and history lengths, rather than only striking patterns. Do not produce an unreadable chart containing all customer histories.

### 2.5 Interpretation and boundaries

- _Preparation:_
    - Preserve original extracts.
    - Record every exploratory transformation and its effects.
    - Do not automatically delete, impute or exclude records because of missing, negative, duplicated or extreme values.
- _Decisions:_
    - Necessary corrections may occur during exploration.
    - Substantive eligibility and cleaning rules require evidence and justification.
    - Systematic application belongs to the subsequent preparation phase.
- _Grouping:_
    - Explore existing business groups first.
    - Optional descriptive categories must have explicit definitions.
    - Algorithmic clustering requires a stated purpose, justified inputs and a separate assessment of its usefulness. It is not a mandatory Phase 2 output.
- _Claims:_
    - Treat apparent changes and associations as exploratory observations.
    - Recorded spending differences do not alone identify behavioural causes.
    - Formal change detection, final taxonomy construction and validation remain outside this phase.
- _Evaluation:_
    - Record cases and periods used to develop decisions.
    - Reusing them later does not constitute independent validation.

### 2.6 Documentation and outputs

**Record the exploration in a reproducible notebook or equivalent scripted report containing:**
1. Customer assessment table and provisional suitability summary.
2. Monthly profiles, definitions and transformation log.
3. Selected tables and graphics, with findings and limitations.
4. Decision register, preparation recommendations and unresolved issues.

For each exploration, record **question → analysis → observation → implication → limitation**. For each proposed rule, record its rationale, supporting evidence, affected records or customers, alternatives and status: proposed, adopted for exploration or unresolved. Record input versions, execution settings and any sampling procedure or random seed used.

### 2.7 Completion criteria

Phase 2 is complete when customer suitability and the principal exploration questions have been assessed, applicable monthly profiles have been produced and preparation recommendations are supported by recorded evidence. Additional questions must be answered, deferred with a reason or marked unresolved.

Completion does not require exhaustive exploration, error-free data or fixed thresholds. Blocked core activities must be identified explicitly, with consequences and follow-up actions. They must not be reported as completed assessments.

---

## Phase 3 - Unify the data and construct reliable customer time series

### 3.1 Purpose

**Phase 3** translates the findings from Phases 1 and 2 into justified preparation rules and reproducible datasets for subsequent purchasing-change analysis. It systematically applies and verifies cleaning, table integration, feature construction and customer eligibility decisions, preserving original extracts and documenting transformations.

The resulting cleaned source tables, customer-period profiles and eligibility records provide the data basis for candidate-change analysis in Phase 4 and subsequent taxonomy development and application. Explicit feature definitions, coverage indicators and preparation records make these outputs interpretable and traceable. Data readiness is assessed against the intended analysis, with unresolved limitations documented rather than assuming that prepared data is complete or error-free.

> **Methodological basis:** This phase adapts the data-selection, cleaning, integration, construction and formatting activities of CRISP-DM's data-preparation phase (IBM, n.d., pp. 19–22), informed by tidy-data principles for organising observations and variables (Wickham, 2014). Data-leakage research informs the separation of evidence used to develop preparation rules or estimate transformations from evidence reserved for independent evaluation, according to the intended research claim (Kapoor & Narayanan, 2023). The ERP-specific treatments, customer eligibility rules, feature definitions and temporal aggregation are project-specific decisions requiring justification.

### 3.2 Inputs and objectives

**Inputs:**
- Original ERP extracts and their extraction information.
- Phase 1 data dictionary, relationship checks and quality assessment.
- Phase 2 exploratory findings, provisional profiles and preparation recommendations.
- Research scope and the intended use of data in development and evaluation.

**Objectives:**
- Apply explicit, justified cleaning and selection rules.
- Integrate tables without unintended duplication or loss.
- Define and calculate interpretable purchasing measures.
- Construct consistent customer-period histories and document analytical eligibility.
- Export reproducible datasets with sufficient information to interpret and reload them correctly.

Rules requiring empirical evidence remain conditional until execution. Missing information must not be replaced by unsupported assumptions.

### 3.3 Procedure

| **Activity**                                       | **Checks and decisions**                                                                                                                                                                     | **Recorded output**                                       |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **1. Specify preparation rules**                   | Define the observation window, relevant records, status treatment, quality rules and proposed eligibility criteria using Phase 2 evidence. Record unresolved choices and their consequences. | Preparation decision table.                               |
| **2. Clean and standardise source tables**         | Correct verified errors. Harmonise identifiers, dates, codes and units. Retain, flag or exclude questionable records according to justified rules. Preserve source-record references.        | Cleaned source tables and cleaning log.                   |
| **3. Integrate relevant tables**                   | Apply verified joins and check unmatched keys, row counts and relevant totals. Aggregate order-line information before combining it with order-level amounts where necessary.                | Validated transaction views and join reconciliation.      |
| **4. Construct customer-period profiles**          | Calculate features using explicit formulas and calendar rules. Distinguish inactivity, missing observations and undefined measures. Retain quality and coverage indicators.                  | Customer-period table and feature specification.          |
| **5. Confirm analytical eligibility**              | Reassess usable history and activity after preparation. Record eligibility for each intended analysis and exclusion reasons. Compare included and excluded customers descriptively.          | Eligibility table and selection summary.                  |
| **6. Prepare method-specific variants, if needed** | Apply only transformations justified by later methods. Preserve untransformed measures and document fitted parameters and the data used to estimate them.                                    | Optional analytical variants and transformation settings. |
| **7. Verify and export outputs**                   | Check keys, formulas, totals, missingness and transformation effects. Save versioned CSVs, schemas, code and execution settings. Verify correct reloading.                                   | Prepared datasets and verification report.                |

Revisit earlier activities when checks reveal problems. Customer selection may require iteration because cleaning can change the usable history. Model-specific transformations can be deferred until their requirements are established.

#### 3.3.1 Preparation decision table

**For each rule, record:**
- Affected table, field or record group.
- Evidence from inspection, exploration or source documentation.
- Action and rationale, including relevant alternatives.
- Number of affected records and customers, with denominators where appropriate.
- Consequences for later analysis and remaining limitations.

Separate technical corrections from business-scope exclusions. A cancelled order, credit note or large project order may be a valid business record even when excluded from a particular analytical view.

#### 3.3.2 Cleaning and selection rules

| **Issue**                                | **Required treatment**                                                                                                                                                        |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identifiers and duplicates**           | Preserve identifier semantics, including leading zeros. Remove only confirmed duplicate representations. Repeated business events are not automatically duplicates.           |
| **Dates and statuses**                   | Specify the relevant event date and included statuses. Do not automatically exclude open orders if the object of analysis is order placement.                                 |
| **Missing or questionable values**       | Correct only with supporting evidence. Otherwise retain with a flag, restrict the affected measure, or exclude with justification. Imputation requires an explicit rationale. |
| **Returns, credits and negative values** | Establish their business meaning and whether to retain, separate or exclude them for each measure.                                                                            |
| **Extreme values and project business**  | Investigate before treatment. Do not automatically smooth, cap or remove values that may represent meaningful changes.                                                        |
| **Currencies, units and categories**     | Combine only compatible values or use documented conversions. Record limitations of historical category mappings.                                                             |
| **Customer eligibility**                 | Justify rules against the intended analysis. Treat 24 months as a proposed window, not a universal sufficiency threshold. Do not require recent purchasing merely to qualify. |

### 3.4 Feature and time-series construction

Maintain a **feature specification table** containing each measure's intended meaning, formula, source fields, unit, aggregation rule, missing-value treatment and interpretation limits.

| **Measure**                                 | **Preparation requirement**                                                                                                                               |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purchasing value**                        | Specify the monetary basis, currency and treatment of adjustments. Avoid repeating header amounts across order lines.                                     |
| **Order frequency**                         | Count distinct orders using the verified key and selected date.                                                                                           |
| **Average order value**                     | Divide the relevant purchasing value by the corresponding order count. With no orders, the average is undefined rather than zero.                         |
| **Assortment breadth and product mix**      | Define categories, category coverage and the mix denominator. Document unknown classifications.                                                           |
| **Discount and margin measures, if usable** | Verify definitions and weighting. Define treatment of zero or otherwise unsuitable denominators. Recorded discounts do not establish discount dependence. |
| **Quantity measures, if usable**            | Aggregate within compatible units or documented conversions.                                                                                              |

**Time-series rules:**
- Use one row per customer and period in the principal profile table, initially monthly unless evidence justifies another resolution.
- Define window boundaries, partial-period treatment and the customer observation period.
- Record zero activity only when coverage and observation support that interpretation. Preserve unknown periods as unknown.
- Retain interpretable values in their original units alongside any transformed variants.
- Document dependencies between measures, such as purchasing value, frequency and average order value, to inform later feature selection.

### 3.5 Verification tables and graphics

| **Recommended output**                               | **Purpose**                                                                                                    |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Record and customer selection table**              | Show counts retained or excluded at each step, with reasons.                                                   |
| **Join reconciliation table**                        | Check key cardinalities, unmatched records and monetary totals before and after integration.                   |
| **Feature validation table**                         | Report uniqueness of customer-period keys, formula checks, missingness, undefined values and plausible ranges. |
| **Selected before-and-after profile plots**          | Check whether preparation alters the apparent purchasing pattern. Explain observed differences.                |
| **Alternative-rule comparison, where consequential** | Assess whether a disputed treatment materially changes histories, features or eligibility.                     |

Checks should reconcile aggregates to the corresponding included source records. Differences caused by intentional exclusions or conversions must be explainable. Use graphics only where they reveal effects more clearly than tables.

### 3.6 Interpretation and boundaries

- Preserve original data and trace prepared records back to their source.
- Do not choose preparation rules to create anticipated change types or improve apparent detection performance.
- If cases or periods are reserved for independent evaluation, do not use them to fit or tune transformations intended to be evaluated on that evidence. Record data already used in exploration as development evidence.
- _Match information availability to the claim:_ retrospective analysis may use a full historical sequence, whereas a claim of detection at a particular time must respect what was available then.
- Formal change detection, final type definitions and taxonomy evaluation remain outside this phase.

### 3.7 Documentation and outputs

| **Output**                      | **Contents**                                                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Cleaned source CSVs**         | Separate prepared order-header, order-line, customer and product tables, where available and relevant.                      |
| **Customer-period CSV**         | Calculated purchasing measures, period identifiers and relevant coverage or quality flags.                                  |
| **Eligibility CSV**             | Customer-level eligibility for intended analyses, reasons and restrictions.                                                 |
| **Cleaning and exclusion logs** | Applied rules, affected source-record identifiers, actions and reasons. Preserve excluded records in the original extracts. |
| **Preparation documentation**   | Feature specifications, schemas, validation results, code, input/output versions and execution settings.                    |

CSV files do not preserve data types. Document encoding, delimiter, decimal notation, date format, missing-value representation and intended column types. Verify that exported files reload with identifiers, dates and missing values interpreted correctly.

### 3.8 Completion criteria

Phase 3 is complete when the prepared datasets can be regenerated, cleaning and eligibility rules are justified, feature definitions are explicit, required checks pass and remaining restrictions are documented. Unresolved issues that prevent a core analysis must be recorded as blockages rather than hidden through arbitrary corrections.

---

## Phase 4 - Compare purchasing profiles and characterise candidate changes

### 4.1 Purpose

**Phase 4** uses the customer-period profiles prepared in Phase 3 to retrospectively identify candidate purchasing changes and describe their timing, affected dimensions, direction, magnitude and observed persistence. The unit of analysis is a **candidate change event within a customer's history**, and one customer may contribute several events.

The resulting event register, linked feature descriptions and documented development cases provide the empirical basis for taxonomy development in Phase 5. Candidates remain method-dependent findings requiring interpretation. Detection alone does not establish statistical significance, commercial relevance or membership in a change type. Before-and-after feature differences describe what changed without automatically explaining the detector's decision or the causes of customer behaviour.

> **Methodological basis:** This phase draws on retrospective change-point detection methodology, including window-based approaches and the explicit specification of the properties investigated and detection procedure (Truong et al., 2020). PELT provides an optional segmentation approach that optimises a specified penalised cost, requiring an appropriate cost function and justified penalty and segment-length settings (Killick et al., 2012). Data-leakage research informs the separation of evidence used to develop detection settings and analytical rules from evidence reserved for independent evaluation (Kapoor & Narayanan, 2023). The comparison windows, candidate-selection criteria, event-consolidation rules, descriptive measures of magnitude and persistence, and selection of taxonomy-development cases are project-specific decisions requiring justification.

### 4.2 Inputs and objectives

**Inputs:**
- Prepared customer-period profiles from Phase 3, including interpretable measures and any documented analytical variants.
- Feature definitions, eligibility rules, quality indicators and coverage information.
- Exploratory findings and unresolved limitations from Phase 2.
- Documented separation between development data and evidence reserved for later evaluation, where applicable.

**Objectives:**
- Specify a reproducible procedure for identifying candidate changes.
- Describe each event using consistent before-and-after comparisons.
- Assess sensitivity to plausible analytical settings and identify ambiguous cases.
- Assemble varied development cases for constructing the taxonomy.

The analysis is retrospective by default. Window lengths, thresholds, penalties and minimum data requirements must be justified during execution rather than treated as universal constants.

### 4.3 Procedure

| **Activity**                                  | **Checks and decisions**                                                                                                                                                                                                     | **Recorded output**                                |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **1. Specify the analysis design**            | Define target purchasing dimensions, changes of interest, temporal resolution, feature selection and minimum support on both sides of a comparison. Identify restrictions arising from missingness, sparsity or seasonality. | Analysis specification and decision register.      |
| **2. Establish a window-comparison baseline** | Define reference and subsequent windows, summary measures, comparison scores and candidate-selection rules. Document window movement and treatment of incomplete or unsuitable comparisons.                                  | Reproducible baseline procedure.                   |
| **3. Identify candidate changes**             | Apply the baseline to eligible histories. Use PELT as a second approach where its assumptions and data requirements are justified. Preserve method-specific results and settings.                                            | Initial candidate-event register.                  |
| **4. Construct change descriptions**          | Calculate before-and-after profiles, feature differences, observed persistence and supporting data counts using explicit definitions.                                                                                        | Event descriptions and feature-level change table. |
| **5. Review context and sensitivity**         | Inspect candidates alongside original-unit profiles and quality flags. Compare selected alternative settings and record method disagreements. Consolidate repeated detections under documented rules.                        | Reviewed event register and sensitivity findings.  |
| **6. Assemble taxonomy-development evidence** | Select varied candidates, borderline cases and a documented sample of histories without detections. Record selection criteria and manually identified patterns separately.                                                   | Development case collection for Phase 5.           |

Activities may be revisited when findings expose inadequate comparisons or preparation issues. Changes to prepared data belong in a versioned revision of Phase 3, followed by regeneration of affected results.

#### 4.3.1 Analysis specification

| **Decision**                     | **Required specification**                                                                                                                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Target changes**               | State which properties are investigated, initially purchasing levels and composition. Record whether gradual changes, variability changes or isolated events are within the chosen method's scope. |
| **Feature selection**            | Distinguish features used to identify candidates from those used only to describe them. Document scaling, weighting and dependencies between measures.                                             |
| **Comparison windows**           | Define reference and subsequent periods, their lengths, movement and minimum usable observations. Prefer adjacent, non-overlapping windows within each baseline comparison. Document alternatives. |
| **Candidate-selection criteria** | Specify comparison scores and thresholds, including data-support requirements and any magnitude or persistence filters. Record the rationale and development data used.                            |
| **Seasonality and context**      | State how recurring patterns, project business, incomplete periods and changing data coverage are considered. Record unresolved ambiguities rather than assuming every difference is behavioural.  |
| **Repeated detections**          | Define when nearby or overlapping detections represent the same candidate event. Preserve original detections and links to consolidated events.                                                    |
| **Evaluation separation**        | Keep tuning decisions within development evidence. Document which cases and periods have already informed the design.                                                                              |

With short monthly histories, limit model complexity and avoid requiring more segments or seasonal information than the observations support. A history without sufficient comparison support is marked **not assessable**, rather than **no change**.

#### 4.3.2 Detection approaches

| **Approach**                        | **Intended role**                                                                                      | **Decisions to document**                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Window-based profile comparison** | Interpretable baseline comparing earlier and later purchasing profiles.                                | Window lengths, summary statistics, feature-specific differences or combined score, scaling, thresholds and candidate consolidation. |
| **PELT, where justified**           | Alternative retrospective segmentation approach for changes represented by the selected cost function. | Input features, cost function, penalty, minimum segment length, transformations and treatment of unavailable values.                 |

Selecting PELT alone does not specify a complete detection method. Its cost function determines which differences influence segmentation. An approach aimed at abrupt level shifts must not be assumed to identify gradual changes or all product-mix changes adequately.

Do not force a second method onto unsuitable histories. Record its applicability limits and use a common eligible subset when directly comparing methods. Report coverage differences separately.

### 4.4 Event and feature descriptions

Create an event register with one row per candidate event and a linked feature table with one row per event and feature.

| **Component**                | **Required information**                                                                                                                      |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identity and provenance**  | Event ID, customer ID, input version, analysis-run identifier, method and settings.                                                           |
| **Timing**                   | Estimated boundary or transition interval and the dates of the reference and subsequent comparison periods. State the boundary convention.    |
| **Data support**             | Number of usable periods and orders on each side, missingness and relevant coverage or quality flags.                                         |
| **Before-and-after profile** | Feature summaries in original units, with the aggregation basis and denominators stated.                                                      |
| **Direction and magnitude**  | Absolute differences, relative differences where meaningful, and percentage-point differences for rates or shares.                            |
| **Observed persistence**     | The period over which the changed pattern satisfies a stated criterion, including gaps or insufficient follow-up.                             |
| **Review status**            | Retained candidate, ambiguous, insufficient evidence or suspected data artefact, with reasons. These are review statuses, not taxonomy types. |

**Comparison rules:**
- Use comparable summaries. For unequal window lengths, compare rates or period averages rather than unadjusted totals where appropriate.
- When a reference value is zero or too small for a meaningful percentage comparison, report the absolute difference and flag the relative difference as undefined or unstable. Specify any minimum-denominator rule.
- For rates and shares, distinguish percentage-point changes from relative percentage changes.
- Preserve unknown observations. Do not silently replace them with zero to enable detection or comparison.
- Record detector scores separately from descriptive feature differences. Neither is automatically a probability or a statistical-significance measure.
- Record the descriptive windows separately from the detector's segments when they differ. Avoid comparisons spanning other known candidate boundaries without explanation.

**Persistence and timing:**
- The length of a post-change segment does not by itself establish sustained change.
- Define how persistence is assessed and report only the follow-up supported by the observations.
- If the pattern continues to the extract's end, report it as ongoing at the observation boundary rather than assigning a completed duration.
- A monthly boundary does not establish an exact transaction-level change date.

### 4.5 Review and sensitivity checks

- Inspect candidate events against the full available customer history, not only selected before-and-after summaries.
- Check for isolated large orders, recurring seasonal patterns, missing periods and relevant preparation decisions.
- Compare a small, justified set of alternative window lengths, thresholds or penalties. Record changes in event selection, timing and magnitude.
- Preserve disagreements between methods. Agreement indicates consistency between approaches, not verified correctness.
- Retain original method outputs when consolidating repeated detections. Specify the temporal matching tolerance used for cross-method comparisons.
- Do not remove an event solely because it does not fit anticipated taxonomy categories.

These checks assess plausibility and stability during development. They do not replace the independent performance evaluation planned for Phase 7.

### 4.6 Recommended tables and graphics

| **Recommended output**                                               | **Purpose**                                                                                                      |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Customer-history plots with marked boundaries and shaded windows** | Inspect candidate timing, surrounding patterns, missing periods and comparison support.                          |
| **Before-and-after feature table**                                   | Show the measured differences in interpretable units, alongside data counts and limitations.                     |
| **Feature-difference plots**                                         | Display direction and magnitude in separate panels for incompatible units. Label any standardisation explicitly. |
| **Product-mix comparison charts, where applicable**                  | Show shifts in category composition with consistent categories and stated denominators.                          |
| **Candidate summary by method and setting**                          | Show assessed histories, unassessable histories, event counts and sensitivity to analytical choices.             |
| **Method-agreement and disagreement table**                          | Identify matched and unmatched candidates using the documented timing tolerance.                                 |

Select displays according to the question. Avoid plotting every customer in a single chart or presenting only the most striking examples.

### 4.7 Evidence for taxonomy development

**Construct a documented development case collection containing:**
- Candidates spanning different purchasing dimensions, directions, magnitudes and observed persistence.
- Customers with varied activity levels, histories and available business-group characteristics.
- Borderline or ambiguous cases and disagreements between methods.
- A documented sample of histories without automatic detections, to inspect possible blind spots.

Record the selection procedure and any sampling seed. Manually noticed patterns must retain their provenance rather than being presented as automatic detections. Histories without detections are not verified no-change cases. This case collection supports development and must not be presented as independent validation or a representative estimate of population frequencies.

### 4.8 Interpretation and boundaries

- Describe observed purchasing changes without assigning final taxonomy types. This follows in Phases 5 and 6.
- Distinguish descriptive magnitude, persistence, statistical evidence and business relevance. Do not label candidates statistically significant unless a suitable inferential procedure supports that claim.
- Feature differences describe what changed. They do not automatically explain the detector's decision or the customer's motivation.
- Restrict claims to purchasing observed with the focal wholesaler. Competitor switching or other causal explanations cannot be inferred directly.
- Retrospective boundaries do not establish when a change could have been detected operationally. Claims about early detection require a separate time-respecting evaluation.
- Keep the number of candidate events separate from the eventual number of taxonomy types. Neither count should be forced to meet an anticipated result.

### 4.9 Documentation and outputs

| **Output**                          | **Contents**                                                                                                                              |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Candidate-event dataset**         | Event identifiers, timing, methods, scores, provenance and review statuses, saved separately as CSV or Parquet.                           |
| **Feature-change dataset**          | Before-and-after values, differences, units, support counts and limitations linked by event ID.                                           |
| **Analysis-run and coverage log**   | Input versions, code and settings. Customers or periods assessed, unassessable, or assessed without detections. Reasons for restrictions. |
| **Sensitivity and review report**   | Selected tables and graphics, alternative settings, consolidation rules and documented interpretation.                                    |
| **Taxonomy-development case index** | Selected event or history references, selection rationale and automatic or manual provenance.                                             |

Preserve initial detections alongside consolidated or reviewed results. Link outputs to the prepared data version and document schemas and reload settings for exported files.

### 4.10 Completion criteria

Phase 4 is complete when the specified procedures have been applied to eligible development histories, assessability and candidate results are recorded, event descriptions are reproducible, sensitivity checks are documented and the development case collection is available for Phase 5.

Completion does not require a predetermined number of changes, agreement between methods or confirmation of anticipated types. If too few assessable events are available to support taxonomy development, record the limitation and the required revision to scope, data or analysis design.

---

## Phase 5 - Knowledge synthesis: Develop the purchasing-change taxonomy

### 5.1 Purpose

**Phase 5** develops a documented taxonomy of observable purchasing changes by combining the thesis's conceptual foundations with the development evidence assembled in Phase 4. It defines purchasing dimensions, change types, their relationships and proposed assignment criteria. The classified object remains a **candidate change event within a customer's history**, which may receive several compatible type labels when different purchasing dimensions change together.

The resulting taxonomy matrix and versioned type codebook provide the specification for systematic implementation, assignment and explanation in Phase 6. Provisional application to development cases supports refinement of the definitions, assessment of their coherence and documentation of unresolved cases. These development checks support a reasoned stopping decision. Independent assessment of taxonomy applicability, assignment consistency and usefulness belongs to Phase 7.

> **Methodological basis:** This phase adapts the iterative conceptual-to-empirical and empirical-to-conceptual taxonomy-development approach of Nickerson et al. (2013). The methodological guidance of Kundisch et al. (2022) informs the specification of the taxonomy's purpose and intended users, as well as the distinction between development checks and subsequent evaluation of usefulness. The purchasing dimensions, type definitions, compatible label combinations, assignment criteria and development-case selection are project-specific decisions requiring justification.

### 5.2 Inputs and objectives

**Inputs:**
- Phase 4 candidate-event dataset and linked feature-change dataset.
- Before-and-after profiles, comparison periods, observed persistence and supporting data counts.
- Feature definitions, analytical eligibility, coverage information and quality flags from Phase 3.
- Phase 4 review statuses, sensitivity findings, consolidation links and taxonomy-development case index.
- Research objectives, conceptual starting points from the project plan and relevant scientific literature.
- Records identifying evidence already used for exploration, method development or parameter tuning and evidence reserved for later evaluation.

Available business definitions and domain feedback may support terminology and interpretation. They are desirable inputs rather than mandatory prerequisites.

**Objectives:**
- Establish the taxonomy's purpose, scope and organising perspective.
- Identify meaningful distinctions supported by the available measurements.
- Develop explicit definitions that accommodate multidimensional changes.
- Specify proposed assignment criteria and the treatment of insufficient or ambiguous evidence.
- Document development cases, revisions, limitations and the handover to Phase 6.

The procedure can be specified before empirical execution. A completed empirical taxonomy requires suitable Phase 4 evidence. Anticipated types and illustrative thresholds are not established findings.

### 5.3 Procedure

| **Activity**                                    | **Checks and decisions**                                                                                                                                                                               | **Recorded output**                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| **1. Specify purpose and scope**                | Define the classified object, intended users, included purchasing changes and excluded interpretations. Establish the organising perspective against which proposed dimensions and types are assessed. | Scope and terminology specification.             |
| **2. Review development evidence**              | Examine the Phase 4 case collection for variation, missing perspectives and repeated evidence from the same histories. Record prior development use and evaluation restrictions.                       | Updated case index and coverage assessment.      |
| **3. Establish a provisional structure**        | Use documented purchasing constructs and conceptual starting points to propose dimensions, characteristics and type labels. Separate substantive changes from evidence statuses.                       | Initial taxonomy matrix.                         |
| **4. Develop and revise definitions**           | Examine development cases, apply provisional definitions and investigate counterexamples. Retain, rename, combine, divide or remove categories with recorded reasons.                                  | Versioned definitions and iteration log.         |
| **5. Specify assignment criteria**              | Define required evidence, rule conditions, parameter rationale, compatible labels and exclusions. Identify unresolved calibration requirements.                                                        | Type codebook and parameter-decision table.      |
| **6. Check coherence and prepare the handover** | Review logical consistency, case coverage, interpretability and unresolved cases. Record the stopping decision and the version to implement in Phase 6.                                                | Development-check report and versioned handover. |

Activities are iterative. If development reveals inadequate feature definitions or event descriptions, revise the relevant earlier phase and regenerate affected outputs. Do not silently alter measurements or comparison windows to make an event fit a proposed type.

#### 5.3.1 Taxonomy purpose, scope and organising perspective

**Use the following _meta-characteristic_ or organising perspective, to guide inclusion:**
> Observable within-customer purchasing changes at the focal wholesaler, represented through differences in purchasing dimensions between documented reference and subsequent periods.

**Specify:**
- _The intended use:_ consistent description and interpretation of candidate events.
- _The intended users, initially the researcher and readers interpreting the findings.
- Included purchasing dimensions and the temporal patterns supported by the analysis.
- Applicable customer histories, observation conditions and measurement restrictions.
- Excluded interpretations, particularly customer motivation, competitor switching and causal mechanisms.

Include increases and decreases where meaningful. Do not restrict the taxonomy to deterioration merely because the project plan's examples emphasise declining activity. Begin with the purchasing constructs defined in Phase 3. **A feature does not automatically require a separate type:** retain a distinction only when its meaning, measurement and usefulness for describing events can be explained.

Keep magnitude and observed persistence primarily as supporting descriptors. Introduce categorical severity or duration distinctions only when they serve a stated purpose and their boundaries can be justified.

#### 5.3.2 Development evidence and case selection

Use and extend the **Phase 4 taxonomy-development case index**, preserving links to the event register, original histories and feature descriptions.

| **Coverage aspect**     | **Assessment**                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| **Purchasing patterns** | Representation of different dimensions, directions, magnitudes and observed persistence.         |
| **Combined changes**    | Cases involving one dimension and several simultaneous dimensions.                               |
| **Customer histories**  | Variation in activity, history length and available business-group characteristics.              |
| **Uncertainty**         | Borderline cases, weak support, quality concerns and detector disagreements.                     |
| **Possible omissions**  | Documented histories without automatic detections and separately identified manual patterns.     |
| **Evidence dependence** | Repeated events, overlapping comparisons and concentration of cases within particular customers. |

Record selection reasons, event counts and distinct customer counts. Avoid allowing numerous similar events from one history to dominate development.

The project plan's proposed 20–30 profiles provide an initial workload estimate, not a sufficiency criterion. Distinguish selected customer histories from the event cases examined within them. Expand or restrict the collection according to observed coverage gaps and available resources, documenting the consequences.

Histories without detections are not verified no-change cases. Manually identified patterns must retain their provenance and receive a documented event description before being used as event-level examples.

Before further refinement, record which customers, periods and cases have already influenced methodological choices. Evidence reserved for independent evaluation must not be used to revise definitions or tune criteria. Where separation is limited, document the dependence and restrict subsequent evaluation claims.

#### 5.3.3 Iterative development and revision

**Combine _conceptual-to-empirical_ and _empirical-to-conceptual_ development:**
1. Propose distinctions from the taxonomy's purpose, documented purchasing constructs and relevant literature.
2. Examine a documented batch of development cases using their original histories and Phase 4 descriptions.
3. Apply the current definitions provisionally and record supporting evidence, non-matches and uncertainties.
4. Identify distinctions that are unclear, redundant, unsupported or missing.
5. Revise the structure or definitions with an explicit rationale.
6. Re-examine previously reviewed cases affected by the revision.

Do not retain a category solely because it appeared in the project plan or create a category solely to accommodate an isolated numerical difference. Conversely, do not discard an event merely because the current taxonomy cannot describe it.

**For each iteration, record:**
- Taxonomy version and cases examined.
- Conceptual or empirical starting point.
- Proposed change and supporting evidence.
- Alternatives considered and reason for the decision.
- Affected definitions, criteria and previously reviewed cases.
- Remaining questions and required follow-up.

Structured manual comparison is the principal development procedure. Clustering is optional and requires a specific unresolved question, justified inputs and an explanation of its additional value. Cluster membership alone does not establish a meaningful change type.

### 5.4 Taxonomy structure and type definitions

#### 5.4.1 Dimensions, characteristics and overlapping types

**Maintain a taxonomy matrix distinguishing the following elements:**

| **Element**                 | **Function**                                                                   | **Illustrative example - not an adopted type definition**   |
| --------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Purchasing dimension**    | Identifies the aspect of purchasing being characterised.                       | Order frequency.                                            |
| **Characteristic or state** | Describes the dimension under specified comparison rules.                      | Increase, decrease or no qualifying directional difference. |
| **Type label**              | Names a defined observable change pattern.                                     | Frequency decrease.                                         |
| **Supporting descriptor**   | Records magnitude, timing, observed persistence or contextual information.     | Absolute difference and available follow-up.                |
| **Assessability status**    | Indicates whether the required evidence permits application of the definition. | Insufficient comparison support.                            |

For each assessable dimension, define states that are non-overlapping and cover the outcomes allowed by its representation. This applies **within a dimension**. It does not require one exclusive type label for the entire event. A frequency decrease and assortment narrowing may coexist. Record compatibility and logical exclusions explicitly. Opposing changes in different product categories are not inherently contradictory.

Product composition requires a suitable representation of distributional change rather than a generic increase/decrease classification. Define the category basis, denominator and evidence needed to describe the shift.

**Structural rules:**
- Do not interpret "no qualifying difference" as proof of stability.
- Keep missing or inadequate evidence separate from substantive characteristics.
- Do not generate a separate named type for every possible label combination.
- Introduce a composite type only when it adds a distinct interpretation and has explicit criteria.
- Record relationships among mathematically or empirically dependent measures.

Report the numbers of dimensions, type labels and observed label combinations separately. The project plan's five-to-seven-type proposal is a scope intention, not a required empirical outcome. Record how the retained structure relates to that intention and justify any departure.

#### 5.4.2 Proposed assignment criteria and parameter decisions

Create a **type codebook** containing one definition record per retained type.

| **Field**                        | **Required content**                                                                      |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| **Identity**                     | Stable type identifier, neutral label and taxonomy version.                               |
| **Conceptual definition**        | Observable pattern represented and distinction from related types.                        |
| **Required evidence**            | Features, units, comparison periods, denominators and data-support requirements.          |
| **Assignment conditions**        | Explicit logical conditions, comparison operators and treatment of boundary values.       |
| **Parameters**                   | Values adopted for development, their rationale and any unresolved calibration procedure. |
| **Relationships**                | Compatible labels, logical exclusions and justified composite relationships.              |
| **Evidence limitations**         | Conditions under which the rule is inapplicable or its outcome remains indeterminate.     |
| **Examples and counterexamples** | Linked development cases illustrating inclusion, exclusion and relevant boundaries.       |
| **Provenance**                   | Conceptual sources, empirical support and revision references.                            |

Apply a label only when the required evidence is assessable and its specified conditions are satisfied. A Phase 4 candidate does not automatically satisfy a taxonomy definition.

**Comparison and parameter rules:**
- Reuse Phase 4's documented descriptive comparisons unless a revision is justified.
- Specify absolute, relative or percentage-point differences according to the measure.
- Define treatment of zero or unsuitable reference values. Do not force an unstable relative comparison.
- State support requirements and any persistence condition explicitly.
- Distinguish detection thresholds from typing thresholds, even when they use the same value.
- Document whether a criterion reflects descriptive materiality, business judgement or statistical evidence. These are not interchangeable.

Numerical choices must use development evidence and a recorded rationale. Do not adopt the project plan's illustrative percentages or durations as validated thresholds.

Phase 5 establishes rule meaning and proposed operational criteria. If calibration is deferred to Phase 6, specify the parameter, permitted development evidence, selection procedure and condition for finalisation. A change affecting the type's meaning requires a versioned taxonomy revision.

#### 5.4.3 Ambiguous cases and insufficient evidence

**Record provisional outcomes separately for each relevant event–type combination:**

| **Outcome**          | **Meaning**                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| **Criteria met**     | Required evidence is assessable and satisfies the proposed definition.                          |
| **Criteria not met** | Required evidence is assessable but does not satisfy the definition.                            |
| **Indeterminate**    | Missing support, ambiguous evidence or an unresolved definition prevents a defensible decision. |
| **Not applicable**   | The case falls outside the type's documented applicability conditions.                          |

These are developmental application outcomes, not additional purchasing-change types. Preserve the Phase 4 event review status separately. Matching a rule does not resolve a suspected data artefact.

**For unresolved cases, identify whether the issue concerns:**
- A measurement or data-support limitation.
- An ambiguous definition or rule.
- A documented scope exclusion.
- A potential gap in the taxonomy.

An event may meet several definitions, remain partly assessable or receive no substantive label. Retain such cases and their reasons. Do not force assignment through an undefined "other" type.

### 5.5 Development checks and revision record

Check the current taxonomy against its purpose and documented development evidence.

| **Check**                          | **Required assessment**                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Conceptual consistency**         | Dimensions and types fit the organising perspective and describe observable purchasing changes.                   |
| **Distinctiveness and simplicity** | Definitions add meaningful distinctions without unnecessary duplication or proliferation of composite types.      |
| **Rule consistency**               | Conditions, boundaries, compatibility and exclusions do not create unintended contradictions.                     |
| **Measurement feasibility**        | Required features and comparison support are available within the stated scope.                                   |
| **Development-case coverage**      | Cases can be described or their non-coverage is explicitly explained.                                             |
| **Interpretability**               | Labels and definitions correspond to recorded feature differences without unsupported causal claims.              |
| **Extensibility**                  | Definitions and identifiers permit documented additions or revisions without silently changing existing meanings. |
| **Traceability**                   | Definitions, provisional outcomes and revisions can be linked to their sources and evidence.                      |

Inspect examples, counterexamples and cases near proposed decision boundaries where available. Record missing examples as limitations rather than inventing empirical support. A limited supervisor or domain review may clarify terminology and practical interpretation. If feedback changes the taxonomy, record it as development input.

After revisions, conduct a final development pass over the affected cases and the retained structure. If substantive changes remain necessary, continue the iteration or report the unresolved limitation. These checks support a reasoned stopping decision. They do not demonstrate independent assignment reliability, population-wide coverage or practical usefulness.

### 5.6 Interpretation and boundaries

- Type labels describe purchasing observed with the focal wholesaler. They do not establish customer motivation, competitor switching or causal mechanisms.
- Recorded discount increases do not establish discount dependence. Absolute margin changes and margin-rate changes require distinct definitions.
- Assortment breadth may change with ordering activity or observation length. Record these dependencies when interpreting narrowing or expansion.
- Multiple related labels do not constitute independent corroboration of a behavioural change.
- The taxonomy's empirical coverage depends partly on the detection procedures and development-case selection. It must not be presented as exhaustive.
- Separate empirically illustrated definitions from conceptual extensions without observed examples.
- Provisional application in this phase supports development. Systematic assignment and explanation generation belong to Phase 6.
- Feature differences, explanations of assignment rules and explanations of a detector's internal decision are distinct outputs.
- Independent evaluation belongs to Phase 7. Revisions prompted by evaluation constitute further development and require a new version.

### 5.7 Documentation and outputs

| **Output**                                | **Contents**                                                                                                            |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Scope and terminology specification**   | Purpose, organising perspective, intended users, analytical scope and exclusions.                                       |
| **Taxonomy matrix**                       | Dimensions, characteristics, type labels, relationships and supporting descriptors.                                     |
| **Type codebook**                         | Definitions, required evidence, assignment conditions, examples, limitations and provenance.                            |
| **Parameter-decision table**              | Adopted settings, rationale, supporting development evidence and deferred calibration requirements.                     |
| **Updated development case index**        | Event or history references, selection reasons, evidence roles and iterations in which cases were examined.             |
| **Provisional application table**         | Event ID, type ID, taxonomy version, outcome, supporting feature references and reasons.                                |
| **Revision and development-check report** | Changes, affected cases, consistency checks, unresolved issues and stopping rationale.                                  |
| **Phase 6 handover**                      | Version to implement, applicable data versions, rule specification and outstanding implementation or calibration tasks. |

Use stable identifiers to link definitions, events, features and revisions. Where several iterations are retained, distinguish provisional applications by iteration as well as taxonomy version. Record input versions, scripts or notebooks used for case preparation, sampling procedures and random seeds where applicable. Save tabular outputs as CSV or Parquet with schemas and reload settings. Qualitative decisions must remain traceable even where they cannot be reproduced automatically.

Freeze the handover version before systematic application. Later changes must preserve the earlier version and identify which assignments or evaluations require reconsideration.

### 5.8 Completion criteria

**Phase 5 is complete when:**
- Purpose, scope and terminology are explicit.
- Development evidence and its limitations are documented.
- Retained dimensions and types have traceable definitions and proposed assignment criteria.
- Compatible labels, exclusions and insufficient evidence have explicit treatment.
- Development checks reveal no unresolved logical contradictions in the retained structure.
- A final development pass requires no substantive revision.
- Unrepresented patterns and conceptual extensions are identified.
- The Phase 6 handover is versioned, including any bounded calibration tasks.

Completion does not require a predetermined number of types, a label for every candidate or proof of universal coverage. Numerical calibration may remain pending only where rule meaning and the development-only calibration procedure are explicit.

If essential measurements, sufficiently varied cases or defensible definitions are unavailable, record the taxonomy as **provisional, restricted or partially completed**, with the affected scope and required follow-up. Unresolved conceptual contradictions prevent completion of the affected definitions.

---

## Phase 6 - Apply the taxonomy and explain assignment outcomes

### 6.1 Purpose

**Phase 6** translates the taxonomy developed in Phase 5 into explicit, executable rules and applies them reproducibly to candidate change events. It generates explanations linking observed feature differences to the conditions that produced or prevented each assignment, including relevant evidence limitations. The unit of classification remains a **candidate change event within a customer's history**, which may receive several compatible labels, remain partly assessable or receive no substantive label.

The resulting assignment records, rule traces and explanations provide reproducible outputs for evaluation in Phase 7. Verification establishes conformity between the codebook, implementation and generated outputs, while assessment of methodological performance, reader understanding and practical usefulness belongs to the subsequent evaluation phase. Explanations describe observed differences and assignment reasoning without automatically explaining the detector's decision or the causes of customer behaviour.

> **Methodological basis:** This phase draws on the distinction between interpretable decision procedures and post-hoc explanations discussed by Rudin (2019), applying it to the direct implementation of the taxonomy's assignment rules. Explanation construction adapts data-to-text generation principles for selecting, organising and expressing structured evidence (Gatt & Krahmer, 2018). Data-leakage research informs the separation of calibration and implementation-driven revisions from evidence reserved for independent evaluation (Kapoor & Narayanan, 2023). The assignment implementation, evidence-status handling, rule traces and explanation templates are project-specific decisions requiring justification.

### 6.2 Inputs and objectives

**Inputs:**
- Phase 5 taxonomy matrix, type codebook, compatibility rules and versioned handover.
- Parameter-decision table, including any explicitly deferred calibration procedure.
- Phase 4 candidate-event and feature-change datasets, with comparison periods, support counts, review statuses and provenance.
- Phase 3 feature definitions, coverage information and quality indicators.
- Phase 5 provisional applications, examples, counterexamples and unresolved issues.
- Records distinguishing development evidence from evidence reserved for later evaluation.

**Objectives:**
- Translate type definitions into explicit, executable assignment rules.
- Resolve authorised calibration tasks using development evidence.
- Apply all relevant type definitions consistently while preserving uncertainty.
- Generate descriptions from recorded feature differences and actual rule outcomes.
- Verify agreement between the specification, implementation, assignments and explanations.
- Export reproducible results and a versioned handover for Phase 7.

Empirical execution requires an operational codebook and suitable event evidence. The existence of a documented taxonomy-development procedure does not establish that these inputs have already been produced.

### 6.3 Procedure

| **Activity**                                 | **Checks and decisions**                                                                                                                                                   | **Recorded output**                                 |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **1. Confirm the operational specification** | Check type definitions, required evidence, logical conditions, applicability and compatibility. Identify unresolved implementation or calibration tasks.                   | Operational specification and issue register.       |
| **2. Complete deferred calibration**         | Apply only the development-only procedures authorised in Phase 5. Record selected settings, rationale and affected definitions.                                            | Versioned parameter configuration.                  |
| **3. Implement assignment rules**            | Translate each retained definition into executable conditions. Preserve missing evidence and record the conditions underlying each outcome.                                | Assignment implementation and rule-trace structure. |
| **4. Verify the implementation**             | Check independently worked examples, decision boundaries, unavailable evidence, compatible labels and contradictions. Resolve discrepancies before systematic application. | Verification results and correction log.            |
| **5. Apply the taxonomy**                    | Process the declared event set, preserve provenance and review statuses, and account for events without substantive assignments.                                           | Assignment dataset and processing summary.          |
| **6. Construct explanations**                | Generate structured descriptions and text from feature evidence and executed rule conditions. Include consequential limitations.                                           | Explanation records and supporting displays.        |
| **7. Verify and export results**             | Reconcile explanations with assignments and evidence. Check reproducibility, output schemas and remaining restrictions.                                                    | Verified outputs and Phase 7 handover.              |

If execution exposes an inadequate type definition, return the issue to Phase 5. Changes to measurements or event descriptions require a versioned revision of the relevant earlier phase and regeneration of affected outputs.

#### 6.3.1 Operational specification and deferred calibration

**Before implementation, confirm that every retained type specifies:**
- Its identifier, definition and applicability conditions.
- Required features, units, comparison periods and denominators.
- Data-support and quality requirements.
- Logical conditions, operators and treatment of boundary values.
- Any magnitude or persistence criteria.
- Compatible labels and logical exclusions.
- Treatment of insufficient evidence.

Separate **conceptual meaning**, **parameter configuration** and **software implementation**. Record a version or identifier for each.

The Phase 5 handover fixes the conceptual specification while permitting explicitly bounded calibration tasks. For each deferred task, record the parameter, permitted development evidence, selection procedure, chosen setting and rationale. Freeze the resulting configuration before systematic application intended for independent evaluation.

Do not choose thresholds merely to maximise the number of assigned events or agreement with labels generated by the same criteria. Settings may express descriptive materiality or documented business judgement without constituting statistical-significance thresholds. Keep calibration and implementation-driven revisions separate from reserved evaluation evidence. This applies the framework's existing leakage safeguards to rule development, informed by Kapoor and Narayanan (2023).

A change affecting a type's meaning requires a taxonomy revision. An unresolved conceptual condition must not be silently completed through an implementation assumption.

#### 6.3.2 Rule implementation and verification

Implement the codebook directly using explicit functions or an equivalent transparent procedure. For a small taxonomy, a documented parameter table and named rule functions are sufficient. A general-purpose rule engine is not required.

**For each event–type combination:**
1. Establish whether the type is applicable.
2. Assess the evidence required by the definition.
3. Evaluate the specified conditions.
4. Record the outcome, supporting evidence and reasons.

Maintain a **rule trace** containing the condition identifier, feature reference, compared value, operator, threshold or comparison value and condition result. Distinguish an unevaluated condition from a condition evaluated as false. For compound rules, preserve the specified conjunctions and alternatives. Define the evidence needed for each valid branch. Missing values must not acquire methodological meaning through software defaults.

**Implementation rules:**
- Evaluate every applicable type. Do not stop after the first matching label.
- Apply decisions to the recorded numerical precision, with rounding reserved for presentation.
- Preserve units and distinguish relative changes from percentage-point differences.
- Reuse the documented comparison periods and persistence measures.
- Do not silently impute unavailable values to enable classification.
- Detect incompatible label combinations and investigate their origin.
- Record execution failures separately from scientific uncertainty.

Use independently worked examples to verify expected outcomes. Include clear matches, non-matches, boundary values, insufficient support and supported combinations of labels. Verification against the codebook establishes implementation conformity, not independent classification validity.

#### 6.3.3 Systematic assignment and unresolved outcomes

Apply the verified rules to a declared input event set. Record its selection criteria and evidence role. Preserve links to original detections, consolidated events and manually identified patterns.

**Maintain the outcomes established in Phase 5:**

| **Outcome**          | **Operational meaning**                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| **Criteria met**     | The required evidence is assessable and satisfies the type definition.   |
| **Criteria not met** | The required evidence is assessable but does not satisfy the definition. |
| **Indeterminate**    | Insufficient or unreliable evidence prevents a defensible decision.      |
| **Not applicable**   | The event falls outside the definition's applicability conditions.       |

An unresolved definition also prevents a defensible assignment, but must be recorded as a specification problem requiring revision rather than an ordinary data limitation. Assign each type whose criteria are met, subject to the documented evidence requirements and compatibility rules. Preserve the **Phase 4 review status separately** from the type outcome.

| **Event situation**                                  | **Required treatment**                                                                                                     |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Retained candidate with sufficient evidence**      | Report applicable rule outcomes and assigned labels.                                                                       |
| **Ambiguous candidate with assessable measurements** | Report matching labels alongside the unresolved event status. Rule satisfaction does not resolve the ambiguity.            |
| **Insufficient evidence for a type**                 | Record an indeterminate outcome and the missing requirement. Other types may remain assessable.                            |
| **Suspected artefact affecting required evidence**   | Withhold the affected assignment where the evidence fails its quality requirements. Preserve the artefact flag and reason. |
| **No substantive label assigned**                    | Retain the event and distinguish assessable non-matches from indeterminate or inapplicable outcomes.                       |

A quality concern affecting one feature does not automatically invalidate every other feature. Its consequences depend on the evidence requirements of each type. If incompatible labels match, retain the diagnostic rule results but flag the affected assignment as unresolved pending correction. Do not select a dominant label through an undocumented priority rule.

Account for every input event in the processing register, including restricted cases and execution failures. Report event counts and distinct customer counts separately. Counts of assigned labels may exceed event counts because membership is not exclusive.

### 6.4 Explanation construction

#### 6.4.1 Observed differences and assignment reasons

**Construct explanations from two distinct components:**

| **Component**                   | **Question answered**                                      | **Required evidence**                                                                 |
| ------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Observed-change description** | What differs between the reference and subsequent periods? | Before-and-after values, units, differences, support counts and observed persistence. |
| **Assignment explanation**      | Why was a type assigned or withheld?                       | The executed conditions, their outcomes and relevant evidence restrictions.           |

A type label alone is not a sufficient explanation. Conversely, a feature difference does not explain an assignment unless its relationship to the rule is identified. For each assigned label, show the conditions sufficient under the implemented definition. If the definition requires both magnitude and persistence, explain both. Where alternative branches can support assignment, identify the branch or branches that were satisfied.

Distinguish features used in assignment from additional descriptive context. A feature recorded only for description must not be presented as determining the label. For unassigned types, retain the reason in the structured output. Include it in the event narrative when it materially affects interpretation, particularly where insufficient evidence prevents assessment.

#### 6.4.2 Structured evidence and text templates

**Create a structured explanation record before generating text. It should contain:**
- Event ID, customer reference and comparison periods.
- Assigned labels and relevant unresolved outcomes.
- Before-and-after values and differences for the relevant features.
- Rule conditions supporting each assignment.
- Observed persistence, where assessed.
- Support counts and consequential coverage or quality limitations.
- Event review status and automatic or manual provenance.
- References to the evidence, taxonomy, parameters and implementation.

Use short, controlled templates to render these records. Selecting relevant content, organising it and expressing it consistently adapts established data-to-text generation tasks (Gatt & Krahmer, 2018).

**Recommended narrative order:**
1. Identify the comparison periods and assigned change labels.
2. Describe the corresponding feature differences.
3. State why the assignment criteria are satisfied.
4. Report relevant unresolved outcomes and limitations.

Use a fixed, documented dimension order initially. Do not rank heterogeneous feature differences as if they formed a common importance scale.

**Text-generation rules:**
- Generate factual statements from recorded evidence rather than separately entered narrative values.
- Include the necessary conditions for every reported assignment.
- State units, comparison bases and denominators where needed for interpretation.
- Use documented rounding without changing the underlying decision.
- Distinguish percentage changes from percentage-point changes.
- Do not describe unavailable values as zero.
- Do not interpret "criteria not met" as proof that no purchasing change occurred.
- Do not describe a pattern as sustained unless the specified persistence criterion is supported.
- If follow-up ends while the pattern continues, report the observation boundary rather than a completed duration.
- Preserve consequential ambiguity or data-quality flags.

Templates require checks for missing fields, inappropriate wording and misleading omissions. Their deterministic construction does not by itself guarantee correct or useful explanations.

#### 6.4.3 Supporting tables and graphics

| **Recommended output**                      | **Purpose**                                                                            |
| ------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Event explanation table**                 | Present labels, relevant feature differences, rule outcomes and limitations together.  |
| **Before-and-after evidence table**         | Show values, units, denominators and support counts underlying the description.        |
| **Rule-trace view**                         | Allow inspection of the conditions that produced or prevented each assignment.         |
| **Selected customer-history plots**         | Place assignments in the context of the full available history and comparison windows. |
| **Product-mix comparisons, where relevant** | Show category-level shifts using consistent categories and stated denominators.        |

Reuse suitable Phase 4 displays. Additional graphics should answer a specific interpretive question. Keep incompatible units in separate panels or clearly labelled columns. Standardised displays require documented transformations and must not be presented as causal importance or contribution to a detector's score.

### 6.5 Verification and evaluation handover

Verify correspondence between the operational specification, computed outcomes and explanations.

| **Check**                                   | **Required assessment**                                                                                              |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Specification conformity**                | Implemented conditions, operators, parameters and applicability match the versioned codebook.                        |
| **Boundary and missing-evidence behaviour** | Values below, at and above thresholds, unsuitable denominators and incomplete support produce the intended outcomes. |
| **Multiple-label consistency**              | Compatible labels coexist. Prohibited combinations are detected.                                                     |
| **Evidence integrity**                      | Assignments and explanations link to the correct events, features, periods and input versions.                       |
| **Explanation accuracy**                    | Numbers, units, direction, conditions and limitations match the structured evidence and rule trace.                  |
| **Processing completeness**                 | All input events are accounted for, including restrictions and execution failures.                                   |
| **Reproducibility and export**              | Fixed inputs and versions reproduce the results. Exported data reload correctly.                                     |

Expected test outcomes must be derived independently from the specification, not generated by the same rule code being checked. Synthetic examples used for boundary verification are software test cases, not evidence of detection performance.

Compare selected outputs with Phase 5 provisional applications. Investigate differences as possible coding errors, calibration effects, definition ambiguities or earlier application errors. Do not automatically treat provisional classifications as ground truth. Review explanation wording using development cases. Record revisions to templates and content-selection rules.

Before applying the system to evidence reserved for independent evaluation, freeze the relevant taxonomy, parameters, code and templates. Record any subsequent correction and identify affected results. Cases used to revise the method must no longer be represented as untouched evaluation evidence. This separation between application and assessment of usefulness is consistent with the taxonomy-design guidance of Kundisch et al. (2022).

Phase 7 evaluates the methodological claims. Successful execution and verification do not establish them.

### 6.6 Interpretation and boundaries

- Assignments indicate membership under the specified taxonomy and rules. They are not automatically probabilities, statistically significant findings or validated business diagnoses.
- Preserve event-level uncertainty even when numerical type criteria are met.
- Multiple labels may reflect dependent measures and must not be presented as independent corroboration.
- Explanations describe observed differences and the actual assignment procedure. Detector attribution and causal explanations require separate justification.
- Restrict behavioural descriptions to purchasing observed with the focal wholesaler.
- Retrospective assignments do not establish when a change could have been detected operationally.
- A learned classifier or surrogate model is not required to implement an explicit codebook. Introducing one would require a distinct purpose and additional evaluation.
- Manual corrections or overrides must be recorded separately with their rationale. They must not silently replace automatic results.
- Assignment frequencies describe the processed event set. They do not automatically estimate the prevalence of change types among all customers.
- Technical transparency and factual consistency do not establish reader understanding or practical usefulness. Such claims depend on the evaluation evidence available in Phase 7.

### 6.7 Documentation and outputs

| **Output**                           | **Contents**                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Operational specification**        | Type definitions, executable conditions, applicability, evidence requirements and compatibility rules.        |
| **Parameter configuration**          | Adopted settings, calibration procedure, rationale and supporting development evidence.                       |
| **Assignment dataset**               | Run ID, event ID, type ID, outcome, reasons and relevant version references.                                  |
| **Rule-trace dataset**               | Condition identifiers, evidence references, compared values, operators and condition outcomes.                |
| **Explanation dataset or report**    | Structured explanation records, generated text, template version and supporting displays.                     |
| **Processing and coverage summary**  | Input and processed events, distinct customers, restricted cases, unresolved outcomes and execution failures. |
| **Verification and revision record** | Checks, expected and observed results, discrepancies, corrections and affected outputs.                       |
| **Phase 7 handover**                 | Frozen versions, reproducible execution instructions, evidence roles and unresolved evaluation questions.     |

Link assignment records by run ID, event ID and type ID. Link rule traces through these identifiers and the condition ID. Preserve the original Phase 4 event register and Phase 5 development records.

Record input versions, code versions, execution settings and relevant software dependencies. Save tabular outputs as CSV or Parquet with schemas, missing-value conventions and reload settings. Document the templates and content-selection rules sufficiently to regenerate explanations.

Do not overwrite earlier results without preserving their version and the reason for replacement.

### 6.8 Completion criteria

**Phase 6 is complete when:**
- The operational specification is explicit and authorised calibration tasks are resolved.
- Retained type definitions are implemented with traceable rule outcomes.
- Meaningful implementation and explanation checks pass.
- Every event in the declared input set is accounted for.
- Multiple labels, non-matches, insufficient evidence and applicability restrictions are handled consistently.
- Explanations correspond to the recorded evidence and executed rules.
- Outputs can be regenerated and reloaded correctly.
- The Phase 7 handover identifies frozen versions, evidence roles and remaining limitations.

Completion does not require assigning every event, eliminating all ambiguity or demonstrating practical usefulness. A correctly recorded indeterminate outcome is compatible with completion.

If essential definitions remain unresolved, required evidence is unavailable or implementation discrepancies prevent trustworthy application, record the phase as **restricted, partially completed or blocked**. State the affected types or cases and the required follow-up rather than concealing the limitation through forced assignments.

---

## Phase 7 - Evaluate the framework and reflect on findings

### 7.1 Purpose

**Phase 7** evaluates the framework's detection performance, taxonomy applicability, assignment consistency and explanation quality, including sensitivity to consequential analytical choices. It combines a controlled detection benchmark, a shared collection of additional real cases and a limited sensitivity analysis. Each component is assessed against explicit claims and suitable evidence, with independent review and semi-synthetic experiments providing supplementary evidence where feasible.

The resulting evaluation findings, failure analyses and documented limitations support qualified answers to the research questions and a critical assessment of the thesis's contributions. Evidence supporting one component does not automatically establish the validity or usefulness of the others. Conclusions remain restricted to the assessed conditions and available evidence, with unsupported claims, unresolved questions and priorities for further work identified explicitly.

> **Methodological basis:** Detection assessment draws on change-point evaluation methods discussed by Truong et al. (2020), while the controlled benchmark follows simulation-study guidance from Morris et al. (2019). Taxonomy assessment draws on the purpose-oriented evaluation guidance of Kundisch et al. (2022). Annotation-agreement research informs the assessment and interpretation of agreement where independent annotations are available (Artstein & Poesio, 2008). Explanation assessment follows the distinction between intrinsic text quality and extrinsic effectiveness in use described by Gatt and Krahmer (2018). Data-leakage research informs the separation of development and evaluation evidence and the treatment of revisions prompted by evaluation findings (Kapoor & Narayanan, 2023). The evaluation scenarios, sampling procedures, matching tolerances, review criteria and sensitivity settings are project-specific decisions requiring justification.

### 7.2 Inputs and prerequisites

**Use the following versioned inputs:**

| **Input**                                          | **Required information**                                                                                                                                |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prepared customer-period profiles from Phase 3** | Feature definitions, units, observation coverage, eligibility rules, missing-value treatments and transformation settings.                              |
| **Candidate-event evidence from Phase 4**          | Detection settings, event timing, before-and-after profiles, persistence evidence, consolidation links, event statuses and processing logs.             |
| **Taxonomy and codebook from Phase 5**             | Dimensions, type definitions, applicability conditions, assignment criteria, permitted combinations, examples, counterexamples and development history. |
| **Assignments and explanations from Phase 6**      | Per-type outcomes, assigned label sets, rule traces, explanation templates, generated descriptions, uncertainty indicators and any manual overrides.    |
| **Development and verification records**           | Cases previously inspected, settings considered, rules revised, implementation checks and known unresolved limitations.                                 |
| **Research questions and scope**                   | The intended retrospective claims, target population, purchasing dimensions and excluded claims.                                                        |

Before evaluating results, specify the evidence available for each claim and identify any missing prerequisites. Distinguish completed implementation verification from empirical evaluation: passing the Phase 6 checks establishes readiness for evaluation, rather than independent evidence of validity.

An independent reviewer is desirable but is not a prerequisite for every evaluation component. Where unavailable, record the resulting restriction on the assessment. Where essential reference evidence is unavailable, identify the corresponding claim as unevaluated rather than substituting an unsuitable performance measure.

### 7.3 Procedure

#### 7.3.1 Specify evaluation claims and evidence roles

Create an evaluation protocol linking each assessment to its claim, evidence, procedure and interpretation.

| **Evaluation object** | **Evaluation question**                                                                                              | **Primary evidence**                                                                          | **Interpretation boundary**                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Change detection**  | Which specified changes are detected, missed or incorrectly flagged and how accurately are detected changes located? | Controlled histories with known reference changes and no-change controls.                     | Performance applies to the tested conditions. It does not establish accuracy across all real ERP histories.                  |
| **Taxonomy**          | Can additional observed patterns be represented clearly within the declared scope?                                   | Additional real cases assessed against the fixed taxonomy.                                    | Applicability and coverage do not alone establish usefulness for intended users.                                             |
| **Type assignment**   | Does the implementation apply the codebook consistently?                                                             | Expected outcomes derived separately from the automated results, supported by rule traces.    | Agreement with the codebook does not establish that the codebook captures an objectively correct behavioural classification. |
| **Explanation**       | Do descriptions accurately communicate observed differences and assignment reasoning?                                | Structured comparison with source evidence and rules. Optional independent reader assessment. | Factual quality and comprehension do not establish improved business decisions.                                              |
| **Robustness**        | How do findings change under justified alternative settings?                                                         | Planned sensitivity comparisons.                                                              | Stability does not itself establish correctness.                                                                             |

Maintain an evidence-role record identifying whether each case or dataset was used for exploration, preparation design, detection tuning, taxonomy development, rule verification or evaluation. Record overlaps explicitly.

Choose separation according to the intended generalisation claim. For an assessment involving additional customers, prefer customer-level separation so that events from the same customer do not appear on both sides of the split. A claim about later periods of existing customers requires an appropriate temporal design. Retrospective evaluation may use the complete historical sequence available for that evaluation. Evaluation of decisions at a particular time must respect the information available then.

If the available histories have already influenced development, describe their subsequent assessment as internal and exploratory. Retrospectively assigning them to an evaluation subset does not remove prior exposure. These safeguards adapt the leakage concerns discussed by Kapoor and Narayanan (2023) to the present workflow.

#### 7.3.2 Freeze the evaluation configuration

**Before inspecting evaluation outcomes, record and freeze:**
- preparation rules, feature definitions and relevant fitted transformations.
- detection methods, parameters, event-consolidation rules and eligibility conditions.
- taxonomy version, assignment criteria and uncertainty handling.
- explanation templates and content-selection rules.
- simulation scenarios, reference definitions and final random-seed schedule.
- case-selection procedures, review instructions and reviewer roles.
- temporal matching tolerance, performance measures, aggregation rules and treatment of undefined measures.
- planned sensitivity settings and any justified acceptance criteria.

Use development data or separate pilot runs to resolve implementation issues and select settings. Keep final simulation realisations separate from those used for tuning. Fresh random seeds provide additional realisations under the specified generating mechanisms. They do not establish generalisation to different purchasing processes.

Do not introduce universal accuracy thresholds, agreement cut-offs or sample-size requirements without justification. Where evaluation is descriptive, state this explicitly and report the observed performance and limitations without inventing a pass/fail boundary.

#### 7.3.3 Evaluate change detection

##### 7.3.3.1 Controlled benchmark design

Structure the simulation protocol around its aims, data-generating mechanisms, targets, methods and performance measures, following the ADEMP guidance of Morris et al. (2019).

Use controlled synthetic customer histories as the primary quantitative benchmark. Define the reference changes through the generating process independently of the detector's output. Include no-change controls containing realistic stochastic variation rather than only constant signals.

**Select a compact set of scenarios relevant to the actual detection claim:**

| **Scenario**                                    | **Purpose**                                                                                                                           |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **No target change**                            | Assess detections caused by ordinary variation under the specified background process.                                                |
| **Sustained increases and decreases**           | Assess sensitivity and localisation for level changes.                                                                                |
| **Different change magnitudes**                 | Examine performance for weaker and stronger changes.                                                                                  |
| **Sparse or intermittent purchasing**           | Examine the influence of limited activity and observation support.                                                                    |
| **Simultaneous changes in relevant dimensions** | Assess the configured multivariate procedure.                                                                                         |
| **Relevant non-target patterns**                | Examine responses to isolated large orders, seasonality or other patterns that the protocol defines as outside the target phenomenon. |

Include product-group redistribution, gradual transitions or temporary reversals only where they belong to the declared scope. Define whether a temporary change contains two reference boundaries and how gradual changes are represented before scoring results.

Justify scenario ranges using development data and substantive reasoning. Preserve the relationships between generated features: for example, derive basket value consistently from revenue and order count and enforce valid category shares. A complete ERP transaction simulator is not required if a coherent profile-level generator is sufficient for the stated claim. Identify any feature dimensions or mechanisms the benchmark does not cover.

Apply the frozen preprocessing and detection procedure at a clearly stated entry point. If simulations begin with prepared profiles, the experiment evaluates downstream detection rather than the correctness of ERP extraction and cleaning. Evaluate at most the detection approaches retained in Phase 4, using the same simulated histories for each. Document method-specific eligibility and failures. Report results on a common assessable set where appropriate, together with coverage of the complete benchmark. Do not silently remove difficult cases.

Choose the number of repetitions with reference to computational feasibility and the precision required for the main performance estimates. Report Monte Carlo uncertainty where estimated performance is summarised across repetitions, using a calculation appropriate to the measure and simulation unit.

##### 7.3.3.2 Reference matching

Define a temporal tolerance in the customer-period profile's time unit. Use one-to-one matching between reference changes and detected events: first maximise the number of permissible matches, then minimise total absolute timing error among those matchings. Resolve any remaining ties deterministically.

Specify the event timestamp used for matching, especially where Phase 4 represents an event as an interval. Apply the frozen consolidation rules before scoring. Exclude algorithmic terminal endpoints that do not represent detected changes. Count matched pairs as true positives, unmatched detections as false positives and unmatched reference changes as false negatives. Multiple detections near the same reference change must not all receive credit. Define edge restrictions and required observation support before evaluation, and report excluded reference changes and histories with their reasons.

Tolerance-based precision and recall and localisation measures are supported by the change-point evaluation discussion in Truong et al. (2020). The matching rule, tolerance and event representation used here are project-specific specifications.

##### 7.3.3.3 Performance reporting

**Report the following measures with their counts and denominators:**

| **Measure**                                | **Definition or reporting rule**                                                                    |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| **Precision**                              | TP / (TP + FP), where the denominator is positive.                                                  |
| **Recall**                                 | TP / (TP + FN), where the denominator is positive.                                                  |
| **F1**                                     | 2TP / (2TP + FP + FN), where the denominator is positive.                                           |
| **Localisation error**                     | Absolute distance between matched reference and detected timestamps, summarised in profile periods. |
| **False detections in no-change controls** | Number of detections per history or observation period, with the exposure denominator stated.       |
| **Histories with false detections**        | Proportion of no-change histories receiving at least one detection.                                 |
| **Coverage and failures**                  | Numbers of assessable, excluded, unassessable and technically failed histories, with reasons.       |

Report measures with zero denominators as undefined. A zero F1 is appropriate where its denominator is positive and no true positive is obtained. No-change controls can have no applicable recall. They remain informative through their false-detection measures.

Present localisation error alongside recall because timing accuracy among matched events excludes missed changes. Specify whether summaries pool event counts or average history-level results. Report performance by scenario and relevant difficulty level before any overall aggregation. These measurements concern retrospective localisation. They do not measure operational detection delay or demonstrate statistical significance of individual real events.

##### 7.3.3.4 Supplementary semi-synthetic and real-data evidence

Where useful, inject known changes into real histories to examine behaviour against a more realistic background. Preserve feature dependencies and record the injection process. Real backgrounds may contain unknown changes, so unmatched detections cannot automatically be labelled false positives. Report recovery of injected changes and describe other detections without assigning unsupported truth labels.

Complement the benchmark with inspection of real histories, including histories without detected events where feasible. Such inspection can identify plausible misses, artefacts and difficult cases, but an incomplete or subjective reference does not establish definitive detection precision or recall.

#### 7.3.4 Evaluate taxonomy applicability

Use a documented collection of additional real cases to assess the fixed taxonomy. Prefer cases not used to define or refine its types. Include straightforward events, overlapping changes, borderline patterns, insufficient evidence and cases receiving no type.

Record the selection procedure and the numbers of customers, histories and events. Where a purposive challenge sample supplements a broader sample, report the two separately. Frequencies in a purposive sample do not estimate population prevalence.

**Assess each case against the following criteria:**

| **Criterion**                 | **Assessment**                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Applicability**             | Whether the definitions and criteria can be applied using the available evidence.                                         |
| **Representational coverage** | Whether the observed pattern can be described within the taxonomy's declared scope.                                       |
| **Distinctiveness**           | Whether relevant types can be distinguished through their definitions and criteria.                                       |
| **Compatibility**             | Whether permitted combinations and prohibited combinations are coherent.                                                  |
| **Interpretability**          | Whether the resulting description communicates the observed pattern without unsupported causal or commercial assumptions. |

For cases not adequately represented, distinguish insufficient evidence, out-of-scope patterns, criteria not met, conflicting definitions and plausible taxonomy gaps. An event may receive some labels while remaining inadequately represented in another dimension. Record such partial coverage rather than treating any assigned label as complete coverage.

High assignment coverage alone does not establish taxonomy quality. Similarly, failure to assign a type because required evidence is missing does not automatically indicate a conceptual gap. Preserve both the full sample denominator and any justified assessable subset.

This assessment provides additional evidence beyond the development ending conditions. Following Kundisch et al. (2022), claims about usefulness must be aligned with the taxonomy's purpose and intended users. Without suitable user-oriented evaluation, restrict conclusions to the applicability and clarity observed in the assessed cases.

#### 7.3.5 Evaluate assignment consistency

**Assess whether the implementation applies the fixed codebook as intended. For selected evaluation cases, derive expected outcomes separately from the system's assignments:**
1. Provide the reviewer with the relevant profile evidence, event status and codebook.
2. Hide automated assignments and generated explanations during the initial assessment.
3. Record expected outcomes and their supporting reasoning.
4. Compare them with the automated results and rule traces.
5. Investigate disagreements while preserving the initial assessments and any subsequent adjudication separately.

**Retain the Phase 6 per-type outcomes:** _criteria met_, _criteria not met_, _indeterminate_ and _not applicable_. Do not treat indeterminate or inapplicable cases as negative assignments. Technical failures remain separate from scientific uncertainty. Evaluate automated results separately from manual overrides.

Report per-type outcome comparisons, agreement of assigned label sets and explanations of disagreements. Where label-set agreement is reported, retain the underlying outcome comparisons so that agreement on empty label sets does not conceal different reasons for withholding assignments.

Where two independent human annotators and adequate category variation are available, an appropriate chance-corrected agreement coefficient may supplement descriptive comparisons. Document its assumptions and category distributions. Artstein and Poesio (2008) discuss the dependence of agreement measures on their assumptions and category prevalence. No universal coefficient threshold is adopted here.

If only the researcher performs the manual assessment, describe it as a structured conformance check. It does not establish independent inter-rater reliability. Agreement with the codebook supports consistent application, not an objectively correct behavioural classification.

#### 7.3.6 Evaluate explanation quality

Assess explanations against the underlying source evidence and the rules actually evaluated. The shared real-case collection may be reused, but complete any blinded assignment review before revealing the system's explanations.

**Use a predefined rubric:**

| **Criterion**                 | **Review question**                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------- |
| **Factual accuracy**          | Are dates, values, units, directions and before-and-after comparisons correct?                |
| **Rule fidelity**             | Does the explanation correctly represent the conditions producing or withholding assignments? |
| **Relevant completeness**     | Are decisive conditions, evidence limitations and necessary qualifications included?          |
| **Uncertainty communication** | Are ambiguous events, missing support and withheld assignments represented accurately?        |
| **Interpretability**          | Can a reader distinguish the observed change from the reason for its assigned type?           |
| **Claim discipline**          | Does the explanation avoid unsupported causal, detector-attribution or commercial claims?     |

Record each issue with the affected explanation, criterion and supporting evidence. Distinguish factual or logical errors from stylistic weaknesses. Report counts and denominators, including the number of explanations reviewed and the number affected by each issue. Do not present uncalibrated reviewer ratings as probabilities or objective correctness scores.

Where an independent reader is available, supplement the audit with a short comprehension task: ask the reader to identify what changed, why the type was assigned and what limitation qualifies the result. Record the reader's relevant background and distinguish demonstrated understanding from general preference ratings.

Gatt and Krahmer (2018) distinguish intrinsic evaluation of text quality from extrinsic evaluation of effectiveness in use. The core assessment here concerns factual quality, rule fidelity and interpretability. Without an appropriate user study, it does not establish improved sales decisions. Researcher-only readability assessment remains a heuristic appraisal rather than independent evidence of reader comprehension.

#### 7.3.7 Assess sensitivity and failure cases

Evaluate a small set of justified alternatives to consequential settings. Depending on the implemented framework, these may include comparison-window length, detection threshold, segmentation penalty, minimum segment length, persistence criteria and assignment thresholds. Include preparation choices where they materially affect the findings.

**Retain the frozen primary configuration as the reference. Change one analytical layer at a time where feasible and distinguish:**
- changes in which events are detected.
- changes in event timing or consolidation.
- changes in type assignments for comparable events.
- changes in uncertainty, withheld assignments or coverage.
- resulting changes in explanation content.

When assessing assignment sensitivity, hold event evidence fixed where possible. Otherwise, explicitly distinguish changed assignments caused by altered event windows from changed assignments caused by the typing rules themselves. Document how events are matched across configurations.

Summarise relevant failure mechanisms, including sparse activity, isolated large orders, missing observations, category changes, overlapping events, insufficient comparison support and rule conflicts. Report whether each limitation concerns data, detection, representation, assignment or explanation. Allow multiple contributing factors.

Account for dependence between events from the same customer. Report customer and event counts separately. Where inferential summaries are justified, use methods consistent with the sampling design. For example, resampling customers rather than treating all their events as independent. For small purposive collections, descriptive counts and case analyses may be more defensible than confidence intervals.

Do not select a better-performing setting after examining evaluation results and report it as if it had been fixed in advance. Such a change constitutes further development.

#### 7.3.8 Reflect on findings and research questions

**For each research question, connect the finding to its evidence and limitations:**

| **Research question or claim**            | **Finding**                                                             | **Supporting evidence**                                    | **Limitation**                                     | **Supported conclusion**                               |
| ----------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------ |
| Record each question or claim separately. | State the observed result, including negative or inconclusive findings. | Identify the relevant experiment, cases and configuration. | State the conditions and unresolved uncertainties. | Limit the conclusion to what the evidence establishes. |

Distinguish the thesis's conceptual contribution, implemented procedure and empirical findings. Explain how data quality, customer eligibility, retrospective analysis, sampling, synthetic assumptions and reviewer availability constrain generalisation.

Address any mismatch between the original research aspirations and the implemented assessment. In particular, retrospective localisation does not demonstrate earlier operational detection. Threshold exceedance does not automatically establish statistical significance. Descriptive feature differences do not establish causes or detector attribution.

If evaluation reveals a defect requiring correction, preserve the original configuration and results. Record the issue, revision and affected evidence. Results obtained after using the same cases to revise the framework must be identified as development-informed reassessment. Further independent evaluation requires suitable unused evidence.

### 7.4 Outputs

**Produce the following traceable outputs:**

| **Output**                                       | **Contents**                                                                                                                    |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Evaluation protocol and configuration record** | Claims, evidence roles, frozen versions, criteria, sampling, matching, aggregation and planned sensitivity settings.            |
| **Benchmark specification and results**          | Generating mechanisms, reference changes, seeds, repetitions, method coverage, performance measures and simulation uncertainty. |
| **Real-case evaluation inventory**               | Selection procedure, customer and event identifiers, previous development exposure, evidence sufficiency and reviewer roles.    |
| **Taxonomy assessment**                          | Applicability findings, partial coverage, unrepresented patterns and reasons for gaps or non-assignment.                        |
| **Assignment assessment**                        | Initial expected outcomes, automated outcomes, agreement summaries, disagreement analysis and separate adjudications.           |
| **Explanation assessment**                       | Rubric outcomes, factual and interpretive issues, representative examples and any independent comprehension evidence.           |
| **Sensitivity and failure analysis**             | Comparisons with the primary configuration, affected events, assignment changes and limitations.                                |
| **Research-question assessment**                 | Findings, supporting evidence, qualified conclusions, unevaluated claims and implications for further work.                     |
| **Revision record**                              | Post-evaluation corrections, preserved original results and the evidence status of subsequent reassessment.                     |

Preserve code, configuration and permissible example data sufficient to reproduce the evaluation. Handle original ERP data and identifiable outputs according to the project's data-access and repository restrictions.

### 7.5 Completion criteria

**Phase 7 is complete when:**
- each evaluation claim is linked to a procedure and evidence source, or explicitly identified as unevaluated.
- development exposure, evaluation roles and configuration versions are documented.
- planned core assessments have been completed, or infeasibility and the resulting reduction in claims are explained.
- detection results include relevant counts, denominators, matching rules, coverage and failures.
- taxonomy gaps, partial coverage and insufficient evidence are distinguished.
- assignment outcomes and disagreements retain their uncertainty and applicability distinctions.
- explanation quality is assessed separately from practical usefulness.
- sensitivity findings, failure cases and material limitations are reported.
- post-evaluation revisions are distinguishable from the original assessment.
- the research questions are answered within the limits of the evidence.

Completion does not require favourable performance, complete assignment coverage, elimination of all ambiguity or confirmation of every original aspiration. Unevaluated or unsupported claims remain explicit limitations of the thesis.

### 7.6 Limitations and interpretation

The evaluation provides evidence conditional on the assessed data, cases, simulated processes and analytical settings. Synthetic benchmarks offer known references but cannot reproduce every feature of ERP purchasing behaviour. Real-case assessments provide contextual evidence but may lack definitive ground truth and representative sampling.

Evidence about taxonomy applicability is restricted by the variety and independence of the assessed cases. Agreement supports reproducibility of application rather than substantive truth. Factual and comprehensible explanations remain descriptive unless separate evidence establishes causal interpretation, detector attribution or decision usefulness. Reusing a real-case collection across taxonomy, assignment and explanation assessment is efficient, but these results are related assessments of the same cases rather than independent replications. Findings from one wholesaler do not by themselves establish transferability to other organisations.

The final conclusions must therefore state both what the framework demonstrated and which capabilities remain uncertain or unevaluated.

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
