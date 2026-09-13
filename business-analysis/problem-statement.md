# Business Context & Problem Statement — RetailCo

**Project:** Retail Sales & Inventory Optimization — End-to-End Business Analysis Case Study
**Company:** RetailCo — a **fictional, simulated company** created for this portfolio case study. RetailCo has no relationship to any real employer, client, or business. No real stakeholders were interviewed; all stakeholder concerns referenced below are **simulated starting assumptions** for the purpose of this exercise.
**Status:** Phase 2–3 — Business Context & Problem Statement
**Built on:** Phase 1 Data Discovery findings (`data/README.md`)

---

## PART A — Business Context

### Business Background

RetailCo is a simulated FMCG (Fast-Moving Consumer Goods) retailer operating across 8 major Indian metro markets — Mumbai, Delhi, Bengaluru, Kolkata, Chennai, Hyderabad, Ahmedabad, and Pune. **[DATA EVIDENCE]**

It sells across 8 product categories (Beverages, Snacks, Dairy, Grocery, Personal Care, Home Care, Fruits, Vegetables), sourced from 8 brand partners, through three store formats (Hyper, Super, Express) and three channels (Online, Offline, Omnichannel). **[DATA EVIDENCE]**

In the 2024 calendar year, the dataset contains 100,000 transactions generating approximately ₹39.33M in revenue at an average margin of 19.34%. **[DATA EVIDENCE]**

---

### Current Situation

RetailCo captures transaction-level data covering sales, cost, margin, inventory snapshots, and basic customer attributes for recorded transactions. **[DATA EVIDENCE — based on fields confirmed in Phase 1]**

The dataset cannot establish how this information is currently reported or used operationally. In particular, it does not provide evidence about existing spreadsheets, reporting processes, BI tools, reporting frequency, decision-making workflows, or operational ownership.

For this case study, RetailCo is therefore **assumed** to be a growing retailer that has outgrown manual or ad-hoc reporting and would benefit from a more structured management reporting approach. This is a **simulated business-context assumption**, not an observed fact about a real organization.

---

### Business Problem

At the beginning of the case study, three simulated stakeholder concerns were defined as hypotheses to be tested against the available data. These represent the types of concerns a BA might receive at project initiation before validating them with evidence.

1. **Management may lack a consolidated view** of sales, margin, and inventory performance across category, brand, city, store format, and channel.
2. **Some categories or brands may generate strong revenue but comparatively weak margins**, which could be difficult to identify without structured profitability reporting.
3. **Some inventory records may indicate potential replenishment risk**, particularly where recorded stock falls below the defined reorder level.

The analysis does **not** assume that these concerns are true.

Transaction-level Margin_% varies between approximately 5% and 31%, but this variation alone does **not** establish that high-revenue categories or brands have weaker margins. Category- and brand-level analysis is required to test that hypothesis.

Separately, 1.62% of recorded transactions have stock below the defined reorder level. This provides an initial signal of potential inventory exceptions, but does not by itself establish a broader operational inventory problem.

These concerns are therefore treated as **testable hypotheses rather than confirmed business problems**. Subsequent data quality, performance analysis, KPI, and root-cause analysis phases test the hypotheses and document where the evidence does or does not support them.

---

### Business Impact

**Not available in the provided dataset.**

The dataset does not contain a baseline for quantifying the current operational or financial impact of the identified concerns. For example, it does not provide reporting effort, missed-sales value, stockout cost, service-level impact, or historical before/after performance.

Potential operational consequences — such as slower identification of inventory exceptions or less consistent management decisions — are therefore treated as **hypothetical impacts**, not measured business results.

No financial impact is presented as fact unless it can be directly supported by the available evidence.

---

### Business Need

RetailCo needs an evidence-based way to monitor sales, profitability, and inventory-risk signals across its available business dimensions.

The case study therefore aims to establish:

* which business concerns are actually supported by the available data;
* which KPIs are useful for monitoring those concerns;
* what information management would need to make informed decisions; and
* what requirements should guide a future reporting or decision-support solution.

The need for this structured approach is a **simulated business assumption grounded in the available data**, rather than evidence from a real organization.

---

### Project Goal

Deliver an evidence-based assessment of RetailCo's 2024 sales, profitability, and inventory performance; identify the business concerns actually supported by the available data; and translate those findings into prioritized requirements and recommendations for a management reporting and decision-support solution.

---

### Business Objectives

See **Part B → Project Objectives** below for the full measurable list.

---

### Project Scope

The case study covers:

* Analysis of the 2024 transaction dataset, including sales, margin, inventory-snapshot, and customer/loyalty fields.
* Business requirements, functional requirements, and KPI definitions for a reporting and decision-support solution.
* Modelling of a **simulated current-state reporting/replenishment workflow** and a proposed future-state workflow.
* Evaluation of potential solution approaches, including Excel, Power BI, and custom BI.
* Definition of dashboard and reporting requirements.
* UAT planning for the proposed solution.

---

### Out of Scope

* Building or deploying a production application, database, or live dashboard connection.
* Machine-learning or forecasting models.
* Real stakeholder interviews or primary research.
* Real organizational change management.
* Production implementation or deployment.
* Measurement of realized business benefits.
* Claims about actual RetailCo operational performance beyond what can be established from the provided dataset.

---

### Constraints

* **Single calendar year of data (2024):** no prior-year data is available, so year-over-year growth cannot be calculated. **[DATA EVIDENCE]**
* **No returns, wastage, or promotional-mechanics fields:** shrink, returns, and promotion-uplift analysis are outside the available evidence base. **[DATA EVIDENCE — confirmed absent in Phase 1]**
* **No Product/SKU or Store ID field:** product-level and store-level inventory analysis cannot be performed reliably; inventory analysis is therefore limited to the dimensions available in the dataset. **[DATA EVIDENCE]**
* **Customer_Age is missing for approximately 40% of records:** age-based segmentation can only be treated as a partial-sample analysis. **[DATA EVIDENCE]**
* **No operational process history:** actual reporting, replenishment, escalation, and decision-making workflows cannot be reconstructed from the dataset alone. **[DATA LIMITATION]**

---

### Assumptions

* RetailCo, its stakeholders, operating context, and current reporting environment are simulated for this case study. **[EXPLICIT ASSUMPTION — NOT DATA EVIDENCE]**
* The stakeholder concerns used at project initiation are simulated hypotheses rather than findings from real interviews. **[EXPLICIT ASSUMPTION]**
* The dataset's category, brand, city, channel, and store-format mix is treated as representative of the simulated RetailCo operating context for analytical purposes. **[BUSINESS ASSUMPTION]**
* Where an operational workflow is required for process modelling, it is explicitly treated as a simulated current-state scenario rather than a verified real-world process. **[BUSINESS ASSUMPTION]**

---

## PART B — Business Problem Statement

### Problem Statement

| Element               | Statement                                                                                                                                                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Current Situation** | RetailCo's simulated operating context includes transaction-level sales, margin, and inventory-snapshot data across multiple business dimensions, but the available dataset does not establish how this information is currently consolidated, monitored, or used for management decisions. |
| **Problem**           | Management therefore lacks an evidence-validated view of which sales, profitability, and inventory-risk signals require attention, and the initial stakeholder concerns have not yet been validated against the available data.                                                             |
| **Impact**            | **Not available in the provided dataset.** Potential operational impacts such as slower identification of exceptions or less consistent decision-making are hypothetical and cannot be quantified from the available evidence.                                                              |
| **Desired Outcome**   | Establish a validated picture of sales, profitability, and inventory performance; identify the concerns actually supported by evidence; and translate the findings into clear KPIs, requirements, and decision-support recommendations.                                                     |

---

### Business Need Statement

RetailCo requires an evidence-based, requirements-driven assessment of its 2024 sales, profitability, and inventory data to distinguish validated business problems from initial assumptions and to inform a future management reporting and decision-support investment.

---

### Project Objectives

The following objectives are measurable using the fields confirmed during Phase 1:

1. **Quantify revenue, units sold, and margin performance** by category, brand, city, store format, and channel.

2. **Identify categories and brands where revenue is high but margin percentage is comparatively low**, or where other material revenue-versus-margin differences are present.

3. **Quantify the proportion of recorded transactions where stock is below the defined reorder level**, with breakdowns by available business dimensions such as category and city.

4. **Compare sales and profitability performance** across Online, Offline, and Omnichannel channels and across Hyper, Super, and Express store formats.

5. **Compare revenue and margin performance** between loyalty and non-loyalty transactions, while clearly identifying any limitations caused by the available customer fields.

6. **Define a core management KPI framework**, including metrics such as revenue, margin percentage, average transaction value, and percentage of transactions below reorder level, with formulas traceable to the available dataset fields.

Each objective is designed around fields confirmed as available during Phase 1. Where the dataset cannot answer a question reliably, the limitation will be documented rather than inferred.

---

### Evidence-Based BA Principle

This case study treats the initial business concerns as **hypotheses to validate rather than requirements to accept unquestioningly**.

The analysis therefore follows the sequence:

**Business Concern → Business Question → Data Validation → Analysis → Finding → Requirement → Recommendation**

This prevents the solution from being designed around an unsupported assumption and ensures that subsequent requirements and recommendations are grounded in evidence.

---

 
