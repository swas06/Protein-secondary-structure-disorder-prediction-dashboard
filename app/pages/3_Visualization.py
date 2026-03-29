import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_processing.dataframe_builder import build_dataframe

st.title("📊 Visualization")

sequence = st.session_state.get("sequence")
structure = st.session_state.get("structure")
disorder = st.session_state.get("disorder")

if sequence and structure and disorder:

    df = build_dataframe(sequence, structure, disorder)

    st.dataframe(df)

    fig = px.line(df, x="Position", y="Disorder Score", title="Disorder Plot")
    st.plotly_chart(fig, use_container_width=True)

    st.text("Sequence:")
    st.text(sequence)

    st.text("Structure:")
    st.text(structure)

else:
    st.warning("Run prediction first")

    st.sidebar.title("🧬 Protein Dashboard")
st.sidebar.markdown("---")
st.sidebar.info("Bioinformatics Analysis Tool")