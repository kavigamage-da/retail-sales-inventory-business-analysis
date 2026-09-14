import os

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="RetailCo — Inventory & Sales Dashboard",
    layout="wide",
    page_icon="📊",
)

# ----------------------------------------------------------------------------
# DATA LOADING
# ----------------------------------------------------------------------------
# Streamlit Community Cloud runs the app from the repository root.
# Build the CSV path relative to this app.py file so it works both locally
# and when deployed from dashboard/streamlit-app/.
DATA_PATH = os.path.join(os.path.dirname(__file__), "data.csv")


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.rename(columns={"Margin_%": "Margin_Pct"})
    df["Invoice_Date"] = pd.to_datetime(df["Invoice_Date"])
    df["Month"] = df["Invoice_Date"].dt.month
    df["Month_Name"] = df["Invoice_Date"].dt.strftime("%b")
    df["Below_Reorder"] = df["Stock_On_Hand"] < df["Reorder_Level"]
    return df


df = load_data()

NAVY = "#1F4E78"
PALETTE = [
    "#1F4E78",
    "#4A6FA5",
    "#2A9D8F",
    "#C98A2C",
    "#7B8FA6",
    "#5B8A99",
    "#B4531E",
    "#3D5A80",
]

# ----------------------------------------------------------------------------
# SIDEBAR — real filters, applied to the live dataframe
# ----------------------------------------------------------------------------
st.sidebar.title("Filters")
st.sidebar.caption(
    "These filter the live 100,000-row dataset below — not a static export."
)

sel_category = st.sidebar.multiselect(
    "Category",
    sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique()),
)

sel_city = st.sidebar.multiselect(
    "City",
    sorted(df["City"].unique()),
    default=sorted(df["City"].unique()),
)

sel_channel = st.sidebar.multiselect(
    "Channel",
    sorted(df["Channel"].unique()),
    default=sorted(df["Channel"].unique()),
)

sel_format = st.sidebar.multiselect(
    "Store Format",
    sorted(df["Store_Format"].unique()),
    default=sorted(df["Store_Format"].unique()),
)

sel_months = st.sidebar.select_slider(
    "Month range",
    options=list(range(1, 13)),
    value=(1, 12),
    format_func=lambda m: pd.Timestamp(2024, m, 1).strftime("%b"),
)

st.sidebar.divider()

st.sidebar.caption(
    "Store and Product/SKU filters are intentionally absent — those identifiers "
    "don't exist in this dataset (see Data Quality Assessment, DQ-004)."
)

f = df[
    df["Category"].isin(sel_category)
    & df["City"].isin(sel_city)
    & df["Channel"].isin(sel_channel)
    & df["Store_Format"].isin(sel_format)
    & df["Month"].between(sel_months[0], sel_months[1])
]

if f.empty:
    st.warning(
        "No transactions match the current filters. "
        "Adjust the sidebar selections."
    )
    st.stop()

# ----------------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------------
st.title("RetailCo — Inventory & Sales Decision Support")

st.caption(
    f"Simulated portfolio case study · {len(f):,} of {len(df):,} transactions "
    "shown after filtering · RetailCo is a fictional company; this is not real "
    "business data."
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📈 Executive Overview",
        "🛒 Sales Performance",
        "💰 Product & Profitability",
        "📦 Inventory Monitoring",
    ]
)

# ----------------------------------------------------------------------------
# TAB 1 — EXECUTIVE OVERVIEW
# ----------------------------------------------------------------------------
with tab1:

    revenue = f["Revenue"].sum()
    units = f["Units"].sum()
    margin = f["Margin"].sum()
    margin_pct = margin / revenue if revenue else 0
    txns = len(f)
    below_rate = f["Below_Reorder"].mean()

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric(
        "Total Revenue",
        f"₹{revenue / 1e6:.2f}M",
    )

    c2.metric(
        "Units Sold",
        f"{units:,}",
    )

    c3.metric(
        "Gross Margin",
        f"₹{margin / 1e6:.2f}M",
    )

    c4.metric(
        "Margin %",
        f"{margin_pct * 100:.2f}%",
    )

    c5.metric(
        "Transactions",
        f"{txns:,}",
    )

    c6.metric(
        "Below Reorder Level",
        f"{below_rate * 100:.2f}%",
    )

    monthly = (
        f.groupby(["Month", "Month_Name"], as_index=False)["Revenue"]
        .sum()
        .sort_values("Month")
    )

    fig = px.line(
        monthly,
        x="Month_Name",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend",
    )

    fig.update_traces(line_color=NAVY)

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Revenue (₹)",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    st.info(
        "**Reading this page:** all figures update live as you change the "
        "sidebar filters — this is real pandas aggregation on the underlying "
        "transactions, not a fixed snapshot.",
        icon="ℹ️",
    )


# ----------------------------------------------------------------------------
# TAB 2 — SALES PERFORMANCE
# ----------------------------------------------------------------------------
with tab2:

    st.caption(
        "Revenue is evenly distributed across every dimension here "
        "(coefficient of variation <1.5% on the full dataset) — these charts "
        "are for ongoing monitoring, not evidence of a current imbalance."
    )

    col1, col2 = st.columns(2)

    with col1:

        cat_rev = (
            f.groupby("Category", as_index=False)["Revenue"]
            .sum()
            .sort_values("Revenue", ascending=False)
        )

        st.plotly_chart(
            px.bar(
                cat_rev,
                x="Category",
                y="Revenue",
                title="Revenue by Category",
                color_discrete_sequence=[PALETTE[1]],
            ),
            width="stretch",
        )

    with col2:

        city_rev = (
            f.groupby("City", as_index=False)["Revenue"]
            .sum()
            .sort_values("Revenue", ascending=False)
        )

        st.plotly_chart(
            px.bar(
                city_rev,
                x="City",
                y="Revenue",
                title="Revenue by City",
                color_discrete_sequence=[PALETTE[0]],
            ),
            width="stretch",
        )

    col3, col4 = st.columns(2)

    with col3:

        ch_rev = (
            f.groupby("Channel", as_index=False)["Revenue"]
            .sum()
        )

        st.plotly_chart(
            px.pie(
                ch_rev,
                names="Channel",
                values="Revenue",
                hole=0.5,
                title="Revenue by Channel",
                color_discrete_sequence=PALETTE,
            ),
            width="stretch",
        )

    with col4:

        fmt_rev = (
            f.groupby("Store_Format", as_index=False)["Revenue"]
            .sum()
        )

        st.plotly_chart(
            px.pie(
                fmt_rev,
                names="Store_Format",
                values="Revenue",
                hole=0.5,
                title="Revenue by Store Format",
                color_discrete_sequence=PALETTE[2:],
            ),
            width="stretch",
        )

    st.subheader("Average Transaction Value by Segment")

    atv_city = (
        f.groupby("City")
        .apply(
            lambda g: g["Revenue"].sum() / len(g),
            include_groups=False,
        )
        .reset_index(name="ATV")
    )

    st.dataframe(
        atv_city.sort_values("ATV", ascending=False),
        width="stretch",
        hide_index=True,
    )


# ----------------------------------------------------------------------------
# TAB 3 — PRODUCT & PROFITABILITY
# ----------------------------------------------------------------------------
with tab3:

    st.caption(
        "The original stakeholder concern — 'high-revenue, low-margin "
        "products' — was tested and **not supported**. Margin % stays within "
        "a narrow band at every level of granularity available."
    )

    col1, col2 = st.columns(2)

    with col1:

        cat_m = (
            f.groupby("Category")
            .apply(
                lambda g: g["Margin"].sum() / g["Revenue"].sum(),
                include_groups=False,
            )
            .reset_index(name="Margin_Pct")
        )

        cat_m = cat_m.sort_values(
            "Margin_Pct",
            ascending=False,
        )

        fig = px.bar(
            cat_m,
            x="Category",
            y="Margin_Pct",
            title="Margin % by Category",
            color_discrete_sequence=[PALETTE[2]],
        )

        fig.update_yaxes(
            tickformat=".1%",
            range=[0.18, 0.22],
        )

        st.plotly_chart(
            fig,
            width="stretch",
        )

    with col2:

        brand_m = (
            f.groupby("Brand")
            .apply(
                lambda g: g["Margin"].sum() / g["Revenue"].sum(),
                include_groups=False,
            )
            .reset_index(name="Margin_Pct")
        )

        brand_m = brand_m.sort_values(
            "Margin_Pct",
            ascending=False,
        )

        fig = px.bar(
            brand_m,
            x="Brand",
            y="Margin_Pct",
            title="Margin % by Brand",
            color_discrete_sequence=[PALETTE[3]],
        )

        fig.update_yaxes(
            tickformat=".1%",
            range=[0.18, 0.22],
        )

        st.plotly_chart(
            fig,
            width="stretch",
        )

    quad = (
        f.groupby("Category")
        .agg(
            Revenue=("Revenue", "sum"),
            Margin=("Margin", "sum"),
        )
        .reset_index()
    )

    quad["Margin_Pct"] = quad["Margin"] / quad["Revenue"]

    fig = px.scatter(
        quad,
        x="Revenue",
        y="Margin_Pct",
        text="Category",
        title="Revenue vs. Margin % — Category Quadrant",
        color_discrete_sequence=[NAVY],
    )

    fig.update_traces(
        textposition="top center",
        marker=dict(size=14),
    )

    fig.update_yaxes(
        tickformat=".1%",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )


# ----------------------------------------------------------------------------
# TAB 4 — INVENTORY MONITORING
# ----------------------------------------------------------------------------
with tab4:

    below_rate = f["Below_Reorder"].mean()

    c1, c2 = st.columns(2)

    c1.metric(
        "% Below Reorder Level",
        f"{below_rate * 100:.2f}%",
    )

    c2.metric(
        "Inventory Availability",
        f"{(1 - below_rate) * 100:.2f}%",
    )

    st.caption(
        "Per Phase 9's chi-square testing: category and city differences "
        "below are **not statistically significant** (p=0.675 and p=0.336 "
        "on the full dataset), and there is no Pareto concentration. Treat "
        "this page as a monitoring view, not a confirmed-hotspot list."
    )

    col1, col2 = st.columns(2)

    with col1:

        cat_b = (
            f.groupby("Category")["Below_Reorder"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        cat_b["Below_Reorder"] *= 100

        st.plotly_chart(
            px.bar(
                cat_b,
                x="Below_Reorder",
                y="Category",
                orientation="h",
                title="Below-Reorder Rate by Category (%)",
                color_discrete_sequence=[PALETTE[3]],
            ),
            width="stretch",
        )

    with col2:

        city_b = (
            f.groupby("City")["Below_Reorder"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        city_b["Below_Reorder"] *= 100

        st.plotly_chart(
            px.bar(
                city_b,
                x="Below_Reorder",
                y="City",
                orientation="h",
                title="Below-Reorder Rate by City (%)",
                color_discrete_sequence=[PALETTE[3]],
            ),
            width="stretch",
        )

    st.subheader("Category × City Heatmap — Below-Reorder Rate")

    pivot = (
        f.pivot_table(
            index="Category",
            columns="City",
            values="Below_Reorder",
            aggfunc="mean",
        )
        * 100
    )

    fig = go.Figure(
        data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns,
            y=pivot.index,
            colorscale=[
                [0, "#2A9D8F"],
                [0.5, "#C98A2C"],
                [1, "#99371E"],
            ],
            text=[
                [f"{v:.2f}%" for v in row]
                for row in pivot.values
            ],
            texttemplate="%{text}",
            colorbar=dict(title="%"),
        )
    )

    fig.update_layout(
        height=420,
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    with st.expander("Why this page doesn't name confirmed 'hotspots'"):

        st.markdown(
            "- Chi-square across all 64 Category×City combinations: "
            "**p = 0.383** (not significant)\n"
            "- Pareto check: the top 10 of 64 combinations account for only "
            "20.2% of below-reorder cases — reaching 80% of cases requires "
            "47 of 64 combinations\n"
            "- Supplier lead time correlation with below-reorder status: "
            "**≈0.0005** (ruled out)\n\n"
            "Full statistical detail: "
            "`business-analysis/root-cause-analysis.md`"
        )


# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.divider()

st.caption(
    "RetailCo Business Analysis Case Study · Built with Streamlit + Plotly · "
    "Source: business-analysis/ folder in this repo"
)