# Business Performance Analysis — RetailCo (2024)

**Status:** Phase 7 — Business Performance Analysis
**All figures below are DATA EVIDENCE**, computed directly from the 100,000-row 2024 dataset. Interpretation notes are explicitly labeled **ANALYST INTERPRETATION**.

---

## Headline Numbers

| Metric | Value |
|---|---|
| Total Revenue | ₹39,335,134.98 |
| Total Units Sold | 299,829 |
| Total Transactions | 100,000 |
| Total Cost | ₹31,461,449.33 |
| Total Gross Margin | ₹7,873,685.66 |
| Overall Margin % (Margin ÷ Revenue) | 20.02% |
| Average Transaction Value | ₹393.35 |

---

## 1. Sales Analysis

### Revenue by Category
| Category | Revenue | Revenue Share | Units |
|---|---|---|---|
| Fruits | 4,985,417.90 | 12.7% | 38,195 |
| Grocery | 4,947,363.17 | 12.6% | 37,400 |
| Snacks | 4,942,554.66 | 12.6% | 37,418 |
| Beverages | 4,941,030.17 | 12.6% | 37,863 |
| Home Care | 4,931,420.48 | 12.5% | 37,790 |
| Vegetables | 4,915,301.88 | 12.5% | 37,381 |
| Personal Care | 4,884,187.45 | 12.4% | 37,012 |
| Dairy | 4,787,859.29 | 12.2% | 36,770 |

### Revenue by Brand
| Brand | Revenue | Revenue Share |
|---|---|---|
| ITC | 5,019,512.90 | 12.8% |
| HUL | 4,967,523.37 | 12.6% |
| Britannia | 4,942,030.33 | 12.6% |
| Nestle | 4,941,904.04 | 12.6% |
| Amul | 4,937,874.07 | 12.6% |
| Tata | 4,868,135.99 | 12.4% |
| PepsiCo | 4,853,369.56 | 12.3% |
| Parle | 4,804,784.72 | 12.2% |

### Revenue by City
| City | Revenue | Avg Transaction Value |
|---|---|---|
| Kolkata | 4,999,465.15 | 394.25 |
| Delhi | 4,985,262.21 | 394.12 |
| Hyderabad | 4,950,786.97 | 397.97 |
| Chennai | 4,900,659.09 | 393.09 |
| Pune | 4,899,356.64 | 395.01 |
| Mumbai | 4,897,600.18 | 392.06 |
| Ahmedabad | 4,877,774.67 | 392.23 |
| Bengaluru | 4,824,230.07 | 388.05 |

### Revenue by Store Format
| Store Format | Revenue | Revenue Share | Avg Transaction Value |
|---|---|---|---|
| Hyper | 13,225,626.24 | 33.6% | 395.47 |
| Super | 13,099,594.73 | 33.3% | 394.06 |
| Express | 13,009,914.01 | 33.1% | 390.52 |

### Revenue by Channel
| Channel | Revenue | Revenue Share | Avg Transaction Value |
|---|---|---|---|
| Omnichannel | 13,162,992.40 | 33.5% | 394.30 |
| Online | 13,117,659.01 | 33.4% | 394.46 |
| Offline | 13,054,483.57 | 33.2% | 391.30 |

### Monthly Revenue Trend (2024)
| Month | Revenue | Transactions |
|---|---|---|
| Jan | 3,365,380.56 | 8,514 |
| Feb | 3,140,896.09 | 7,944 |
| Mar | 3,350,248.06 | 8,474 |
| Apr | 3,280,835.98 | 8,287 |
| May | 3,346,824.18 | 8,468 |
| Jun | 3,175,117.85 | 8,095 |
| Jul | 3,346,063.43 | 8,497 |
| Aug | 3,375,015.06 | 8,524 |
| Sep | 3,211,407.61 | 8,316 |
| Oct | 3,330,184.25 | 8,522 |
| Nov | 3,192,325.89 | 8,088 |
| Dec | 3,220,836.04 | 8,271 |

### Loyalty Comparison
| Loyalty_Flag | Revenue | Transactions | Avg Txn Value | Margin % |
|---|---|---|---|---|
| Loyalty member (1) | 11,753,652.55 | 29,720 | 395.48 | 20.03% |
| Not loyalty (0) | 27,581,482.44 | 70,280 | 392.45 | 20.02% |

**ANALYST INTERPRETATION — Sales:** Revenue is **remarkably evenly distributed** across every dimension tested. The coefficient of variation across categories is 1.2%, across brands 1.4%, across cities 1.2%, across store formats 0.8%, and across channels just 0.4% — no category, brand, city, format, or channel meaningfully outperforms or underperforms the others. Average transaction value is similarly flat (₹388–₹398 across all cuts). The monthly trend shows mild fluctuation (₹3.14M–₹3.38M) with no strong seasonal pattern. Loyalty members and non-members show essentially identical spending behavior. **This is worth stating plainly: the data does not support a narrative of "winning" or "losing" segments** — RetailCo's 2024 performance, as captured in this dataset, looks operationally uniform across markets and merchandise lines.

---

## 2. Profitability Analysis

### Margin % by Category
| Category | Margin % (revenue-weighted) |
|---|---|
| Grocery | 20.14% |
| Personal Care | 20.10% |
| Snacks | 20.07% |
| Vegetables | 20.05% |
| Dairy | 20.02% |
| Fruits | 19.92% |
| Home Care | 19.92% |
| Beverages | 19.90% |

### Margin % by Brand
| Brand | Margin % (revenue-weighted) |
|---|---|
| Amul | 20.18% |
| Nestle | 20.06% |
| Tata | 20.04% |
| Parle | 20.03% |
| ITC | 20.03% |
| HUL | 20.00% |
| PepsiCo | 19.92% |
| Britannia | 19.87% |

### High-Revenue / Low-Margin and Low-Revenue / High-Margin Products
**ANALYST INTERPRETATION — this is the most important finding of this phase.** At Category level, margin % spans only **19.90%–20.14%** (a 0.25-percentage-point range). At Brand level it spans **19.87%–20.18%** (0.31 points). Neither range is large enough to represent a genuine "high-revenue-but-weak-margin" business problem — this is well within normal noise, not a pattern a business would act on.

At the more granular Category×Brand level (64 combinations, ~1,500–1,650 transactions each), the spread widens slightly to 19.44%–20.49% (about 1.05 points):
- **Highest margin %:** Vegetables × HUL (20.49%), Grocery × Amul (20.48%), Snacks × Amul (20.45%)
- **Lowest margin %:** Home Care × Britannia (19.44%), Beverages × Britannia (19.61%), Fruits × HUL (19.69%)

Even at this finer cut, no combination is a high-revenue/low-margin outlier — the lowest-margin combinations are not simultaneously the highest-revenue ones. **Conclusion: the stakeholder concern from Phase 2 ("some products generate strong revenue but weak margins") is not supported by this dataset at any level of granularity available.** This is reported honestly rather than manufactured — it is a legitimate, useful finding in its own right (it tells management that margin is *not* where their attention is best spent, based on this data).

---

## 3. Inventory Analysis

### Overview
| Metric | Value |
|---|---|
| Stock_On_Hand range | 50–499 units (never 0 — no literal stockouts recorded) |
| Reorder_Level range | 20–79 units |
| Transactions with Stock_On_Hand < Reorder_Level | 1,624 of 100,000 (**1.62%**) |
| Transactions in a "near reorder" band (Stock_On_Hand within 25% above Reorder_Level) | 2,086 (2.09%) |
| Combined "attention zone" (below + near reorder) | 3,710 (**3.71%**) |
| Average supplier lead time | 8.52 days |

*(Reminder from Phase 1: Stock_On_Hand/Reorder_Level are transaction-level snapshots, not a running per-SKU balance — figures below describe the share of transactions recorded in a below-reorder state, not the status of a specific product.)*

### % of Transactions Below Reorder Level, by Category
| Category | % Below Reorder |
|---|---|
| Dairy | 1.74% |
| Grocery | 1.70% |
| Snacks | 1.69% |
| Beverages | 1.68% |
| Personal Care | 1.64% |
| Fruits | 1.53% |
| Vegetables | 1.51% |
| Home Care | 1.50% |

### % of Transactions Below Reorder Level, by City
| City | % Below Reorder |
|---|---|
| Mumbai | 1.75% |
| Kolkata | 1.75% |
| Chennai | 1.74% |
| Hyderabad | 1.65% |
| Pune | 1.60% |
| Delhi | 1.53% |
| Bengaluru | 1.53% |
| Ahmedabad | 1.43% |

### Highest-Risk Category × City Combinations
| Category | City | % Below Reorder | Transactions |
|---|---|---|---|
| Dairy | Mumbai | 2.47% | 1,582 |
| Snacks | Chennai | 2.45% | 1,550 |
| Snacks | Pune | 2.21% | 1,537 |
| Personal Care | Mumbai | 2.14% | 1,543 |
| Beverages | Mumbai | 2.07% | 1,544 |

### Supplier Lead Time vs. Below-Reorder Rate
| Lead Time Band | % Below Reorder |
|---|---|
| 3–5 days | 1.64% |
| 6–8 days | 1.54% |
| 9–11 days | 1.70% |
| 12–14 days | 1.62% |

**ANALYST INTERPRETATION — Inventory:** Unlike margin, inventory shows a small but somewhat more real pattern: below-reorder-level rate ranges from **1.43% (Ahmedabad) to 1.75% (Mumbai/Kolkata)** by city — about a 20–25% relative difference between the lowest and highest — and **1.50% (Home Care) to 1.74% (Dairy)** by category. **Dairy in Mumbai (2.47%) and Snacks in Chennai (2.45%)** stand out as the combinations most often recorded below reorder level. That said, these are still modest percentages in absolute terms (no city or category exceeds ~2.5%), so this should be framed as a **monitoring priority, not an urgent crisis**. Correlation between supplier lead time and below-reorder rate is effectively zero (0.0005) — **lead time does not explain inventory risk in this dataset**, which is a useful negative finding: any future root-cause investigation should look elsewhere (e.g., demand variability, reorder-level calibration) rather than assuming slow suppliers are the driver.

No transactions show Stock_On_Hand = 0 anywhere in the dataset, so **the word "stockout" is not used anywhere in this project** — only "below reorder level," which is what the data actually supports.

---

## Summary: Which Phase 2 Concerns Does the Evidence Support?

| Stakeholder Concern (Phase 2) | Supported by Evidence? |
|---|---|
| Lack of consolidated cross-dimensional visibility | Not testable from data alone — this is about *reporting tooling*, addressed later via requirements, not performance analysis |
| High-revenue / low-margin products exist | **Not supported.** Margin % is flat (within ~0.3 points) at category and brand level; even at the finest available cut, no high-revenue/low-margin pattern emerges |
| Inventory may be at risk in some categories/locations | **Modestly supported.** Real but small variation exists by category and city (1.43%–2.47%), concentrated in Dairy/Mumbai and Snacks/Chennai |

This matters for every phase that follows: the strongest, most evidence-backed problem to carry into Root Cause Analysis, Requirements, and the Dashboard is **inventory monitoring by category and city** — not a margin-optimization story the data doesn't actually tell.

---

**Next step:** Phase 8 — KPI Framework, followed by Phase 9 — Root Cause Analysis (focused on the inventory-risk finding above).
