import numpy as np
import string
from collections import Counter

def normalize_text(text: str) -> str:
    """
    Normalizes a text for fair comparison.
    Args:
        text (str): The input text to normalize.
    Returns:
        str: The normalized text.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = " ".join(text.split())
    # Remove unwanted characters (keep only alphanumeric and punctuation)
    allowed_characters = string.ascii_lowercase + string.digits + string.punctuation + " "
    text = "".join(c for c in text if c in allowed_characters)
    return text


def compute_frequencies(text: str) -> dict:
    """
    Computes the frequency of each character in a text.
    Args:
        text (str): The input text.
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    return Counter(text)


def compute_word_frequencies(text: str) -> dict:
    """
    Computes the frequency of each word in a text.
    Args:
        text (str): The input text.
    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    words = text.split()  # Split the text into words
    return Counter(words)


def gini_index(frequencies: dict) -> float:
    """
    Calculates the Gini index for a given distribution.
    Args:
        frequencies (dict): A dictionary with elements (e.g., characters or words) as keys and their frequencies as values.
    Returns:
        float: The Gini index for the given distribution.
    """
    values = np.array(list(frequencies.values()))
    total = np.sum(values)
    if total == 0:
        return 0  # Avoid division by zero
    probabilities = values / total
    gini = 1 - np.sum(probabilities ** 2)
    return gini


def compare_gini(extracted_text: str, reference_text: str) -> dict:
    """
    Compares the extracted text to the reference text using Gini indices.
    Args:
        extracted_text (str): The text extracted (e.g., from OCR).
        reference_text (str): The true reference text.
    Returns:
        dict: A dictionary containing the Gini indices and discrepancies for characters and words.
    """
    # Normalize texts
    extracted_text_norm = normalize_text(extracted_text)
    reference_text_norm = normalize_text(reference_text)
    
    # Compute character and word frequencies
    extracted_word_freq = compute_word_frequencies(extracted_text_norm)
    reference_word_freq = compute_word_frequencies(reference_text_norm)
    
    # Calculate Gini indices
    extracted_word_gini = gini_index(extracted_word_freq)
    reference_word_gini = gini_index(reference_word_freq)
    
    # Calculate discrepancies
    word_gini_diff = abs(extracted_word_gini - reference_word_gini)
    
    # Return results
    return 1 - word_gini_diff
