VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")

def clean_sequence(seq):
    return seq.upper().replace(" ", "").replace("\n", "")

def is_valid_sequence(seq):
    return all(residue in VALID_AA for residue in seq)