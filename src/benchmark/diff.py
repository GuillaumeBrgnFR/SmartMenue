import difflib

def compare_texts_difflib(extracted_text: str, reference_text: str) -> float:
    """
    Compare two texts based on difflib (score between 0 and 1)
    Args: 
        extracted_text (str): extracted text
        reference_text (str): reference text
    Returns:
        float: difflib score 
    """
    matcher = difflib.SequenceMatcher(None, extracted_text, reference_text)
    return matcher.ratio()

