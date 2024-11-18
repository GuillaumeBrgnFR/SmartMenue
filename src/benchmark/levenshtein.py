import Levenshtein

def compare_texts_levenshtein(extracted_text: str, reference_text: str) -> float:
    """
    Compare two texts based on levenshtein (score between 0 and 1)
    Args: 
        extracted_text (str): extracted text
        reference_text (str): reference text
    Returns:
        float: levenshtein score 
    """
    distance = Levenshtein.distance(extracted_text, reference_text)
    max_len = max(len(extracted_text), len(reference_text))
    similarity = 1 - distance / max_len 
    return similarity