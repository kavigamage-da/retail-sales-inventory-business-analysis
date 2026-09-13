# Data Quality Assessment — RetailCo

**Status:** Phase 6 — Data Quality Analysis
**Builds on:** Phase 1 Data Discovery. No data has been silently modified — every issue below is documented, not cleaned, per project rules.

---

## Issue Register

| Issue ID | Data Issue | Evidence | Business Impact | Severity | Recommendation |
|---|---|---|---|---|---|
| DQ-001 | Invoice_ID is not a guaranteed-unique key | 62 ID values are reused across 124 rows; each pair has a different date/city/product, so these are distinct transactions sharing an ID by chance, not true duplicates | Low risk of double-counting if Invoice_ID is used alone as a join/dedup key in SQL or Excel | Low | Use a composite key (Invoice_ID + Invoice_Date + City + Category + Brand) for any dedup or join logic; never rely on Invoice_ID alone as a primary key |
| DQ-002 | High missingness in Customer_Age | 40,081 of 100,000 rows missing (40.08%) | Any age-based segmentation reflects only ~60% of transactions; risk of a biased view if missingness isn't random | Medium | Disclose the missing % every time an age-based figure is reported; do not present age segmentation as covering "all customers" |
| DQ-003 | Missingness in Customer_Gender | 5,048 of 100,000 rows missing (5.05%) | Minor — gender-based views still cover ~95% of transactions | Low | Disclose missing % alongside gender-based reporting |
| DQ-004 | No persistent Product/SKU or Store identity behind the inventory fields | Stock_On_Hand and Reorder_Level show essentially the same variance *within* each Category+Brand or City+Store_Format group as *across* the whole dataset (see Phase 1, Section 7) — i.e., they behave as independent per-transaction values, not a tracked running balance | Cannot report "current stock position of Product X at Store Y"; inventory analysis is necessarily transaction-level, not SKU-level | Medium | If a future solution needs real per-SKU stock tracking, the source system will need a proper Product/Store master with a stock ledger — flag this as a solution constraint, not something Excel/Power BI can fix on top of this data |
| DQ-005 | Revenue, Cost, and Margin contain a right-skewed tail flagged by the standard 1.5×IQR outlier test | 1.19% of Revenue rows, 0.72% of Cost rows, and 4.95% of Margin rows fall outside 1.5×IQR bounds | None — inspection confirms these are legitimate high-value transactions (high Units × high Selling_Price), not data errors. Margin shows the widest "outlier" band because it's a difference of two already-skewed fields, which mechanically widens its spread | Low (informational) | No cleaning needed. Do not remove or cap these rows — they are valid transactions, not errors |
| DQ-006 | No returns, wastage, or promotional-mechanics fields exist | Confirmed absent from the 21 columns in Phase 1; also disclosed as a limitation in the source dataset's own overview document | Cannot analyze promotion effectiveness or shrink; profitability analysis is limited to gross margin only | Low (scope limitation, not an error) | Already reflected as a project Constraint (Phase 2) |
| DQ-007 | Single fiscal year of data (2024 only) | Confirmed date range Jan 1 – Dec 30, 2024 | No year-over-year growth KPI is possible | Low (scope limitation) | "Revenue Growth" KPI marked *Not available in the provided dataset* in the KPI Framework (Phase 8) |

---

## Checks Performed With No Issues Found

To be transparent about what was tested and came back clean, not just what was flagged:

- **Invalid/unparseable dates:** 0 found across 100,000 rows
- **Negative or impossible numeric values:** 0 found in any of the 11 numeric fields (Units, prices, Revenue, Cost, Margin, Margin_%, Stock_On_Hand, Reorder_Level, Lead_Time_Days, Customer_Age)
- **Loss-making transactions (Selling_Price ≤ Cost_Price):** 0 found
- **Revenue/Cost/Margin/Margin_% formula consistency:** holds exactly across all 100,000 rows (Revenue = Units×Selling_Price, Cost = Units×Cost_Price, Margin = Revenue−Cost, Margin_% = Margin÷Revenue)
- **Inconsistent category spelling/casing/whitespace:** none found in City, Store_Format, Category, Brand, Channel, Payment_Mode, or Customer_Gender
- **Fully duplicate rows:** 0 found

---

## Severity Summary

| Severity | Count | Issues |
|---|---|---|
| Medium | 2 | DQ-002 (Customer_Age missingness), DQ-004 (no persistent inventory identity) |
| Low | 5 | DQ-001, DQ-003, DQ-005, DQ-006, DQ-007 |

**Overall assessment:** this is a clean dataset. No issue found required silent correction — every issue above is a *disclosure and framing* matter (what the data can and can't reliably support), not a data-cleaning task. The two Medium-severity items (age missingness, no per-SKU inventory identity) are the ones that most directly shape what can credibly be claimed in Phases 7–9.

---

**Next step:** Phase 7 — Business Performance Analysis, followed by Phase 8 — KPI Framework.
