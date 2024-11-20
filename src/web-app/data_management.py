import json


data = [
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

def write_json(data):
    with open('data/json/default.json', 'w') as outfile:
        json.dump(data, outfile)

def recover_data():
    with open('data/json/default.json', 'r') as infile:
        info = json.load(infile)
    print(f"Data: {info} and is type: {type(info)}")

