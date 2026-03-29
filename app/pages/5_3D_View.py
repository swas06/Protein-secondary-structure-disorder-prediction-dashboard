import streamlit as st
import requests
import pandas as pd
from src.visualization.structure_viewer import show_structure

st.title("🧬 3D Protein Structure Explorer")

# -------------------------------
# INPUT SECTION
# -------------------------------
st.subheader("🔍 Input")

sequence = st.session_state.get("sequence")
uniprot_id = st.text_input("Enter UniProt ID (optional)")

# -------------------------------
# FUNCTIONS
# -------------------------------

def get_pdb_from_uniprot(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
    response = requests.get(url)

    pdb_ids = []

    if response.status_code == 200:
        data = response.json()
        for ref in data.get("uniProtKBCrossReferences", []):
            if ref["database"] == "PDB":
                pdb_ids.append(ref["id"])

    return pdb_ids


def search_pdb(sequence):
    url = "https://search.rcsb.org/rcsbsearch/v2/query"

    query = {
        "query": {
            "type": "terminal",
            "service": "sequence",
            "parameters": {
                "value": sequence,
                "evalue_cutoff": 1,
                "identity_cutoff": 0.3
            }
        },
        "return_type": "entry"
    }

    response = requests.post(url, json=query)

    if response.status_code == 200:
        data = response.json()
        return [item["identifier"] for item in data.get("result_set", [])]

    return []

# -------------------------------
# FETCH BUTTON
# -------------------------------
if st.button("🔍 Fetch Related PDB Structures"):

    results = []

    with st.spinner("Fetching data..."):

        # UniProt results
        if uniprot_id:
            uni_results = get_pdb_from_uniprot(uniprot_id)
            for pdb in uni_results:
                results.append({"PDB ID": pdb, "Source": "UniProt"})

        # Sequence results
        if sequence:
            seq_results = search_pdb(sequence)
            for pdb in seq_results:
                results.append({"PDB ID": pdb, "Source": "Sequence"})

    if results:
        df = pd.DataFrame(results).drop_duplicates()
        st.session_state["pdb_df"] = df
        st.success(f"Found {len(df)} unique structures")
    else:
        st.error("No structures found")

# -------------------------------
# DISPLAY TABLE SECTION
# -------------------------------
df = st.session_state.get("pdb_df")

if df is not None:

    st.subheader("📊 Related PDB Structures")

    st.dataframe(df, use_container_width=True)

    # -------------------------------
    # SELECT STRUCTURE
    # -------------------------------
    selected_pdb = st.selectbox(
        "🧪 Select PDB ID to visualize",
        df["PDB ID"].tolist()
    )

    if st.button("🚀 Show 3D Structure"):
        show_structure(selected_pdb)