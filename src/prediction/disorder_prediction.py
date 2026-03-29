from src.api.iupred_api import predict_disorder_iupred
import random

def predict_disorder(sequence):
    return [round(random.uniform(0, 1), 2) for _ in sequence]