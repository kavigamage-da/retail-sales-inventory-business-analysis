# KPI Framework — RetailCo

**Status:** Phase 8 — KPI Framework
**Built on:** Phase 7 — Business Performance Analysis

This framework converts the evidence identified during business performance analysis into a consistent set of business measures for reporting and decision support.

Every **Current Value** shown below is based on the available 2024 dataset. No targets, thresholds, or operational ownership have been invented where the dataset or simulated business context does not provide them.

---

## KPI Definition Standard

### Margin %

Two valid approaches can be used to summarize transaction-level margin percentages:

* **Simple average of transaction-level `Margin_%`:** 19.34%
* **Revenue-weighted margin:** Total Gross Margin ÷ Total Revenue = **20.02%**

This project standardizes on the **revenue-weighted Margin % (20.02%)** for overall profitability reporting because it reflects the contribution of transactions according to their revenue value rather than giving every transaction equal weight.

This definition should remain consistent across the dashboard, SQL analysis, Excel analysis, and executive recommendation.

---

## Core KPI Framework

| KPI                                    | Definition                                                                                 | Formula                                           |                               Current Baseline | Target / Threshold               | Business Importance                                                                | Decision Supported                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------- | ---------------------------------------------: | -------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Revenue**                            | Total sales value generated during the analysis period                                     | `SUM(Revenue)`                                    |                                 ₹39,335,134.98 | To be defined by business        | Measures top-line sales performance                                                | Revenue planning and resource allocation                          |
| **Units Sold**                         | Total number of units recorded as sold                                                     | `SUM(Units)`                                      |                                        299,829 | To be defined by business        | Indicates sales volume independently of revenue value                              | Demand and replenishment planning                                 |
| **Gross Margin**                       | Revenue remaining after recorded cost                                                      | `SUM(Revenue) − SUM(Cost)`                        |                                  ₹7,873,685.66 | To be defined by business        | Measures absolute gross profit contribution                                        | Profitability monitoring                                          |
| **Margin %**                           | Gross margin as a percentage of revenue                                                    | `SUM(Margin) ÷ SUM(Revenue)`                      |                                         20.02% | To be defined by business        | Measures profitability efficiency relative to sales                                | Pricing and cost-structure discussions                            |
| **Average Revenue per Transaction**    | Average revenue generated per transaction record                                           | `SUM(Revenue) ÷ COUNT(*)`                         |                                        ₹393.35 | To be defined by business        | Provides a consistent transaction-level sales benchmark                            | Comparison across city, channel, and store format                 |
| **Revenue Growth (YoY)**               | Change in revenue compared with the previous year                                          | `(Current Year − Prior Year) ÷ Prior Year`        | **Not available** — dataset contains 2024 only | Requires prior-year data         | Would indicate longer-term business trajectory                                     | Trend and growth assessment when additional periods are available |
| **% Transactions Below Reorder Level** | Percentage of transaction records where recorded stock is below the recorded reorder level | `COUNT(Stock_On_Hand < Reorder_Level) ÷ COUNT(*)` |                                      **1.62%** | Business threshold not available | Provides an inventory-attention signal within the available transaction-level data | Replenishment monitoring and exception investigation              |
| **Revenue by Channel**                 | Revenue distributed across Online, Offline, and Omnichannel transactions                   | `SUM(Revenue)` grouped by `Channel`               |              Approx. **33.5% / 33.2% / 33.4%** | No target available              | Provides visibility into channel contribution                                      | Channel performance monitoring                                    |
| **Revenue by Store Format**            | Revenue distributed across Hyper, Super, and Express formats                               | `SUM(Revenue)` grouped by `Store_Format`          |              Approx. **33.6% / 33.3% / 33.1%** | No target available              | Provides visibility into format contribution                                       | Store-format performance monitoring                               |

> **Interpretation note:** Revenue by Channel and Revenue by Store Format are included as **management metrics / KPI breakdowns** rather than independent profitability KPIs. Their purpose is to provide dimensions through which core measures such as Revenue, Gross Margin, and Margin % can be analyzed.

---

## Inventory KPI Boundary

### % Transactions Below Reorder Level

The dataset contains:

* **1,624 / 100,000 transaction records** below the recorded reorder level
* **Overall rate: 1.62%**
* City-level range: **1.43%–1.75%**
* Category-level range: **1.50%–1.74%**

This KPI must **not** be described as:

* Stockout Rate
* Inventory Shortage Rate
* Inventory Risk Rate
* Percentage of products out of stock

The dataset does not contain persistent Product/SKU and Store identities or inventory movement history. Therefore, the measure represents **transaction records observed below the recorded reorder level**, rather than confirmed product/store stock shortages.

The highest observed category/city combinations in Phase 7 were:

* Dairy × Mumbai: **2.47%**
* Snacks × Chennai: **2.45%**
* Snacks × Pune: **2.21%**
* Personal Care × Mumbai: **2.14%**
* Beverages × Mumbai: **2.07%**

These are **descriptive observations**, not confirmed operational hotspots or automatically defined business priorities.

Further investigation would require persistent SKU/store inventory data, demand history, inventory movements, replenishment records, and business-defined reorder policies.

---

## KPI Governance

| Governance Element       | Definition                                                                                                     |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Baseline**             | Current value calculated from the available 2024 dataset                                                       |
| **Target**               | Not available in the simulated business context; should be defined by the business                             |
| **Threshold**            | Not assumed unless supported by business policy or explicitly identified as an analyst-defined case-study rule |
| **Owner**                | To be defined by the simulated business                                                                        |
| **Reporting Frequency**  | To be defined based on operational requirements                                                                |
| **Source**               | RetailCo 2024 transaction dataset                                                                              |
| **Calculation Standard** | Formulas documented in this framework                                                                          |
| **Data Limitations**     | Must be considered when interpreting each KPI                                                                  |

This prevents the case study from inventing business targets, ownership, or governance arrangements that were not available in the source data.

---

## KPIs Considered but Not Included

| Rejected KPI                      | Reason                                                                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Stockout Rate**                 | No transaction shows `Stock_On_Hand = 0`; therefore, the available data does not support a stockout-rate KPI |
| **Basket Size / Items per Order** | Each row represents a single-line transaction; there is no multi-item basket structure                       |
| **Customer Lifetime Value**       | No persistent Customer ID is available to identify and link repeat purchases                                 |
| **Customer Repeat Rate**          | No persistent Customer ID is available                                                                       |
| **Promotion ROI**                 | No promotional-mechanics field is available                                                                  |
| **Return Rate**                   | No return transactions or return-value field is available                                                    |
| **Shrink / Wastage Rate**         | No shrinkage, wastage, or inventory-loss field is available                                                  |
| **Year-over-Year Revenue Growth** | Only 2024 data is available; a prior-year comparison cannot be calculated                                    |

Excluding these measures is a deliberate BA decision based on data availability rather than an omission.

---

## KPI Interpretation Rules

The following rules apply to subsequent analysis and reporting:

1. **Every KPI must have a documented definition and calculation method.**
2. **Current values must be traceable to the available dataset.**
3. **Targets must not be invented.**
4. **Unavailable KPIs must be explicitly identified as unavailable.**
5. **Descriptive differences must not automatically be presented as business problems.**
6. **Inventory observations must retain their transaction-level interpretation.**
7. **Margin % must use the agreed revenue-weighted definition when presented as the overall profitability KPI.**
8. **New KPIs should not be introduced later without documenting their definition and data source.**
9. **Where a KPI depends on missing business data, the missing data requirement should be documented rather than estimated.**

---

## How This Framework Will Be Used

This KPI framework provides the measurement standard for the subsequent business-analysis artifacts.

The same definitions should be carried into:

**KPI Framework → Root Cause Analysis → Requirements → Dashboard Requirements → SQL Analysis → Excel Analysis → UAT → Executive Recommendation**

This prevents metric-definition drift between different project artifacts.

The dashboard requirements should therefore use the same KPI names, formulas, and interpretation boundaries defined here.

---

## BA Conclusion

The KPI framework deliberately prioritizes measures that can be supported by the available evidence.

The strongest inventory-related signal identified in Phase 7 is the **1.62% transaction-level below-reorder observation rate**, with modest variation across categories and cities. This supports further investigation and monitoring requirements, but does **not** establish a confirmed inventory crisis.

Conversely, the available analysis did not support a material high-revenue/low-margin problem at the available Category, Brand, and Category × Brand levels. Margin optimization should therefore not be treated as the primary problem solely because margin is a commonly used retail KPI.

The framework therefore translates **validated evidence into measurable business requirements without overstating what the dataset can prove.**

---

**Next step:** Phase 9 — Root Cause Analysis, focused on understanding the possible drivers and data limitations behind the observed below-reorder transaction pattern.
