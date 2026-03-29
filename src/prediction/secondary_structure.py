def predict_secondary_structure(sequence):
    # Placeholder (replace with real API later)
    result = ""

    for i in range(len(sequence)):
        if i % 3 == 0:
            result += "H"
        elif i % 3 == 1:
            result += "E"
        else:
            result += "C"

    return result