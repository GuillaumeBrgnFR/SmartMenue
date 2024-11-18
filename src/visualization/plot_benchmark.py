import matplotlib.pyplot as plt
import numpy as np


# Function to plot bar charts for a given metric
def plot_metric(metric: str, data: dict):
    """
    Plot bar charts comparing the given metric for EasyOCR and Pytesseract,
    displaying the values on top of the bars.
    
    Args:
        metric (str): The metric to plot (e.g., 'gini', 'difflib', 'jaccard', 'levenshtein').
        data (dict): The dictionary containing the OCR results.
    """
    images = list(data['easyocr'].keys())  # List of image filenames
    easyocr_scores = [data['easyocr'][img][metric] for img in images]
    pytesseract_scores = [data['pytesseract'][img][metric] for img in images]

    # Define bar positions
    x = np.arange(len(images))
    width = 0.35

    # Create the bar chart
    plt.figure(figsize=(12, 6))
    bars_easyocr = plt.bar(x - width/2, easyocr_scores, width, label='EasyOCR', color='blue')
    bars_pytesseract = plt.bar(x + width/2, pytesseract_scores, width, label='Pytesseract', color='orange')

    # Add labels, title, and legend
    plt.xlabel('Images')
    plt.ylabel(f'{metric.capitalize()} Score')
    plt.title(f'Comparison of {metric.capitalize()} Scores for EasyOCR and Pytesseract')
    plt.xticks(x, [img.split('/')[-1] for img in images], rotation=45)
    plt.ylim(0, 1)
    plt.legend()

    # Add values on top of the bars
    for bar in bars_easyocr:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    for bar in bars_pytesseract:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    # Show the chart
    plt.tight_layout()
    plt.show()




def plot_average_scores(data: dict):
    """
    Plot a bar chart comparing the average scores of EasyOCR and Pytesseract
    for each image across all metrics.

    Args:
        data (dict): The dictionary containing the OCR results.
    """
    images = list(data['easyocr'].keys())  # List of image filenames
    easyocr_scores = []
    pytesseract_scores = []

    # Calculate the average score for each image
    for img in images:
        easyocr_avg = np.mean(list(data['easyocr'][img].values()))
        pytesseract_avg = np.mean(list(data['pytesseract'][img].values()))
        easyocr_scores.append(easyocr_avg)
        pytesseract_scores.append(pytesseract_avg)

    # Define bar positions
    x = np.arange(len(images))
    width = 0.35

    # Create the bar chart
    plt.figure(figsize=(12, 6))
    bars_easyocr = plt.bar(x - width / 2, easyocr_scores, width, label='EasyOCR', color='blue')
    bars_pytesseract = plt.bar(x + width / 2, pytesseract_scores, width, label='Pytesseract', color='orange')

    # Add labels, title, and legend
    plt.xlabel('Images')
    plt.ylabel('Average Score')
    plt.title('Comparison of Average Scores for EasyOCR and Pytesseract')
    plt.xticks(x, [img.split('/')[-1] for img in images], rotation=45)
    plt.ylim(0, 1)
    plt.legend()

    # Add values on top of the bars
    for bar in bars_easyocr:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    for bar in bars_pytesseract:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    # Show the chart
    plt.tight_layout()
    plt.show()


def plot_overall_average_scores(data: dict):
    """
    Plot a bar chart comparing the overall average scores of EasyOCR and Pytesseract
    across all metrics and all images.

    Args:
        data (dict): The dictionary containing the OCR results.
    """
    # Calculate the overall average score for each model
    easyocr_scores = []
    pytesseract_scores = []

    for img in data['easyocr']:
        easyocr_scores.append(np.mean(list(data['easyocr'][img].values())))
        pytesseract_scores.append(np.mean(list(data['pytesseract'][img].values())))

    easyocr_overall_avg = np.mean(easyocr_scores)
    pytesseract_overall_avg = np.mean(pytesseract_scores)

    # Create the bar chart
    models = ['EasyOCR', 'Pytesseract']
    overall_scores = [easyocr_overall_avg, pytesseract_overall_avg]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(models, overall_scores, color=['blue', 'orange'])

    # Add labels, title, and values on the bars
    plt.ylabel('Average Score')
    plt.title('Overall Average Scores for EasyOCR and Pytesseract')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)

    # Show the chart
    plt.tight_layout()
    plt.show()

