import cohere

co = cohere.ClientV2("jDRziy0rPDlXjCY9gvzEcV4BxfVCSQ4BavvnJ011")
#co = cohere.ClientV2("7HJV6CGrabnCQWomhg45iZHzDuOHiI91RfkrhDNr")


def text_to_allergene(dishes:str):
    prompt = (
        f"Voici les noms des plats d'un restaurant : {dishes}. Chaque plat est entre guillemets comme ceci : 'nom du plat'. Si un plat comporte plusieurs éléments, il faudra associer la liste des allergènes dans la même chaine de caractères"
        "Donne moi la liste des allergènes présents dans chaque plat sous la forme d'une liste de chaine de caractères (des allergènes séparés par des virgules)."
        "S'il est possible que des allergènes soient présent dans un tel plat, même sans être sur, tu peux les mentionner. Il doit y avoir autant de chaine de caractères d'allergènes que de plats."
        "Le resultat doit être sous la forme d'une liste de chaine de caractères qui contiennent les allergenes séparés par des virgules sans répéter le nom des plats. Uniquement les allergènes : ['plat1_allergene_1, plat1_allergene_2, ...', 'plat2_allergene_1, plat2_allergene_2, ...', ...]"
    )

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content":prompt}],
    )

    res = response.dict()["message"]["content"][0]["text"] 
    res = res.replace("-", "")
    res = res.split("\n")

    return res



def add_allergene_to_json(json_data):
    for category in json_data:
        category['item_allergene'] = text_to_allergene(str(category['category_items']))
    return json_data

