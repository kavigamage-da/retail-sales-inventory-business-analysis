-- ============================================================================
-- RetailCo — SQL Business Analysis
-- Inventory Exception & Sales Performance Queries
-- ============================================================================
-- Assumed table: sales_transactions
-- Columns match the source dataset exactly, EXCEPT: the source CSV column
-- "Margin_%" is not a valid unquoted SQL identifier (percent sign). Rather
-- than rename/quote it, every query below computes Margin % directly as
-- SUM(Margin)/SUM(Revenue) — the revenue-weighted definition standardized
-- in Phase 8 (20.02% overall), not the raw column's simple average (19.34%).
--
-- Dialect note: date functions vary by engine. Queries use EXTRACT(...FROM...)
-- (PostgreSQL/ANSI-style). For SQLite, replace with strftime('%m', Invoice_Date)
-- / strftime('%Y-%m', Invoice_Date); for MySQL, use MONTH(Invoice_Date) /
-- DATE_FORMAT(Invoice_Date, '%Y-%m').
--
-- No column below was invented — all 21 fields are exactly as documented in
-- Phase 1's Data Dictionary (data/README.md).
-- ============================================================================


-- ----------------------------------------------------------------------------
-- Q1. Business Question: What was RetailCo's total 2024 revenue?
-- Expected Business Interpretation: Confirms the top-line figure established
-- in Phase 7 (~₹39.33M) — a sanity-check query before anything more complex.
-- ----------------------------------------------------------------------------
SELECT
    SUM(Revenue) AS Total_Revenue,
    SUM(Units)   AS Total_Units,
    COUNT(*)     AS Total_Transactions
FROM sales_transactions;


-- ----------------------------------------------------------------------------
-- Q2. Business Question: Which categories generate the most revenue?
-- Expected Business Interpretation: Per Phase 7, expect a near-even spread
-- (Fruits highest ~₹4.99M, Dairy lowest ~₹4.79M, ~12% share each) — no single
-- category dominates.
-- ----------------------------------------------------------------------------
SELECT
    Category,
    SUM(Revenue) AS Revenue,
    SUM(Units)   AS Units,
    COUNT(*)     AS Transactions
FROM sales_transactions
GROUP BY Category
ORDER BY Revenue DESC;


-- ----------------------------------------------------------------------------
-- Q3. Business Question: How does revenue trend month-to-month across 2024?
-- Expected Business Interpretation: Mild fluctuation (~₹3.14M–₹3.38M per
-- month, Phase 7) with no strong seasonal pattern.
-- ----------------------------------------------------------------------------
SELECT
    EXTRACT(MONTH FROM Invoice_Date) AS Month_Number,
    SUM(Revenue)  AS Monthly_Revenue,
    COUNT(*)      AS Transactions
FROM sales_transactions
GROUP BY Month_Number
ORDER BY Month_Number;


-- ----------------------------------------------------------------------------
-- Q4. Business Question: Which Category + Brand combinations generate the
-- most revenue? (No Product/SKU ID exists — Category+Brand is the finest
-- "product" grain available per Phase 1.)
-- Expected Business Interpretation: Top combinations should cluster close
-- together — Phase 7 found only a ~15% relative spread at this grain, mostly
-- attributable to smaller per-cell sample sizes rather than a real driver.
-- ----------------------------------------------------------------------------
SELECT
    Category,
    Brand,
    SUM(Revenue) AS Revenue,
    COUNT(*)     AS Transactions
FROM sales_transactions
GROUP BY Category, Brand
ORDER BY Revenue DESC
LIMIT 10;


-- ----------------------------------------------------------------------------
-- Q5. Business Question: Which Category + Brand combinations have the
-- lowest margin %?
-- Expected Business Interpretation: Per Phase 7, expect Home Care x Britannia
-- lowest (~19.44%) — a narrow range, not a margin crisis at any combination.
-- ----------------------------------------------------------------------------
SELECT
    Category,
    Brand,
    SUM(Revenue)                    AS Revenue,
    SUM(Margin)                     AS Margin,
    SUM(Margin) / SUM(Revenue)      AS Margin_Pct
FROM sales_transactions
GROUP BY Category, Brand
HAVING SUM(Revenue) > 0
ORDER BY Margin_Pct ASC
LIMIT 10;


-- ----------------------------------------------------------------------------
-- Q6. Business Question: Are any categories simultaneously high-revenue AND
-- low-margin, or vice versa? (Directly tests the original Phase 2 stakeholder
-- concern using ranks rather than eyeballing two separate sorted lists.)
-- Expected Business Interpretation: Per Phase 7, no category should show both
-- a top-3 revenue rank and a bottom-3 margin rank at the same time.
-- ----------------------------------------------------------------------------
SELECT
    Category,
    SUM(Revenue) AS Revenue,
    RANK() OVER (ORDER BY SUM(Revenue) DESC)                      AS Revenue_Rank,
    SUM(Margin) / SUM(Revenue) AS Margin_Pct,
    RANK() OVER (ORDER BY SUM(Margin) / SUM(Revenue) ASC)         AS Margin_Pct_Rank_Ascending
FROM sales_transactions
GROUP BY Category
ORDER BY Revenue_Rank;


-- ----------------------------------------------------------------------------
-- Q7. Business Question: Which cities perform best on revenue and average
-- transaction value?
-- Expected Business Interpretation: Near-even across all 8 cities (Phase 7);
-- ATV stays within ₹388–₹398 regardless of city.
-- ----------------------------------------------------------------------------
SELECT
    City,
    SUM(Revenue)              AS Revenue,
    COUNT(*)                  AS Transactions,
    SUM(Revenue) / COUNT(*)   AS Avg_Transaction_Value
FROM sales_transactions
GROUP BY City
ORDER BY Revenue DESC;


-- ----------------------------------------------------------------------------
-- Q8. Business Question: Which channel (Online/Offline/Omnichannel) performs
-- best on revenue and margin?
-- Expected Business Interpretation: Near-even revenue split (~33% each,
-- Phase 7); margin % also flat across channels.
-- ----------------------------------------------------------------------------
SELECT
    Channel,
    SUM(Revenue)                 AS Revenue,
    SUM(Margin) / SUM(Revenue)   AS Margin_Pct,
    COUNT(*)                     AS Transactions
FROM sales_transactions
GROUP BY Channel
ORDER BY Revenue DESC;


-- ----------------------------------------------------------------------------
-- Q9. Business Question: What share of transactions are recorded with stock
-- below the reorder level? (The core inventory KPI, Phase 8.)
-- Expected Business Interpretation: ~1.62% overall. Note: Stock_On_Hand never
-- reaches 0 in this dataset, so this is deliberately NOT called a "stockout
-- rate" anywhere in this project.
-- ----------------------------------------------------------------------------
SELECT
    COUNT(*)                                                            AS Total_Transactions,
    SUM(CASE WHEN Stock_On_Hand < Reorder_Level THEN 1 ELSE 0 END)      AS Below_Reorder_Count,
    CAST(SUM(CASE WHEN Stock_On_Hand < Reorder_Level THEN 1 ELSE 0 END) AS FLOAT)
        / COUNT(*)                                                      AS Below_Reorder_Rate
FROM sales_transactions;


-- ----------------------------------------------------------------------------
-- Q10. Business Question: Which Category + City combinations have the
-- highest below-reorder-level rate, and are they a good starting point for
-- monitoring?
-- Expected Business Interpretation: Surfaces Dairy/Mumbai (~2.47%) and
-- Snacks/Chennai (~2.45%) at the top. IMPORTANT: Phase 9's chi-square test
-- across all 64 Category x City combinations was NOT significant (p=0.383),
-- and a Pareto check found no real concentration. Treat this query's output
-- as an operational starting point for monitoring — not proof of a hotspot.
-- ----------------------------------------------------------------------------
SELECT
    Category,
    City,
    COUNT(*)                                                            AS Transactions,
    SUM(CASE WHEN Stock_On_Hand < Reorder_Level THEN 1 ELSE 0 END)      AS Below_Reorder_Count,
    CAST(SUM(CASE WHEN Stock_On_Hand < Reorder_Level THEN 1 ELSE 0 END) AS FLOAT)
        / COUNT(*)                                                      AS Below_Reorder_Rate
FROM sales_transactions
GROUP BY Category, City
ORDER BY Below_Reorder_Rate DESC
LIMIT 10;


-- ----------------------------------------------------------------------------
-- Q11. Business Question: Does supplier lead time relate to below-reorder-
-- level inventory?
-- Expected Business Interpretation: Per Phase 9, expect a FLAT rate across
-- all lead-time bands (~1.5%-1.7%) — lead time is a ruled-out factor
-- (correlation ~0.0005), not a driver, in this dataset.
-- ----------------------------------------------------------------------------
SELECT
    CASE
        WHEN Lead_Time_Days BETWEEN 3  AND 5  THEN '3-5 days'
        WHEN Lead_Time_Days BETWEEN 6  AND 8  THEN '6-8 days'
        WHEN Lead_Time_Days BETWEEN 9  AND 11 THEN '9-11 days'
        WHEN Lead_Time_Days BETWEEN 12 AND 14 THEN '12-14 days'
    END AS Lead_Time_Band,
    COUNT(*)                                                            AS Transactions,
    SUM(CASE WHEN Stock_On_Hand < Reorder_Level THEN 1 ELSE 0 END)      AS Below_Reorder_Count,
    CAST(SUM(CASE WHEN Stock_On_Hand < Reorder_Level THEN 1 ELSE 0 END) AS FLOAT)
        / COUNT(*)                                                      AS Below_Reorder_Rate
FROM sales_transactions
GROUP BY Lead_Time_Band
ORDER BY Lead_Time_Band;


-- ----------------------------------------------------------------------------
-- Q12. Business Question: Do loyalty members generate different revenue or
-- margin patterns than non-loyalty customers?
-- Expected Business Interpretation: Per Phase 7, essentially identical
-- (ATV ~₹395 loyalty vs. ~₹392 non-loyalty; margin % ~20.03% vs ~20.02%).
-- ----------------------------------------------------------------------------
SELECT
    Loyalty_Flag,
    SUM(Revenue)                 AS Revenue,
    COUNT(*)                     AS Transactions,
    SUM(Revenue) / COUNT(*)      AS Avg_Transaction_Value,
    SUM(Margin) / SUM(Revenue)   AS Margin_Pct
FROM sales_transactions
GROUP BY Loyalty_Flag;


-- ----------------------------------------------------------------------------
-- Q13. Business Question: What is 2024 revenue growth vs. the prior year?
-- Expected Business Interpretation: NOT AVAILABLE — only one calendar year
-- (2024) exists in this dataset (Phase 1). This query is included to
-- document what CANNOT be answered, not to compute a number.
-- ----------------------------------------------------------------------------
-- Not available in the provided dataset — no prior-year data exists to
-- compare against. No query can produce this figure from this table alone.
