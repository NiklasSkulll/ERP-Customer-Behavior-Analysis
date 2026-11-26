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
        - [1.3.3 Assess observation coverage and customer histories](#133-assess-observation-coverage-and-customer-histories)
        - [1.3.4 Examine the core measures and comparison support](#134-examine-the-core-measures-and-comparison-support)
        - [1.3.5 Consolidate preparation and analysis decisions](#135-consolidate-preparation-and-analysis-decisions)
    - [1.4 Required outputs](#14-required-outputs)
    - [1.5 Completion criteria](#15-completion-criteria)
    - [1.6 Optional refinements](#16-optional-refinements)
- [Phase 2 - Use ERP data to prepare customer profiles](#phase-2---use-erp-data-to-prepare-customer-profiles)
    - [2.1 Purpose](#21-purpose)
    - [2.2 Inputs](#22-inputs)
    - [2.3 Core procedure](#23-core-procedure)
        - [2.3.1 Finalise technical and analytical preparation rules](#231-finalise-technical-and-analytical-preparation-rules)
        - [2.3.2 Construct and verify the enriched order-level interim table](#232-construct-and-verify-the-enriched-order-level-interim-table)
        - [2.3.3 Define eligibility and calculate the core measures](#233-define-eligibility-and-calculate-the-core-measures)
        - [2.3.4 Construct monthly customer-currency histories](#234-construct-monthly-customer-currency-histories)
        - [2.3.5 Confirm suitability and verify the prepared data](#235-confirm-suitability-and-verify-the-prepared-data)
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

The **FUUCCE framework** operationalises the [thesis project plan](docs/project/bachelor_thesis_project_plan.md), the source of truth for research objectives, scope and evaluation strategy, through six phases: familiarising with and assessing the data, preparing customer profiles, uncovering and characterising changes, constructing a change taxonomy, classifying and explaining events, and evaluating the findings.

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

Select the conversion stage explicitly with `--folder raw`, `--folder interim` or `--folder processed`, for example `uv run --locked python setup/csv_to_parquet.py --folder raw`. The converter reads only immediate CSV files in the selected folder under `data/data-example/`; it does not scan nested folders. Add `--update` to refresh existing Parquet files. For user-run production conversion, `--prd` selects the corresponding folder under `data/data-prd/`.

Use the configured data and output directories consistently and preserve the original extracts.

---

## Phase 1 - Familiarise yourself with the data and assess its suitability

### 1.1 Purpose

Establish whether the available ERP extracts support the planned analysis of customer ordering activity and recorded net order values. Verify the documented source structure, assess observation coverage and data quality, and identify the decisions required to prepare trustworthy order-level and monthly customer profiles.

This phase combines technical inspection with focused exploration. It begins with the data inventory, then examines overall and industry-level monthly summaries, customer histories and selected individual orders. These summaries provide context and inform preparation decisions. A conspicuous aggregate change is not a prerequisite for examining an individual customer.

The main output is a documented assessment of the data and a set of preparation recommendations. The definitive enriched order table, monthly profiles and systematic change detection are constructed in later phases.

> **Methodological basis:** This phase adapts the inspection and exploration activities of CRISP-DM's data-understanding phase (IBM, n.d.) and exploratory data-analysis principles (Heckert & Filliben, 2003). The ERP-specific checks, analytical priorities and suitability decisions are project-specific operational choices.

### 1.2 Inputs

- The project plan, including the research questions, 24-month observation window, analytical scope and order-eligibility principles.
- The raw order header and item extract, customer master extract, order-reason mapping and industry mapping described in the data description.
- Available information about the extraction date, source formats, filters, coverage and relevant ERP field meanings.
- The target schemas and calculation rules for the order-level interim table and monthly customer profiles.

Record information that is unavailable and its consequences. Distinguish documented field meanings, observations from the extracts, provisional assumptions and unresolved questions. Treat the data description as the starting specification and verify consequential expectations against the available data.

### 1.3 Core procedure

#### 1.3.1 Inspect the datasets and verify their meaning

Load the extracts reproducibly while preserving identifiers and codes as strings. Inspect the recorded source formats before applying import or conversion settings.

**Check:**
- the row and column counts, fields, observed data types and missing-value representations of each dataset.
- the distinct order, order-item and customer counts.
- duplicate combinations of `SALESORDER` and `SALESORDERITEM`.
- repeated header values within each `SALESORDER`, including conflicting identifiers, dates, statuses, currencies or net amounts.
- the available order dates, extraction information, apparent coverage gaps and incomplete calendar months.
- observed document types, processing statuses, rejection statuses and order reasons.
- the distribution of `TRANSACTIONCURRENCY` and the availability of `TOTALNETAMOUNT`.
- the uniqueness and completeness of customer and lookup keys and the extent of unmatched assignments.

The raw order extract contains item rows. Repeated header attributes do not represent additional orders, and repeated `TOTALNETAMOUNT` values must not be summed across items. Investigate contradictory header values rather than selecting an arbitrary item row to construct an order.

Examine the expected relationships between orders, the customer master and the two lookup datasets. Report missing matches and potentially conflicting mappings. A missing industry or text description does not, by itself, make an otherwise usable order invalid.

Record unusual values as investigation flags. Neither a large order amount nor an uncommon status code automatically establishes a data error or an analytical exclusion.

#### 1.3.2 Establish development and evaluation boundaries

Reserve evidence for final evaluation before inspecting individual behavioural patterns to select comparison windows, thresholds or taxonomy types.

Customer-level separation is the starting option for held-out real histories. Where a customer has orders in several currencies, keep all of that customer's currency histories in the same partition. If temporal separation is chosen instead, address shared observations, overlapping comparison windows and the resulting limits on independence.

General structural checks may cover the full extracts. Behavioural exploration used to develop analytical rules must use the declared development evidence. Record any previous exposure to reserved cases that limits their independence.

Document which cases and observations are available for development, which are reserved for evaluation and how those boundaries will be enforced in subsequent phases.

#### 1.3.3 Assess observation coverage and customer histories

Establish the intended 24-month observation window from extraction information and `SALESORDERDATE`. Identify its exact boundaries, incomplete calendar months and any periods for which extraction coverage is uncertain. Do not infer complete observation solely from the first and last order dates.

Examine ordering activity within development evidence at the overall, industry and customer levels. Distinguish the inventory of recorded orders from provisional summaries based on orders considered analytically eligible. Where eligibility is unresolved, label the affected summaries accordingly.

**Use focused summaries and selected histories to examine:**
- monthly recorded and provisionally eligible order counts, by currency where appropriate.
- monthly recorded net order values within each currency, without adding EUR and GBP amounts.
- industry summaries, including customers without an available industry assignment.
- customer activity, ordering gaps, first and last observed orders, and differences between customers with frequent and sparse orders.
- the distribution of excluded, unresolved and monetarily incomplete orders across months and customers.
- the possible influence of individual large orders on apparent monetary changes.

An observed period without eligible orders is not automatically a period of zero ordering activity. First establish whether the period was covered and whether excluded or unresolved records affect its interpretation. The first recorded order does not by itself identify a newly acquired customer; the last recorded order does not end observation while extraction coverage continues.

Use the summaries to assess whether suitable reference and subsequent periods can be formed. Do not require an order in every month or year, recent activity, or membership in an industry with an aggregate change as a condition for examining a customer.

#### 1.3.4 Examine the core measures and comparison support

Focus on the three measures defined in the data description: `ORDERCOUNT`, `TOTALORDERNETVALUE` and `AVGORDERNETVALUE`. They describe distinct aspects of the recorded orders but are mathematically related; changes in all three are not independent confirmation of a behavioural change.

Create provisional monthly customer-currency views where useful. Monthly profiles are the fixed basic representation of the prepared data. This phase assesses the support available for comparisons; it does not decide whether monthly aggregation itself should be adopted. Later detection may compare windows spanning several months.

**Use a small number of tables and graphics to answer specific questions:**

| **Question**                                                      | **Suggested evidence**                                                                                            |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Can the measures be calculated from the available orders?**     | Checks of distinct order identities, repeated header amounts, missing net amounts and currency assignments.       |
| **Which histories support comparisons?**                          | Eligible order counts, observed months, ordering gaps and coverage in potential reference and subsequent periods. |
| **How do status and eligibility decisions affect the measures?**  | Counts of included, excluded and unresolved orders by reason, month and currency.                                 |
| **Could individual orders dominate a monetary difference?**       | Selected customer histories alongside their underlying order-level values.                                        |
| **Which apparent zero periods or monetary totals are uncertain?** | Coverage checks, unresolved orders and missing contributing amounts.                                              |

Check whether a missing monetary amount can leave an order count available while making the corresponding total and average unavailable. Examine the extent of this issue before recommending comparison rules.

Select development examples with varied activity and data-quality characteristics, including ordinary histories and difficult cases. Apparent changes observed during exploration are development observations, not automatically detected events or established taxonomy types.

#### 1.3.5 Consolidate preparation and analysis decisions

Translate the findings into explicit recommendations for Phase 2 and identify decisions that still require ERP clarification or source evidence.

**Address:**
- the exact observation boundaries and treatment of incomplete or uncovered months.
- the resolution or documented restriction of duplicate and conflicting order records.
- the interpretation of observed document types, processing statuses, rejection statuses and order reasons.
- the treatment of partially rejected orders and the meaning of their recorded header amounts.
- unmatched customer and lookup records, missing required fields and unusual monetary values.
- the definition of relevant customer-currency histories and periods with zero eligible orders.
- the availability of the three core measures and restrictions on their interpretation.
- development and evaluation boundaries and their effect on later exploration.

For each consequential decision, record the supporting evidence, rationale, status and expected effect on records, customers or measures. Distinguish rules adopted for provisional exploration from rules approved for preparing the primary analytical population.

### 1.4 Required outputs

**Maintain one reproducible notebook containing:**
1. **Data inventory and structural assessment:** Source granularity, order and customer counts, field meanings, keys, relationships and relevant quality findings.
2. **Coverage and eligibility assessment:** Observation boundaries, incomplete periods, status distributions and recorded, provisionally eligible, excluded or unresolved orders.
3. **Focused exploratory findings:** Overall and industry-level monthly summaries, selected customer histories and underlying orders where needed for interpretation.
4. **Measure and suitability assessment:** Feasibility of the three core measures, missing monetary information and support for customer-level window comparisons.
5. **Preparation decisions and open issues:** Recommended rules, evidence, effects and dependencies requiring clarification.
6. **Evidence-use record:** Development examples, reserved evaluation evidence and known prior exposure.

These outputs may be sections and tables within the same notebook. Export figures and tables to the directory specified by the project configuration in [src/config](src/config). The default export directory is [outputs/exports](outputs/exports). Outputs derived from production data must use [outputs/.exports](outputs/.exports). Use the configured path consistently throughout the notebook.

### 1.5 Completion criteria

**Phase 1 is complete when:**
- the source granularity and relationships needed for an order-level table are understood.
- consequential quality problems, code meanings and coverage limitations are documented.
- the three core measures have been assessed for calculability and interpretation.
- recorded, provisionally eligible, excluded and unresolved orders are distinguishable in the assessment.
- customer histories have been examined sufficiently to inform comparison support and preparation rules.
- development and evaluation boundaries are documented.
- Phase 2 can proceed using explicit recommendations and a list of issues that must be resolved before the primary profiles are generated.

Exhaustive exploration is not required. An unresolved issue that prevents a trustworthy core measure or comparison must be identified as a blocker with a specified next action.

### 1.6 Optional refinements

After the core assessment, additional exploration may examine ordering intervals, recency at a defined reference date or more detailed industry and activity-group summaries.

Undertake these refinements only when they address a specific limitation or analytical question. They do not add required columns to the monthly profile schema or expand the investigation to item-level purchasing characteristics.

---

## Phase 2 - Use ERP data to prepare customer profiles

### 2.1 Purpose

Transform the raw ERP extracts into a reproducible order-level interim table and monthly customer profiles suitable for the core change analysis.

This phase applies and verifies the preparation decisions from Phase 1. It keeps technical representation, analytical order eligibility and measure-specific assessability distinct. The interim table retains technically validated orders, including orders later excluded from analytical measures. The monthly profiles contain the documented measures for the eligible population.

The main outputs are an enriched table with one row per order, profiles with one row per customer, calendar month and transaction currency, and the records needed to understand exclusions, unavailable values and observation coverage.

> **Methodological basis:** This phase adapts CRISP-DM's data-selection, cleaning, integration, construction and formatting activities (IBM, n.d.), supported by tidy-data principles for organising observations and variables (Wickham, 2014). The separation of development and evaluation evidence informs empirically selected rules and transformations (Kapoor & Narayanan, 2023). ERP-specific eligibility, coverage and calculation rules are project-specific decisions requiring justification.

### 2.2 Inputs

- The preserved raw extracts and their verified import settings.
- The raw, interim and processed schemas defined in the data description.
- Phase 1 findings on source structure, relationships, coverage, customer histories and data quality.
- The project plan's observation window, order-eligibility policy and three core measures.
- Documented ERP clarifications needed to settle consequential status and amount interpretations.
- The declared separation between development evidence and final evaluation evidence.

Resolve issues affecting the construction or interpretation of the primary profiles before generating them. Record any remaining restrictions explicitly.

### 2.3 Core procedure

#### 2.3.1 Finalise technical and analytical preparation rules

Specify the exact 24-month observation boundaries using `SALESORDERDATE`. Record the extraction date, available coverage and treatment of incomplete calendar months.

Define reproducible rules for parsing identifiers, dates, codes, currencies and monetary values. Preserve leading zeros in identifiers and codes. Investigate missing order identities and conflicting header values before representing an affected record as a unique order. Do not replace missing monetary values with zero.

**Keep three decisions separate:**
1. **Technical representation:** Can the source rows be represented reliably as one identified order?
2. **Analytical eligibility:** Does that order belong to the defined population for purchasing-change analysis?
3. **Measure assessability:** Can the relevant count, monetary measure or comparison be calculated from the available evidence?

Translate the project plan's working eligibility policy into an explicit, verified configuration:

- Treat `OR` as the documented sales-order type. Include another type only after its meaning and suitability have been verified.
- Include orders with rejection status `A` when other requirements are met.
- Exclude fully rejected orders with rejection status `C` from the primary analytical population.
- Settle the treatment of partially rejected orders with status `B` only after clarifying what `TOTALNETAMOUNT` represents for those orders. Until then, exclude them from the primary profiles and report their extent.
- Do not interpret a missing or unknown rejection status as `A`; resolve it or record the order as outside the primary eligible population.
- Do not exclude open or in-progress orders solely because processing is incomplete. Review unrecognised processing statuses.
- Use `SDDOCUMENTREASON` as context unless a verified reason code identifies a business process outside the analytical scope.
- Do not use order magnitude or a zero or negative amount as an automatic exclusion rule. Investigate unusual values and document any justified treatment.

Apply the same adopted analytical order population to all three core measures. An otherwise eligible order with an unavailable amount remains in the count population, while affected monetary measures are marked unavailable.

Record the number of source rows, distinct orders and affected customers for technical issues, analytical exclusions and missing amounts. Report overlapping reasons without adding their counts as if they were disjoint groups.

#### 2.3.2 Construct and verify the enriched order-level interim table

Construct `data/data-example/interim/001_order_header_data.csv` with exactly one row per reliably identified `SALESORDER`, following the schema in the data description.

Check that repeated header fields agree across the order's item rows. Retain `TOTALNETAMOUNT` once per order; do not sum repeated header values across items. Preserve the original codes and attach the documented text descriptions where mappings are available.

Join `SOLDTOPARTY` to the customer master, `SDDOCUMENTREASON` to its description mapping, and customer `INDUSTRY` to its description mapping. Before each join, verify the expected uniqueness of the mapping key and investigate conflicting assignments. Use left joins so that an unmatched customer or description does not silently remove an order. Do not match missing join keys to one another.

**Verify:**
- uniqueness of `SALESORDER` in the completed interim table.
- the number of represented orders before and after enrichment.
- unchanged recorded net amounts within each currency after enrichment.
- unmatched customers, reasons and industries and their effects on the available descriptions.
- unresolved source conflicts and orders that could not be represented reliably.

Retain technically validated orders with their types and statuses even when they will later be analytically excluded. Document records that cannot be represented in the interim table and keep them visible in the preparation report.

The available customer-master assignment is not assumed to be the customer's historically verified industry at every order date. Likewise, a recorded net order amount is not automatically realised revenue.

#### 2.3.3 Define eligibility and calculate the core measures

Apply the adopted order-eligibility rules to the interim table before constructing analytical measures. Retain a reproducible account of which orders are included, excluded or unresolved and why.

Use `SOLDTOPARTY` as the customer identifier, `SALESORDERDATE` to assign a calendar month and `TRANSACTIONCURRENCY` to keep currency histories separate. Each month is represented by its first calendar day.

**Calculate the three measures for each customer-month-currency combination:**

| **Measure**              | **Calculation and missing-value rule**                                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ORDERCOUNT`**         | Count distinct eligible `SALESORDER` values.                                                                                                                  |
| **`TOTALORDERNETVALUE`** | Sum `TOTALNETAMOUNT` once per eligible order. If an eligible contributing order has an unavailable amount, mark the complete total as missing.                |
| **`AVGORDERNETVALUE`**   | Divide the complete `TOTALORDERNETVALUE` by `ORDERCOUNT` when the total is available and the count is greater than zero. Otherwise leave the average missing. |

Maintain a feature specification with each measure's meaning, source fields, formula, unit, eligible population, missing-value treatment and interpretation limits. State later which measures act as detection inputs and which support classification or description. The three stored measures are mathematically related and must not be treated as independent evidence.

Do not add EUR and GBP monetary amounts without a documented conversion. Order counts may be combined across currencies for a separately specified analysis only if each order contributes once.

#### 2.3.4 Construct monthly customer-currency histories

Construct `data/data-example/processed/001_customer_monthly_profiles.csv` using the schema in the data description. Its composite key is `CUSTOMER_ID`, `PERIODSTART` and `TRANSACTIONCURRENCY`. Retain `INDUSTRY` and `INDUSTRY_TEXT` as contextual attributes.

Define the relevant customer-currency combinations and their observation intervals using the available extraction and coverage evidence. Do not define the end of observation as a customer's last order merely because later orders are absent.

**For periods without eligible orders:**
- Set `ORDERCOUNT` and `TOTALORDERNETVALUE` to zero only when observation coverage supports zero eligible activity for that customer-currency combination.
- Leave `AVGORDERNETVALUE` missing when `ORDERCOUNT` is zero.
- Do not convert missing extraction coverage, incomplete observation periods or unresolved evidence into zero activity.
- Do not infer inactivity across all currencies from a zero count in one currency.

Preserve the distinction between an observed zero, an unavailable monetary measure and an unobserved or unassessable period. Record coverage restrictions in linked preparation information if they are not columns of the documented monthly schema.

Use the same monthly table to construct overall and industry summaries and longer customer comparison windows. Sum counts and complete monetary totals within the relevant currency and coverage scope. Recalculate an aggregate average as the aggregate total divided by the aggregate count; do not average monthly or customer averages without the appropriate weighting.

If a required contributing monetary total is missing, the complete broader total and its average remain missing. A partial sum may be shown separately only when labelled incomplete and accompanied by its coverage. Retain customers without an industry assignment in customer-level and overall analyses, and show their contribution when reporting industry groups.

#### 2.3.5 Confirm suitability and verify the prepared data

Reassess suitability for the intended comparisons after technical validation and analytical selection. A prepared monthly row alone does not establish sufficient evidence for change detection.

Distinguish comparisons with adequate evidence and no detected change from comparisons that cannot be assessed. Do not require activity in every month or year, a recent order, a later purchase or an available industry assignment merely to retain a customer. A history with unavailable monetary measures may still support an order-count comparison.

**Verify:**
- uniqueness of the order-level and monthly composite keys.
- reconciliation of monthly `ORDERCOUNT` with eligible interim orders.
- reconciliation of complete monetary totals by month and currency, including propagation of missing amounts.
- calculation of averages and treatment of zero-order periods.
- unchanged observed counts and amounts after adding justified zero-activity months.
- the effects of exclusions, unresolved orders and incomplete coverage.
- selected monthly profiles against their underlying orders.
- correct regeneration and reloading of the exported files.

Investigate discrepancies before using affected profiles for detection. Report how preparation decisions change the number of assessable customers, months and comparisons.

### 2.4 Required outputs

**Produce:**
1. **Enriched order-level interim table:** One validated row per represented order, including original codes, available descriptions and customer industry information.
2. **Monthly customer-currency profiles:** The documented composite key and three core measures.
3. **Eligibility and coverage record:** Technical issues, analytical exclusions, unresolved orders, observed zero periods and restrictions on measures or comparisons.
4. **Preparation and feature specification:** Applied rules, ERP clarifications, formulas, configuration and interpretation limits.
5. **Verification results:** Key checks, reconciliation, discrepancies and their resolution.
6. **Reproducible preparation code:** Input references, transformations, output schemas and data versions.

Export the interim and processed datasets as CSV according to the data description: UTF-8, semicolon-separated fields, dates in `YYYY-MM-DD` format, decimal points for monetary values and empty fields for missing values. Preserve identifiers as strings and monetary precision during calculation.

Convert the exported CSV files to Parquet and use the Parquet versions in subsequent phases according to the [shared data-format workflow](#data-formats-and-file-workflow). Verify that conversion and reloading preserve the intended identifiers, values, types and missingness. Preserve the original extracts.

### 2.5 Completion criteria

**Phase 2 is complete when:**
- observation boundaries and primary order-eligibility rules are explicit and justified.
- technically representable orders and analytical exclusions remain distinguishable.
- the enriched interim table is unique at order level and its joins have been verified.
- the monthly profiles match the documented customer-month-currency schema.
- the three core measures reconcile with eligible orders and handle missing amounts correctly.
- observed zero activity, unavailable measures and uncertain coverage are distinguishable.
- customer and comparison suitability restrictions are recorded.
- the outputs can be regenerated and reloaded correctly and are ready for the planned window comparisons.

An unresolved issue affecting the primary analytical population, a core measure or trustworthy comparisons is a blocker until its treatment and consequences are documented.

### 2.6 Optional refinements

The order-level dates may support additional temporal descriptions, such as the interval between eligible orders or days since the last eligible order at a defined reference date. Such descriptions require adequate prior observation and a stated choice between currency-specific and combined ordering activity.

These refinements are not required columns of the current monthly profile schema. Introduce them only when they address an identified limitation of the core analysis, and keep their definitions and evidence requirements separate from the three core measures.

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

| **Decision**                | **Required specification**                                                                                                                |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Target patterns**         | State which changes the initial approach addresses, such as changes in ordering activity, recorded net order values or their combination. |
| **Detection inputs**        | Identify the selected measures and distinguish them from additional descriptive measures.                                                 |
| **Comparison windows**      | Define reference and subsequent window lengths, movement, boundary conventions and treatment of incomplete windows.                       |
| **Comparison support**      | Specify the observations, order activity and coverage needed to assess each measure.                                                      |
| **Change criteria**         | Define how deviation from usual variability, minimum magnitude and sufficient evidence are assessed.                                      |
| **Contextual restrictions** | Specify how recurring patterns, isolated large orders and coverage changes affect interpretation or assessability.                        |

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
- missing monetary values, excluded or unresolved orders, changes in currency use and other preparation effects.
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

Possible refinements include additional temporal descriptions based on eligible order dates, alternative window designs or a second detection method such as change-point segmentation.

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

See [docs/literature/bibliography.md](docs/literature/bibliography.md).
