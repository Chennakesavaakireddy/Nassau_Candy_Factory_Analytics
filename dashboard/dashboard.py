import streamlit as st

from simulator_ui import simulator

from recommendation_ui import recommendation

from risk_panel import risk_panel


def dashboard():

    st.title(

        "Factory Reallocation Optimization"

    )

    page = st.sidebar.selectbox(

        "Module",

        [

            "Simulator",

            "Recommendations",

            "Risk Panel"

        ]

    )

    if page == "Simulator":

        simulator()

    elif page == "Recommendations":

        recommendation()

    else:

        risk_panel()