<div align="center">

# Project plan for the Bachelor's Thesis

This project plan defines the objectives, scope and methodological approach for detecting, classifying and explainably describing changes in B2B customers’ purchasing behaviour using ERP sales order data. It outlines the data basis, candidate analytical measures, taxonomy development and evaluation strategy, distinguishing the core investigation from optional extensions.

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
    - [7.1 Purchasing behaviour and profitability](#71-purchasing-behaviour-and-profitability)
    - [7.2 Project orders and routine orders](#72-project-orders-and-routine-orders)
- [8 Observation period and order eligibility](#8-observation-period-and-order-eligibility)
    - [8.1 Observation period](#81-observation-period)
    - [8.2 Order eligibility](#82-order-eligibility)
    - [8.3 Customer suitability](#83-customer-suitability)
- [9 Analytical measures and feature definitions](#9-analytical-measures-and-feature-definitions)
    - [9.1 Core candidate measures](#91-core-candidate-measures)
    - [9.2 Additional candidate measures](#92-additional-candidate-measures)
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

This bachelor's thesis investigates which types of significant changes in customer purchasing behaviour can be automatically detected, classified and explainably described using ERP sales order data from a B2B wholesaler. The analysis covers a 24-month observation window and focuses on changes in individual customers' ordering activity, net order value and assortment. Significance is assessed through justified criteria concerning deviations from usual behaviour, change magnitude and sufficient evidence.

Eligible sales orders are transformed into customer profiles using a compact set of measures selected according to data quality and analytical suitability. Time-window-based profile comparisons provide the initial approach for identifying change candidates. A taxonomy is then developed through systematic examination of development cases, supported by conceptual and domain-informed reasoning. Documented rules enable automatic assignment of change events to the resulting types. Standardised descriptions and visualisations show what changed, by how much and which observations support the classification.

The intended contribution is an evaluated approach combining an interpretable taxonomy, reproducible automatic classification and descriptions traceable to the underlying data. Evaluation addresses detection performance, taxonomy suitability, assignment quality and description accuracy and completeness using controlled cases, held-out real customer histories and selected sensitivity analyses. The findings concern purchasing activity recorded with the focal company. They do not establish the causes of customer behaviour or capture purchases from other suppliers.

---

## 3 Research objectives and intended contributions

The thesis aims to develop and evaluate an approach for detecting, classifying and explainably describing significant changes in customer purchasing behaviour using ERP sales order data. Significance is understood according to the operational definition provided alongside the research question.

The intended contributions are an interpretable taxonomy of purchasing behaviour changes, the automatic assignment of detected changes to its types, and evidence-based descriptions that make the findings and their classification understandable.

### 3.1 Development and automatic assignment of change types

The thesis develops a taxonomy that describes what changes in a customer's observed purchasing behaviour. Its development combines the examination of change patterns in the available data with conceptual and domain-informed reasoning. The candidate analytical measures provide the observational basis. They do not predetermine the final change types.

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

The thesis prioritises a complete, manageable investigation covering data preparation, change detection, taxonomy development, automatic type assignment, explainable descriptions and evaluation. Optional extensions deepen this investigation but are not prerequisites for answering the research question.

The main emphasis is on the taxonomy, reproducible type assignment and understandable descriptions. Change detection provides the methodological basis. An extensive comparison of detection algorithms is not a primary objective.

### 4.1 Core scope

| **Component**                          | **Required scope**                                                                                                                                                                                                                |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data understanding and preparation** | Examine the agreed 24-month observation window, assess data quality and customer suitability, and construct a reproducible analytical dataset with documented inclusion rules and limitations.                                    |
| **Behavioural measures**               | Assess ordering activity, order value and assortment as initial dimensions. Select a compact set of suitable measures based on data quality and analytical usefulness. Not every catalogue measure must become a detection input. |
| **Change detection**                   | Select, justify and implement one main detection approach that operationalises the documented definition of significant purchasing behaviour changes.                                                                             |
| **Taxonomy development**               | Develop a compact taxonomy through the examination of observed patterns and conceptual and domain-informed reasoning. Document type definitions, distinctions and assignment criteria.                                            |
| **Automatic assignment**               | Assign detected events reproducibly, with explicit treatment of combined changes, ambiguous assignments and insufficient evidence. A rule-based approach is sufficient where appropriate.                                         |
| **Explainable descriptions**           | Produce standardised descriptions supported by numerical comparisons and suitable visualisations, covering the change, its classification and relevant limitations.                                                               |
| **Evaluation and discussion**          | Evaluate detection, taxonomy and assignment, and descriptions. Report successful cases, errors, sensitivity to selected analytical choices and limits to interpretation and generalisation.                                       |

The number of change types is not fixed in advance. It will reflect distinguishable and sufficiently supported patterns rather than a numerical target.

### 4.2 Evaluation as part of the core scope

Evaluation is required for the minimum complete investigation.

**It will combine:**
- controlled cases with known changes and suitable no-change cases to assess detection performance and false alarms.
- a manageable selection of real customer histories to examine type suitability, assignment plausibility and the accuracy of descriptions, including ambiguous and unsuccessful cases.
- a limited sensitivity analysis of consequential choices, such as selected thresholds or comparison periods.

Cases used for the final evaluation will be separated from those used to develop the taxonomy and tune the approach. Evaluation evidence will be interpreted according to what it can establish: performance on controlled cases does not, by itself, demonstrate usefulness on real customer histories.

Without a user study, the assessment of descriptions will focus on factual correctness and traceability to the underlying evidence. It will not claim demonstrated comprehensibility or usefulness for sales staff.

### 4.3 Optional extensions

| **Extension**                                         | **Condition for inclusion**                                                                                                                                                     |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Discount level as an additional dimension**         | Price assignment, quantity compatibility and data coverage support reliable calculation. Feasibility is examined during exploration. Full integration is optional.              |
| **An additional detection method**                    | Sufficient time remains for a meaningful comparison after completing the main approach and its evaluation. A simple reference approach may already support the core evaluation. |
| **More detailed assortment or quantity analyses**     | The core analysis leaves relevant questions unresolved and the data support valid comparisons.                                                                                  |
| **Subgroup analyses**                                 | Attributes such as industry or ordering activity provide meaningful groups with sufficient observations.                                                                        |
| **Expert feedback or additional explanation methods** | Access and time are available, or the selected approach benefits from further explanation.                                                                                      |

### 4.4 Implementation priorities and boundaries

Development proceeds from a complete initial analysis using a small set of suitable measures to optional refinements. Evaluation is included in this initial analysis rather than postponed until after extensions.

Reproducible notebooks, scripts and documented outputs constitute the required technical deliverables. A dashboard, production integration and real-time monitoring are outside the core scope. Churn prediction, causal explanations of customer behaviour and profitability analysis are outside the analytical scope.

---

## 5 Methodological approach

The thesis follows an exploratory development process followed by a separate evaluation. The approach connects data preparation, change detection, taxonomy development, automatic type assignment and explainable descriptions. Development may be iterative, while the final evaluation assesses the established approach using cases not employed to develop the taxonomy or tune its settings.

### 5.1 Main analytical steps

| **Step**                                         | **Approach**                                                                                                                                                                | **Main output**                                                                                                            |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **1. Understand and assess the data**            | Examine data quality, observation coverage, ordering activity and the feasibility of candidate measures.                                                                    | Justified selection of suitable customer histories and behavioural measures.                                               |
| **2. Prepare the analytical basis**              | Clean and link eligible orders, calculate selected measures and choose a temporal representation appropriate to the observed ordering activity.                             | Reproducible customer histories for subsequent analysis.                                                                   |
| **3. Detect and characterise change candidates** | Apply the selected detection approach and describe differences in terms of affected dimensions, direction, magnitude and temporal characteristics.                          | Structured change candidates supported by the underlying observations.                                                     |
| **4. Develop the taxonomy**                      | Systematically examine development cases and combine observed patterns with conceptual and domain-informed reasoning. Define distinguishable types and assignment criteria. | A documented taxonomy of purchasing behaviour changes.                                                                     |
| **5. Automate assignment and descriptions**      | Implement the assignment criteria and generate standardised descriptions from the measured changes and classification results.                                              | Automatically classified and explained change events, including explicit treatment of ambiguity and insufficient evidence. |
| **6. Evaluate and discuss the approach**         | Assess the established approach using controlled cases and held-out real customer histories, including error analysis and selected sensitivity checks.                      | Evidence concerning performance, limitations and the conclusions supported by the investigation.                           |

### 5.2 Initial detection approach

A time-window-based comparison of customer profiles serves as the initial methodological direction. Behaviour in a reference period is compared with behaviour in a subsequent period. Change candidates are assessed against justified criteria reflecting usual variability, change magnitude and sufficient evidence.

The temporal resolution, comparison windows and detection criteria will be selected during data exploration and methodological development. Time-window-based profile comparison is the planned main detection approach and provides the methodological basis for SQ1. If the available data require a different main approach, the reasons for this change will be documented and the method-specific wording of SQ1 will be aligned accordingly. The registered thesis title and main research question remain unchanged. An extensive comparison of detection methods is outside the core scope.

### 5.3 Taxonomy development and automatic classification

Taxonomy development is researcher-led and data-informed. It involves systematic examination of development cases rather than manual classification of every event in the final analysis. The inspected cases, identified patterns, conceptual considerations and reasons for defining or revising types will be documented.

Once the taxonomy is established, a rule-based algorithm will automatically apply its assignment criteria to detected events. The implementation will accommodate combined changes and explicitly identify cases that cannot be assigned unambiguously.

Clustering may support exploratory pattern identification if useful, but it is not required for the core approach. Automatically generated groups would still require interpretation and validation before being adopted as change types.

### 5.4 Explainable output and evaluation separation

Descriptions will be generated from calculated before-and-after differences, temporal information and the criteria supporting each type assignment. They will explain the observed change and its classification without claiming to establish its causes.

The separation between development and final evaluation cases will be planned early. Feature definitions, detection settings, taxonomy criteria and description rules will be fixed before the final evaluation. Subsequent sensitivity analyses will be reported separately from the primary evaluation results.

### 5.5 Relationship to the methodological framework

The accompanying methodological framework specifies the detailed workflow, including phase-specific tasks, decision criteria and expected outputs. It operationalises the approach outlined here within the agreed research objectives, scope and evaluation strategy.

---

## 6 Evaluation strategy

The evaluation assesses four components separately: change detection, the taxonomy, automatic type assignment and generated descriptions. Results are interpreted against the evidence available for each component rather than combined into a single overall score.

The evaluation design combines established metrics with project-specific assessment criteria. Metric selection and interpretation will be documented explicitly, reflecting the importance of matching evaluation measures to the intended assessment goals (Opitz, 2024).

### 6.1 Evaluation data and reference information

**The evaluation will use:**
- **Controlled cases:** Time series with known changes and suitable no-change controls, covering different change magnitudes, behavioural dimensions and combinations.
- **Held-out real cases:** Customer histories and change events not used to develop the taxonomy or tune the approach.
- **Selected sensitivity scenarios:** Variations of consequential analytical choices to examine the stability of the findings.

The controlled scenarios will be informed by observed data characteristics without being restricted to cases that directly reproduce the detection rules.

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

A limited sensitivity analysis will examine selected thresholds or comparison periods. The primary configuration will be fixed before final evaluation. Alternative settings will be reported separately rather than selected retrospectively to maximise the final scores.

No universal numerical success threshold is assumed. Any acceptance criteria will require justification before the final evaluation. Conclusions will distinguish demonstrated performance in the evaluated cases from claims that the available evidence cannot support.

Detailed sampling procedures, matching rules and review checklists will be specified in the [methodological framework](docs/framework/fuuckae_framework.md).

---

## 7 Data scope and limitations

This thesis analyses changes in customer purchasing behaviour using ERP sales order data from a B2B wholesaler (view the [data description](docs/project/data_description.md)). The analysis focuses on purchases recorded with the focal company. It does not capture customers' purchases from other suppliers or establish the causes of observed changes.

### 7.1 Purchasing behaviour and profitability

The analysis focuses on observable ordering patterns and their changes over time. Contribution margin and contribution margin ratios are outside the analytical scope. Accordingly, the thesis does not assess changes in customer profitability or define margin deterioration as a purchasing-change type.

This boundary keeps the investigation focused on purchasing behaviour and limits data acquisition and preparation to information required for the research objective. Changes in ordering patterns may have financial consequences, but these consequences are not evaluated.

### 7.2 Project orders and routine orders

The dataset includes both project-related orders and routine orders. Quotation identifiers and links between quotations and sales orders are not included in the analytical dataset. Consequently, the analysis does not systematically distinguish between these two forms of business. Obtaining and validating the additional ERP relationships required for this distinction would exceed the resources allocated to this thesis. The findings therefore describe changes in the combined ordering activity observed for each customer.

Large individual orders may substantially affect purchasing values and before-and-after comparisons. Their influence will be examined when interpreting relevant customer histories. Order value alone is not treated as sufficient evidence that an order belongs to project business, and large orders are not excluded solely because of their size.

**Detected changes must therefore be interpreted in context:** A difference associated with an individual project order does not necessarily indicate a sustained change in routine purchasing.

---

## 8 Observation period and order eligibility

### 8.1 Observation period

The analysis covers a 24-month observation window based on the sales order date (`SALESORDERDATE`). The exact start and end dates will be recorded during data preparation. Any incomplete calendar months will be identified and their treatment documented.

### 8.2 Order eligibility

Only valid, non-cancelled sales orders within the observation window are included. Eligibility is determined using the document type (`SALESORDERTYPE`), processing status (`OVERALLSDPROCESSSTATUS`), order reason (`SDDOCUMENTREASON`) and rejection status (`OVERALLSDDOCUMENTREJECTIONSTS`).

The accepted code values and their combinations will be specified before constructing the analytical profiles. Fully rejected orders are excluded. The treatment of partially rejected orders, including the interpretation of their recorded net amounts, requires clarification during data preparation. Open or in-progress orders are not considered invalid solely because processing is incomplete.

Order frequency is calculated by counting distinct eligible sales orders. Total net order value is calculated using `TOTALNETAMOUNT` once per eligible order, avoiding duplication across order-item rows. Monetary values in different currencies must not be summed without a documented conversion or restriction.

### 8.3 Customer suitability

Customer suitability is assessed using the available observation coverage, eligible order counts, ordering intervals and the evidence required for the intended comparisons.

An activity level of approximately two to four orders per customer per year serves as an initial orientation for exploration, not as a fixed inclusion threshold or evidence of sufficient information. Final eligibility criteria will be justified using the observed data and the requirements of the selected analysis.

A minimum order count is not imposed separately on each year, since this could exclude customers whose declining activity is relevant to the research question. Low activity and insufficient evidence will be distinguished from an absence of purchasing changes.

---

## 9 Analytical measures and feature definitions

The following measures are candidates for describing customer purchasing behaviour and its changes over time. Their final selection depends on data availability, quality, ordering activity and suitability for the analysis. Including a measure in this catalogue does not predetermine a purchasing-change type or require its use in automatic detection.

Measures are calculated for each customer and observation period unless stated otherwise. The temporal aggregation will be selected after examining customer histories.

### 9.1 Core candidate measures

| **Measure**                 | **Derived column**          | **Definition and source fields**                                                                                                      | **Analytical purpose**                                                              |
| --------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Order count**             | `ORDERCOUNT`                | Number of distinct eligible `SALESORDER` values per customer and period, assigned using `SOLDTOPARTY` and `SALESORDERDATE`.           | Describes changes in ordering frequency.                                            |
| **Total net order value**   | `TOTALORDERVALUE`           | Sum of `TOTALNETAMOUNT` across eligible orders, counting each order-level amount once.                                                | Describes changes in the monetary value of recorded orders.                         |
| **Average net order value** | `AVGORDERVALUE`             | `TOTALORDERVALUE / ORDERCOUNT`. Undefined when no eligible orders are recorded.                                                       | Helps distinguish changes in ordering frequency from changes in average order size. |
| **Product breadth**         | `DISTINCTPRODUCTCOUNT`      | Number of distinct `MATERIAL` values in eligible order items during the period.                                                       | Describes the variety of products ordered.                                          |
| **Product-group breadth**   | `DISTINCTPRODUCTGROUPCOUNT` | Number of distinct `PRODUCTGROUP` values associated with eligible order items, joining `MATERIAL` to `PRODUCT` in the product master. | Describes purchasing breadth at product-group level.                                |

Order values represent recorded net order amounts and are not automatically interpreted as invoiced or realised revenue. Average order value is mathematically related to total order value and order count. These measures must not be treated as independent evidence of change.

### 9.2 Additional candidate measures

| **Measure**                      | **Derived column**       | **Definition and source fields**                                                                                                                              | **Analytical purpose and requirements**                                                                                                                     |
| -------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Order share by product group** | `PRODUCTGROUPORDERSHARE` | Number of distinct eligible orders containing a specified product group, divided by `ORDERCOUNT`.                                                             | Describes how frequently each group occurs in a customer's orders. Requires reliable product-group assignments.                                             |
| **Weighted discount percentage** | `WEIGHTEDDISCOUNTPCT`    | Sum of derived discount amounts divided by the corresponding total list-price value, multiplied by 100. Both sums use the same set of assessable order items. | Describes the granted discount level. Requires valid price conditions, compatible price units and quantities, and an unambiguous assignment to order items. |
| **Days since last order**        | `DAYSSINCELASTORDER`     | Number of days between a defined reference date, such as period end, and the latest eligible `SALESORDERDATE` on or before that date.                         | Describes ordering gaps. Unknown when no preceding order is observable in the available history.                                                            |

Product-group order shares are stored separately by customer, period and product group. An order may contain several groups, so their shares may sum to more than one. These shares describe order incidence, not a revenue-weighted composition.

Discount calculations use the applicable `CONDITIONTYPE` and `CONDITIONRATEVALUE`, respecting validity dates and relevant customer or customer-price-group conditions. Quantity weighting requires verification of the meaning and compatibility of `CONFDDELIVQTYINORDERQTYUNIT`. Missing or unmaintained prices are not interpreted as zero discounts. The proportion of eligible order items with calculable discounts is reported alongside the aggregate. Discount levels do not establish customer dependence on discounts.

### 9.3 Calculation and interpretation rules

- Apply the documented order-eligibility rules consistently across measures. Preserve the distinction between order-level and item-level data.
- Use `CUSTOMERID`, derived from `SOLDTOPARTY`, and `PERIODSTART` as identifiers in the customer-period table.
- Distinguish observed inactivity from missing coverage. Zero counts and totals are appropriate only where coverage supports that interpretation.
- Leave averages and shares undefined when their denominators are zero. Record missing product classifications and their effect on assortment measures.
- Combine monetary values only within a consistent currency basis.
- Do not aggregate quantities across incompatible units such as metres, pieces, rolls and bundles.
- Consider relationships between measures during selection: for example, fewer orders may also reduce observed product breadth.

Final feature selection, calculation decisions and any distinction between detection inputs and descriptive measures will be documented before the final evaluation.

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
