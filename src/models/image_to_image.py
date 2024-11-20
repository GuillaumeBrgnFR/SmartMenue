from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import os


def extract_image_to_image(filename:str, threshold:float=0.1):
    """
    Extract the image to image model and save it.
    Args:
        filename (str): the name of the image file
    Returns:
        None
    """
    # Load the model
    processor = DetrImageProcessor.from_pretrained('facebook/detr-resnet-50')
    model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')

    # Load the image
    image = Image.open(filename)

    # Process the image
    inputs = processor(images=image, return_tensors="pt")

    # Perform the inference
    outputs = model(**inputs)

    #Extract the features
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=threshold)[0]

    for i, (_, _, box) in enumerate(zip(results["scores"], results["labels"], results["boxes"])):
        box = [round(i) for i in box.tolist()] 
        cropped_image = image.crop((box[0], box[1], box[2], box[3])) # Crop the detected object

        # Save the cropped image
        cropped_image.save(os.path.join(f"src/web-app/data/images/extracted/extracted_image_{i}.jpg"))
