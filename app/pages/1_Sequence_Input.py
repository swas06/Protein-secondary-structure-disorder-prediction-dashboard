import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import streamlit as st
from src.api.uniprot_api import fetch_uniprot_sequence
from src.utils.sequence_validator import clean_sequence, is_valid_sequence

st.title("🔬 Sequence Input")

sequence = st.text_area("Enter Protein Sequence")
uniprot_id = st.text_input("Enter UniProt ID")

if st.button("Load Sequence"):

    if uniprot_id:
        fasta = fetch_uniprot_sequence(uniprot_id)

        if fasta:
            sequence = "".join(fasta.split("\n")[1:])
        else:
            st.error("Invalid UniProt ID")

    sequence = clean_sequence(sequence)

    if not is_valid_sequence(sequence):
        st.error("Invalid Protein Sequence")
    else:
        st.session_state["sequence"] = sequence
        st.success("Sequence Loaded Successfully")


        st.sidebar.title("🧬 Protein Dashboard")
st.sidebar.markdown("---")
st.sidebar.info("Bioinformatics Analysis Tool")