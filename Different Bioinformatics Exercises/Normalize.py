def Normalize(Probabilities):
    normalized={}
    for j in Probabilities:
        normalized[j] = Probabilities[j]/sum(Probabilities.values())
    return normalized