import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import streamlit as st
from src.prediction.secondary_structure import predict_secondary_structure
from src.prediction.disorder_prediction import predict_disorder

st.title("⚙️ Run Prediction")

sequence = st.session_state.get("sequence")

if not sequence:
    st.warning("Load sequence first")
else:
    if st.button("Run Prediction"):
        with st.spinner("Running Predictions..."):

            structure = predict_secondary_structure(sequence)
            disorder = predict_disorder(sequence)

            st.session_state["structure"] = structure
            st.session_state["disorder"] = disorder
            
        st.success("Prediction Completed")


        st.sidebar.title("🧬 Protein Dashboard")
st.sidebar.markdown("---")
st.sidebar.info("Bioinformatics Analysis Tool")


