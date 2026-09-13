# Business Context & Problem Statement — RetailCo

**Project:** Retail Sales & Inventory Optimization — End-to-End Business Analysis Case Study
**Company:** RetailCo — a **fictional, simulated company** created for this portfolio case study. RetailCo has no relationship to any real employer, client, or business. No real stakeholders were interviewed; all stakeholder concerns referenced below are **simulated** for the purpose of this exercise.
**Status:** Phase 2–3 — Business Context & Problem Statement
**Built on:** Phase 1 Data Discovery findings (`data/README.md`)

---

## PART A — Business Context

### Business Background
RetailCo is a simulated FMCG (Fast-Moving Consumer Goods) retailer operating across 8 major Indian metro markets — Mumbai, Delhi, Bengaluru, Kolkata, Chennai, Hyderabad, Ahmedabad, and Pune. **[DATA EVIDENCE]** It sells across 8 product categories (Beverages, Snacks, Dairy, Grocery, Personal Care, Home Care, Fruits, Vegetables) sourced from 8 brand partners, through three store formats (Hyper, Super, Express) and three channels (Online, Offline, Omnichannel). **[DATA EVIDENCE]** In the 2024 calendar year, RetailCo recorded 100,000 transactions generating ₹39.33M in revenue at a 19.34% average margin. **[DATA EVIDENCE]**

### Current Situation
RetailCo captures transaction-level data — sales, cost, margin, inventory snapshot, and basic customer attributes — for every sale. **[DATA EVIDENCE — these fields exist and are populated]** How this data is currently reported to management (spreadsheets, ad hoc exports, no formal BI tool) is not something the dataset can tell us. **[BUSINESS ASSUMPTION — simulated]** For this case study, RetailCo is assumed to be a growing retailer that has outgrown manual/ad hoc reporting but has not yet invested in a structured BI or dashboard solution — a common and realistic stage for a mid-size FMCG retailer.

### Business Problem
Simulated business stakeholders (Business Sponsor, Sales Manager, Inventory Manager — see Phase 4 Stakeholder Analysis) have raised the following concerns. **[BUSINESS ASSUMPTION — these are the simulated "starting concerns" a BA would typically be handed at project kickoff, before data validation]**:

1. Management lacks a consolidated view of sales, margin, and inventory performance across category, brand, city, store format, and channel.
2. Some products may generate strong revenue but weak margins, which may be going unnoticed without category/brand-level margin reporting.
3. Some inventory may be at risk of falling below reorder thresholds without a systematic way to flag it.

Two of these already have partial support in the data: transaction-level Margin_% ranges widely (5%–31%), which is *consistent with* — but does not yet confirm — a revenue/margin mismatch at the category or brand level; and 1.62% of transactions are recorded with stock below reorder level. **[ANALYST INTERPRETATION]** Phases 6–9 (Data Quality, Performance Analysis, KPI Framework, Root Cause Analysis) will test all three concerns against the evidence and report honestly wherever a concern turns out **not** to be supported.

### Business Impact
**Not available in the provided dataset.** The dataset does not contain a "before" baseline (e.g., cost of manual reporting hours, missed-sale value from inventory gaps), so no financial business impact can be quantified yet. Any impact figures stated later in this project will be clearly labeled as illustrative planning assumptions, never as measured impact.

### Business Need
RetailCo needs a reliable, evidence-based way to monitor sales, profitability, and inventory-risk signals across its markets — and a defined set of KPIs and reporting requirements so any future reporting investment (Excel, Power BI, or otherwise) is built around real business questions rather than guesswork. **[BUSINESS ASSUMPTION, grounded in the confirmed data evidence above]**

### Project Goal
Deliver an evidence-based analysis of RetailCo's 2024 sales, profitability, and inventory data, and translate the confirmed findings into a requirements-driven recommendation for a management reporting/decision-support solution.

### Business Objectives
See **Part B → Project Objectives** below for the full measurable list.

### Project Scope
- Analysis of the 2024 transaction dataset (sales, margin, inventory-snapshot, customer/loyalty fields)
- Business requirements, functional requirements, and KPI definitions for a reporting/decision-support solution
- Process modelling (as-is / to-be) for how sales and inventory data currently informs decisions
- Solution evaluation (Excel vs. Power BI vs. custom BI) and dashboard requirements
- UAT planning for the proposed solution

### Out of Scope
- Building or deploying a production application, database, or live dashboard connection
- Any machine-learning/forecasting model
- Real stakeholder interviews or real organizational change management
- Any claim of implemented, realized business results

### Constraints
- Single calendar year of data (2024) — no prior-year data, so year-over-year growth cannot be calculated. **[DATA EVIDENCE]**
- No returns, wastage, or promotional-mechanics fields — shrink and promotion-uplift analysis are out of scope. **[DATA EVIDENCE — confirmed absent in Phase 1]**
- No Product/SKU or Store ID field — inventory analysis is limited to transaction-level framing (see Phase 1, Section 7). **[DATA EVIDENCE]**
- Customer_Age missing for 40% of records — age-based segmentation covers a partial sample only. **[DATA EVIDENCE]**

### Assumptions
- RetailCo, its stakeholders, and its current reporting process are simulated for this case study. **[explicitly labeled — not evidence]**
- The dataset's category/brand/city mix is treated as representative of RetailCo's actual 2024 operations for the purposes of this exercise. **[BUSINESS ASSUMPTION]**

---

## PART B — Business Problem Statement

### Problem Statement

| Element | Statement |
|---|---|
| **Current Situation** | RetailCo records detailed transaction-level sales, margin, and inventory-snapshot data across 8 cities, 8 categories, and 3 channels, but (per simulated stakeholder input) has no consolidated, KPI-driven view of this data. |
| **Problem** | Sales, profitability, and inventory-risk signals are not consistently visible to management in a form that supports timely decisions — and it is not yet confirmed which specific categories, brands, cities, or channels are driving the concerns stakeholders have raised. |
| **Impact** | *Not available in the provided dataset* — no baseline exists to quantify current-state cost. Qualitatively, unclear visibility plausibly delays decisions on pricing, assortment, and replenishment. **[BUSINESS ASSUMPTION]** |
| **Desired Outcome** | A validated, evidence-based picture of sales/margin/inventory performance, translated into clear KPIs and requirements for a reporting solution management can act on. |

### Business Need Statement
RetailCo needs an evidence-based, requirements-driven analysis of its 2024 sales, profitability, and inventory data — validated against the data itself rather than assumption — to inform a future reporting/decision-support investment.

### Project Objectives
Measurable against this dataset:

1. Quantify revenue, units sold, and margin % by category, brand, city, store format, and channel.
2. Identify any products/categories where revenue is high but margin % is comparatively low (or vice versa).
3. Quantify the proportion of transactions recorded with stock below reorder level, broken down by category and city.
4. Compare performance across the three channels (Online/Offline/Omnichannel) and three store formats (Hyper/Super/Express).
5. Compare revenue and margin between loyalty and non-loyalty transactions.
6. Define a core management KPI set (e.g., revenue, margin %, avg transaction value, % of transactions below reorder level) with formulas traceable to dataset fields.

Each objective above maps directly to fields confirmed present in Phase 1 — nothing here requires data the dataset doesn't have.

---

**Next step:** Phase 4 — Stakeholder Analysis, then Phase 5 — Business Questions.
