# KPI Framework — RetailCo

**Status:** Phase 8 — KPI Framework
**Built on:** Phase 7 Business Performance Analysis. Every "Current Value" below is DATA EVIDENCE, computed directly from the 2024 dataset — nothing here is projected or assumed.

> **Definitional note on Margin %:** two valid ways exist to average margin % across many transactions — the simple average of each row's Margin_% (19.34%), or the revenue-weighted figure (Total Margin ÷ Total Revenue = 20.02%). This framework standardizes on the **revenue-weighted figure (20.02%)** for all KPIs and dashboards going forward, because it correctly reflects overall portfolio profitability rather than giving a small transaction the same weight as a large one. This choice is documented here so it stays consistent across every later phase (dashboard, SQL, Excel).

---

## KPI Table

| KPI | Definition | Formula | Current Value | Business Importance | Decision Supported |
|---|---|---|---|---|---|
| Revenue | Total sales value generated | SUM(Revenue) | ₹39,335,134.98 | Top-line performance indicator | Target-setting, resource allocation |
| Units Sold | Total product volume sold | SUM(Units) | 299,829 | Volume indicator, independent of pricing | Demand/replenishment planning |
| Gross Margin | Total profit after cost of goods sold | SUM(Revenue) − SUM(Cost) | ₹7,873,685.66 | Absolute profitability | Profitability monitoring |
| Margin % | Profitability rate on sales | SUM(Margin) ÷ SUM(Revenue) | 20.02% | Efficiency of sales, not just volume | Pricing/cost-structure discussions |
| Average Transaction Value (ATV) | Average revenue per transaction | SUM(Revenue) ÷ COUNT(Transactions) | ₹393.35 | Basket-size proxy (each row is a single-line transaction) | Sales performance benchmarking across city/channel/format |
| Revenue Growth (YoY) | Period-over-period revenue change | (Current Yr − Prior Yr) ÷ Prior Yr | **Not available in the provided dataset** — only 2024 data exists | Would indicate business trajectory | Not usable until a second year of data is available |
| % Transactions Below Reorder Level | Share of transactions recorded with stock under the reorder threshold | COUNT(Stock_On_Hand < Reorder_Level) ÷ COUNT(*) | 1.62% overall (1.43%–1.75% range by city; 1.50%–1.74% by category) | Inventory attention signal — **not** a stockout rate (Stock_On_Hand never reaches 0 in this data) | Replenishment-priority discussions, targeted at Dairy/Mumbai and Snacks/Chennai |
| Revenue by Channel | Revenue split across Online / Offline / Omnichannel | SUM(Revenue) grouped by Channel | Near-even: 33.5% / 33.2% / 33.4% | Channel mix visibility | Channel investment discussions (though evidence shows no channel currently under/over-performs) |
| Revenue by Store Format | Revenue split across Hyper / Super / Express | SUM(Revenue) grouped by Store_Format | Near-even: 33.6% / 33.3% / 33.1% | Format mix visibility | Format investment discussions (same caveat as above) |

---

## KPIs Considered but Not Included

| Rejected KPI | Reason |
|---|---|
| Stockout Rate | No transaction shows Stock_On_Hand = 0; using "stockout" language would overstate what the data supports |
| Basket Size (items per order) | Each row is a single-line transaction — no multi-item basket structure exists to measure |
| Customer Lifetime Value / Repeat Rate | No customer ID exists to link repeat purchases to the same individual |
| Promotion ROI | No promotional-mechanics field exists |
| Return Rate / Shrink | No returns or wastage field exists |

Leaving these out is itself a documented decision, not an oversight — a KPI framework should only promise what the underlying data can actually deliver.

---

## How This Framework Will Be Used Going Forward

- These 9 KPIs are the ones that will appear in the **Dashboard Requirements (Phase 23)** and the **SQL/Excel analysis (Phases 24–25)** — kept consistent rather than introducing new, undefined metrics later.
- The Margin % weighting decision above applies everywhere margin is shown.
- "% Transactions Below Reorder Level" — not "Inventory Risk Rate" or "Stockout Rate" — is the standing name for the inventory KPI throughout the rest of this project, to stay consistent with what Phase 7 found.

---

**Next step:** Phase 9 — Root Cause Analysis, focused on the one KPI with a real (if modest) pattern: inventory attention by category and city.
