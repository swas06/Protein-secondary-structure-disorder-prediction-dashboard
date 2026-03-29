import requests

def predict_disorder_iupred(sequence):

    url = "https://iupred2a.elte.hu/iupred2a/long"

    data = {
        "seq": sequence
    }

    try:
        response = requests.post(url, data=data)

        if response.status_code == 200:
            result = response.text

            scores = []
            for line in result.split("\n"):
                if line and line[0].isdigit():
                    parts = line.split()
                    scores.append(float(parts[2]))

            return scores

        return None

    except:
        return None