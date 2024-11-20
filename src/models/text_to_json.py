import cohere

#co = cohere.ClientV2("jDRziy0rPDlXjCY9gvzEcV4BxfVCSQ4BavvnJ011")
co = cohere.ClientV2("7HJV6CGrabnCQWomhg45iZHzDuOHiI91RfkrhDNr")


def generate_json(text: str, section_list:str="Entrées, Plats, Desserts, Boissons, Vins"):
    prompt = (
        f"Voici un menu de restaurant :\n\n{text}\n\n"
        f"Transforme ce texte en une liste de dictionnaires. Chaque section du menu)"
        "doit être le nom category_name. Cela peut être Entrées, Plats, Desserts, Boissons, Vins ou un nom personnalisé donné dans le menu."
        "Dans chaque dictionnaire, tu dois avoir category_name, category_items et category_prices."
        """La forme doit être la suivante : [{"nom_de_section":nom, "category_items":liste, "category_prices":liste}, ...]."""
        "Ne réponds rien d'autre que la la liste de dictionnaires."
    )

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content":prompt}],
    )

    return eval(response.dict()["message"]['content'][0]['text'])
