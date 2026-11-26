<div align="center">

# AI Tool Use Disclosure

[![Claude Sonnet 4.6](https://img.shields.io/badge/Claude%20Sonnet%204.6-Anthropic%20model-%23352898?style=flat&labelColor=%2315934E)](https://www.anthropic.com/claude/sonnet)
[![Consensus in ChatGPT](https://img.shields.io/badge/Consensus-Research%20tool-%23352898?style=flat&labelColor=%2315934E)](https://consensus.app/)
[![GPT-5.5 Pro](https://img.shields.io/badge/GPT--5.5%20Pro-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-5.5-pro)
[![GPT-5.6 Sol](https://img.shields.io/badge/GPT--5.6%20Sol-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
[![GPT-6 Astra](https://img.shields.io/badge/GPT--6%20Astra-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6-astra)
[![GPT-6.1 Sol](https://img.shields.io/badge/GPT--6.1%20Sol-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
[![GPT-6 Sol](https://img.shields.io/badge/GPT--6%20Sol-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6-sol)

</div>

## Table of Contents

- [Overview](#overview)
- [AI use by project stage](#ai-use-by-project-stage)
- [Verification, data protection and responsibility](#verification-data-protection-and-responsibility)
- [Bibliography](#bibliography)

---

## Overview

This document discloses the AI tools used in preparing this bachelor's thesis project and carrying out its analysis. It identifies the tools and models, the tasks for which they were used, the material provided as context and the kinds of output they produced. The project follows the six-phase [FUUCCE framework](docs/framework/fuucce_framework.md). The documented use concerns project preparation and Phases 1–6.

AI tools supported research, planning, documentation and programming. Their outputs were suggestions and working material. The selection of sources, methodological decisions, interpretation of findings and final project content remain my responsibility. This disclosure follows the German Research Foundation's recommendation to make the purpose and extent of generative AI use transparent (Deutsche Forschungsgemeinschaft, 2023).

---

## AI use by project stage

| **Project stage**                                             | **AI tool and model**                                                                         | **Purpose and context provided**                                                                                                              | **AI-assisted output**                                                                                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Preparation:** Research topic and literature search         | Claude Sonnet 4.6 (Anthropic, 2026); GPT-5.5 Pro (OpenAI, 2026a); GPT-6 Astra (OpenAI, 2026c) | Research topic, planned contribution and questions about related scientific work and methodological foundations.                              | Suggestions for relevant literature, comparisons with related research and feedback on the research focus.                                             |
| **Preparation:** Bibliography and literature overview         | GPT-5.6 Sol (OpenAI, 2026b); Consensus in ChatGPT (Consensus, n.d.)                           | Publication details or PDFs of selected papers; questions about the relevance and accuracy of sources and references.                         | Draft BibTeX entries and structured paper summaries. Additional AI-assisted searches and checks of references.                                         |
| **Preparation:** Project plan, data description and framework | GPT-6 Astra (OpenAI, 2026c); GPT-6 Sol (OpenAI, 2026e)                                        | Drafts of the project plan, data description and methodological framework, together with the research question and project scope.             | Critical feedback, proposed revisions, text drafts and suggestions for aligning the six framework phases with the available data and the project plan. |
| **Preparation:** Repository and development workflow          | GPT-6 Astra (OpenAI, 2026c); GPT-6 Sol (OpenAI, 2026e); GPT-6.1 Sol via Codex (OpenAI, 2026d) | Repository structure, configuration files and questions about Git, uv, Git LFS, Serena and the setup workflow.                                | Suggestions and revisions for repository documentation, configuration, a pre-commit hook, a pull request template and the project backlog.             |
| **Preparation:** Setup scripts and guides                     | GPT-6 Astra (OpenAI, 2026c); GPT-6 Sol (OpenAI, 2026e); GPT-6.1 Sol via Codex (OpenAI, 2026d) | Existing scripts, draft code and requirements for CSV-to-Parquet conversion, documentation generation, notebook conversion and initial setup. | Drafts and revisions of Python and shell scripts, explanations of their code and supporting setup documentation.                                       |
| **Phase 1:** Data understanding                               | GPT-6.1 Sol via Codex (OpenAI, 2026d)                                                         | Phase 1 requirements, the project documentation and the structure of the example datasets.                                                    | Assistance with generating the Phase 1 notebook. Its analytical content and results require review against the underlying data.                        |

The table summarises types of use rather than individual prompts or every iteration. A tool's presence in a row does not mean that it independently produced every document or file mentioned in that row.

---

## Verification, data protection and responsibility

I read AI-generated text and code before adopting it and requested detailed explanations of generated code to understand its operation. For the literature work, I searched for the publications independently, obtained available PDFs, generated AI-assisted summaries and reviewed the summaries alongside the papers. I also used Consensus for additional AI-assisted checks of references.

I ran the AI-assisted scripts and notebooks myself, inspected their outputs and analysed the resulting data and findings. I compared the results with the underlying data, the documented calculation rules and the intended analytical steps, and revised the code where necessary. I also read the generated code and requested detailed explanations to understand how it works.

AI tools were provided with example datasets, project documentation and analyses of the example data. Original company ERP data were not provided to these tools; access to those data remained with me. Findings from example data must not be presented as findings from the original company data.

I decide which suggestions to adopt, revise or reject. I remain responsible for source selection and citation accuracy, the correctness of incorporated code and text, the interpretation of analytical results and the final contents of this repository. AI tools are not authors of the project.

---

## Bibliography

See [docs/literature/bibliography.md](docs/literature/bibliography.md).
