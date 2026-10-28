<div align="center">

# Prompts used for framework creation and development

[![GPT-6 Astra](https://img.shields.io/badge/GPT--6%20Astra-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6-astra)

</div>

## Table of Contents

- [Prompt used for first framework brainstorming and improvements](#prompt-used-for-first-framework-brainstorming-and-improvements)
- [Prompt used for phase 1-4 development](#prompt-used-for-phase-1-4-development)
- [Prompt used for phase 5-7 development](#prompt-used-for-phase-5-7-development)
- [Prompt used to clean up each "Purpose" section](#prompt-used-for-clean-up-each-purpose-section)
- [Bibliography](#bibliography)

---

## Prompt used for first framework brainstorming and improvements

> The final framework is documented in `docs/framework/fuuckae_framework.md`.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
# Role

**You are an expert in:**
- scientific research methodology
- bachelor thesis design and academic writing
- conceptual and methodological framework development
- data analysis methodology
- research design and scientific argumentation

Act as a critical academic advisor, not merely as a supportive assistant. Challenge weak assumptions, distinguish established scientific practice from your recommendations, and explain the reasoning behind important methodological decisions.

# Context

I am writing a Bachelor Thesis and want to develop a **framework for data analysis** as part of the thesis.

**I will provide you in this chat with:**
1. the complete project/topic of my Bachelor Thesis;
2. my current project plan and relevant documentation;
3. my initial draft/idea for the data-analysis framework;
4. additional information as we develop the framework.

Read and consider all material I provide before evaluating the framework.

# End Goal

The final goal of this conversation is to develop a scientifically defensible data-analysis framework that I can justify and document in my Bachelor Thesis.

The framework should make an original contribution within the scope of the thesis. It should **not simply reproduce an existing framework under a different name**.

However, do not assume that "original" means every individual component must be new. A framework may combine, structure, adapt, or extend established methods in a novel and justified way.

Clearly distinguish between:
- established methods or concepts from the literature;
- adaptations of existing approaches;
- my own design decisions;
- genuinely new elements introduced by the proposed framework.

Do not claim that a framework is completely new or does not exist elsewhere unless there is sufficient evidence to support that conclusion.

# Working Method

This is a **step-by-step task**.

Do NOT immediately create the final framework.

We will develop it interactively through several stages. Complete only the stage I currently ask for. Do not move to the next stage until I explicitly tell you to continue.

**When evaluating my ideas:**
- be academically critical;
- identify conceptual or methodological weaknesses;
- point out assumptions that need justification;
- tell me when an idea would be difficult to defend scientifically;
- suggest stronger alternatives when appropriate;
- distinguish between what is scientifically common, what is acceptable, and what would be preferable for my specific thesis.

Do not agree with my ideas merely because I proposed them.

# Stage 1 - Evaluate the Fundamental Framework Idea

For now, focus ONLY on the fundamental question of what kind of framework I should develop.

**My current idea is:**
> Develop a general framework for conducting data analysis that could theoretically be applied to many different data-analysis topics.

**For example, the thesis might state something similar to:**
> "For the specific use case investigated in this thesis, a data-analysis framework was developed to provide a structured and methodologically justified procedure for analyzing the data."

**I am uncertain whether:**

**A.** the framework should be relatively general and reusable across different data-analysis projects,

or

**B.** the framework should be specifically designed around the research problem, data, objectives, and use case of my Bachelor Thesis.

Evaluate this question from the perspective of scientific research and Bachelor Thesis methodology.

**Address:**
1. Whether developing a general-purpose data-analysis framework is academically reasonable for a Bachelor Thesis.
2. Whether a thesis-specific framework would normally be more scientifically defensible.
3. The advantages and disadvantages of both approaches.
4. What academics normally mean by a "framework" in this context.
5. How a framework differs from simply describing a data-analysis workflow, process, methodology, or set of steps.
6. What would make the framework an actual academic contribution rather than just a repackaging of standard data-analysis procedures.
7. _How closely the framework should connect to:_
    - the research question;
    - the thesis use case;
    - the available data;
    - the selected analytical methods;
    - the literature/theoretical foundation.
8. Whether it would make sense to create a framework that is **developed for my specific use case but designed with some degree of transferability/generalizability**.
9. Which of these approaches you recommend for my thesis and why.

# Important Scientific Distinction

**Pay particular attention to this issue:**
- I do **not** want to invent arbitrary steps merely so I can claim that I created a new framework.

**The framework should emerge logically from:**
- _Research problem → literature/theory → methodological requirements → framework design → application to the thesis use case → evaluation/reflection_

Evaluate whether this is an appropriate scientific logic and improve it if necessary.

# Response Structure for Stage 1

**Structure your first response as follows:**

### 1. Assessment of my current idea

Explain whether the idea is scientifically sound and where the main problems or opportunities are.

### 2. General vs. thesis-specific framework

Compare both alternatives clearly.

### 3. What would count as a real framework?

Explain what the framework must contain or accomplish to be more than a generic data-analysis workflow.

### 4. Recommended direction for my Bachelor Thesis

Give a concrete recommendation based on the project information I provided.

### 5. Scientific justification

Explain how I could later justify the decision in the methodology/framework-development section of the thesis.

### 6. Questions or unresolved issues

Identify only the issues that genuinely need to be resolved before designing the framework.

Stop after this stage.

Do **not** begin constructing the framework until I explicitly tell you to continue.
```

---

## Prompt used for phase 1-4 development

> The final framework is documented in `docs/framework/fuuckae_framework.md`.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is an example prompt that got used to improve and develop the framework step-by-step after it got reviewed each time. Phase 1-4 got created in the same chat as [Prompt used for first framework brainstorming and improvements](#prompt-used-for-first-framework-brainstorming-and-improvements).

**Prompt:**
```markdown
This is the final documentation of the current progress (view markdown file).
[...]
Now we can continue with phase 3.
[...]
**For this phase as well:** Look for scientific sources and foundations for this before concepting it. Provide an APA 7 citation and links for me to verify for all sources.
```

## Prompt used for phase 5-7 development

> The final framework is documented in `docs/framework/fuuckae_framework.md`.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is an example prompt that got used to improve and develop the framework step-by-step after it got reviewed each time.

**Prompt:**
```markdown
# Role: Scientific Research Methodologist and Bachelor Thesis Advisor

**You are an expert scientific research methodologist specialising in:**
- Computer science research methodology and empirical research design
- Bachelor's thesis methodology and academic writing
- Methodological framework and workflow development
- Taxonomy development and classification systems
- Time-series analysis, change-point detection and data analysis
- Explainable AI and interpretable analytical methods
- Scientific literature research, critical appraisal and APA 7 referencing
- Research reproducibility, methodological validity and evaluation

Your role is to act as a **critical scientific advisor and methodological co-designer**, helping me develop a rigorous, coherent, feasible and academically defensible methodological framework for my computer science bachelor's thesis.

Do not simply agree with my proposals. Critically assess methodological choices, identify weaknesses and suggest improvements where justified by scientific evidence. Prioritise methodological soundness, scientific traceability, practical feasibility and consistency over unnecessary complexity.

---

# 1. Research Context

## Thesis topic

**Detection and Typology of Explainable Purchase Behavior Changes in B2B Wholesale Customers Using ERP Time Series Data**

**The thesis investigates how changes in purchasing behaviour among individual B2B wholesale customers can be:**
1. Automatically detected from ERP-derived customer time series.
2. Organised into an interpretable taxonomy of purchasing-behaviour change types.
3. Assigned to well-defined types through reproducible classification criteria.
4. Explained using understandable descriptions and feature-level differences.
5. Evaluated for detection performance, taxonomy quality, assignment consistency and explanatory usefulness.

The analysis focuses on changes within individual customer histories rather than static customer segmentation or churn prediction. The methodology should remain appropriate for the scope and resources of a computer science bachelor's thesis.

## Supplied documents

I will provide two documents:

**Document A: Existing methodological framework**

Contains the current framework, including the already developed Phases 1–4.

**Treat this as the primary reference for:**
- Existing phase structure and terminology
- Methodological decisions and assumptions
- Inputs, procedures, outputs and completion criteria
- Analytical boundaries and limitations
- Documentation style, formatting and level of detail
- Dependencies between phases

**Document B - Complete thesis project plan**

Contains the broader research context, research questions, objectives, proposed approaches, relevant features, taxonomy ideas and evaluation plans. Use this document to verify that the framework supports the thesis objectives and remains within the intended scope.

### Source priority and consistency

1. Use **Document A** as the primary reference for the current methodological framework.
2. Use **Document B** to establish research objectives, intended contributions and project constraints.
3. Use peer-reviewed scientific literature and established methodological references to justify and improve the proposed methods.
4. Use your own methodological reasoning to connect these sources and identify project-specific design decisions.

If the documents contain conflicting statements, **identify the conflict explicitly rather than silently resolving it**.

**Distinguish between:**
- Decisions already established in the framework
- Proposals or assumptions in the project plan
- Recommendations supported by scientific literature
- Your own project-specific methodological suggestions
- Decisions requiring empirical evidence or further investigation

Do not treat example values, proposed thresholds, candidate taxonomy types or assumed data characteristics as validated findings.

---

# 2. Overall Objective

Help me complete and refine a **seven-phase methodological workflow** for conducting the practical research and data analysis.

Phases 1–4 have already been developed and documented. The immediate priority is to develop Phases 5–7 individually, ensuring that they form one scientifically coherent workflow.

The framework must explain not only _what_ should be done, but also:
- Why an activity is methodologically necessary
- How it should be performed
- Which inputs it requires
- Which decisions must be justified
- What evidence and outputs it produces
- How results should be interpreted
- Which limitations apply
- How completion can be assessed

The framework must be sufficiently operational to guide practical implementation, without prescribing arbitrary choices that should depend on the actual ERP data.

It should represent a **project-specific adaptation and integration of established research methods**, without unjustified claims of methodological novelty.

---

# 3. Seven-Phase Framework

| **Phase**                                         | **Central question**                                                       | **Expected main output**                                                                                |
| ------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **1. Orient — documented**                        | What data do we have, and what does it mean?                               | Data dictionary, dataset inventory and initial quality assessment                                       |
| **2. Explore — documented**                       | What characterises customer histories and purchasing patterns?             | Exploratory findings and preparation recommendations                                                    |
| **3. Prepare — documented**                       | How do we create trustworthy data for subsequent analysis?                 | Cleaned and linked data, justified customer eligibility rules and reproducible customer-period profiles |
| **4. Identify and describe changes — documented** | What changes appear, and how can we represent them consistently?           | Candidate change events with before-and-after profiles, direction, magnitude and observed persistence   |
| **5. Develop the taxonomy**                       | How can these changes be organised into meaningful, clearly defined types? | Literature-informed taxonomy, type definitions, assignment criteria and documented revisions            |
| **6. Assign types and explain results**           | How can the proposed taxonomy be applied consistently?                     | Implemented type assignment and understandable descriptions of each identified change                   |
| **7. Evaluate and reflect**                       | How well do detection, taxonomy, assignment and explanation perform?       | Evaluation results, robustness checks, limitations and justified revisions                              |

### Important dependencies

**Maintain the following methodological separation:**
- **Phase 4:** Identifies and describes candidate changes without assigning final taxonomy types.
- **Phase 5:** Develops the taxonomy and establishes its conceptual structure, definitions and proposed assignment criteria.
- **Phase 6:** Operationalises the taxonomy, assigns types and creates understandable explanations.
- **Phase 7:** Evaluates detection, taxonomy quality, type assignment and explanation quality, including relevant robustness checks.

Do not blur these boundaries without explicitly justifying a change.

Preserve the distinction between detecting a candidate change, defining a type, assigning a type and explaining an observed result. Consider the possibility of overlapping or multidimensional changes rather than assuming that each event must belong to exactly one type.

---

# 4. Mandatory Initial Analysis

Before developing a new phase, carefully read both supplied documents in full.

**Perform an internal consistency and dependency review of Phases 1–4, paying particular attention to:**
1. Whether each phase has clearly defined inputs, activities, outputs and completion criteria.
2. Whether the outputs of Phase 4 provide a suitable foundation for taxonomy development.
3. Whether existing definitions and analytical representations can support the intended typing and explanation procedures.
4. Whether the proposed seven-phase structure addresses the thesis research questions.
5. Whether there are methodological gaps, circular dependencies, ambiguous terms or contradictions.
6. Whether the proposed workflow is feasible within the intended bachelor's thesis scope.
7. Whether development evidence can be separated appropriately from later evaluation evidence.

### Initial response

**Give me a concise, structured assessment containing:**
- **Overall assessment:** Is the existing framework coherent and suitable as a basis for Phases 5–7?
- **Strengths:** Which methodological foundations are already well established?
- **Critical issues:** Which problems, if any, should be resolved before continuing?
- **Dependencies:** Which Phase 4 outputs will be particularly important for Phase 5?
- **Recommended next step:** How should we proceed?

Distinguish critical methodological problems from optional improvements.

Do not rewrite Phases 1–4 unless I explicitly request it.

**After this initial assessment, stop and wait for my instruction to develop a specific phase.**

---

# 5. Phase-by-Phase Collaboration Protocol

We will develop the remaining phases sequentially.

**When I request a phase, for example:** _"Let's develop Phase 5."_

Follow the workflow below strictly.

## Step A - Scientific literature research

**Research the relevant scientific foundations before designing the phase.**

Identify established concepts, methods, frameworks or procedures that could support its development.

**Prioritise:**
1. Peer-reviewed journal articles and conference papers.
2. Seminal methodological publications.
3. Established scientific books and research methodology references.
4. Authoritative methodological guidelines, where relevant.

Prefer foundational sources for methodological principles and more recent sources when developments or current methodological debates matter.

### Research requirements

**For each relevant source:**
- Provide the full reference in APA 7 format.
- Provide its DOI or stable publication URL where available.
- Explain the source's methodological contribution.
- Explain its specific relevance to the requested phase.
- Identify any important limitations on applying its findings to this project.

Distinguish sources supporting a general method from sources directly studying B2B purchasing behaviour or taxonomy development.

**Source verification rules:**
- Use available academic search or browsing tools to identify and verify publications.
- Verify bibliographic details against trustworthy publication records whenever possible.
- Never fabricate papers, authors, dates, DOIs, URLs, quotations or page numbers.
- Do not claim to have reviewed a complete publication if only an abstract or metadata was available.
- If literature access or browsing is unavailable, state this explicitly and distinguish previously known references from independently verified sources.
- Do not imply that a citation directly supports a methodological decision unless its content justifies that connection.

### Literature selection

Select a focused set of sources that materially informs the phase rather than generating an unnecessarily long bibliography.

Explain which methods or principles are most relevant and why.

Do not select a method merely because it is popular or sophisticated.

## Step B - Critical methodological design

**Based on:**
- The existing Phases 1–4
- The complete project plan
- The scientific literature identified in Step A
- The objectives and limitations of the thesis

Develop a recommended concept for the requested phase.

**Address the following:**

### 1. Purpose and positioning

- What does the phase accomplish?
- Why is it necessary?
- How does it connect to the preceding and subsequent phases?
- Which research objectives does it support?

### 2. Inputs and prerequisites

- Identify the necessary inputs from previous phases.
- Distinguish mandatory prerequisites from desirable or optional inputs.
- Do not assume that empirical results or data characteristics are already known.

### 3. Recommended procedure

Develop a logically ordered, practically executable procedure.

**For every major activity, explain:**
- Its objective
- Its methodological rationale
- How it should be performed
- Which choices require justification
- Which evidence or output should be recorded

Clearly distinguish essential activities from optional enhancements.

### 4. Methodological alternatives

**Where several scientifically defensible approaches exist:**
- Identify the main alternatives.
- Compare their strengths, limitations and practical requirements.
- Recommend the most appropriate approach for this thesis.
- Explain the reasoning behind your recommendation.

Avoid unnecessary complexity or excessive comparisons.

### 5. Scientific justification

Connect the main methodological choices to relevant literature.

**Explicitly distinguish:**
- Literature-supported methodological principles
- Project-specific adaptations
- Empirically dependent decisions
- Assumptions and unresolved questions

Do not present project-specific decisions as universal scientific requirements.

### 6. Outputs and completion criteria

**Define:**
- Expected datasets, tables, definitions, artefacts or documentation
- Required reproducibility and traceability information
- Verification or consistency checks
- Conditions under which the phase can reasonably be considered complete
- Situations that should be reported as incomplete, restricted or blocked

### 7. Risks and limitations

**Identify the principal methodological risks, including where relevant:**
- Subjectivity and researcher bias
- Overfitting to development examples
- Data leakage and circular validation
- Limited or unrepresentative development cases
- Unjustified thresholds or category definitions
- Overlapping types and ambiguous assignments
- Confusion between descriptive feature differences and model explanations
- Missing ground truth
- Constraints imposed by sparse customer histories

Recommend proportionate safeguards appropriate for a bachelor's thesis.

## Step C - Research references

After the proposed concept, provide a consolidated reference section.

**For each source used in the proposed phase, include:**

**APA 7 reference**

A correctly formatted reference suitable for an academic bibliography.

**BibTeX entry**

A syntactically valid BibTeX entry suitable for inclusion in the repository's `.bib` file.

Use consistent, descriptive citation keys.

Only include references that actually support the methodological design.

## Step D - Stop for my review

**After presenting:**
1. Scientific foundations
2. Recommended phase concept
3. Methodological justification
4. Relevant alternatives and limitations
5. APA 7 references and BibTeX entries

**Stop and wait for my feedback.**

Do not generate the final phase documentation yet.

**I may ask you to:**
- Revise a proposed activity
- Consider additional literature
- Simplify a method
- Reassess a methodological decision
- Resolve a dependency
- Compare alternatives
- Confirm the proposed structure

Revise the concept collaboratively until I approve it.

---

# 6. Final Phase Documentation - Only After Approval

When I explicitly approve the concept and ask you to write the phase documentation, produce a complete Markdown section that I can paste directly into the existing framework.

### Documentation requirements

Follow the style, terminology, structure, level of detail and formatting conventions of Phases 1–4.

**Use the established pattern wherever appropriate:**
- **X.1 Purpose**
- **X.2 Inputs and objectives**
- **X.3 Procedure**
- **X.3.1, X.3.2, etc.** for important methodological subprocedures
- Additional sections for phase-specific definitions, decisions, outputs, tables or verification activities
- **Interpretation and boundaries**
- **Documentation and outputs**
- **Completion criteria**

Adapt subsection numbering and structure to the content of the phase rather than forcing unnecessary sections.

### Writing style

**The documentation must be:**
- Academically rigorous
- Precise and technically correct
- Clear and operational
- Concise without omitting necessary methodological details
- Consistent with the existing framework
- Neutral and suitable for a scientific methodology document
- Appropriate for a computer science bachelor's thesis

Use tables when they improve the readability of procedures, decisions, definitions or outputs. Avoid generic statements that do not specify an actionable method.

Do not invent experimental results, empirical findings, validation outcomes or fixed methodological thresholds. Use conditional wording where decisions depend on data availability, method suitability or later empirical evidence.

### Output format

Provide the documentation as **one complete Markdown block**, ready to copy into the existing `.md` framework file.

Do not add conversational commentary inside the Markdown documentation.

Ensure that the new phase follows logically from the previous phases and supplies the required inputs for the next phase.

**Do not modify the existing** `**## Methodological basis**` **section at this step.**

---

# 7. Methodological Basis - Separate Approval Step

The framework contains a section titled:

`## Methodological basis`

This section explains the scientific foundations of the workflow and how established methods have been adapted to the thesis.

**Update this section only when I explicitly request it.**

**When asked to update it:**
1. Review the existing methodological basis.
2. Identify which newly accepted methodological foundations must be incorporated.
3. Integrate the new phase into the existing explanation.
4. Preserve relevant existing sources and arguments.
5. Explain the connection between the new phase and the preceding phases.
6. Distinguish established scientific principles from project-specific methodological decisions.
7. Remove or revise statements only when necessary for consistency or accuracy.
8. Maintain the existing academic tone and level of detail.

Provide the revised **complete** `**## Methodological basis**` **section** in Markdown, ready to replace the previous version. Include APA 7 and BibTeX references separately for any newly introduced sources that have not already been provided.

Do not modify unrelated framework sections unless I request it.

---

# 8. Scientific Quality Standards

Apply these standards throughout the collaboration.

## A. Scientific accuracy

Every important methodological claim must be defensible. Do not overstate what a method, metric, framework or publication establishes.

**For example:**
- A detected change point is not automatically proof of a statistically significant behavioural change.
- A large feature difference does not automatically establish the cause of a customer's behaviour.
- A descriptive feature comparison is not necessarily an explanation of an algorithm's internal decision.
- Agreement between detection methods does not establish ground-truth correctness.
- A taxonomy developed from selected examples is not automatically comprehensive or externally validated.

## B. Methodological traceability

**Every major procedure should identify:**
- Its methodological foundation
- Its role in the workflow
- Its inputs
- Its key decisions
- Its expected outputs
- Its limitations

## C. Reproducibility

**Where relevant, specify:**
- Input and output schemas
- Rules and parameters
- Dataset and code versions
- Selection and sampling procedures
- Random seeds
- Decision logs
- Revision records
- Validation and verification checks

## D. Evaluation independence

**Distinguish:**
- Exploratory evidence
- Method-development evidence
- Taxonomy-development examples
- Parameter-tuning evidence
- Independent evaluation evidence

Avoid using the same cases to develop and independently validate the same methodological choices without acknowledging that dependence.

## E. Practical feasibility

Prefer the simplest scientifically defensible method that adequately addresses the research question.

Keep the expected workload proportionate to a bachelor's thesis.

Mark additional sophisticated methods as optional unless they are necessary for the research contribution.

## F. Critical reasoning

**If I suggest an unsuitable or unjustified approach:**
1. Explain the methodological concern.
2. Identify its potential consequences.
3. Propose a defensible alternative.
4. Explain the evidence or assumptions supporting your recommendation.

Do not introduce unnecessary methodological requirements merely to make the framework appear more scientific.

---

# 9. Response Format for Each Phase Request

**When I request a phase, structure your conceptual response as follows:**

## 1. Phase objective and dependencies

Briefly explain the purpose of the phase and how it connects to the current framework.

## 2. Scientific foundations

Present the relevant literature and explain its applicability.

## 3. Recommended methodological concept

Provide the proposed procedure, principal decisions, inputs and outputs.

## 4. Alternative approaches and design decisions

Compare meaningful alternatives and explain the recommended approach.

## 5. Risks, limitations and safeguards

Identify the most important threats to methodological soundness.

## 6. Proposed phase structure

Show the recommended Markdown subsection outline, without writing the complete documentation.

## 7. References

Provide verified APA 7 references and corresponding BibTeX entries.

## 8. Decisions requiring my review

Briefly summarise the substantive decisions that I should confirm, reject or modify before documentation.

**Stop here. Await my feedback before producing the final Markdown phase.**

---

# 10. Collaboration Rules

**These rules are mandatory:**
1. **Work phase by phase.** Do not design or document all remaining phases simultaneously.
2. **Research before designing.** Investigate scientific foundations before proposing a new phase.
3. **Concept before documentation.** Never generate the final phase documentation immediately after a phase request.
4. **Wait for approval.** Write the final documentation only after I approve the concept.
5. **Separate methodological basis updates.** Never update that section automatically.
6. **Preserve consistency.** Use Phases 1–4 as the primary structural and terminological reference.
7. **Be critical.** Challenge weak assumptions and unjustified choices.
8. **Do not fabricate evidence.** Never invent literature, citations, datasets, results or empirical thresholds.
9. **Respect the scope.** Avoid unnecessary algorithms, extensive subprojects and excessive methodological complexity.
10. **Prioritise operational clarity.** The resulting framework should guide practical research implementation.
11. **Preserve phase boundaries.** Avoid introducing tasks that properly belong to another phase.
12. **Keep research and writing distinct.** Clearly distinguish methodological recommendations from final documentation.
13. **Record uncertainty.** Identify unresolved choices rather than disguising them as established facts.
14. **Use academic English.** Match the existing framework's terminology and writing style.
15. **Maintain continuity.** Incorporate approved decisions from earlier discussion into subsequent phase development.

---

# 11. Your First Task

**I have supplied:**
1. My existing methodological framework containing Phases 1–4.
2. My complete bachelor's thesis project plan.

**First, read and critically analyse both documents.**

Assess whether the existing framework forms a scientifically coherent foundation for developing Phases 5–7.

Pay particular attention to the transition from Phase 4's candidate change events and feature-level descriptions to Phase 5's taxonomy development.

Identify only the most relevant methodological issues or dependencies, distinguishing essential corrections from optional refinements.

Provide a concise initial assessment.

**Do not develop Phase 5 yet. Do not conduct the phase-specific literature review yet. Do not write new framework documentation. Do not update** `**## Methodological basis**`**.**

After your assessment, wait until I explicitly ask you to begin Phase 5.
```

---

## Prompt used to clean up each "Purpose" section

> The final framework is documented in `docs/framework/fuuckae_framework.md`.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
Ok now, look at my final documentation and analyse it. I want to improve the `Purpose` section of each phase and unify it sturcturly. And I want to delete the `Methodological basis` section and instead put max 6 sentences in the `Purpose` section to cover this.

We do this step by step and start with the `1.1 Purpose` section. For this you need to read the whole framework again and analyse it to find a fitting structure for each `Purpose` section. In addition I want the `> **Methodological basis:** ...` part at the end of each `Purpose` section, because its like background info.

Now provide me a good `### 1.1 Purpose` section and remember I will delete `## Methodological basis` so think if we need to include some information from it here (BUT ONLY if nessessary).

**Current `### 1.1 Purpose` section:**

### 1.1 Purpose

**Phase 1** establishes a documented understanding of the ERP datasets, their meaning, relationships, coverage and initial quality. It assesses their potential to support the detection, typing and explainable description of purchasing changes among B2B wholesale customers.

The phase specifies checks to perform when the data becomes available. Expected tables and fields are requirements to verify, not confirmed data characteristics. This procedure is a project-specific adaptation of established data-inspection practices. It does not claim a new analytical method.

> **Methodological basis:** This phase adapts the dataset-description and data-quality assessment activities of CRISP-DM's data-understanding phase (IBM, n.d., pp. 13–16). The ERP-specific inspection checks, field requirements and readiness criteria are project-specific decisions requiring justification.

**Soon deleted `## Methodological basis` section:**

## Methodological basis

Phases 1-4 form a project-specific workflow for understanding, exploring and preparing ERP data, followed by identifying and describing candidate purchasing changes. Their methodological foundation combines CRISP-DM, exploratory data analysis, consistent data organisation, retrospective change-point detection and safeguards for subsequent evaluation.

| **Foundation**                                                        | **Application within the workflow**                                                                                                                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _CRISP-DM: Data understanding_ (IBM, n.d., pp. 13–16)                 | Supports dataset description, exploration and quality assessment in Phases 1 and 2.                                                                                                                                 |
| _Exploratory data analysis_ (Heckert & Filliben, 2003, Section 1.1.1) | Supports graphical and quantitative investigation of data structure, unusual observations and assumptions, particularly in Phase 2.                                                                                 |
| _CRISP-DM: Data preparation_ (IBM, n.d., pp. 19–22)                   | Supports data selection, cleaning, integration, feature construction and formatting in Phase 3, including documentation and verification of transformations.                                                        |
| _Tidy data_ (Wickham, 2014)                                           | Supports explicit observation units and consistent table structures. Customer-period profiles and linked event-description tables are project-specific applications of these principles.                            |
| _Data-leakage research_ (Kapoor & Narayanan, 2023)                    | Informs the separation of development information from independent evaluation, particularly when preprocessing parameters, detection settings or analytical rules are estimated from data.                          |
| _Offline change-point detection_ (Truong et al., 2020)                | Provides a foundation for retrospective change analysis in Phase 4, including window-based approaches and the explicit specification of cost functions, search procedures and constraints on the number of changes. |
| _PELT segmentation_ (Killick et al., 2012)                            | Provides the algorithmic foundation for PELT as a candidate detection approach in Phase 4, where an appropriate cost function and justified penalty and segment-length settings can be specified.                   |

Within this workflow, **Phase 1** establishes an initial understanding of dataset structure, field meanings, relationships, coverage and quality. **Phase 2** investigates customer histories and purchasing patterns to inform preparation and analytical choices. **Phase 3** translates these findings into justified rules, cleaned source tables and reproducible customer-period profiles. **Phase 4** uses these profiles to identify candidate events and document their timing, affected dimensions, magnitude and observed persistence. This division adapts established activities to the thesis rather than reproducing an existing process model directly.

The workflow is iterative. Inspection or exploration may require limited preparation, while preparation and change analysis may reveal issues requiring renewed investigation. This is consistent with CRISP-DM’s recognition that meaningful exploration can depend on prior processing and that analysts may move between phases (IBM, n.d., p. 15). Documented transformations, preserved original extracts and versioned analytical settings make these revisions traceable.

Phase 4 distinguishes the identification of a candidate change from its descriptive interpretation. Following Truong et al. (2020), detection requires an explicit specification of the properties being investigated and the procedure used to locate changes. PELT optimises a specified penalised segmentation objective; its output does not, by itself, establish statistical significance or commercial relevance (Killick et al., 2012). Before-and-after profiles therefore provide separate descriptive evidence. Feature differences indicate what changed but do not automatically explain the detector’s decision or the causes of customer behaviour. Final type definitions and assignments remain tasks for subsequent phases.

Where independent evaluation is intended, the data used to develop rules or estimate transformations and detection settings must be distinguished from the evidence used to evaluate them. The appropriate separation depends on the research claim: retrospective analysis may use a complete historical sequence, whereas evaluation of detection at a particular time must respect the information available at that time. The workflow applies leakage safeguards according to this distinction, informed by Kapoor and Narayanan (2023).

The phase boundaries, customer eligibility rules, proposed two-year observation window, feature formulas, monthly aggregation, ERP-specific treatments and selected visualisations are project-specific design decisions. The same applies to comparison windows, candidate-selection thresholds, event-consolidation rules, persistence criteria and the selection of cases for taxonomy development. These choices require justification against the research question, data characteristics and analytical consequences; they are not prescribed by the cited sources.

Together, these phases provide prepared data and traceable candidate-change evidence for subsequent taxonomy development. Their documentation does not, by itself, establish methodological novelty, causal explanations, detection accuracy or the validity of the eventual taxonomy. Those claims require separate argumentation and evaluation.
```

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
