# 🏪 Retail Sales & Inventory Optimization

### End-to-End Business Analysis Case Study

<p align="center">
  <img src="https://img.shields.io/badge/Business%20Analysis-Case%20Study-6C63FF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Data%20Analytics-Python%20%7C%20SQL-00B8D9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Requirements-Engineering-7C4DFF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Process%20Modeling-BPMN%20%7C%20Mermaid-FF6B6B?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Simulated%20Portfolio%20Case%20Study-222222?style=flat-square" />
  <img src="https://img.shields.io/badge/Data-100%2C000%20Transactions-222222?style=flat-square" />
  <img src="https://img.shields.io/badge/Period-2024-222222?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Core%20BA%20Analysis%20Complete-2EA44F?style=flat-square" />
</p>

> **Independent Business Analysis Case Study**
> A simulated FMCG retail environment created to demonstrate how a BA can move from **business concern → evidence → analysis → requirements → process design → decision support**.

**Important:** RetailCo, its stakeholders, operational processes, and business concerns are simulated. The dataset is synthetic and no real employment, client engagement, implementation, stakeholder interview, or realized business result is claimed.

---

## 🎯 What This Case Study Demonstrates

This project is designed to show **how I think as a Business Analyst**, rather than simply demonstrating technical tools.

I started with simulated management concerns, tested them against available evidence, identified which assumptions were supported or unsupported, and then translated the validated opportunity into BA artifacts and decision-support requirements.

### The BA evidence chain

```text
Business Concern
      ↓
Business Questions
      ↓
Data Discovery & Quality
      ↓
Performance Analysis
      ↓
KPI Framework
      ↓
Root Cause Analysis
      ↓
As-Is Process
      ↓
Requirements
      ↓
User Stories & Acceptance Criteria
      ↓
To-Be Process
      ↓
Solution Evaluation
      ↓
Dashboard Requirements
      ↓
UAT Planning
      ↓
Executive Recommendation
```

---

# 🔎 Executive Findings

The most important part of this case study is not the number of files.

It is the **decision-making process**.

Three initial stakeholder concerns were tested against the available data:

| Initial Business Concern                                     | Evidence-Based Result                            | BA Decision                              |
| ------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------- |
| High-revenue products have weak margins                      | ❌ **Not supported**                              | Do not prioritize margin optimization    |
| Inventory risk is concentrated in specific categories/cities | ⚠️ **Modestly supported as a monitoring signal** | Investigate exception visibility further |
| Supplier lead time drives inventory risk                     | ❌ **No meaningful relationship observed**        | Do not treat lead time as the root cause |

### Key evidence

* **100,000** transaction records
* **₹39.34M** total revenue
* **₹7.87M** gross margin
* **20.02%** revenue-weighted overall margin
* **1.62%** of transaction records below reorder level
* Category margin range: approximately **19.90%–20.14%**
* Brand margin range: approximately **19.87%–20.18%**
* Supplier lead-time correlation with below-reorder indicator: approximately **0.0005**
* Chi-square testing did **not** establish statistically significant category/city variation
* Pareto analysis found **no concentrated inventory-risk pattern**

> **Important interpretation:** the 1.62% figure represents transaction records below the recorded reorder level. Because the dataset does not contain persistent SKU/store inventory identities or inventory movement history, it is **not presented as a stockout rate, shortage rate, or confirmed operational inventory crisis**.

---

# 💡 The Business Analysis Insight

The project deliberately **changed direction based on evidence**.

The original assumption was that the business might need margin optimization and inventory-risk intervention.

The analysis showed:

**Margin problem → Not supported**

**Supplier lead-time problem → Not supported**

**Broad inventory crisis → Not supported**

**Inventory exception visibility → Strongest remaining BA opportunity**

Therefore, the later requirements and solution design focus on **inventory exception monitoring and decision visibility**, rather than forcing the original assumptions into the final recommendation.

That evidence-driven pivot is one of the main BA capabilities demonstrated by this case study.

---

# 🧩 BA Deliverables

## 01 — Business Analysis

| Artifact                                                                        | Purpose                                                                    |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| [Problem Statement](business-analysis/problem-statement.md)                     | Defines the simulated business problem, scope, objectives and constraints  |
| [Stakeholder Register](business-analysis/stakeholder-analysis.xlsx)             | Maps simulated stakeholder power, interest and engagement                  |
| [Business Questions](business-analysis/business-questions.md)                   | Converts initial concerns into answerable analytical questions             |
| [KPI Framework](business-analysis/kpi-framework.md)                             | Defines measurable indicators and calculation standards                    |
| [Root Cause Analysis](business-analysis/root-cause-analysis.md)                 | Tests possible explanations instead of assuming causes                     |
| [Business Requirements](business-analysis/business-requirements.xlsx)           | Converts validated business needs into requirements                        |
| [Functional Requirements](business-analysis/functional-requirements.xlsx)       | Defines expected system capabilities                                       |
| [Requirements Specification](business-analysis/requirements-specification.md)   | Consolidates requirements, rules, data, NFRs, RACI and acceptance criteria |
| [User Stories](business-analysis/user-stories.xlsx)                             | Translates requirements into user-centered delivery items                  |
| [Solution Options Evaluation](business-analysis/solution-options-evaluation.md) | Compares solution approaches using a weighted decision matrix              |

---

## 02 — Process Modeling

| Artifact                                                                  | Purpose                                                                           |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [As-Is Process](process-modeling/as-is-process/as-is-process-analysis.md) | Documents the current-state process boundaries, assumptions, pain points and gaps |
| [To-Be Process](process-modeling/to-be-process/to-be-process-design.md)   | Defines the proposed future-state workflow and improved exception handling        |

**Modeling approach:** BPMN-style process thinking + Mermaid diagrams.

---

## 03 — Data & Analytics

| Artifact                                                      | Purpose                                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Data Discovery](data/README.md)                              | Documents dataset structure, fields and analytical scope                 |
| [Data Quality Assessment](data/data-quality-assessment.md)    | Identifies completeness, structure and usability limitations             |
| [Performance Analysis](data-analysis/performance-analysis.md) | Evaluates sales, profitability, customer, channel and inventory patterns |
| [SQL Analysis](data-analysis/sql-analysis.sql)                | Demonstrates analytical querying                                         |
| [Excel Analysis](data-analysis/excel-analysis/)               | Provides spreadsheet-based analysis and BA-oriented evidence             |

---

## 04 — Decision Support

| Artifact                                                          | Purpose                                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [Dashboard Requirements](dashboard/dashboard-requirements.md)     | Defines decision-support requirements without claiming a production dashboard |
| [UAT Test Cases](testing/uat-test-cases.xlsx)                     | Defines acceptance testing scenarios                                          |
| [Executive Recommendation](executive/executive-recommendation.md) | Converts analysis into management-oriented recommendations                    |

> **UAT status:** Not Executed.
> No implementation or test execution is claimed.

---

# 📊 Analytical Snapshot

### Revenue

**₹39,335,134.98**

### Units Sold

**299,829**

### Transactions

**100,000**

### Gross Margin

**₹7,873,685.66**

### Revenue-Weighted Margin

**20.02%**

### Below-Reorder Transaction Records

**1.62%**

---

# 🧠 What I Tested

### 1. Profitability hypothesis

I tested whether high-revenue categories and brands were associated with comparatively weak margins.

**Finding:** the available Category, Brand and Category × Brand analysis did not support a meaningful high-revenue/low-margin problem.

**Decision:** margin optimization was not carried forward as the primary problem.

---

### 2. Inventory exception hypothesis

I examined the proportion of transaction records where:

```text
Stock_On_Hand < Reorder_Level
```

Result:

```text
1,624 / 100,000
= 1.62%
```

The descriptive differences across categories and cities were modest, and statistical testing did not establish significant category/city variation.

**Decision:** treat this as an **inventory monitoring signal**, not evidence of an inventory crisis.

---

### 3. Supplier lead-time hypothesis

The relationship between supplier lead time and the below-reorder indicator was tested.

```text
Correlation ≈ 0.0005
```

**Decision:** no meaningful relationship was observed in the available dataset.

Supplier lead time was therefore **not treated as a root cause**.

---

# 🧪 Analytical Methods

### Descriptive Analysis

* Revenue
* Units
* Gross margin
* Margin %
* Revenue per transaction
* Channel
* Store format
* Category
* Brand
* City
* Inventory indicators

### Statistical Analysis

* Chi-square testing
* Correlation analysis
* Pareto analysis
* Distribution/outlier review

### Business Analysis

* Problem framing
* Stakeholder analysis
* Business questions
* KPI definition
* Root cause analysis
* Process modeling
* Requirements engineering
* User stories
* Acceptance criteria
* MoSCoW prioritization
* Traceability
* Solution evaluation
* UAT planning
* Executive recommendation

---

# 🛠️ Tools & Techniques

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" />
<img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />

</p>

<p align="center">

<img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/Mermaid-Diagrams-FF3670?style=for-the-badge&logo=mermaid&logoColor=white" />
<img src="https://img.shields.io/badge/Business%20Analysis-Requirements-6C63FF?style=for-the-badge" />
<img src="https://img.shields.io/badge/UAT-Testing-8A2BE2?style=for-the-badge" />

</p>

---

# 📁 Repository Structure

```text
retail-sales-inventory-business-analysis/
│
├── 📂 business-analysis/
│   ├── problem-statement.md
│   ├── stakeholder-analysis.xlsx
│   ├── business-questions.md
│   ├── kpi-framework.md
│   ├── root-cause-analysis.md
│   ├── business-requirements.xlsx
│   ├── functional-requirements.xlsx
│   ├── requirements-specification.md
│   ├── user-stories.xlsx
│   └── solution-options-evaluation.md
│
├── 📂 process-modeling/
│   ├── as-is-process/
│   │   └── as-is-process-analysis.md
│   └── to-be-process/
│       └── to-be-process-design.md
│
├── 📂 data/
│   ├── README.md
│   └── data-quality-assessment.md
│
├── 📂 data-analysis/
│   ├── performance-analysis.md
│   ├── sql-analysis.sql
│   └── excel-analysis/
│
├── 📂 dashboard/
│   └── dashboard-requirements.md
│
├── 📂 testing/
│   └── uat-test-cases.xlsx
│
├── 📂 executive/
│   └── executive-recommendation.md
│
└── README.md
```

---

# 🔗 Traceability

The project is structured so that the major BA outputs connect rather than existing as isolated documents:

```text
Dataset
   ↓
Data Quality
   ↓
Business Questions
   ↓
Performance Analysis
   ↓
KPI Framework
   ↓
Root Cause Analysis
   ↓
As-Is Process
   ↓
Business Requirements
   ↓
Functional Requirements
   ↓
User Stories
   ↓
To-Be Process
   ↓
Solution Evaluation
   ↓
Dashboard Requirements
   ↓
UAT
   ↓
Executive Recommendation
```

This is intended to demonstrate **requirements traceability and evidence-based decision making**, rather than simply collecting unrelated portfolio artifacts.

---

# ⚖️ Scope & Limitations

This case study intentionally does **not** claim capabilities that the dataset cannot support.

### Available

* 100,000 transaction records
* 2024 transaction data
* Revenue and cost
* Margin
* Units
* Category
* Brand
* City
* Channel
* Store format
* Inventory snapshot indicators
* Supplier lead-time field
* Customer demographic fields with missing values

### Not Available

* Prior-year data
* Persistent Product/SKU identity
* Persistent Store identity
* Inventory movement history
* Purchase-order history
* Supplier performance history
* Returns
* Wastage/shrinkage
* Promotion mechanics
* True stockout events
* Production implementation data
* Real stakeholder interviews

Therefore, claims such as **stockout rate, true inventory availability, YoY growth, promotion ROI, customer lifetime value, or operational root cause** are not presented as measurable facts from this dataset.

---

# 🎯 BA Principles Demonstrated

### Evidence before assumptions

A business concern is treated as a hypothesis until the available evidence supports it.

### Questions before solutions

Business questions are defined before jumping into dashboard or system requirements.

### Data limitations matter

Unavailable fields are documented rather than silently estimated.

### Symptoms are not automatically root causes

A correlation, descriptive difference, or operational assumption is not automatically treated as a confirmed cause.

### Requirements follow validated needs

The solution direction changes when evidence changes.

### Recommendations must be traceable

Management recommendations are linked back to analysis and documented limitations.

---

# 🚧 Project Status

### Core BA Analysis — Complete

The core analytical and BA foundation is complete, including:

* Business problem framing
* Stakeholder analysis
* Business questions
* Data quality assessment
* Performance analysis
* KPI framework
* Root cause analysis
* As-Is process analysis
* Requirements engineering
* User stories
* Solution evaluation
* Dashboard requirements
* UAT planning
* Executive recommendation

### Portfolio Enhancements — In Progress

* Risk register
* Change management plan
* Implementation roadmap
* Portfolio narrative
* Presentation deck
* Interview preparation materials

---

# 👩‍💻 About This Project

This project was independently created as a **Business Analysis portfolio case study** to demonstrate the ability to connect:

**Business → Data → Process → Requirements → Product/Technology**

The objective was not to make the dataset look perfect.

The objective was to demonstrate the ability to:

> **Ask the right question, test the assumption, understand the limitation, and turn the evidence into a business decision.**

---

<p align="center">

 

<p align="center">
  <sub>Independent simulated case study • No real client or employment claims</sub>
</p>
