from src.models import image_to_text, text_to_json


def image_to_json_pipeline(image_path: str, model_name: str = "pytesseract") -> list:
    """
    args: 
        image_path: path to the image
        model_name: name of the model (pytesseract, easyocr, keras_ocr, doctr)
    return: 
        list of dictionaries containing the menu items
    """
    # Extract text from the image
    text = image_to_text.extract_image_to_text(image_path, model_name)
    # Generate JSON from the extracted text
    json_data = text_to_json.generate_json(text)
    # Normalize JSON data
    return text_to_json.normalize_json(json_data)
