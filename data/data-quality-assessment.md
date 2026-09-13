# Data Quality Assessment — RetailCo

**Status:** Phase 6 — Data Quality Analysis  
**Builds on:** Phase 1 — Data Discovery

No data has been silently modified. Issues identified during the assessment are documented and their potential business implications are stated explicitly, in accordance with the project rules.

---

## Issue Register

| Issue ID | Data Issue | Evidence | Business Impact | Severity | Recommendation |
|---|---|---|---|---|---|
| DQ-001 | `Invoice_ID` is not a guaranteed-unique key | 62 `Invoice_ID` values are reused across 124 rows. The associated records differ across fields such as date, city, category and brand, so these are not automatically treated as duplicate rows. | Using `Invoice_ID` alone as a unique join or deduplication key could result in incorrect record matching or double-counting. | Low | Use a documented composite transaction identifier such as `Invoice_ID + Invoice_Date + City + Category + Brand` where `Invoice_ID` alone is insufficient. Do not treat `Invoice_ID` alone as a unique primary key. |
| DQ-002 | High missingness in `Customer_Age` | 40,081 of 100,000 rows are missing `Customer_Age` (40.08%). | Age-based segmentation represents only the available records and may be subject to bias if the missing values are not random. | Medium | Disclose the missing-data rate whenever age-based results are reported. Do not present age-based findings as representative of all transactions without qualification. |
| DQ-003 | Missingness in `Customer_Gender` | 5,048 of 100,000 rows are missing `Customer_Gender` (5.05%). | Gender-based analysis excludes a relatively small portion of records and should therefore be interpreted as analysis of the available data. | Low | Disclose the missing-data rate alongside gender-based reporting. |
| DQ-004 | No persistent Product/SKU or Store identity behind the inventory fields | `Stock_On_Hand` and `Reorder_Level` do not provide evidence of a persistent SKU/store inventory balance. Their variation is observed at transaction level rather than as a tracked running inventory position. | The dataset cannot support reliable reporting of the current stock position of a specific product at a specific store. Inventory analysis is therefore limited to transaction-level indicators such as below-reorder-level observations. | Medium | If future requirements include persistent SKU/store inventory tracking, the source solution would require appropriate Product and Store master data together with an inventory ledger. This is a source-data/solution constraint rather than something that Excel or Power BI can reliably resolve. |
| DQ-005 | Right-skewed tails in Revenue, Cost and Margin | The standard 1.5×IQR rule identifies 1.19% of Revenue rows, 0.72% of Cost rows and 4.95% of Margin rows outside the calculated IQR bounds. Review indicates these observations are consistent with high-value transactions rather than obvious data-entry errors. | Extreme but valid transactions may influence averages and other aggregate statistics. Treating them as errors could distort the analysis. | Low (informational) | No cleaning is required based on the available evidence. Retain valid high-value transactions and consider distribution-aware measures or clearly documented outlier treatment where appropriate. |
| DQ-006 | No returns, wastage or promotional-mechanics fields | These fields are absent from the 21 columns identified during data discovery and are documented as dataset limitations. | Promotion effectiveness, returns-related performance and shrink/wastage analysis cannot be reliably assessed. Profitability analysis is therefore limited to the measures available in the dataset, including gross margin. | Low (scope limitation) | Treat these as analytical scope limitations and reflect them in the project requirements, KPI framework and recommendations. |
| DQ-007 | Single fiscal year of data | The available date range is 1 January–30 December 2024. | Year-over-year growth and multi-year trend comparisons cannot be calculated from this dataset alone. | Low (scope limitation) | Mark year-over-year growth as unavailable in the KPI framework and avoid presenting single-year movement as year-over-year growth. |

---

## Checks Performed With No Issues Found

The following checks were performed to distinguish confirmed data-quality issues from conditions that were tested and found acceptable:

- **Invalid or unparseable dates:** 0 found across 100,000 rows.
- **Negative or impossible numeric values:** 0 found across the reviewed numeric fields (`Units`, prices, `Revenue`, `Cost`, `Margin`, `Margin_%`, `Stock_On_Hand`, `Reorder_Level`, `Lead_Time_Days`, and `Customer_Age`).
- **Loss-making transactions (`Selling_Price ≤ Cost_Price`):** 0 found.
- **Revenue, Cost, Margin and Margin_% consistency:** calculations are consistent across all 100,000 rows: `Revenue = Units × Selling_Price`, `Cost = Units × Cost_Price`, `Margin = Revenue − Cost`, and `Margin_% = Margin ÷ Revenue`.
- **Inconsistent category/text formatting:** no inconsistent spelling, casing or leading/trailing whitespace was identified in the reviewed categorical fields, including `City`, `Store_Format`, `Category`, `Brand`, `Channel`, `Payment_Mode` and `Customer_Gender`.
- **Fully duplicated rows:** 0 found.

---

## Severity Summary

| Severity | Count | Issues |
|---|---:|---|
| Medium | 2 | DQ-002 — Customer_Age missingness; DQ-004 — lack of persistent inventory identity |
| Low | 5 | DQ-001, DQ-003, DQ-005, DQ-006, DQ-007 |

---

## Overall Assessment

The dataset is **generally suitable for the planned business analysis**, with several limitations that affect how findings should be interpreted.

No issue identified required silent correction. The documented issues are primarily **data completeness, data-structure and analytical-scope limitations rather than confirmed data-entry errors**.

The two Medium-severity issues are particularly important for later analysis:

1. **Customer_Age missingness** limits the completeness of demographic segmentation.
2. **Lack of persistent SKU/store inventory identity** limits inventory analysis to transaction-level indicators rather than true current-stock reporting.

These limitations should be carried forward into the KPI framework, analysis, requirements and final recommendations so that the solution does not claim capabilities that the available data cannot support.

---

**Next step:** Phase 7 — Business Performance Analysis, followed by Phase 8 — KPI Framework.