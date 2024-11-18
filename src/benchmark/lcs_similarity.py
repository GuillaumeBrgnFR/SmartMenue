import textdistance

def calculate_lcs_similarity(reference: str, prediction: str) -> float:
    """
    Calculate the Longest Common Subsequence (LCS) similarity between a reference text and a predicted text.
    Args:
        reference (str): The reference text.
        prediction (str): The predicted text.
    Returns:
        float: LCS similarity score (between 0 and 1).
    """
    # Calculate the normalized LCS similarity
    lcs_similarity = textdistance.lcsseq.normalized_similarity(reference, prediction)
    return lcs_similarity