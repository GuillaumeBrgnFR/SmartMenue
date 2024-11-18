import pytesseract
import easyocr
#import keras_ocr
#from doctr.models import ocr_predictor
from PIL import Image

def extract_image_to_text(filename: str, model_name: str) -> str:
    """
    args: 
        filename: path to the image
        model_name: name of the model (pytesseract, easyocr, keras_ocr, doctr)
    return: 
        text extract from the image as a single string
    """
    # Load the image
    try:
        image = Image.open(filename)
    except Exception as e:
        return f"Error loading image: {str(e)}"

    if model_name == "easyocr":
        reader = easyocr.Reader(['fr'])
        # Read text from an image
        result = reader.readtext(filename, detail=0)  # detail=0 returns only the text
        return "\n".join(result)
    
    # elif model_name == "doctr":
    #     # Perform OCR on the document
    #     predictor = ocr_predictor(pretrained=True)
    #     # Perform OCR on the image
    #     result = predictor([image])
    #     # Extract and combine text from all blocks
    #     return "\n".join(block["value"] for page in result.pages for block in page.blocks)
    
    # elif model_name == "keras_ocr":
    #     # Create pipeline
    #     pipeline = keras_ocr.pipeline.Pipeline()
    #     # Perform OCR
    #     predictions = pipeline.recognize([filename])
    #     # Extract and combine text
    #     return "\n".join(word for word, box in predictions[0])
    
    elif model_name == "pytesseract":
        # Perform OCR on an image
        return pytesseract.image_to_string(image, lang='fra')
    
    else:
        return "Invalid model name. Please choose from 'pytesseract', 'easyocr', 'keras_ocr', or 'doctr'."