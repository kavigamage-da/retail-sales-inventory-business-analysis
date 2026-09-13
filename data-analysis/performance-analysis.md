# Business Performance Analysis — RetailCo (2024)

**Status:** Phase 7 — Business Performance Analysis
**Builds on:** Phase 6 — Data Quality Analysis

All figures below are **DATA EVIDENCE**, computed directly from the 100,000-row 2024 dataset. Interpretation notes are explicitly labeled **ANALYST INTERPRETATION**.

---

## Analytical Scope and Interpretation

This analysis evaluates transaction-level sales, profitability, customer, channel, and inventory indicators available in the 2024 dataset.

Findings describe observed patterns within the available data and should not be interpreted as evidence of actual store-level operational performance where persistent Product/SKU identity, Store identity, inventory history, or operational process data is unavailable.

Descriptive differences are distinguished from statistically validated relationships. Stakeholder concerns are treated as business hypotheses and are not carried forward as confirmed problems unless supported by the available evidence.

---

## Headline Numbers

| Metric                              |          Value |
| ----------------------------------- | -------------: |
| Total Revenue                       | ₹39,335,134.98 |
| Total Units Sold                    |        299,829 |
| Total Transactions                  |        100,000 |
| Total Cost                          | ₹31,461,449.33 |
| Total Gross Margin                  |  ₹7,873,685.66 |
| Overall Margin % (Margin ÷ Revenue) |         20.02% |
| Average Revenue per Transaction     |        ₹393.35 |

---

# 1. Sales Analysis

## Revenue by Category

| Category      |      Revenue | Revenue Share |  Units |
| ------------- | -----------: | ------------: | -----: |
| Fruits        | 4,985,417.90 |         12.7% | 38,195 |
| Grocery       | 4,947,363.17 |         12.6% | 37,400 |
| Snacks        | 4,942,554.66 |         12.6% | 37,418 |
| Beverages     | 4,941,030.17 |         12.6% | 37,863 |
| Home Care     | 4,931,420.48 |         12.5% | 37,790 |
| Vegetables    | 4,915,301.88 |         12.5% | 37,381 |
| Personal Care | 4,884,187.45 |         12.4% | 37,012 |
| Dairy         | 4,787,859.29 |         12.2% | 36,770 |

## Revenue by Brand

| Brand     |      Revenue | Revenue Share |
| --------- | -----------: | ------------: |
| ITC       | 5,019,512.90 |         12.8% |
| HUL       | 4,967,523.37 |         12.6% |
| Britannia | 4,942,030.33 |         12.6% |
| Nestle    | 4,941,904.04 |         12.6% |
| Amul      | 4,937,874.07 |         12.6% |
| Tata      | 4,868,135.99 |         12.4% |
| PepsiCo   | 4,853,369.56 |         12.3% |
| Parle     | 4,804,784.72 |         12.2% |

## Revenue by City

| City      |      Revenue | Avg Revenue per Transaction |
| --------- | -----------: | --------------------------: |
| Kolkata   | 4,999,465.15 |                      394.25 |
| Delhi     | 4,985,262.21 |                      394.12 |
| Hyderabad | 4,950,786.97 |                      397.97 |
| Chennai   | 4,900,659.09 |                      393.09 |
| Pune      | 4,899,356.64 |                      395.01 |
| Mumbai    | 4,897,600.18 |                      392.06 |
| Ahmedabad | 4,877,774.67 |                      392.23 |
| Bengaluru | 4,824,230.07 |                      388.05 |

## Revenue by Store Format

| Store Format |       Revenue | Revenue Share | Avg Revenue per Transaction |
| ------------ | ------------: | ------------: | --------------------------: |
| Hyper        | 13,225,626.24 |         33.6% |                      395.47 |
| Super        | 13,099,594.73 |         33.3% |                      394.06 |
| Express      | 13,009,914.01 |         33.1% |                      390.52 |

## Revenue by Channel

| Channel     |       Revenue | Revenue Share | Avg Revenue per Transaction |
| ----------- | ------------: | ------------: | --------------------------: |
| Omnichannel | 13,162,992.40 |         33.5% |                      394.30 |
| Online      | 13,117,659.01 |         33.4% |                      394.46 |
| Offline     | 13,054,483.57 |         33.2% |                      391.30 |

## Monthly Revenue Trend — 2024

| Month |      Revenue | Transactions |
| ----- | -----------: | -----------: |
| Jan   | 3,365,380.56 |        8,514 |
| Feb   | 3,140,896.09 |        7,944 |
| Mar   | 3,350,248.06 |        8,474 |
| Apr   | 3,280,835.98 |        8,287 |
| May   | 3,346,824.18 |        8,468 |
| Jun   | 3,175,117.85 |        8,095 |
| Jul   | 3,346,063.43 |        8,497 |
| Aug   | 3,375,015.06 |        8,524 |
| Sep   | 3,211,407.61 |        8,316 |
| Oct   | 3,330,184.25 |        8,522 |
| Nov   | 3,192,325.89 |        8,088 |
| Dec   | 3,220,836.04 |        8,271 |

## Loyalty Comparison

| Loyalty_Flag       |       Revenue | Transactions | Avg Revenue per Transaction | Margin % |
| ------------------ | ------------: | -----------: | --------------------------: | -------: |
| Loyalty member (1) | 11,753,652.55 |       29,720 |                      395.48 |   20.03% |
| Not loyalty (0)    | 27,581,482.44 |       70,280 |                      392.45 |   20.02% |

### ANALYST INTERPRETATION — Sales

Revenue is broadly evenly distributed across the dimensions tested.

The coefficient of variation across categories is approximately 1.2%, across brands 1.4%, across cities 1.2%, across store formats 0.8%, and across channels 0.4%. Average revenue per transaction is also relatively stable across the available dimensions.

The monthly revenue range is approximately ₹3.14M–₹3.38M, indicating moderate month-to-month fluctuation but no strong seasonal pattern that can be established from this single-year dataset.

Loyalty members and non-members also show similar average revenue per transaction and margin percentages.

**BA finding:** The 2024 transaction data shows relatively uniform revenue and margin patterns across the dimensions available for analysis. The data does not provide strong evidence for a single "winning" or "losing" sales segment.

This does not mean that RetailCo's overall operations are uniform; it means that **the available transaction data does not show material performance differentiation across the dimensions tested.**

---

# 2. Profitability Analysis

## Margin % by Category

*Margin % is calculated on a revenue-weighted basis.*

| Category      | Margin % |
| ------------- | -------: |
| Grocery       |   20.14% |
| Personal Care |   20.10% |
| Snacks        |   20.07% |
| Vegetables    |   20.05% |
| Dairy         |   20.02% |
| Fruits        |   19.92% |
| Home Care     |   19.92% |
| Beverages     |   19.90% |

## Margin % by Brand

*Margin % is calculated on a revenue-weighted basis.*

| Brand     | Margin % |
| --------- | -------: |
| Amul      |   20.18% |
| Nestle    |   20.06% |
| Tata      |   20.04% |
| Parle     |   20.03% |
| ITC       |   20.03% |
| HUL       |   20.00% |
| PepsiCo   |   19.92% |
| Britannia |   19.87% |

## Category × Brand Margin Analysis

Because the dataset does not contain a persistent Product/SKU identifier, the analysis is performed at the available **Category × Brand** level rather than product level.

There are 64 Category × Brand combinations, with approximately 1,500–1,650 transactions per combination.

### Observed highest-margin combinations

* Vegetables × HUL — 20.49%
* Grocery × Amul — 20.48%
* Snacks × Amul — 20.45%

### Observed lowest-margin combinations

* Home Care × Britannia — 19.44%
* Beverages × Britannia — 19.61%
* Fruits × HUL — 19.69%

### ANALYST INTERPRETATION — Profitability

At Category level, margin % ranges from **19.90% to 20.14%**, a difference of 0.24 percentage points.

At Brand level, margin % ranges from **19.87% to 20.18%**, a difference of 0.31 percentage points.

At the more granular Category × Brand level, the observed range is **19.44%–20.49%**, approximately 1.05 percentage points.

The available analysis does not identify a Category, Brand, or Category × Brand combination that simultaneously demonstrates a materially high revenue position and a materially weak margin position.

### BA Conclusion

The Phase 2 business hypothesis that strong-revenue products or segments may have weak margins is **not supported by the available Category, Brand, and Category × Brand analysis**.

This finding should be retained rather than replaced with a stronger margin narrative that the data does not support.

**BA implication:** Margin optimization should not be prioritized as the primary business problem based on this dataset. Further margin investigation would require more granular product-level data and potentially additional commercial fields such as discounts, promotions, returns, and other cost components.

---

# 3. Inventory Analysis

## Inventory Overview

| Metric                                            |                    Value |
| ------------------------------------------------- | -----------------------: |
| Stock_On_Hand range                               |             50–499 units |
| Reorder_Level range                               |              20–79 units |
| Transactions with Stock_On_Hand < Reorder_Level   | 1,624 of 100,000 (1.62%) |
| Transactions in analyst-defined near-reorder band |            2,086 (2.09%) |
| Combined attention zone                           |            3,710 (3.71%) |
| Average supplier lead time                        |                8.52 days |

No transaction records Stock_On_Hand = 0. Therefore, this analysis does **not** classify any observation as a stockout.

### Inventory Interpretation Boundary

Stock_On_Hand and Reorder_Level are treated as **transaction-level inventory indicators**, not as a persistent inventory balance for a specific Product/SKU at a specific Store.

Therefore:

* 1.62% means that 1.62% of transaction records were observed below the recorded reorder level.
* It does **not** mean that 1.62% of products or stores experienced an inventory shortage.
* The dataset cannot establish stockout duration, lost sales, inventory turnover, or SKU-level replenishment performance.

### Analyst-Defined Near-Reorder Band

For monitoring purposes, the near-reorder band is defined as:

**Stock_On_Hand > Reorder_Level and Stock_On_Hand ≤ 1.25 × Reorder_Level**

This 25% threshold is an **analyst-defined case-study monitoring rule**, not a validated RetailCo operating policy.

---

## Below-Reorder Observations by Category

| Category      | % Below Reorder |
| ------------- | --------------: |
| Dairy         |           1.74% |
| Grocery       |           1.70% |
| Snacks        |           1.69% |
| Beverages     |           1.68% |
| Personal Care |           1.64% |
| Fruits        |           1.53% |
| Vegetables    |           1.51% |
| Home Care     |           1.50% |

## Below-Reorder Observations by City

| City      | % Below Reorder |
| --------- | --------------: |
| Mumbai    |           1.75% |
| Kolkata   |           1.75% |
| Chennai   |           1.74% |
| Hyderabad |           1.65% |
| Pune      |           1.60% |
| Delhi     |           1.53% |
| Bengaluru |           1.53% |
| Ahmedabad |           1.43% |

By city, the observed below-reorder rate ranges from **1.43% to 1.75%**, a difference of 0.32 percentage points.

By category, it ranges from **1.50% to 1.74%**, a difference of 0.24 percentage points.

---

## Highest Observed Below-Reorder Category × City Combinations

| Category      | City    | % Below Reorder | Transactions |
| ------------- | ------- | --------------: | -----------: |
| Dairy         | Mumbai  |           2.47% |        1,582 |
| Snacks        | Chennai |           2.45% |        1,550 |
| Snacks        | Pune    |           2.21% |        1,537 |
| Personal Care | Mumbai  |           2.14% |        1,543 |
| Beverages     | Mumbai  |           2.07% |        1,544 |

These represent the highest observed rates among the Category × City combinations shown. They should be treated as **monitoring signals rather than confirmed operational risk hotspots**.

---

## Supplier Lead Time vs. Below-Reorder Rate

| Lead Time Band | % Below Reorder |
| -------------- | --------------: |
| 3–5 days       |           1.64% |
| 6–8 days       |           1.54% |
| 9–11 days      |           1.70% |
| 12–14 days     |           1.62% |

The observed correlation between supplier lead time and the below-reorder indicator is approximately **0.0005**.

### ANALYST INTERPRETATION — Inventory

The inventory analysis identifies modest descriptive variation in below-reorder observations across categories and cities.

The highest observed category rate is **Dairy at 1.74%**, while the lowest is **Home Care at 1.50%**.

By city, the highest observed rate is **1.75% in Mumbai and Kolkata**, compared with **1.43% in Ahmedabad**.

At the Category × City level, **Dairy × Mumbai (2.47%)** and **Snacks × Chennai (2.45%)** have the highest observed below-reorder rates among the combinations shown.

However, these differences are modest in absolute terms. They should therefore be treated as **descriptive monitoring signals rather than confirmed operational risk hotspots** until further statistical and business validation is completed.

The correlation of approximately 0.0005 indicates **no meaningful relationship observed in this dataset between supplier lead time and the below-reorder indicator**.

Therefore, supplier lead time should **not be treated as an evidence-backed driver** of the observed inventory pattern at this stage.

Further root-cause investigation would require additional operational data, potentially including:

* demand variability
* historical inventory movements
* replenishment history
* reorder-level logic
* Product/SKU identity
* Store identity
* purchase-order history
* supplier performance history

These fields are not available in the current dataset.

---

# 4. Key Findings

| Finding                                                      | Evidence                                                                       | BA Implication                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Revenue is broadly evenly distributed                        | Category, brand, city, store-format and channel results show limited variation | No single sales dimension emerges as an evidence-backed priority            |
| Margin variation is limited                                  | Category: 19.90%–20.14%; Brand: 19.87%–20.18%                                  | Margin optimization is not supported as the primary problem                 |
| Below-reorder observations exist                             | 1.62% of transaction records are below reorder level                           | Inventory exception monitoring may provide useful visibility                |
| Category and city differences are modest                     | Category: 1.50%–1.74%; City: 1.43%–1.75%                                       | Differences should be investigated rather than treated as confirmed risk    |
| Some Category × City combinations have higher observed rates | Dairy × Mumbai: 2.47%; Snacks × Chennai: 2.45%                                 | Candidate monitoring areas, not confirmed risk hotspots                     |
| Supplier lead time shows no meaningful observed relationship | Correlation ≈ 0.0005                                                           | Lead time should not currently be treated as an evidence-backed driver      |
| Loyalty performance is similar                               | Average revenue per transaction and margin are close between groups            | No strong loyalty performance difference is evident                         |
| Monthly revenue fluctuates moderately                        | Monthly revenue ranges from approximately ₹3.14M to ₹3.38M                     | No strong seasonal pattern can be established from this single-year dataset |

---

# 5. Evidence-Based BA Conclusion

The analysis converts the Phase 2 business hypotheses into evidence-based conclusions.

| Phase 2 Business Hypothesis                           | Analytical Result                                                                                                                | BA Decision                                                                           |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Lack of consolidated cross-dimensional visibility     | Not testable from transaction data alone because reporting-tool usage and operational processes are not contained in the dataset | Address through reporting and dashboard requirements rather than performance findings |
| High-revenue / low-margin segments exist              | Not supported by the available Category, Brand and Category × Brand analysis                                                     | Do not prioritize margin optimization based on this dataset                           |
| Inventory may be at risk in some categories/locations | Descriptive variation is observed, but the differences are modest and require further validation                                 | Carry inventory exception monitoring into Root Cause Analysis and requirements        |
| Supplier lead time drives inventory risk              | No meaningful relationship observed; correlation ≈ 0.0005                                                                        | Do not treat supplier lead time as an evidence-backed root cause                      |

### Overall BA Finding

The strongest evidence-supported opportunity emerging from Phase 7 is **improved visibility and monitoring of below-reorder inventory observations**, particularly through category and city-level reporting.

This should **not** be framed as a confirmed inventory crisis. The available data supports an **inventory monitoring and exception-visibility opportunity**, while the underlying operational causes remain unconfirmed.

The margin hypothesis is deliberately not carried forward because the available evidence does not support it.

This evidence-based narrowing of the problem is a key BA outcome:

**Business Hypothesis → Business Question → Data Validation → Analysis → Finding → Requirement → Recommendation**

---

**Next step:** Phase 8 — KPI Framework, followed by Phase 9 — Root Cause Analysis focused on the validated inventory-monitoring opportunity.
