<div align="center">

# Project plan for the Bachelor's Thesis

This project plan defines the objectives, scope and methodological approach for detecting, classifying and explainably describing changes in B2B customers' purchasing behaviour using ERP sales order data. It defines a header-based investigation of ordering activity and recorded net order values, the selection of orders and customer histories, taxonomy development and evaluation. The scope distinguishes the required investigation from optional refinements using the same data basis.

</div>

## Table of Contents

- [1 Title and research question of the Bachelor's Thesis](#1-title-and-research-question-of-the-bachelors-thesis)
    - [1.1 Title](#11-title)
    - [1.2 Research question](#12-research-question)
        - [1.2.1 Meaning of significant purchasing behaviour changes](#121-meaning-of-significant-purchasing-behaviour-changes)
    - [1.3 Sub-questions](#13-sub-questions)
- [2 Brief description of the topic](#2-brief-description-of-the-topic)
- [3 Research objectives and intended contributions](#3-research-objectives-and-intended-contributions)
    - [3.1 Development and automatic assignment of change types](#31-development-and-automatic-assignment-of-change-types)
    - [3.2 Explainable descriptions of detected changes](#32-explainable-descriptions-of-detected-changes)
- [4 Scope and priorities](#4-scope-and-priorities)
    - [4.1 Core scope](#41-core-scope)
    - [4.2 Evaluation as part of the core scope](#42-evaluation-as-part-of-the-core-scope)
    - [4.3 Optional extensions](#43-optional-extensions)
    - [4.4 Implementation priorities and boundaries](#44-implementation-priorities-and-boundaries)
- [5 Methodological approach](#5-methodological-approach)
    - [5.1 Main analytical steps](#51-main-analytical-steps)
    - [5.2 Initial detection approach](#52-initial-detection-approach)
    - [5.3 Taxonomy development and automatic classification](#53-taxonomy-development-and-automatic-classification)
    - [5.4 Explainable output and evaluation separation](#54-explainable-output-and-evaluation-separation)
    - [5.5 Relationship to the methodological framework](#55-relationship-to-the-methodological-framework)
- [6 Evaluation strategy](#6-evaluation-strategy)
    - [6.1 Evaluation data and reference information](#61-evaluation-data-and-reference-information)
    - [6.2 Change detection](#62-change-detection)
    - [6.3 Automatic type assignment](#63-automatic-type-assignment)
    - [6.4 Taxonomy evaluation](#64-taxonomy-evaluation)
    - [6.5 Description evaluation](#65-description-evaluation)
    - [6.6 Reporting, sensitivity and interpretation](#66-reporting-sensitivity-and-interpretation)
- [7 Data scope and limitations](#7-data-scope-and-limitations)
    - [7.1 Behavioural scope and economic interpretation](#71-behavioural-scope-and-economic-interpretation)
    - [7.2 Project orders and routine orders](#72-project-orders-and-routine-orders)
    - [7.3 Observation and contextual limitations](#73-observation-and-contextual-limitations)
- [8 Observation period and order eligibility](#8-observation-period-and-order-eligibility)
    - [8.1 Observation period](#81-observation-period)
    - [8.2 Order eligibility](#82-order-eligibility)
        - [8.2.1 Technical representation and interim retention](#821-technical-representation-and-interim-retention)
        - [8.2.2 Analytical inclusion and exclusion rules](#822-analytical-inclusion-and-exclusion-rules)
        - [8.2.3 Reporting selection effects](#823-reporting-selection-effects)
    - [8.3 Customer suitability](#83-customer-suitability)
    - [8.4 Decisions to finalise during data assessment](#84-decisions-to-finalise-during-data-assessment)
- [9 Analytical measures and feature definitions](#9-analytical-measures-and-feature-definitions)
    - [9.1 Core measures](#91-core-measures)
    - [9.2 Optional temporal descriptions](#92-optional-temporal-descriptions)
    - [9.3 Calculation and interpretation rules](#93-calculation-and-interpretation-rules)
- [Bibliography](#bibliography)

---

## 1 Title and research question of the Bachelor's Thesis

### 1.1 Title

**Title of the thesis in English:**
_Detection and Typology of Explainable Purchase Behavior Changes in B2B Wholesale Customers Using ERP Time Series Data._

> **Title of the thesis in German:**
> _Erkennung und Typisierung erklärbarer Kaufverhaltensveränderungen bei B2B-Großhandelskunden auf Basis von ERP-Zeitreihendaten._

### 1.2 Research question

**Key research question in English:**
_What types of significant changes in purchasing behavior among B2B wholesale customers can be automatically identified, classified, and described in an explainable manner based on ERP order data?_

> **Key research question in German:**
> _Welche Typen signifikanter Kaufverhaltensveränderungen lassen sich bei B2B-Großhandelskunden anhand von ERP-Auftragsdaten automatisch erkennen, klassifizieren und erklärbar beschreiben?_

#### 1.2.1 Meaning of significant purchasing behaviour changes

In this thesis, a significant purchasing behaviour change is defined as a change in at least one examined behavioural dimension of a customer that is sufficiently supported by the available ERP sales order data, exceeds the customer's usual variability relative to an appropriate reference period, and reaches a minimum magnitude justified for the investigation.

**This definition combines three requirements:**
- **Deviation from usual behaviour:** The observed change exceeds the variation normally present in the customer's ordering history.
- **Meaningful magnitude:** The change meets a justified magnitude criterion appropriate to the behavioural dimension under investigation.
- **Sufficient evidence:** The available observations and data quality support the comparison and interpretation.

The term "significant" is used in this operational sense and does not, by itself, imply statistical significance established through a hypothesis test. Any claims of statistical significance require an explicit statistical assessment.

The duration of a change is considered when distinguishing temporary deviations from sustained changes. Reference periods, magnitude criteria, evidence requirements and any duration criteria will be specified and justified during methodological development, before the final evaluation.

### 1.3 Sub-questions

The main research question is supported by four sub-questions addressing detection, taxonomy development, automatic classification and explainable descriptions.

Sub-questions are used rather than formal hypotheses because the thesis develops and evaluates an exploratory approach without presupposing specific change types or theoretically established expectations about its performance. They structure the investigation while allowing both successful results and limitations to contribute to answering the main research question.

**Sub-questions in English:**
- **SQ1 - Change detection:** _To what extent can purchasing behaviour changes be detected through time-window-based comparisons of customer profiles derived from ERP data, according to the defined significance criteria?_
- **SQ2 - Taxonomy development:** _Which interpretable change types can be developed from the examined behavioural patterns and conceptual and domain-informed reasoning, and which characteristics distinguish these types and support their combination?_
- **SQ3 - Automatic classification:** _How reliably can detected change events be assigned to the developed types using documented rules, and which cases remain ambiguous or unassigned?_
- **SQ4 - Explainable descriptions:** _To what extent do the generated descriptions represent the detected changes and the rationale for their type assignments accurately, completely and in a manner traceable to the underlying data?_

> **Sub-questions in German:**
>- **UF1 - Erkennung:** _In welchem Umfang lassen sich Kaufverhaltensveränderungen durch zeitfensterbasierte Vergleiche kundenbezogener ERP-Profile entsprechend den festgelegten Signifikanzkriterien erkennen?_
>- **UF2 - Taxonomieentwicklung:** _Welche interpretierbaren Veränderungstypen lassen sich aus den untersuchten Verhaltensmustern und fachlich-theoretischen Überlegungen entwickeln, und anhand welcher Merkmale lassen sie sich unterscheiden und kombinieren?_
>- **UF3 - Automatische Klassifikation:** _Wie zuverlässig lassen sich erkannte Veränderungsereignisse anhand dokumentierter Regeln den entwickelten Typen zuordnen, und welche Fälle bleiben mehrdeutig oder nicht zuordenbar?_
>- **UF4 - Erklärbare Beschreibung:** _Inwieweit geben die erzeugten Beschreibungen die erkannten Veränderungen und die Gründe ihrer Typenzuordnung sachlich korrekt, vollständig und anhand der zugrunde liegenden Daten nachvollziehbar wieder?_

**Evaluation of the sub-questions (see [6 Evaluation strategy](#6-evaluation-strategy)):**
- **SQ1:** Precision, recall, F1 score, and false positives in controlled cases. Supplemented by real-case analyses and sensitivity analyses.
- **SQ2:** Examination of type definitions and their applicability to held-out cases, including overlaps and uncovered patterns.
- **SQ3:** Consistency with reference classifications, key metrics per type, and transparent presentation of ambiguous or unclassified cases.
- **SQ4:** Verification of correctness and completeness, as well as the relationship between statements, measured values, and classification criteria.

The evaluation addresses each sub-question separately. Detection is assessed against reference changes, the taxonomy through structured examination of held-out cases, automatic classification against reference assignments, and descriptions through checks of factual correctness, completeness and traceability.

Data preparation and feature selection provide the methodological foundation for these investigations. They do not constitute separate research objectives requiring an exhaustive comparison of all possible measures.

---

## 2 Brief description of the topic

This bachelor's thesis investigates which types of significant changes in customer purchasing behaviour can be automatically detected, classified and explainably described using ERP sales order data from a B2B wholesaler. The investigation covers a 24-month observation window and is limited to changes in ordering activity and recorded net order values observable from sales order headers. Customer industry information provides context for grouped summaries. Product, assortment, quantity and discount analyses are outside the selected scope.

The analytical basis consists of an enriched table with one row per order and monthly profiles with one row per customer, calendar month and transaction currency. The core measures are order count, total net order value and average net order value. Reference and comparison windows may span several months, depending on the available ordering activity and the evidence required for detection.

Exploration proceeds from the overall data inventory and monthly company-level summaries to industry summaries, customer histories and individual change events. This sequence structures data understanding and presentation; customer-level detection is not restricted to customers in groups with conspicuous aggregate changes. Comparisons use a documented analytical order population, while the inventory also reports orders excluded or unresolved for analytical purposes.

The intended contribution is an evaluated approach combining an interpretable taxonomy, reproducible automatic classification and descriptions traceable to the underlying data. Evaluation addresses detection, taxonomy suitability, assignment quality and description correctness and completeness using controlled cases, held-out real customer histories and selected sensitivity analyses. The findings describe recorded ordering behaviour with the focal company, within the examined dimensions. They do not establish behavioural causes, actual purchases from other suppliers or realised revenue.

---

## 3 Research objectives and intended contributions

The thesis aims to develop and evaluate an approach for detecting, classifying and explainably describing significant changes in customer purchasing behaviour using ERP sales order data. Significance is understood according to the operational definition provided alongside the research question.

The intended contributions are an interpretable taxonomy of purchasing behaviour changes, the automatic assignment of detected changes to its types, and evidence-based descriptions that make the findings and their classification understandable.

### 3.1 Development and automatic assignment of change types

The thesis develops a taxonomy that describes what changes in a customer's observed purchasing behaviour. Its development combines the examination of change patterns in the available data with conceptual and domain-informed reasoning. The selected header-based measures provide the observational basis. They do not predetermine the final change types. Possible patterns include changes in ordering frequency or net order values, their combinations and observable interruptions in activity. These are development candidates rather than a fixed or exhaustive taxonomy.

Each type will have a clear name, definition and documented assignment criteria. Once established, these criteria will support the reproducible automatic classification of detected change events.

**The following principles guide taxonomy development and application:**
- **Changes are classified, rather than customers permanently labelled.** A customer may exhibit different change types at different points in time.
- **Combined changes remain representable.** Simultaneous changes in several behavioural dimensions may be expressed through multiple assignments or a combined type, depending on the justified taxonomy design.
- **Uncertain assignments remain explicit.** Events that are ambiguous or insufficiently supported are not forced into a type.

The taxonomy is intended to organise and distinguish the change patterns supported by the investigated dataset. Its applicability beyond this context will be discussed rather than assumed.

### 3.2 Explainable descriptions of detected changes

For each detected change event, the approach will provide a description that allows a reader to understand the observed change and the basis for its type assignment.

**Descriptions will include:**
- the temporal context and comparison periods.
- the affected behavioural dimensions and measures.
- the direction and magnitude of the change, supported by before-and-after values.
- the observations and criteria supporting the assigned type or types.
- relevant limitations, such as sparse ordering activity, missing data or the influence of an individual large order.

Standardised descriptions, numerical comparisons and suitable visualisations form the intended basis of this output. Additional explanation methods will be selected where required by the detection or classification approach. Explainability concerns the evidence for the detected change and its classification. It does not establish why the customer changed their behaviour or support causal claims about motives, competitors or future purchasing decisions.

---

## 4 Scope and priorities

The thesis prioritises a complete, manageable investigation covering data preparation, change detection, taxonomy development, automatic type assignment, explainable descriptions and evaluation. The reduction in data scope concentrates the investigation on ordering activity and net order values. Evaluation remains part of the required scope.

The main emphasis is on the taxonomy, reproducible type assignment and evidence-based descriptions. One interpretable main detection approach is sufficient. An extensive comparison of algorithms is not a primary objective.

### 4.1 Core scope

| **Component**                          | **Required scope**                                                                                                                                                                                                     |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data understanding and preparation** | Assess the 24-month extract, its order-item structure, repeated header values, statuses, currencies, customer assignments and observation coverage. Construct the documented order-level and monthly profile datasets. |
| **Behavioural measures**               | Use `ORDERCOUNT`, `TOTALORDERNETVALUE` and `AVGORDERNETVALUE`. Distinguish detection inputs from descriptive measures and account for their mathematical dependence.                                                   |
| **Descriptive overview**               | Report order and customer counts, analytical eligibility and monthly counts and net order values at overall, industry and customer levels. These summaries establish context and support method choices.               |
| **Change detection**                   | Select, justify and implement one main time-window comparison approach that operationalises the documented significance criteria on suitable customer histories.                                                       |
| **Taxonomy development**               | Develop a compact taxonomy of supported header-based change patterns. Document definitions, distinctions, combinations and assignment criteria.                                                                        |
| **Automatic assignment**               | Apply the documented rules reproducibly, with explicit treatment of combined changes, ambiguity and insufficient evidence.                                                                                             |
| **Explainable descriptions**           | Generate standardised descriptions and selected visualisations showing what changed, by how much, over which periods and why a type was assigned.                                                                      |
| **Evaluation and discussion**          | Assess detection, taxonomy applicability, automatic assignment and descriptions. Report errors, uncertainty, selected sensitivity checks and limitations.                                                              |

The number of change types is not fixed in advance. Descriptive summaries alone do not answer the research question; the complete investigation includes automatic event detection, type assignment, descriptions and evaluation.

### 4.2 Evaluation as part of the core scope

Evaluation is required for the minimum complete investigation.

**It will combine:**
- controlled cases with known changes and suitable no-change cases to assess detection performance and false alarms.
- a manageable selection of held-out real customer histories to examine type suitability, assignment plausibility and description correctness, including ambiguous and unsuccessful cases.
- a limited sensitivity analysis of consequential choices, such as comparison windows, thresholds or an analytically plausible alternative eligibility treatment.

Cases used for final evaluation will be separated from those used to develop the taxonomy and tune the approach. Controlled-case performance does not, by itself, demonstrate performance or usefulness on real customer histories.

Without a user study, description assessment concerns factual correctness, completeness and traceability. It does not establish demonstrated comprehensibility or usefulness for sales staff.

### 4.3 Optional extensions

Optional refinements use the selected data basis and are undertaken only after the main approach and its evaluation are complete.

| **Extension**                                         | **Condition for inclusion**                                                                                                                                               |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **An additional detection method**                    | Sufficient time remains for a meaningful comparison. A simple reference approach may already support the core evaluation.                                                 |
| **Additional temporal descriptions**                  | Order dates and observation coverage support interpretable ordering-gap or recency measures, and they resolve a relevant limitation of the core measures.                 |
| **Deeper subgroup comparisons**                       | Industry or activity groups contain sufficient observations for a clearly defined supplementary question. Basic industry summaries are already part of the core overview. |
| **Expert feedback or additional explanation methods** | Access and time are available and the extension contributes evidence beyond the required correctness and traceability checks.                                             |

Product, assortment, quantity, price-condition and discount analyses are outside the agreed investigation rather than expected optional implementation tasks.

### 4.4 Implementation priorities and boundaries

Development proceeds through a complete initial workflow using the three core measures, followed by justified refinements. Reproducible Python code, Jupyter notebooks and documented outputs constitute the required technical deliverables. The detailed table schemas, field origins and CSV representation are maintained in the [data description](docs/project/data_description.md).

A dashboard, production integration and real-time monitoring are outside the technical scope. Churn prediction, customer-motive inference, profitability analysis and causal decomposition of price, quantity or product-mix effects are outside the analytical scope.

---

## 5 Methodological approach

The thesis follows an exploratory development process followed by a separate evaluation. Preparation, detection, taxonomy development, classification and explanation may be refined iteratively on development evidence. The final evaluation assesses the fixed approach on evidence not used for those decisions.

### 5.1 Main analytical steps

| **Step**                                    | **Approach**                                                                                                                                                                                              | **Main output**                                                                                  |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **1. Understand and assess the data**       | Examine distinct customers and orders, monthly coverage, statuses, currencies, repeated header values and customer-master matches. Reserve evaluation evidence before behavioural exploration and tuning. | Data assessment, development/evaluation boundaries and documented preparation decisions.         |
| **2. Prepare the analytical basis**         | Construct the enriched order-level interim table. Apply analytical eligibility rules and create the monthly customer-currency profiles.                                                                   | Reproducible profiles and an account of exclusions, unresolved records and unavailable measures. |
| **3. Detect and characterise changes**      | Compare suitable reference and subsequent windows. Assess usual variability, magnitude, evidence and temporal extent, then consolidate repeated detections of the same event.                             | Change events with comparison values, decision evidence and limitations.                         |
| **4. Develop the taxonomy**                 | Examine development events and conceptual and domain-informed distinctions. Define supported types and combinations.                                                                                      | A documented taxonomy with reproducible assignment criteria.                                     |
| **5. Automate assignment and descriptions** | Implement the type rules and generate descriptions from measurements, applied criteria and source evidence.                                                                                               | Classified and explained events, including ambiguous or unassigned outcomes.                     |
| **6. Evaluate and discuss**                 | Evaluate the fixed components and selected complete customer histories using controlled cases, held-out real cases and limited sensitivity analyses.                                                      | Evidence of performance, applicability, errors and limitations.                                  |

The exploratory presentation moves from the data inventory to overall monthly trends, industry summaries, customer histories and individual events. Counts and values for the analytical population are distinguished from summaries of all recorded source orders. Individual customer changes may offset one another in aggregate; therefore, a conspicuous company-level or industry-level change is not a prerequisite for customer-level detection.

General structural checks may cover the extracts. Behavioural exploration used to choose windows, thresholds or taxonomy types uses the declared development evidence. All currency histories of a customer belong to the same development or evaluation partition when customers are held out. Population-wide descriptive results are not used retrospectively to tune the final evaluation configuration.

### 5.2 Initial detection approach

A time-window-based comparison of customer profiles is the planned main approach. Monthly profiles are the fixed basic representation. Reference and subsequent windows may combine several months; monthly storage does not imply that a single-month comparison is informative for every customer.

Comparison-window lengths, minimum evidence requirements and feature-specific change criteria are selected using development data and fixed before final evaluation. Criteria address deviation from usual variability, a justified minimum magnitude and sufficient observation support. If the history cannot support these assessments, the comparison is reported as unassessable.

The three stored measures are mathematically related. Their use as detection inputs or supporting descriptions must be stated explicitly; concurrent changes in all three are not independent confirmations. Count comparisons may additionally use totals across currencies, while monetary comparisons remain within a currency. Any such count aggregation must be documented and must not create duplicate reports of the same event.

Interpretation considers seasonal patterns, irregular ordering, changes in currency use and the influence of individual large orders. The 24-month window provides limited evidence about recurring annual patterns. A change in one currency alone does not establish a change in the customer's overall ordering activity. Sustained-change claims require an explicit duration or follow-up rule, not merely a long comparison window.

Successive rolling comparisons may overlap. The approach specifies how repeated detections are consolidated and how event timing is represented at the available temporal resolution. An extensive method comparison is outside the core scope. If a different main detection approach becomes necessary, its rationale and the method-specific wording of SQ1 will be aligned; the registered title and main research question remain unchanged.

### 5.3 Taxonomy development and automatic classification

Taxonomy development is researcher-led and data-informed. It combines systematic examination of development cases with conceptual and domain-informed reasoning. The inspected cases, type definitions and reasons for revisions will be documented.

The taxonomy covers observable changes in ordering activity and net order values. It does not claim to exhaust all dimensions of purchasing behaviour. Once established, a rule-based algorithm applies the assignment criteria automatically, permits justified combinations and identifies ambiguous or unsupported cases. Changes are classified as events; customers are not permanently labelled by one type.

Clustering is not required for the core approach. If used as an exploratory aid, its outputs still require interpretation and evaluation before becoming taxonomy types.

### 5.4 Explainable output and evaluation separation

Descriptions are generated from before-and-after measurements, comparison periods, applied criteria and relevant data limitations. They explain the observed change and its classification, without claiming behavioural causes. Templates and numerical evidence are sufficient for the core output.

Order-selection rules, measure definitions, comparison settings, taxonomy criteria and description rules are fixed before final evaluation. Subsequent sensitivity settings and their results are reported separately. Customer-level separation is the starting option; any temporal split must address overlapping observations and windows.

### 5.5 Relationship to the methodological framework

This project plan defines the objectives, scope, eligibility principles and evaluation commitments. The [data description](docs/project/data_description.md) defines the raw, interim and processed schemas and their preparation contracts. The [FUUCCE framework](docs/framework/fuucce_framework.md) operationalises the six methodological phases and must be aligned with this header-based scope before its detailed tasks are applied.

Detailed field lists and CSV settings are maintained in the data description rather than duplicated here. Prepared CSV outputs use the documented semicolon separator; import, export and conversion routines must follow the same convention while respecting the actual format of preserved raw extracts.

---

## 6 Evaluation strategy

The evaluation assesses four components separately: change detection, the taxonomy, automatic type assignment and generated descriptions. Results are interpreted against the evidence available for each component rather than combined into a single overall score.

The evaluation design combines established metrics with project-specific assessment criteria. Metric selection and interpretation will be documented explicitly, reflecting the importance of matching evaluation measures to the intended assessment goals (Opitz, 2024).

### 6.1 Evaluation data and reference information

**The evaluation will use:**
- **Controlled cases:** Time series with known changes and suitable no-change controls, covering different change magnitudes, behavioural dimensions and combinations.
- **Held-out real cases:** Customer histories and change events not used to develop the taxonomy or tune the approach.
- **Selected sensitivity scenarios:** Variations of consequential analytical choices to examine the stability of the findings.

The controlled scenarios will be informed by observed data characteristics without being restricted to cases that directly reproduce the detection rules. They will cover the selected count and net-value dimensions, combined changes, sparse activity, isolated large orders and suitable no-change controls with ordinary variation. Generated counts, totals and averages must remain mathematically consistent. A profile-level generator is sufficient; a complete ERP simulator is not required.

Unmodified real histories are not automatically treated as no-change controls. When changes are injected into real histories, additional detections cannot automatically be counted as false positives because the original histories may contain unknown changes. Quantitative detection scores will therefore be calculated only where the reference information supports the required judgements.

The separation of development and evaluation data, case-selection procedures and reference construction will be documented before the final evaluation.

### 6.2 Change detection

Detection will be evaluated at event level using _precision_, _recall_ and _F1_. These measures and the use of a temporal tolerance for matching detected and reference changes are established in change-point evaluation (Truong et al., 2020).

| **Metric**                | **Definition**                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Precision**             | Matched detected events divided by all detected events.                                                    |
| **Recall**                | Matched reference events divided by all reference events.                                                  |
| **F1-score**              | Harmonic mean of precision and recall: `2 × precision × recall / (precision + recall)`.                    |
| **False-alarm frequency** | Number of detected events in known no-change controls, normalised by their evaluated observation duration. |

Before evaluation, the event representation, temporal tolerance and treatment of repeated detections will be specified. **Matching will be one-to-one:** a reference event and a detected event can each contribute to at most one successful match.

True-positive, false-positive and false-negative counts will accompany the scores. Zero-denominator cases will be handled explicitly and reported rather than silently assigned a perfect score. Results will be presented by scenario to distinguish performance across change magnitudes and behavioural patterns.

### 6.3 Automatic type assignment

Assignment will first be assessed on reference events supplied directly to the classification component, separating classification errors from detection errors.

Reference assignments will be established through documented scenario expectations or manual review of held-out events without prior inspection of the algorithm's assignments. They will not be generated by the same classification code being evaluated.

| **Metric**                               | **Definition**                                                                                                 |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Exact-match ratio**                    | Proportion of evaluable events for which the predicted set of types exactly matches the reference set.         |
| **Precision and recall per type**        | Type-specific assessment of incorrect assignments and missed reference assignments.                            |
| **Unassigned and ambiguous proportions** | Proportions of evaluated events for which the system provides no assignment or flags an unresolved assignment. |

Exact match corresponds to subset accuracy in multi-label evaluation and is complemented by type-specific measures because it gives no partial credit for partly correct label sets (Zhang & Zhou, 2014).

System abstentions will not be silently excluded from classification scores where a definite reference assignment exists. Cases without a defensible reference assignment will be reported separately. Each type's reference frequency and the number of excluded or uncertain cases will be disclosed.

If reference review is performed by the thesis author alone, the resulting potential for reviewer bias will be acknowledged. An additional reviewer is an optional extension.

In addition to the separate component assessments, selected held-out customer histories will be processed through the complete sequence of change detection, automatic type assignment and description generation. These case analyses will examine how errors or uncertainty in earlier steps affect subsequent assignments and descriptions, including missed changes, false detections and unassigned events where the available reference evidence supports such judgements. The findings will be reported as part of the planned real-case analyses.

### 6.4 Taxonomy evaluation

The taxonomy will be examined separately from the correctness of its software implementation. This follows the distinction between taxonomy development and subsequent evaluation emphasised by Kundisch et al. (2022).

**A structured review of held-out cases will assess:**
- whether observed change patterns can be represented adequately.
- whether type definitions and assignment criteria are clear.
- whether overlaps represent meaningful combinations or unclear distinctions.
- which cases remain unsupported, ambiguous or outside the taxonomy.

Findings will be documented through case evidence and counterexamples. A high assignment rate alone will not be interpreted as evidence of taxonomy quality.

### 6.5 Description evaluation

Descriptions will be assessed for factual correctness and completeness. This distinction is informed by the separation of faithfulness and completeness in FineSurE (Song et al., 2024).

The thesis uses a project-specific adaptation for structured ERP evidence and standardised descriptions. It does not implement the original LLM-based FineSurE evaluator.

| **Measure**             | **Project-specific definition**                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Factual correctness** | Number of correct, source-supported factual claims divided by all assessed factual claims.                          |
| **Completeness**        | Number of correctly communicated required information items divided by all information items required for the case. |

A predefined checklist will specify claim boundaries, numerical tolerances and required information, including temporal context, affected measures, direction, magnitude, assignment rationale and applicable limitations.

Descriptions will be checked against the underlying analytical data and the documented classification criteria. Scores will be accompanied by assessed counts and examples of errors or omissions. Missing descriptions will be recorded as output failures rather than omitted from evaluation.

These measures assess correspondence with the evidence and required content. Without a user study, they do not establish comprehensibility or usefulness for sales staff.

### 6.6 Reporting, sensitivity and interpretation

Evaluation results will be reported with their denominators, case-selection basis and relevant scenario characteristics. Controlled and real-case findings will remain distinguishable.

A limited sensitivity analysis will examine selected thresholds or comparison periods and, where consequential and interpretable, an alternative order-eligibility treatment. The primary configuration will be fixed before final evaluation. Alternative settings will be reported separately rather than selected retrospectively to maximise the final scores.

No universal numerical success threshold is assumed. Any acceptance criteria will require justification before the final evaluation. Conclusions will distinguish demonstrated performance in the evaluated cases from claims that the available evidence cannot support.

Detailed sampling procedures, matching rules and review checklists will be specified in the [methodological framework](docs/framework/fuucce_framework.md).

---

## 7 Data scope and limitations

The analysis concerns ordering behaviour recorded with the focal B2B wholesaler. The [data description](docs/project/data_description.md) defines the reduced source basis: order header information, customer-to-industry assignments, order-reason descriptions and industry descriptions. Product master data, product price data and behavioural item-level features are not required. `SALESORDERITEM` may remain in the raw extract to verify its structure; it is not a behavioural input.

The prepared data comprise an enriched order table and monthly profiles keyed by `CUSTOMER_ID`, `PERIODSTART` and `TRANSACTIONCURRENCY`. Industry is a contextual grouping attribute, not a substitute for individual customer histories. Its absence does not automatically exclude a customer's otherwise usable history.

### 7.1 Behavioural scope and economic interpretation

The thesis investigates ordering frequency, recorded net order values and observable temporal patterns. It does not investigate assortment breadth, product-group shifts, quantities, pricing conditions, discount behaviour, contribution margins or profitability.

Net order values are not automatically invoiced or realised revenue. A change in monetary value cannot be attributed separately to price, quantity or product-mix effects using the selected fields. Currency conversion and inflation adjustment are not required parts of the investigation; monetary findings concern recorded nominal values within a currency.

The approach does not observe purchases from other suppliers or identify customer motives. A period without orders is described as an observed ordering gap, not established churn. The first observed order does not by itself identify a newly acquired customer. A return after an observed gap may be described only within the available history.

### 7.2 Project orders and routine orders

The dataset includes project-related and routine orders. Quotation identifiers and links between quotations and sales orders are not part of the analytical basis. The thesis therefore does not systematically distinguish these forms of business and does not acquire additional ERP relationships for that purpose.

Large individual orders may strongly influence monetary comparisons. Their effect is examined when interpreting relevant histories. High value alone does not establish a data error or project-order status and is not an exclusion rule. A change dominated by one order does not by itself demonstrate a sustained change in routine purchasing.

### 7.3 Observation and contextual limitations

The 24-month window and monthly profiles limit temporal precision, follow-up and the assessment of annual recurrence. Sparse order histories may support description but not reliable change detection. Partial periods, extraction gaps and unassessable comparisons remain explicit.

Unless historical snapshots are supplied, customer industry assignments and document statuses describe the available extract. The thesis does not reconstruct historical industry or status changes. Later ERP updates may affect the values associated with older order dates; the extraction date and relevant field semantics must therefore be documented.

Overall and industry summaries may change because the composition of active customers changes. Such aggregate movements provide context but do not establish an individual behavioural change or its cause.

---

## 8 Observation period and order eligibility

### 8.1 Observation period

The analysis covers a 24-month window based on `SALESORDERDATE`. Exact start and end dates, extraction date and any incomplete calendar months are recorded during preparation. Complete calendar months are used for primary monthly comparisons where available; incomplete periods must be identified and handled explicitly rather than treated as complete months with reduced activity.

The observation interval is supported by extraction coverage, not merely by the first and last order dates. Periods after a customer's last observed order remain relevant when coverage continues. Zero activity is recorded only where observation supports that interpretation.

### 8.2 Order eligibility

Three decisions are kept distinct: whether source records can be represented consistently, whether an order belongs to the analytical population, and whether a particular measure or comparison is assessable. All recorded orders can contribute to the data inventory; they are not automatically all eligible for the purchasing-change analysis.

#### 8.2.1 Technical representation and interim retention

The raw extracts are preserved. The interim dataset retains technically validated order records together with original codes and descriptions, including orders that will later be excluded from analytical measures.

| **Condition**                                            | **Treatment**                                                                                                                                                                    |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Repeated, consistent header values across order items    | Represent the order once and retain its net amount once. Repetition is not an additional order.                                                                                  |
| Missing order identity or contradictory header values    | Investigate and document the affected records. Do not choose an arbitrary row. Only use fields and orders whose representation has been resolved reliably.                       |
| Missing or invalid customer identifier, date or currency | Retain the issue in the preparation record. Do not assign the order to an invented customer, month or currency; it cannot contribute to profiles requiring the unresolved field. |
| Missing customer-master or text-mapping match            | Retain an otherwise usable order. Record the missing assignment; enrichment failure alone is not an analytical exclusion.                                                        |
| Missing or invalid monetary value                        | Do not replace it with zero. If the order is otherwise eligible and assignable, retain it in the count population and mark affected monetary aggregates as unavailable.          |

Technical issues and their effects are recorded separately from business exclusions. Source rows, distinct orders and customers affected by each treatment are distinguished in the preparation report.

#### 8.2.2 Analytical inclusion and exclusion rules

The following specification retains non-cancelled sales orders as the primary analytical population. It is a documented working policy to validate against the ERP definitions before generating the primary profiles; it does not assert that uninspected source codes have already been verified.

| **Field or condition**                    | **Primary treatment**                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Observation date                          | Include orders within the documented observation window. Treat boundary months according to Section 8.1.                                                                                                                                                                                                                                     |
| `SALESORDERTYPE`                          | Use `OR` as the documented sales-order type. Other types enter the primary population only after their equivalence to the intended ordering activity has been verified and explicitly recorded.                                                                                                                                              |
| Rejection status `A` — nothing rejected   | Include where the other eligibility and technical requirements are satisfied.                                                                                                                                                                                                                                                                |
| Rejection status `C` — fully rejected     | Exclude from the primary analytical order population. Retain in the inventory and interim data where technically representable.                                                                                                                                                                                                              |
| Rejection status `B` — partially rejected | Inclusion requires verification that the retained header amount supports the intended interpretation of the non-rejected order value. Until resolved, keep these orders outside the primary profile population and report their extent. Any adopted treatment applies consistently to the population underlying counts, totals and averages. |
| Missing or unknown rejection status       | Do not interpret it as `A`. Resolve its business meaning or keep the order outside the primary eligible population with an explicit unresolved-status reason.                                                                                                                                                                                |
| Processing statuses `A`, `B`, `C`         | Open, in-progress and completed orders are not distinguished by an automatic validity filter. Incomplete processing alone is not an exclusion. Unrecognised statuses are flagged and reviewed for their effect on interpretation.                                                                                                            |
| `SDDOCUMENTREASON`                        | Retain as context. Apply a reason-based exclusion only where the verified mapping establishes a business process outside the defined analytical scope; document the exact codes and rationale.                                                                                                                                               |
| Large, zero or negative order values      | Do not apply a blanket magnitude or positivity filter. Investigate unusual values and document their meaning. A verified error or incompatible business process may justify correction or exclusion; magnitude alone does not.                                                                                                               |

The partially rejected-order rule is conditional on ERP clarification. No proportion of rejected items is inferred from header data, and no missing adjusted amount is reconstructed from unavailable item-level prices. An inclusion rule must be settled before primary profiles are generated and before final evaluation. Alternative, defensible treatments may be examined in a limited sensitivity analysis.

Eligibility defines a common order population for `ORDERCOUNT`, `TOTALORDERNETVALUE` and `AVGORDERNETVALUE`. An otherwise eligible order with a missing monetary amount remains counted; the total and average for the affected profile remain missing. This separates business eligibility from monetary assessability.

#### 8.2.3 Reporting selection effects

Report recorded orders, eligible orders and excluded or unresolved orders, with reasons and monthly distributions. Where appropriate, also report affected customers and monetary coverage within each currency. Overlapping reasons must not be summed as though they represented disjoint order sets.

Changes in exclusion rates, missingness or extraction coverage may create apparent behavioural differences. Investigate these effects before interpreting a customer event. Missing or excluded data do not establish that no ordering activity occurred.

### 8.3 Customer suitability

Customer suitability is assessed for the intended comparison using observation coverage, usable reference and subsequent periods, eligible ordering activity and the requirements of the selected measure. A calculable monthly profile is not automatically sufficient evidence for detecting a change.

**The following principles apply:**
- Do not impose a fixed minimum number of orders separately in every month or year.
- Do not require recent activity or a later purchase as a condition for retaining a customer; declining activity and ordering gaps are relevant outcomes.
- Do not exclude a customer solely because industry information is missing.
- Do not discard a customer solely because some monetary measures are unavailable if supported frequency comparisons remain possible.
- Do not require a customer to belong to an industry with an aggregate change before assessing the individual history.
- Determine evidence requirements using development cases and justify them before final evaluation. Record the resulting population and limitations.

Distinguish assessable comparisons with no detected change, comparisons with detected changes and comparisons with insufficient evidence. Low activity, short history or missing coverage must not be reported as proof of stable behaviour. The findings apply to the customer histories and comparisons that meet the stated evidence requirements.

### 8.4 Decisions to finalise during data assessment

The structural scope and three core measures are fixed by this plan. The following operational decisions require source evidence or method development:

| **Decision**                                                      | **Required basis and timing**                                                                                            |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Exact observation dates and incomplete-month handling             | Establish extraction coverage before constructing primary profiles.                                                      |
| Source code meanings and allowed document types                   | Verify the observed codes and any additional exclusions before applying the eligibility configuration.                   |
| Partially rejected orders and their stored amounts                | Clarify ERP amount semantics and adopt the conditional policy in Section 8.2.2 before generating primary profiles.       |
| Missing, conflicting or unusual values                            | Document reproducible treatments and their effects during preparation.                                                   |
| Relevant customer-currency combinations and observation intervals | Define how complete monthly histories are constructed without assuming activity or coverage from order occurrence alone. |
| Comparison windows, evidence requirements and thresholds          | Develop on reserved development evidence and fix before final evaluation.                                                |

Record each adopted rule with its rationale, configuration and effect on the data.

---

## 9 Analytical measures and feature definitions

The analytical basis uses the core measures below. Their definitions and column names match the [data description](docs/project/data_description.md). A stored measure need not act as an independent detection input; its role in detection, classification or description is specified during method development.

Monthly profiles are identified by `CUSTOMER_ID`, derived from `SOLDTOPARTY`, `PERIODSTART`, representing the first calendar day of the month, and `TRANSACTIONCURRENCY`. `INDUSTRY` and `INDUSTRY_TEXT` provide contextual group assignments.

### 9.1 Core measures

| **Measure**                 | **Derived column**   | **Definition**                                                                                                                           | **Analytical purpose**                                                                    |
| --------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Order count**             | `ORDERCOUNT`         | Number of distinct eligible `SALESORDER` values per customer, calendar month and currency.                                               | Describes ordering activity.                                                              |
| **Total net order value**   | `TOTALORDERNETVALUE` | Sum of `TOTALNETAMOUNT` retained once per eligible order in the same profile. Unavailable if an eligible contributing amount is missing. | Describes the recorded nominal net value of orders.                                       |
| **Average net order value** | `AVGORDERNETVALUE`   | `TOTALORDERNETVALUE / ORDERCOUNT`, where the total is available and the count is greater than zero.                                      | Helps distinguish frequency changes from changes in the average monetary value per order. |

These measures are mathematically dependent and do not constitute independent corroborating signals. Average net order value is not a measure of purchased physical quantity or unit price. Their inclusion does not predetermine taxonomy types.

### 9.2 Optional temporal descriptions

The order-level interim data may support additional descriptions without introducing product or price data. Examples are the days since the last eligible order at a defined reference date and the intervals between eligible orders. These are optional refinements, not additional required columns in the current monthly schema.

Temporal descriptions require a stated reference date, observation support and an explicit choice of whether ordering is considered within one currency or across currencies. A last-order calculation uses only orders on or before its reference date. If the preceding history is unavailable, recency remains unknown. Monthly profiles alone do not provide exact within-month order dates.

### 9.3 Calculation and interpretation rules

- Use the documented eligible order population consistently for counts, totals and averages. Preserve missing monetary information rather than silently reducing the population used for a total.
- Calculate monthly measures from the unique order-level representation, not by summing repeated header values in the raw item rows.
- Represent zero-order periods only within justified observation coverage. Set count and total to zero where inactivity is observed; leave the average undefined. Unknown coverage is not a zero.
- Keep EUR and GBP separate for monetary analysis. Combining currencies requires a documented conversion; no conversion is assumed in the primary schema. Counts may be combined across currencies only where each order is represented once.
- Construct overall, industry and longer-window summaries by summing counts and totals within the applicable currency and evidence scope. Recompute averages from those aggregates, rather than averaging monthly or customer averages without weighting.
- If any required contributing total is missing, the complete aggregate total and its average remain missing. Any partial sum is reported separately, labelled incomplete and accompanied by coverage information. Complete counts may still be reported.
- Retain customers with missing industry assignments and identify their contribution in grouped summaries. A current industry assignment is not assumed to be historically verified at each order date.
- Use comparable window lengths or appropriate rates where exposure differs. Report absolute changes and relative changes where meaningful; relative change from a zero or insufficiently supported baseline remains undefined or explicitly qualified.
- Account for individual large orders, calendar patterns, changes in currency use and selection effects when interpreting a candidate. Descriptions must distinguish measured differences from unsupported causes or persistence claims.

Final detection-input choices, comparison rules, type criteria and explanation templates are documented before final evaluation. The table schemas remain centrally maintained in the data description.

---

## Bibliography

See [docs/literature/bibliography.md](docs/literature/bibliography.md).
