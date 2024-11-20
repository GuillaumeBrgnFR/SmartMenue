import cohere

co = cohere.ClientV2("jDRziy0rPDlXjCY9gvzEcV4BxfVCSQ4BavvnJ011")
#co = cohere.ClientV2("7HJV6CGrabnCQWomhg45iZHzDuOHiI91RfkrhDNr")


def text_to_allergene(name_dish:str):
    prompt = (
        f"Voici le nom d'un plat de restaurant : {name_dish}."
        "Donne moi la liste des allergènes présents dans ce plat sous la forme d'une chaine de caractères séparés par des virgules."
        "S'il est possible que des allergènes soient présent dans un tel plat, même sans être sur, tu peux les mentionner."
    )

    prompt = (
        f"Voici les noms des plats d'un restaurant : {name_dish}."
        "Donne moi la liste des allergènes présents dans chaque plat sous la forme d'une liste de chaine de caractères (des allergènes séparés par des virgules)."
        "S'il est possible que des allergènes soient présent dans un tel plat, même sans être sur, tu peux les mentionner."
    )

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content":prompt}],
    )

    return response.dict()["message"]['content'][0]['text']



def add_allergene_to_json(json_data):
    for category in json_data:
        item_allergenes = [text_to_allergene(item) for item in category['category_items']]
        category['item_allergene'] = item_allergenes
    return json_data

