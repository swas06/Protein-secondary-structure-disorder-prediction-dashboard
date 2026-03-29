import streamlit as st
import py3Dmol
import requests

def show_structure(pdb_id):
    """
    Fetches PDB structure from RCSB and displays it using py3Dmol in Streamlit
    """

    # -------------------------------
    # CLEAN INPUT
    # -------------------------------
    pdb_id = pdb_id.strip().lower()

    if not pdb_id:
        st.error("Invalid PDB ID")
        return

    # -------------------------------
    # FETCH PDB FILE
    # -------------------------------
    url = f"https://files.rcsb.org/view/{pdb_id}.pdb"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            st.error(f"Failed to fetch structure for {pdb_id.upper()}")
            return

        pdb_data = response.text

    except Exception as e:
        st.error("Error fetching structure")
        st.write(e)
        return

    # -------------------------------
    # CREATE 3D VIEW
    # -------------------------------
    try:
        view = py3Dmol.view(width=800, height=500)

        view.addModel(pdb_data, "pdb")

        # STYLE: Cartoon (best for proteins)
        view.setStyle({
            "cartoon": {
                "color": "spectrum"
            }
        })

        # Zoom to fit structure
        view.zoomTo()

        # -------------------------------
        # DISPLAY IN STREAMLIT
        # -------------------------------
        html = view._make_html()

        st.components.v1.html(html, height=500)

        st.success(f"Showing structure: {pdb_id.upper()}")

    except Exception as e:
        st.error("Error rendering 3D structure")
        st.write(e)