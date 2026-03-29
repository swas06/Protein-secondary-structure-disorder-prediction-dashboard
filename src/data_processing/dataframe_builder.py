import pandas as pd

def build_dataframe(sequence, structure, disorder):

    df = pd.DataFrame({
        "Position": list(range(1, len(sequence)+1)),
        "Amino Acid": list(sequence),
        "Structure": list(structure),
        "Disorder Score": disorder
    })

    return df