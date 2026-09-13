# Data Discovery Report — RetailCo FMCG Sales, Customer & Inventory Dataset (2024)

**Project:** Retail Sales & Inventory Optimization — End-to-End Business Analysis Case Study
**Company:** RetailCo *(fictional company created for this portfolio case study — not a real employer or client)*
**Status:** Phase 1 — Data Discovery
**Date prepared:** September 2026

> **Dataset note:** The source file is a **synthetic / simulated** dataset (per its accompanying overview document, built for analytics teaching and portfolio purposes). It does not represent a real company, and no real stakeholders, transactions, or customers are involved. All figures in this report are **DATA EVIDENCE** — computed directly from the file — unless explicitly marked otherwise.

---

## 1. File Overview

| Item | Value |
|---|---|
| Source archive | `archive.zip` |
| Data file | `Indian FMCG Retail Sales  Customer  Inventory (2024).csv` |
| Supporting doc | `Retail FMCG Sales Dataset - Overview.docx` (author-provided dataset overview) |
| File size | 20.46 MB |
| Rows | 100,000 |
| Columns | 21 |
| Grain (what one row represents) | One sales transaction **line item** — one product (Category × Brand), one quantity, one date/time, one store/channel. There is no multi-line "basket" structure; this matches a limitation the source overview document itself discloses ("single-line invoices restrict basket analysis"). |
| Date range | 2024-01-01 00:00:00 → 2024-12-30 23:57:00 (covers effectively the full 2024 calendar year; timestamps include time-of-day, not just date) |
| Records per month | Roughly even, from 7,944 (Feb) to 8,524 (Aug) — no missing months, no obvious collection gaps |

---

## 2. Column Names & Data Types

| # | Column | Data Type |
|---|---|---|
| 1 | Invoice_ID | Integer |
| 2 | Invoice_Date | Text → parses cleanly to datetime |
| 3 | City | Text (categorical) |
| 4 | Store_Format | Text (categorical) |
| 5 | Category | Text (categorical) |
| 6 | Brand | Text (categorical) |
| 7 | Channel | Text (categorical) |
| 8 | Payment_Mode | Text (categorical) |
| 9 | Units | Integer |
| 10 | Cost_Price | Decimal |
| 11 | Selling_Price | Decimal |
| 12 | Revenue | Decimal |
| 13 | Cost | Decimal |
| 14 | Margin | Decimal |
| 15 | Margin_% | Decimal |
| 16 | Stock_On_Hand | Integer |
| 17 | Reorder_Level | Integer |
| 18 | Lead_Time_Days | Integer |
| 19 | Customer_Age | Decimal (missing for many rows) |
| 20 | Customer_Gender | Text (categorical, missing for some rows) |
| 21 | Loyalty_Flag | Integer (0/1) |

**Numerical fields:** Units, Cost_Price, Selling_Price, Revenue, Cost, Margin, Margin_%, Stock_On_Hand, Reorder_Level, Lead_Time_Days, Customer_Age, Loyalty_Flag (binary)
**Categorical fields:** City, Store_Format, Category, Brand, Channel, Payment_Mode, Customer_Gender
**Identifier field:** Invoice_ID
**Date field:** Invoice_Date

---

## 3. Missing Values

| Column | Missing Count | Missing % |
|---|---|---|
| Customer_Age | 40,081 | 40.08% |
| Customer_Gender | 5,048 | 5.05% |
| All other 19 columns | 0 | 0% |

No missingness was found anywhere outside these two customer-demographic fields.

---

## 4. Duplicate Records

- **Fully duplicate rows:** 0
- **Duplicate Invoice_ID values:** 62 IDs are reused across 124 rows. Checked individually, each pair of "duplicate" rows has a **different date, city, and product** — these are not repeated transactions.
- **ANALYST INTERPRETATION:** Invoice_ID is an 8-digit number (range 10,001,195–99,996,325). With 100,000 rows drawn from an ~90-million-value space, ~62 collisions is consistent with random ID generation, not a system error. **Practical implication: Invoice_ID should not be treated as a guaranteed-unique primary key** for any downstream SQL/Excel work (e.g., joins or COUNT DISTINCT logic) without acknowledging this.

---

## 5. Categorical Field Distributions

| Field | Unique Values | Distribution |
|---|---|---|
| City | 8 | Kolkata, Delhi, Mumbai, Chennai, Hyderabad, Ahmedabad, Bengaluru, Pune — each 12,403–12,681 records (near-even) |
| Store_Format | 3 | Hyper 33,443 · Express 33,314 · Super 33,243 (near-even) |
| Category | 8 | Fruits, Home Care, Beverages, Snacks, Vegetables, Grocery, Personal Care, Dairy — each 12,270–12,708 records (near-even) |
| Brand | 8 | ITC, HUL, Nestle, Amul, PepsiCo, Britannia, Tata, Parle — each 12,233–12,649 records (near-even) |
| Channel | 3 | Omnichannel 33,383 · Offline 33,362 · Online 33,255 (near-even) |
| Payment_Mode | 4 | UPI 25,236 · Card 25,127 · Wallet 24,888 · Cash 24,749 (near-even) |
| Customer_Gender | 3 (+missing) | M 44,920 · F 44,905 · O 5,127 · missing 5,048 |
| Loyalty_Flag | 2 | Not loyalty (0) 70,280 (70.3%) · Loyalty (1) 29,720 (29.7%) |

No whitespace or casing inconsistencies were found in any categorical field (checked programmatically).

**ANALYST INTERPRETATION:** Every Brand appears under every Category (64 of 64 possible combinations exist) — e.g., all 8 brands show up in "Home Care" as well as "Beverages." In a real FMCG catalog, brands are usually category-specialists (a dairy brand wouldn't typically sell home-care products). This is a simplification of the simulated data, not a genuine business finding, and is worth acknowledging as a dataset characteristic rather than a real cross-category expansion strategy.

---

## 6. Numerical Field Summary

| Field | Min | Mean | Max | Negative/Zero values |
|---|---|---|---|---|
| Units | 1 | 3.00 | 5 | None |
| Cost_Price (₹) | 10.00 | 104.86 | 200.00 | None |
| Selling_Price (₹) | 10.58 | 131.11 | 289.70 | None |
| Revenue (₹) | 10.65 | 393.35 | 1,443.13 | None |
| Cost (₹) | 10.00 | 314.61 | 999.99 | None |
| Margin (₹) | 0.56 | 78.74 | 447.21 | None |
| Margin_% | 5% | 19.34% | 31% | None |
| Stock_On_Hand | 50 | 274.16 | 499 | None (never 0) |
| Reorder_Level | 20 | 49.47 | 79 | None |
| Lead_Time_Days | 3 | 8.52 | 14 | None |
| Customer_Age | 18 | 41.08 | 64 | None (59,919 non-missing values) |

No negative, zero, or otherwise impossible values were found in any numeric field. Selling_Price is greater than Cost_Price in 100% of rows (no loss-making line items).

---

## 7. Field Relationships (Consistency Checks)

These formulas were tested row-by-row across all 100,000 records:

| Relationship | Result |
|---|---|
| Revenue = Units × Selling_Price | Holds exactly (differences only at floating-point rounding level, <0.0000000001) |
| Cost = Units × Cost_Price | Holds exactly |
| Margin = Revenue − Cost | Holds exactly |
| Margin_% = Margin ÷ Revenue | Holds exactly |

**DATA EVIDENCE:** The financial fields are internally consistent — there are no calculation errors between Units, prices, Revenue, Cost, Margin, and Margin_%. This is a clean foundation for Phase 7 financial analysis.

**ANALYST INTERPRETATION — Inventory fields:** Stock_On_Hand and Reorder_Level do **not** vary systematically by Category+Brand, or by City+Store_Format (the spread within each group is essentially identical to the spread across the whole dataset). There is also no Product/SKU ID or Store ID field. This indicates Stock_On_Hand and Reorder_Level behave as an **independent value attached to each transaction line**, not a running, trackable inventory balance for a specific product at a specific location. Practical implication for later phases: inventory analysis should be framed as *"% of transactions recorded with stock below reorder level, by category/city"* rather than *"current stock position of Product X"* — the dataset does not support the latter.

**DATA EVIDENCE — on "stockouts":** Stock_On_Hand is never 0 anywhere in the dataset, and there is no separate stockout/fulfillment-failure field. Rows where Stock_On_Hand < Reorder_Level: **1,624 of 100,000 (1.62%)**. Per the project's own analysis rule, this will be labeled **"transactions recorded below reorder level,"** not "stockouts," since the data does not evidence actual stockouts.

---

## 8. Data Dictionary

| Field | Description | Data Type | Business Meaning | BA Relevance |
|---|---|---|---|---|
| Invoice_ID | Numeric transaction identifier | Integer | Identifies a transaction line | Not a guaranteed-unique key (62 collisions) — flag in any data-governance discussion |
| Invoice_Date | Date & time of the transaction | Datetime | When the sale occurred | Basis for all trend/seasonality analysis |
| City | City where the sale took place | Categorical (8) | Geographic market | Store/city performance comparison |
| Store_Format | Store type: Hyper / Super / Express | Categorical (3) | Store size/format | Format-level performance & inventory analysis |
| Category | Product category | Categorical (8) | Product grouping | Category-level revenue/margin analysis |
| Brand | Product brand | Categorical (8) | Brand sold | Brand-level profitability analysis |
| Channel | Online / Offline / Omnichannel | Categorical (3) | Sales channel | Channel performance comparison |
| Payment_Mode | UPI / Card / Wallet / Cash | Categorical (4) | Payment method used | Secondary — payment mix context |
| Units | Quantity sold in the line | Integer (1–5) | Volume of the transaction | Price–volume decomposition |
| Cost_Price | Per-unit cost | Decimal (₹) | Retailer's unit cost | Feeds Cost/Margin |
| Selling_Price | Per-unit selling price | Decimal (₹) | Price charged to customer | Feeds Revenue |
| Revenue | Units × Selling_Price | Decimal (₹) | Sales value of the line | Core sales KPI |
| Cost | Units × Cost_Price | Decimal (₹) | Cost of the line | Core cost KPI |
| Margin | Revenue − Cost | Decimal (₹) | Gross profit of the line | Core profitability KPI |
| Margin_% | Margin ÷ Revenue | Decimal (%) | Profitability rate | Category/brand margin comparison |
| Stock_On_Hand | Stock quantity recorded with this transaction | Integer | Inventory snapshot at transaction time | Inventory-risk analysis (transaction-level, see Section 7 caveat) |
| Reorder_Level | Reorder threshold recorded with this transaction | Integer | Replenishment trigger point | Basis for "below reorder level" flag |
| Lead_Time_Days | Supplier replenishment lead time | Integer (3–14) | Days to restock | Inventory responsiveness analysis |
| Customer_Age | Customer's age | Decimal (18–64), 40.08% missing | Demographic attribute | Segmentation — missingness must be disclosed wherever used |
| Customer_Gender | Customer's gender (M/F/O), 5.05% missing | Categorical | Demographic attribute | Segmentation — missingness must be disclosed wherever used |
| Loyalty_Flag | 1 = loyalty member, 0 = not | Integer (0/1) | Loyalty membership indicator | Loyalty uplift analysis |

---

## 9. Initial Data-Quality Observations (flagged here, formally assessed in Phase 6)

| # | Observation | Evidence | Severity (preliminary) |
|---|---|---|---|
| 1 | Invoice_ID is not guaranteed unique | 62 collisions across 124 rows | Low — cosmetic, doesn't affect revenue/margin totals, but relevant for any query using Invoice_ID as a key |
| 2 | High missingness in Customer_Age | 40.08% missing | Medium — limits age-based segmentation to ~60% of transactions |
| 3 | Some missingness in Customer_Gender | 5.05% missing | Low |
| 4 | No stable product/store identity for inventory fields | Within-group variance ≈ overall variance (Section 7) | Medium — constrains inventory analysis to transaction-level framing, not per-SKU stock tracking |
| 5 | No returns, wastage, or promotion fields | Confirmed absent from the 21 columns; also disclosed as a limitation in the source overview document | Low — simply narrows analysis scope; not an error |

---

## 10. Source Documentation Notes

The uploaded `Retail FMCG Sales Dataset - Overview.docx` describes this as a synthetic dataset simulating a multi-city Indian FMCG retailer across 2024, built for analytics teaching. Two figures it states were independently verified against the raw data:

- Total revenue "≈ ₹39.33 Million" → **confirmed**: ₹39,335,134.98
- "Average gross margin percentage 19.33%" → **confirmed as the simple average of per-row Margin_%**: 19.34%. Note this differs slightly from the *revenue-weighted* overall margin (Total Margin ÷ Total Revenue = 20.02%) — both are legitimate figures but answer slightly different questions, and the KPI framework in a later phase will specify which one is used.

---

**Next step:** Phase 2 — Business Context for RetailCo, built on top of the evidence captured here.
