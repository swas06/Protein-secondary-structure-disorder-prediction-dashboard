import streamlit as st

# Page Config
st.set_page_config(
    page_title="Protein Dashboard",
    layout="wide",
    page_icon="🧬"
)

# Custom CSS
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0E1117;
}

/* Title styling */
h1 {
    color: #00C9A7;
    font-weight: 700;
}

/* Card style */
.card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background-color: #00C9A7;
    color: black;
    border-radius: 8px;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("🧬 Protein Structure Dashboard")

st.markdown("""
<div class="card">
<h3>Welcome</h3>
<p>This dashboard allows protein sequence analysis, structure prediction, and disorder visualization.</p>
</div>
""", unsafe_allow_html=True)

# Feature Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h4>🔬 Sequence Input</h4>
    <p>Upload or fetch sequences using UniProt ID</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h4>📊 Visualization</h4>
    <p>Interactive disorder and structure plots</p>
    </div>
    """, unsafe_allow_html=True)