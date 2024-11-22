import cohere
from src.data.api_key import get_api_key

co = cohere.ClientV2(get_api_key())


def generate_json(text: str):
    """
    This function takes a string of text and a list of sections and returns a list of dictionaries.
    Each dictionary represents a section of a restaurant menu.
    Args: 
        - text: a string of text representing a restaurant menu
    Returns:
        - a list of dictionaries, where each dictionary represents a section of a restaurant menu
    """
    prompt = (
        f"Voici un menu de restaurant :\n\n{text}\n\n"
        f"Transforme ce texte en une liste de dictionnaires. Chaque section du menu)"
        "doit être le nom category_name. Cela peut être Entrées, Plats, Desserts, Boissons, Vins ou un nom personnalisé donné dans le menu."
        "Dans chaque dictionnaire, tu dois avoir category_name (nom de la catégorie), category_items (nom du plat et sa description), et item_prices (prix du plat)."
        """La forme doit être la suivante : [{"category_name":nom, "category_items":liste, "item_prices":liste}, ...]."""
        "Ne réponds rien d'autre que la la liste de dictionnaires."
    )

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content":prompt}],
    )

    return eval(response.dict()["message"]['content'][0]['text'])


def normalize_json(json_data):
    """
    This function takes a list of dictionaries and returns a list of dictionaries.
    Args:
        - json_data: a list of dictionaries
    Returns:
        - a list of dictionaries where the prices are formatted as strings
    """
    for section in json_data:
        formatted_prices = []
        for price in section["item_prices"]:
            try:
                formatted_price = f"{float(price):05.2f}".replace('.', ',') + " €"
                formatted_prices.append(formatted_price)
            except (ValueError, TypeError):
                formatted_prices.append("- €")
        section["item_prices"] = formatted_prices
    return json_data
