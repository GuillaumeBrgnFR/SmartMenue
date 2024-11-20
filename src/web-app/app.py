from flask import Flask, jsonify, send_from_directory, request, abort, send_file
from flask_cors import CORS
from PIL import Image
from flask import request
import json
import os

from werkzeug.utils import secure_filename

print(os.getcwd())
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
    categories = "src/web-app/data/json/data.json" if os.path.exists("src/web-app/data/json/data.json") else "src/web-app/data/json/default.json"
    with open(categories) as f:
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
    print(f"app.root_path: {app.root_path}")

    # Chemin absolu vers le répertoire contenant les logos
    logo_directory = os.path.join(app.root_path, 'data', 'images', 'logos')
    print(f"logo_directory: {logo_directory}")

    # Chemin complet vers le fichier logo
    full_path = os.path.join(logo_directory, filename)
    print(f"full_path: {full_path}")

    if os.path.exists(os.path.join(logo_directory, filename)):
        print(f"hey dude: {os.path.join(logo_directory, filename)}")
        return send_file(os.path.join(logo_directory, filename))
    else:
        print('so sad')
        abort(404)  # Fichier non trouvé

@app.route('/api/upload-menu', methods=['POST'])
def upload_menu():
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
    save_dir = os.path.join(app.root_path, 'data', 'menu_name')
    save_path = os.path.join(save_dir, 'menu_name.txt')

    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as f:
            menu_name = f.read()
        return jsonify({'menuName': menu_name}), 200
    else:
        return jsonify({'menuName': None}), 200

@app.route('/data/images/logos/<filename>')
def get_logo_image(filename):
    print("Trying to get logo image: {}".format(filename))
    return send_from_directory('src/web-app/data/images/logos/', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)