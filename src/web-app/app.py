from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# Initialisation de Flask
app = Flask(__name__, static_folder="frontend/build", static_url_path="")
CORS(app)

# Fonction pour générer les catégories dynamiques
def extract_categories():
    return [
        {
            'category_name': 'Entrées',
            'category_items': ['Salade', 'Soupe', 'Bruschetta'],
            'category_prices': ["31,90€", "26,99€", "45,50€"]
        },
        {
            'category_name': 'Plats',
            'category_items': ['Steak', 'Poulet rôti', 'Poisson grillé'],
            'category_prices': ["52,30€", "43,99€", "27,89€"]
        },
        {
            'category_name': 'Desserts',
            'category_items': ['Tarte aux pommes', 'Mousse au chocolat', 'Crème brûlée'],
            'category_prices': ["21,90€", "17,90€", "23,00€"]
        },
        {
            'category_name': 'Glaces',
            'category_items': ['Vanille', 'Chocolat', 'Fraise'],
            'category_prices': ["10,00€", "12,99€", "8,00€"]
        },
        {
            'category_name': 'Salades',
            'category_items': ['Salade César', 'Salade niçoise'],
            'category_prices': ["50,00€", "65,99€"]
        }
    ]


@app.template_filter('zip')
def zip_filter(a, b):
    return zip(a, b)

app.jinja_env.filters['zip'] = zip_filter


# API pour récupérer les données sous forme JSON
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify({'categories': extract_categories()})

# Route pour servir les fichiers de React
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path and path.startswith("static/"):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)