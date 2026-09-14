# RetailCo Streamlit Dashboard

A real, interactive dashboard — not a static mockup. Filters in the sidebar re-run live pandas aggregations against the full 100,000-row dataset.

## Run it locally

```bash
cd dashboard/streamlit-app
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`. `data.csv` must sit next to `app.py` (it already does in this folder).

## Deploy it for free (recommended for your portfolio)

A local screenshot is fine, but a **live link** is what actually impresses in an interview — someone can click it and interact with your filters themselves, no install required.

1. Push this repo to GitHub (you've already got the guide for this)
2. Go to [share.streamlit.io](https://share.streamlit.io) → sign in with GitHub → **New app**
3. Point it at this repo, branch `main`, file path `dashboard/streamlit-app/app.py`
4. Click **Deploy** — takes about 2 minutes

You'll get a public URL like `retailco-inventory-dashboard.streamlit.app` — put that link in your resume/LinkedIn/README, not just "see attached file."

## Important: this app needs its data file committed

The rest of this repo's `.gitignore` excludes `*.csv` (to avoid bloating the repo with the raw dataset). **This folder is the one exception** — Streamlit Cloud needs `data.csv` physically present in the repo to run. Add this to your `.gitignore` before pushing, so this one file isn't excluded:

```gitignore
!dashboard/streamlit-app/data.csv
```

## What's interactive vs. what's fixed

- **Interactive:** Category, City, Channel, Store Format, and Month-range filters — every chart and metric on every tab recalculates from the filtered data
- **Fixed by design:** Store and Product/SKU filters are not offered, because those identifiers don't exist in this dataset (Phase 6, DQ-004) — the app doesn't pretend to filter by something it can't
- **Built in:** the same evidence-based captions used throughout the rest of this project (e.g., "not statistically significant," "not a confirmed hotspot list") — the app carries the analytical honesty, not just the charts

## Validated

This app was run end-to-end (not just syntax-checked) using Streamlit's `AppTest` framework before delivery, including simulating a live filter change and confirming the numbers actually recompute correctly — e.g., filtering to Beverages + Snacks correctly returns ₹9.88M revenue (matching 4,941,030.17 + 4,942,554.66 from `data-analysis/performance-analysis.md`).
