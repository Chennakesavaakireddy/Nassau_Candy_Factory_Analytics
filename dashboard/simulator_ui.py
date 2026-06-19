import streamlit as st


def simulator():

    st.header(

        "Factory Optimization Simulator"

    )

    st.selectbox(

        "Select Product",

        []

    )

    st.selectbox(

        "Select Region",

        []

    )

    st.selectbox(

        "Ship Mode",

        []

    )

    st.slider(

        "Optimization Priority",

        0,

        100,

        50

    )