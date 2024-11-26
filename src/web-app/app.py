from flask import Flask, jsonify, send_from_directory, request, abort, send_file
from flask_cors import CORS
from PIL import Image
from flask import request
import json
import os

from werkzeug.utils import secure_filename

from src.pipelines.image_to_json_pipeline import image_to_json_pipeline



# Initialisation de Flask
app = Flask(__name__, static_folder="frontend/build", static_url_path="")
CORS(app)

# Fonction pour générer les catégories dynamiques



@app.template_filter('zip')
def zip_filter(a, b):
    return zip(a, b)

app.jinja_env.filters['zip'] = zip_filter


# API pour récupérer les données sous forme JSON
@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Function that search data to display the content of the menu.
    Returns:

    """
    data_file_path = os.path.join(app.root_path, 'data', 'json', 'data.json')
    default_file_path = os.path.join(app.root_path, 'data', 'json', 'default.json')
    categories_file = data_file_path if os.path.exists(data_file_path) else default_file_path
    with open(categories_file, 'r', encoding='utf-8') as f:
        categories = json.load(f)

    return jsonify({'categories': categories})

# Route pour servir les fichiers de React
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path and path.startswith("static/"):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


@app.route('/images/logos/<filename>')
def serve_logo(filename):
    """
    Function that search the logo to display it on the web page
    Args:
        filename:

    Returns:

    """
    # Chemin absolu vers le répertoire contenant les logos
    logo_directory = os.path.join(app.root_path, 'data', 'images', 'logos')

    # Chemin complet vers le fichier logo
    full_path = os.path.join(logo_directory, filename)

    if os.path.exists(os.path.join(logo_directory, filename)):
        return send_file(os.path.join(logo_directory, filename))
    else:
        abort(404)  # Fichier non trouvé

@app.route('/api/upload-menu', methods=['POST'])
def upload_menu():
    """
    Function that save the menu as a JSON.
    Returns:

    """
    file = request.files['menu']
    image = Image.open(file)
    save_dir = "src/web-app/data/images/"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, file.filename)
    image.save(save_path)
    json_data = image_to_json_pipeline(save_path)
    json.dump(json_data, open('src/web-app/data/json/data.json', 'w'))
    return jsonify({"message": "Image uploadée avec succès", "path": save_path})

@app.route('/api/upload-logo', methods=['POST'])
def upload_logo():
    """
    Function that gte the logo and save it.
    Returns:

    """
    file = request.files['logo']
    filename = secure_filename(file.filename)
    extension = os.path.splitext(filename)[1]  # Récupère l'extension avec le point (par exemple, '.png')

    if not extension:
        return jsonify({"message": "Extension de fichier invalide"}), 400

    image = Image.open(file)
    save_dir = "src/web-app/data/images/logos/"
    os.makedirs(save_dir, exist_ok=True)
    image = image.resize((50, 50))  # Redimensionner à 50x50 pixels
    save_path = os.path.join(save_dir, f"logo{extension}")
    image.save(save_path)
    return jsonify({"message": "Logo uploadé avec succès"})


@app.route('/api/save-menu-name', methods=['POST'])
def save_menu_name():
    """
    Function that save the menu name in a .txt file.
    Returns:

    """
    data = request.get_json()
    menu_name = data.get('menuName')

    if menu_name:
        # Chemin vers le répertoire de sauvegarde
        save_dir = os.path.join(app.root_path, 'data', 'menu_name')
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, 'menu_name.txt')

        # Sauvegarde du nom du menu dans le fichier
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(menu_name)

        return jsonify({'message': 'Nom du menu sauvegardé avec succès'}), 200
    else:
        return jsonify({'message': 'Nom du menu manquant'}), 400

@app.route('/api/get-menu-name', methods=['GET'])
def get_menu_name():
    """
    Function that get the menu name from the .txt file.
    Returns:

    """
    save_dir = os.path.join(app.root_path, 'data', 'menu_name')
    save_path = os.path.join(save_dir, 'menu_name.txt')

    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as f:
            menu_name = f.read()
        return jsonify({'menuName': menu_name}), 200
    else:
        return jsonify({'menuName': None}), 200


@app.route('/api/save-menu', methods=['POST'])
def save_menu():
    """
    Function that get the menu uploaded by the user
    Returns:

    """
    categories = request.get_json()

    if not categories:
        return jsonify({'message': 'Aucune donnée reçue'}), 400
    print(f"categories: {categories}")
    # Chemin vers le fichier data.json
    data_file_path = os.path.join(app.root_path, 'data', 'json', 'data.json')

    # S'assurer que le dossier existe
    os.makedirs(os.path.dirname(data_file_path), exist_ok=True)
    for dictionnary in categories:
        print(f"dictionnary: {dictionnary}")
        for i in range(len(dictionnary["item_prices"])):
            price = dictionnary["item_prices"][i]
            if price == "Invalid price" or price == "" or price is None:
                price = "- €"
                dictionnary["item_prices"][i] = price
            elif price is not None and price != "" and price[-1] != "€":
                try:
                    price = f"{float(price):05.2f}"
                    print(f"price after: {price}")
                    price = price + " €"
                except:
                    pass
                finally:
                    dictionnary["item_prices"][i] = price
    try:
        with open(data_file_path, 'w', encoding='utf-8') as f:
            json.dump(categories, f, ensure_ascii=False, indent=4)
        return jsonify({'message': 'Menu sauvegardé avec succès'}), 200
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du menu : {e}")
        return jsonify({'message': 'Erreur lors de la sauvegarde du menu'}), 500


@app.route('/data/images/logos/<filename>')
def get_logo_image(filename):
    """
    Function that get the logo image saved by the user.
    Args:
        filename:

    Returns:

    """
    print("Trying to get logo image: {}".format(filename))
    return send_from_directory('src/web-app/data/images/logos/', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)