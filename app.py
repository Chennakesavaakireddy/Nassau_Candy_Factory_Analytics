import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.feature_engineering import prepare_data
from src.modeling import train_model
from src.optimizer import simulate_factory
from src.recommendation import recommend_factory

st.set_page_config(
    page_title="Nassau Candy Factory Optimization",
    page_icon="🍭",
    layout="wide"
)

@st.cache_data
def get_data():
    df, mapping = load_data()
    df = prepare_data(df)
    return df, mapping

df, mapping = get_data()

st.title("🍭 Nassau Candy Factory Optimization Dashboard")

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${df['Sales'].sum():,.0f}"
)

col2.metric(
    "Total Profit",
    f"${df['Gross Profit'].sum():,.0f}"
)

col3.metric(
    "Orders",
    len(df)
)

col4.metric(
    "Avg Lead Time",
    round(df["Lead_Time"].mean(), 2)
)

st.divider()

# Sidebar
st.sidebar.header("Optimization Controls")

selected_product = st.sidebar.selectbox(
    "Product",
    sorted(df["Product Name"].unique())
)

selected_region = st.sidebar.selectbox(
    "Region",
    sorted(df["Region"].unique())
)

selected_shipmode = st.sidebar.selectbox(
    "Ship Mode",
    sorted(df["Ship Mode"].unique())
)

priority = st.sidebar.slider(
    "Speed vs Profit",
    0,
    100,
    50
)

tab1, tab2, tab3 = st.tabs(
    [
        "Analytics",
        "Recommendations",
        "Scenario Analysis"
    ]
)

with tab1:

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index(),
            x="Region",
            y="Sales",
            title="Sales by Region"
        )

        st.plotly_chart(fig, use_container_width=True)

    with c2:

        fig = px.pie(
            df,
            names="Ship Mode",
            title="Ship Mode Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:

        fig = px.histogram(
            df,
            x="Lead_Time",
            title="Lead Time Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with c4:

        fig = px.bar(
            df.groupby("Factory")["Units"]
            .sum()
            .reset_index(),
            x="Factory",
            y="Units",
            title="Factory Utilization"
        )

        st.plotly_chart(fig, use_container_width=True)

    c5, c6 = st.columns(2)

    with c5:

        fig = px.scatter(
            df,
            x="Sales",
            y="Gross Profit",
            color="Division",
            title="Sales vs Profit"
        )

        st.plotly_chart(fig, use_container_width=True)

    with c6:

        fig = px.box(
            df,
            x="Region",
            y="Lead_Time",
            title="Lead Time by Region"
        )

        st.plotly_chart(fig, use_container_width=True)

with tab2:

    st.subheader("Factory Recommendations")

    rec = recommend_factory(
        df,
        selected_product,
        selected_region,
        priority
    )

    st.dataframe(
        pd.DataFrame(rec),
        use_container_width=True
    )

with tab3:

    st.subheader("What-If Scenario Analysis")

    scenario = simulate_factory(
        df,
        selected_product
    )

    st.dataframe(
        scenario,
        use_container_width=True
    )

    fig = px.bar(
        scenario,
        x="Factory",
        y="Predicted Lead Time",
        title="Lead Time Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig2 = px.bar(
        scenario,
        x="Factory",
        y="Expected Profit Impact",
        title="Profit Impact Comparison"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    avg_profit = scenario[
        "Expected Profit Impact"
    ].mean()

    if avg_profit < 0:
        st.error(
            "High Risk Reallocation"
        )
    else:
        st.success(
            "Low Risk Reallocation"
        )