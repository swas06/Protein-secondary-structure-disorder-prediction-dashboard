import streamlit as st
import requests

st.title("🔎 Protein Database Search")

query = st.text_input("Search Protein")

if st.button("Search"):

    url = f"https://rest.uniprot.org/uniprotkb/search?query={query}&format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for entry in data["results"][:5]:
            name = entry["primaryAccession"]
            desc = entry["proteinDescription"]["recommendedName"]["fullName"]["value"]

            st.write(f"{name} - {desc}")
    else:
        st.error("API Error")