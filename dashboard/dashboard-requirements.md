# Dashboard Requirements — RetailCo Inventory & Sales Decision Support

**Status:** Dashboard Requirements (builds on Phase 12.11 high-level scope and the Power BI recommendation from Solution Options)
**Rule carried through every page below:** every visual has a stated business question and decision it supports — no decorative charts. Where Phase 7/9 found a pattern was **not statistically significant or not concentrated**, the visual is explicitly framed as *ongoing monitoring*, not as evidence of a confirmed problem.

---

## Global Filters (apply across all pages unless noted)

| Filter | Status |
|---|---|
| Date range | Available today |
| Category | Available today |
| City | Available today |
| Channel | Available today |
| Store | **Future-state** — no Store ID exists in the current dataset |
| Product/SKU | **Future-state** — no Product/SKU ID exists in the current dataset |

---

## Page 1 — Executive Overview

| Visual | Business Question | Data | KPI | Decision Supported |
|---|---|---|---|---|
| KPI card: Total Revenue | What is our overall sales performance? | SUM(Revenue) | Revenue | Target-setting, resource allocation |
| KPI card: Units Sold | What volume are we moving? | SUM(Units) | Units Sold | Demand/replenishment planning |
| KPI card: Gross Margin | What is our absolute profitability? | SUM(Margin) | Gross Margin | Profitability monitoring |
| KPI card: Margin % | How efficient is our profitability, not just its size? | SUM(Margin)÷SUM(Revenue) | Margin % | Pricing/cost-structure monitoring *(currently uniform ~20% per Phase 7 — tracked here to catch future change, not because a gap exists today)* |
| KPI card: Total Transactions | What is our overall sales activity level? | COUNT(*) | — (context for ATV) | Operational scale context |
| KPI card: % Transactions Below Reorder Level | How exposed are we to inventory exceptions right now? | COUNT(Stock_On_Hand<Reorder_Level)÷COUNT(*) | Below-Reorder-Level Rate | Primary signal for the confirmed business opportunity (Phase 9) |
| Line chart: Monthly Revenue Trend | How does revenue move across the year? | Revenue by Month | Revenue trend | Seasonal planning, monitoring cadence |

---

## Page 2 — Sales Performance

> **Framing note for this whole page:** Phase 7 found revenue is evenly distributed across category, brand, city, format, and channel (coefficient of variation under 1.5% everywhere). These visuals exist for **ongoing monitoring of a currently uniform business**, not because any imbalance was found — a future shift is exactly what they'd be designed to catch.

| Visual | Business Question | Data | KPI | Decision Supported |
|---|---|---|---|---|
| Bar chart: Revenue by Category | Which categories generate the most revenue? | Revenue grouped by Category | Revenue by Category | Merchandising/assortment monitoring |
| Bar chart: Revenue by Brand | Which brands generate the most revenue? | Revenue grouped by Brand | Revenue by Brand | Brand-partnership monitoring |
| Bar/map: Revenue by City | Which markets perform best? | Revenue grouped by City | Revenue by City | Market-investment monitoring |
| Donut: Revenue by Store Format | How does format relate to sales? | Revenue grouped by Store_Format | Revenue by Store Format | Format-investment monitoring |
| Donut: Revenue by Channel | How does channel relate to sales? | Revenue grouped by Channel | Revenue by Channel | Channel-investment monitoring |
| Table: Avg Transaction Value by City/Channel/Format | Does basket size vary by segment? | Revenue÷Transactions, segmented | Average Transaction Value | Sales performance benchmarking |

---

## Page 3 — Product & Profitability

> **Framing note:** the original stakeholder concern that "some products generate high revenue but weak margin" was tested at every level of granularity available and **not supported** (Phase 7). These visuals monitor for that pattern emerging in the future rather than illustrate a current finding.

| Visual | Business Question | Data | KPI | Decision Supported |
|---|---|---|---|---|
| Bar chart: Margin % by Category | Which categories are most/least profitable per rupee of sales? | Margin % grouped by Category | Margin % | Pricing/category-strategy monitoring *(range confirmed only 19.9%–20.1%)* |
| Bar chart: Margin % by Brand | Which brands are most/least profitable per rupee of sales? | Margin % grouped by Brand | Margin % | Brand-strategy monitoring *(range confirmed only 19.87%–20.18%)* |
| Scatter/quadrant: Revenue vs. Margin % (Category level) | Are there high-revenue/low-margin outliers? | Category-level Revenue & Margin % (8 points) | Revenue, Margin % | Would flag a pricing issue **if** one emerges — none currently confirmed |
| Grouped bar: Loyalty vs. Non-Loyalty (Revenue, Margin %, ATV) | Do loyalty members behave differently? | Grouped by Loyalty_Flag | Revenue, Margin %, ATV by loyalty | Loyalty-program investment monitoring |

---

## Page 4 — Inventory Monitoring *(the confirmed business opportunity — most detailed page)*

| Visual | Business Question | Data | KPI | Decision Supported |
|---|---|---|---|---|
| KPI card: % Transactions Below Reorder Level | What is our current inventory exception rate? | As above | Below-Reorder-Level Rate | Primary inventory health signal |
| KPI card: Inventory Availability Rate | What share of transactions had healthy stock? | 1 − Below-Reorder-Level Rate | Inventory Availability Rate | Positive-framing complement to the above |
| KPI card: Open Exceptions | How many exceptions currently need attention? | COUNT(Status = Open) | Inventory Exception Rate | Operational workload visibility — **future-state**, depends on the exception log (Phase 12.6) |
| Bar chart: % Below Reorder Level by Category | Which categories warrant monitoring priority? | Below-reorder rate grouped by Category | Below-Reorder-Level Rate | Monitoring priority — **not a confirmed hotspot list**: chi-square not significant (p=0.675, Phase 9) |
| Bar/map: % Below Reorder Level by City | Which cities warrant monitoring priority? | Below-reorder rate grouped by City | Below-Reorder-Level Rate | Same caveat — chi-square not significant (p=0.336) |
| Heatmap: % Below Reorder Level, Category × City | Which specific combinations are the best starting point for monitoring? | 64-cell cross-tab | Below-Reorder-Level Rate | Highlights Dairy/Mumbai (2.47%) and Snacks/Chennai (2.45%) as starting points — explicitly **not proven hotspots** (combo-level p=0.383, no Pareto concentration, Phase 9) |
| Bar chart: % Below Reorder Level by Channel | Does channel relate to inventory exceptions? | Below-reorder rate grouped by Channel | Below-Reorder-Level Rate | Weak, marginal signal only (p=0.026, doesn't survive multi-factor correction) — monitor, don't over-index |
| Line/aging chart: Open Exception Aging | How long are open exceptions sitting unresolved? | Time since detection, for open exceptions | Open Exception Aging | Escalation trigger — **future-state**, depends on detection timestamps (Phase 12.6) |
| Table: Recurring Exceptions | Which product/store combinations repeatedly fall below reorder level? | Product/SKU + Store exception history | Recurring Exception Rate | Systemic-issue identification — **future-state**, depends on Product/SKU + Store IDs (Phase 6, DQ-004) |

---

## Summary: What Ships Today vs. What Waits on Future-State Data

| Ships with current data | Waits on future-state Product/SKU, Store ID, or exception log |
|---|---|
| All of Page 1, 2, 3 | Open Exceptions KPI card |
| Below-Reorder-Level Rate by Category/City/Channel (Page 4) | Open Exception Aging |
| Category × City heatmap (Page 4) | Recurring Exceptions table |
| | Store / Product-SKU filters |

This split gives RetailCo a fully functional Page 1–4 dashboard from day one, with a clear, honest roadmap for the exception-lifecycle features that depend on data this project confirmed doesn't exist yet (Phase 6, Phase 11.12).

---

**Next step:** SQL Business Analysis and Excel BA Analysis — the queries and workbook techniques that would produce the figures feeding every visual above.
