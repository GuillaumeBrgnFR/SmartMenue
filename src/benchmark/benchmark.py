from src.benchmark import diff, gini, jaccard, levenshtein, lcs_similarity
from src.models import image_to_text


def evaluate_ocr_model(image_path: str, reference_text: str, model_name: str) -> dict:
    """
    Evaluate OCR model based on different metrics
    Args:
        image_path (str): path to the image
        reference_text (str): reference text
        model_name (str): name of the OCR model
    Returns:
        dict: evaluation results
    """
    extracted_text = image_to_text.extract_image_to_text(image_path, model_name)
    # replace new lines with spaces, remove ponctution, etc.
    extracted_text = extracted_text.replace("\n", " ").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace("…", "").replace("|", "").replace("/", "").replace("-", "")
    reference_text = reference_text.replace("\n", " ").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace("…", "").replace("|", "").replace("/", "").replace("-", "")
    results = {}
    results['difflib'] = diff.compare_texts_difflib(extracted_text, reference_text)
    results['jaccard'] = jaccard.jaccard_similarity(extracted_text, reference_text)
    results['levenshtein'] = levenshtein.compare_texts_levenshtein(extracted_text, reference_text)
    results['lcs'] = lcs_similarity.calculate_lcs_similarity(extracted_text, reference_text)
    return results


def evaluate_ocr_batch(image_path: list, reference_path: list, model_name: str) -> dict:
    """
    Evaluate OCR model based on different metrics for a batch of images
    Args:
        image_path (list): list of paths to the images
        reference_text (str): reference text
        model_name (str): name of the OCR model
    Returns:
        dict: evaluation results for each image
    """
    results = {}
    for i in range(len(image_path)):
        reference_file = reference_path[i]
        path = image_path[i]
        with open(reference_file, "r", encoding="utf-8") as file:
                    reference_text = file.read().replace("\n", " ")
        results[path] = evaluate_ocr_model(path, reference_text, model_name)
    return results


def evaluate_ocr_ensemble(image_path: list, reference_path: list, model_names: list) -> dict:
    """
    Evaluate OCR ensemble model based on different metrics for a batch of images
    Args:
        image_path (list): list of paths to the images
        reference_text (str): reference text
        model_names (list): list of OCR model names
    Returns:
        dict: evaluation results for each image
    """
    results = {}
    for model in model_names:
        results[model] = evaluate_ocr_batch(image_path, reference_path, model)
    return results