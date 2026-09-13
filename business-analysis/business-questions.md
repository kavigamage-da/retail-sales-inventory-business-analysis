# Business Questions — RetailCo

**Purpose:** Before running the performance analysis (Phase 6–7), these are the questions a BA would take to management up front. Only questions the dataset can actually answer are included — no question here requires a field that Phase 1 found missing (e.g., no promotion, returns, or prior-year questions).

| # | Business Question | Data Needed | KPI / Analysis | Decision Supported |
|---|---|---|---|---|
| 1 | Which categories and brands generate the most revenue? | Category, Brand, Revenue | Revenue by Category / Brand | Merchandising & assortment focus |
| 2 | Which categories and brands have the strongest margin %? | Category, Brand, Margin_% | Margin % by Category / Brand | Pricing and category strategy |
| 3 | Are there products with high revenue but comparatively low margin %? | Category, Brand, Revenue, Margin_% | Revenue vs. Margin_% cross-analysis | Pricing / promotion prioritization |
| 4 | Which cities and store formats perform best on revenue and margin? | City, Store_Format, Revenue, Margin | Revenue & Margin by City / Format | Store investment & format decisions |
| 5 | Which channel — Online, Offline, or Omnichannel — is most profitable? | Channel, Revenue, Margin | Revenue & Margin by Channel | Channel investment priority |
| 6 | What share of transactions show stock below reorder level, and where? | Stock_On_Hand, Reorder_Level, Category, City | % of transactions below reorder level, by Category / City | Inventory attention / replenishment priority |
| 7 | How does supplier lead time relate to inventory risk? | Lead_Time_Days, Stock_On_Hand, Reorder_Level | Lead time vs. below-reorder-level rate | Supplier / replenishment policy discussion |
| 8 | Do loyalty customers generate different revenue or margin patterns than non-loyalty customers? | Loyalty_Flag, Revenue, Margin | Revenue & Margin by Loyalty_Flag | Loyalty program investment case |
| 9 | How does revenue trend month-to-month across 2024? | Invoice_Date, Revenue | Monthly revenue trend | Seasonal planning, monitoring cadence |
| 10 | What is the average transaction value, and does it vary by city, channel, or format? | Revenue, Units, City, Channel, Store_Format | Average Transaction Value, segmented | Sales performance benchmarking |
| 11 | Which payment modes are most used, and does usage vary by channel? | Payment_Mode, Channel | Payment mix by Channel | Secondary / operational context |
| 12 | Are there age- or gender-based differences in purchasing patterns? | Customer_Age, Customer_Gender, Revenue | Segmentation analysis | Marketing/segmentation discussion — **caveat: Customer_Age is 40% missing, Customer_Gender 5% missing, so this covers a partial sample only** |

**Questions deliberately excluded** (dataset cannot support them): year-over-year growth (single year of data only), promotion/markdown impact (no promotion field), returns or shrink analysis (no returns field), true stockout rate (Stock_On_Hand never reaches 0 in this data), and basket-level analysis (each row is a single-line transaction, not a multi-item basket).

---

**Next step:** Phase 6 — Data Quality Analysis, followed by Phase 7 — Business Performance Analysis (this is where Questions 1–12 above actually get answered against the data).
