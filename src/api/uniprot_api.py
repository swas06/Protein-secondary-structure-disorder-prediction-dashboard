import requests

def fetch_uniprot_sequence(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None
    import requests

def fetch_uniprot_sequence(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except:
        return None