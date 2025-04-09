def calculate_jaccard_similarity(a_hashes, b_hashes):
    intersection = len(a_hashes & b_hashes)
    union = len(a_hashes | b_hashes)
    return intersection / union if union != 0 else 0.0