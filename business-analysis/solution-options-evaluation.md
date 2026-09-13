# Solution Options Evaluation — RetailCo Inventory Exception Management

**Status:** Solution Options Evaluation
**Builds on:** Phase 12 Requirements (10 BR, 23 FR, 10 NFR, 16 DR) and Phase 13 User Stories. The evaluation below is scored against those actual requirements — not assumed in advance.

---

## The Three Options

### Option A — Improved Excel-Based Reporting
Pivot-table-driven workbooks for KPI reporting, with manual tracking of exception ownership/status in a shared sheet.

### Option B — Power BI Decision-Support Dashboard
A Power BI model built on the transaction data, delivering the KPI cards, filters, and visualizations defined in Section 12.11.

### Option C — Custom Business Intelligence / Case-Management Application
A purpose-built application combining reporting and exception workflow (assignment, status, notifications) in one system.

---

## A Distinction That Matters Before Scoring

Looking at the actual requirements rather than assuming a tool: **roughly half of the Functional Requirements are reporting/analysis (FR-01–03, FR-15–21 — well suited to a BI tool), and roughly the other half are exception *workflow* (FR-04–11, FR-22–23: create a record, assign an owner, change status, notify, escalate) — capabilities a pure BI/reporting tool does not natively provide.** Excel and Power BI alone can both deliver strong reporting; neither is a case-management system out of the box. This shapes the scoring and the final recommendation below rather than being an afterthought.

---

## Evaluation Against the Nine Criteria

| Criterion | Option A — Excel | Option B — Power BI | Option C — Custom App |
|---|---|---|---|
| Business value | Covers reporting (BR-06/07/10) reasonably; workflow requirements (BR-02/03/08) need manual workarounds | Strong for reporting/KPI requirements; same workflow gap as Excel unless paired with another tool | Can, in principle, cover both reporting and workflow requirements fully |
| Cost | Near-zero incremental cost — existing licenses/skills | Moderate — Power BI licensing | High — development, hosting, and ongoing support |
| Complexity | Low — familiar to every stakeholder in the register | Moderate — requires data modeling/DAX skill | High — requires dedicated development resources |
| Implementation effort | Fastest to stand up | Moderate — dashboard build once data model is ready | Slowest — full build-and-test cycle |
| Scalability | Weak — struggles with concurrent editing and growing record volume | Strong for data volume and visualization | Strong, if properly resourced and maintained |
| Usability | Good for reporting; poor for workflow (no real assignment/notification) | Strong for viewing/filtering (matches most dashboard FRs) | Depends entirely on design investment — unproven |
| Maintainability | Spreadsheet logic tends to degrade over time ("spreadsheet risk") | Centralized KPI definitions — matches the Phase 8 standardization goal | Weak without a dedicated maintenance team — technical-debt risk |
| Risk | No audit trail, single point of failure, version-control issues | Mature, widely supported tool — lower operational risk | Highest risk — also runs against this project's own scope principle of avoiding large custom builds |
| Data requirements fit | Handles existing fields well; workflow fields need manual simulation | Strong for existing analytical fields; still needs a separate structured store for new exception-tracking fields (Exception ID, Owner, Status, etc.) | Most flexible — could be designed to the exact schema from day one |

---

## Weighted Decision Matrix

Weights reflect RetailCo's profile established in Phase 2 (a growing retailer that hasn't yet invested in BI — cost and time-to-value matter, but not at the expense of actually meeting the confirmed requirements):

| Criterion | Weight | Option A Score (1–5) | Option B Score (1–5) | Option C Score (1–5) |
|---|---|---|---|---|
| Business value | 25% | 3 | 4 | 5 |
| Cost | 15% | 5 | 3 | 1 |
| Implementation effort | 10% | 5 | 3 | 1 |
| Complexity | 10% | 5 | 3 | 2 |
| Scalability | 10% | 2 | 4 | 5 |
| Usability | 10% | 3 | 4 | 3 |
| Maintainability | 10% | 3 | 4 | 2 |
| Risk | 5% | 2 | 4 | 2 |
| Data requirements fit | 5% | 3 | 3 | 5 |
| **Weighted Total** | 100% | **3.55** | **3.60** | **3.05** |

**Option B (Power BI) narrowly wins**, driven mainly by the highest-weighted criterion (Business Value, 25%), where it scores higher than Excel because most of the confirmed requirements are reporting/KPI-driven. Option C scores lowest overall — its higher Business Value and Data Requirements fit are outweighed by cost, effort, and risk that don't match RetailCo's evidenced scale (a ~1,624-exception-per-year signal, per Phase 9) or this project's own stated principle of avoiding unnecessary custom software architecture.

**Sensitivity check:** the gap between A and B (3.55 vs. 3.60) is small enough that a different, still-reasonable weighting could flip it — e.g., if Cost were weighted at 25% instead of 15% (a tighter-budget scenario), Excel would edge ahead. This is disclosed rather than hidden: the recommendation below is a considered judgment call on close numbers, not an obvious landslide.

---

## Recommendation

**Primary recommendation: Option B — Power BI**, for the reporting and KPI-monitoring requirements (BR-06, BR-07, BR-10, and the dashboard FRs in Section 12.11) — this is where it clearly outperforms Excel and comfortably beats the custom-build option on cost and effort.

**With an explicit caveat:** Power BI alone does not satisfy the exception-workflow requirements (BR-02, BR-03, BR-08 — assignment, status lifecycle, escalation; FR-04 through FR-11, FR-22, FR-23). Building a full custom case-management system (Option C) to cover this gap would contradict this project's own scope principle of avoiding unnecessary large software builds. The realistic path is a **lightweight companion structure** — e.g., a simple structured list or small tracked table holding Exception ID, Owner, Status, and Priority — feeding the same data model Power BI reports on. This is a scope decision for stakeholders to confirm, not a default assumption.

**Phasing note:** given RetailCo has no existing BI investment (Phase 2), starting with **Option A (Excel)** for an initial, low-cost reporting pass and migrating to Power BI once the KPI definitions are validated in real use is also a defensible sequencing — the two options are close enough on the matrix that "start simple, upgrade deliberately" is a reasonable alternative to jumping straight to Power BI.

---

**Next step:** Dashboard Requirements — translating the Power BI recommendation into specific dashboard pages and visuals, each tied to a business question (Section 12.11 already scoped the KPI cards, filters, and visualizations at a high level).
