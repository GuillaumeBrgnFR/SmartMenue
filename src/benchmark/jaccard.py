
def jaccard_similarity(extracted_text: str, reference_text: str) -> float:
    """
    Compare two texts based on Jaccard (score between 0 and 1)
    Args: 
        extracted_text (str): extracted text
        reference_text (str): reference text
    Returns:
        float: jaccard score 
    """
    set1 = set(extracted_text.split())
    set2 = set(reference_text.split())
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union
