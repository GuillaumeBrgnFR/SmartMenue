from src.models import image_to_text, text_to_json, image_to_image, text_to_text_allergene


def image_to_json_pipeline(image_path: str, model_name: str = "pytesseract", threshold: float = 0.1) -> list:
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
    json_data = text_to_text_allergene.add_allergene_to_json(json_data)
    for category in json_data:
        if len(category['category_items']) != len(category["item_allergene"]):
            allergenes = []
            for allerg in category["item_allergene"]:
                allergenes.append(allerg)
            allergenes = list(set(allergenes))
            allergenes = ", ".join(allergenes).replace(",  ", ", ")
            allergenes = allergenes.lower()
            allergenes = allergenes.split(",")
            allergenes = list(set(allergenes))
            allergenes = ", ".join(allergenes).replace(",  ", ", ")
            if allergenes[0] == " ":
                allergenes = allergenes[1:]
            category["item_allergene"] = [allergenes for i in range(len(category['category_items']))]

    # Extract the images
    image_to_image.extract_image_to_image(image_path, threshold)
    # Normalize JSON data
    return text_to_json.normalize_json(json_data)
