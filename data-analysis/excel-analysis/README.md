# Excel BA Analysis — RetailCo

**File:** `retailco-excel-analysis.xlsx` (7 sheets, built on the full 100,000-row 2024 dataset)

GitHub can't render `.xlsx` content inline — open the file in Excel or LibreOffice to interact with it. Every number in it is a live formula, not a typed-in value: change a row in `Raw Data` and everything downstream recalculates.

## What's inside

| Sheet | Contents |
|---|---|
| **KPI Dashboard** | The 9 headline KPIs from Phase 8, each a formula pulling from Raw Data |
| **Raw Data** | Full 100,000-row transaction table (named Excel Table `SalesData`), with two formula-driven helper columns (`Below_Reorder_Flag`, `Month_Num`) and conditional formatting highlighting below-reorder rows |
| **Category & Brand Summary** | SUMIFS-based revenue/units/margin by Category and by Brand, with data bars and a margin % color scale |
| **City Channel Format** | SUMIFS-based revenue/transactions/ATV by City, Channel, and Store Format |
| **Inventory Monitoring** | Below-reorder rate by Category, by City, and a full Category × City cross-tab heatmap — plus an INDEX/MATCH lookup demo |
| **Monthly Trend** | Monthly revenue table with a line chart and trendline |
| **BA Notes** | Why each technique (Table, helper columns, SUMIFS, INDEX/MATCH, conditional formatting, trend chart) was the right tool for this specific problem |

## Validation

Every figure in this workbook was cross-checked against the Python analysis in `data-analysis/sql-analysis.sql` and the earlier phase documents — total revenue, category/brand margins, and below-reorder rates all match exactly (e.g., Mumbai's below-reorder rate returns 1.75% via the INDEX/MATCH lookup, matching Phase 9). One formula bug (an off-by-one cell reference on the Margin % and Below-Reorder KPI cards) was caught during this cross-check and fixed before delivery — a concrete example of why "the recalculation succeeded" and "the numbers are right" are different checks.

## Why SUMIFS instead of a native PivotTable

A real PivotTable in Excel would produce the same summaries (right-click `SalesData` → Insert PivotTable). SUMIFS/COUNTIFS were used here instead so every number stays visible as an auditable formula on the page — useful when a stakeholder asks "where does this figure come from?" See the **BA Notes** sheet for the full rationale behind every technique used.
