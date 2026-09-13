# Executive Recommendation — RetailCo Inventory Exception Management

*Simulated portfolio case study — RetailCo is a fictional company; no real stakeholders, employment, or implementation are claimed.*

---

### Problem
RetailCo's 2024 transaction data was analyzed to test stakeholder concerns about sales visibility, product margin, and inventory risk. Management currently has no consolidated, evidence-based view of where — if anywhere — these concerns are real.

### Evidence
- **Margin is not the problem.** Margin % is uniform across every category (19.9%–20.1%) and brand (19.87%–20.18%) — the original "high-revenue/low-margin products" concern is not supported at any level of granularity tested.
- **Inventory is the real, if modest, signal.** 1.62% of 100,000 transactions (1,624) are recorded with stock below reorder level. Category and city variation exists descriptively (1.43%–1.75%) but is **not statistically significant** (chi-square p = 0.675 and p = 0.336); a Pareto check found **no concentration** — this is a diffuse pattern, not a few "bad" segments.
- **Supplier lead time is ruled out** as a driver (correlation ≈ 0.0005, flat across all lead-time bands).
- **A real structural gap exists:** no persistent Product/SKU or Store ID in the data, so recurring exceptions at the same item/location cannot currently be tracked.

### Root Cause
The dataset can identify **where** below-reorder events occur but not **why** — no replenishment timestamps, demand-forecast, or stock-audit fields exist. What is confirmed is a **process gap**: no evidenced automated detection, ownership, or historical tracking exists today. Establishing the true operational cause requires stakeholder validation and additional data, not further querying of this dataset.

### Recommended Solution
**Power BI dashboard** for KPI/reporting, paired with a **lightweight structured exception tracker** for ownership, status, and escalation (a pure BI tool doesn't natively provide workflow). Selected via a weighted decision matrix against Excel-only (3.55) and a custom-built application (3.05) — Power BI scored highest (3.60), and a full custom build was rejected as disproportionate to the confirmed problem size.

### Expected Benefits *(qualitative — no realized results are claimed)*
Expected to improve inventory exception visibility, ownership, and historical tracking; expected to give management a single, consistent KPI view instead of fragmented reporting; expected to enable recurring-issue detection once Product/SKU and Store IDs exist.

### Risks
- **Data dependency:** recurring-exception tracking and several KPIs depend on future-state Product/SKU and Store identifiers that don't exist yet.
- **Unvalidated thresholds:** escalation windows, alert priorities, and NFR targets are proposed placeholders pending stakeholder sign-off.
- **Adoption risk:** the exception workflow introduces new steps (ownership, status updates) for users with no prior structured process to compare it to.

### Next Steps
1. Validate proposed business rules and thresholds (BRL-01–06) with real stakeholders.
2. Confirm a plan for capturing Product/SKU and Store IDs.
3. Execute the 12 UAT test cases already defined (`testing/uat-test-cases.xlsx`).
4. Roll out Power BI reporting first; add the exception tracker once ownership/workflow rules are confirmed.
