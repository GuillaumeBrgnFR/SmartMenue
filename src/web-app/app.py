from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from PIL import Image
from flask import request
import json
import os

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
    categories = "../web-app/data/json/data.json" if os.path.exists("../web-app/data/json/data.json") else "../web-app/data/json/default.json"
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


@app.route('/api/upload-menu', methods=['POST'])
def upload_menu():
    print("SIUUUUUUU menu")
    file = request.files['menu']
    image = Image.open(file)
    save_dir = "../web-app/data/images/"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, file.filename)
    image.save(save_path)

    return jsonify({"message": "Image uploadée avec succès", "path": save_path})

@app.route('/api/upload-logo', methods=['POST'])
def upload_logo():
    print("SIUUUUUUU logo")
    file = request.files['logo']
    image = Image.open(file)
    save_dir = "../web-app/data/images/logos/"
    os.makedirs(save_dir, exist_ok=True)
    image = image.resize((50, 50))  # Redimensionner à 50x50 pixels
    save_path = os.path.join(save_dir, file.filename)
    image.save(save_path)
    return jsonify({"message": "Logo uploadé avec succès"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)