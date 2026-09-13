# Retail Sales & Inventory Optimization — End-to-End Business Analysis Case Study

**Independent Business Analysis Case Study** (simulated portfolio project — not real employment, clients, or implementation)

RetailCo is a fictional FMCG retailer created for this case study. The dataset (100,000 transactions, 2024, 21 fields — [source overview](data/README.md)) is synthetic, built for analytics practice. No real stakeholders were interviewed; all stakeholders and processes are clearly labeled as simulated throughout.

## The headline finding

The project started by testing three stakeholder concerns against the data — and **two turned out not to be true**:

| Concern | Result |
|---|---|
| "Some products generate high revenue but weak margins" | ❌ **Not supported.** Margin % is uniform across every category (19.9%–20.1%) and brand (19.87%–20.18%). |
| "Inventory is at risk in specific categories/cities" | ⚠️ **Modestly supported, but weaker than it first looked.** 1.62% of transactions fall below reorder level — real, but chi-square testing shows category/city variation isn't statistically significant, and a Pareto check found no concentration at all. |
| "Supplier lead time drives inventory risk" | ❌ **Ruled out.** Correlation ≈ 0.0005. |

The whole project — requirements, process design, dashboard, and recommendation — was redirected around what the evidence actually supported (**inventory exception visibility and monitoring**), not the assumptions the project started with. See [`business-analysis/root-cause-analysis.md`](business-analysis/root-cause-analysis.md) for the full statistical breakdown.

## Project navigation

| Folder | Contents |
|---|---|
| [`data/`](data/) | [Data discovery & dictionary](data/README.md) · [Data quality assessment](data/data-quality-assessment.md) |
| [`business-analysis/`](business-analysis/) | [Problem statement](business-analysis/problem-statement.md) · [Stakeholder register](business-analysis/stakeholder-analysis.xlsx) · [Business questions](business-analysis/business-questions.md) · [KPI framework](business-analysis/kpi-framework.md) · [Root cause analysis](business-analysis/root-cause-analysis.md) · [Business requirements](business-analysis/business-requirements.xlsx) · [Functional requirements](business-analysis/functional-requirements.xlsx) · [Full requirements spec (NFR/data/rules/RACI/AC)](business-analysis/requirements-specification.md) · [User stories](business-analysis/user-stories.xlsx) · [Solution options evaluation](business-analysis/solution-options-evaluation.md) |
| [`process-modeling/`](process-modeling/) | [As-Is process](process-modeling/as-is-process/as-is-process-analysis.md) · [To-Be process](process-modeling/to-be-process/to-be-process-design.md) |
| [`data-analysis/`](data-analysis/) | [Performance analysis](data-analysis/performance-analysis.md) · [SQL queries](data-analysis/sql-analysis.sql) · [Excel workbook + BA notes](data-analysis/excel-analysis/) |
| [`dashboard/`](dashboard/) | [Dashboard requirements](dashboard/dashboard-requirements.md) |
| [`testing/`](testing/) | [UAT test cases](testing/uat-test-cases.xlsx) *(status: Not Executed)* |
| [`executive/`](executive/) | [Executive recommendation](executive/executive-recommendation.md) |

## What this demonstrates

Business problem framing · stakeholder analysis · data quality assessment · statistical hypothesis testing (chi-square, Pareto) · KPI design · root cause analysis · as-is/to-be process modelling (BPMN-style, Mermaid) · business/functional/non-functional requirements · user stories · MoSCoW prioritization · requirements traceability · solution evaluation (weighted decision matrix) · dashboard design · SQL · Excel (SUMIFS, INDEX/MATCH, conditional formatting, pivot-style summaries) · UAT planning · executive communication.

## Project status

Phases 1–12 above are complete. Still in progress: risk register, change management plan, implementation roadmap, portfolio narrative write-up, slide deck, and interview prep materials.

## Ground rules this project followed throughout

- Every number traces to the dataset — anything the data couldn't answer is labeled **"Not available in the provided dataset"** rather than estimated.
- Evidence, assumptions, and recommendations are labeled separately at every phase — nothing is presented as fact unless the data supports it.
- No claim of real implementation, real stakeholders, or realized business results anywhere in this repository.
