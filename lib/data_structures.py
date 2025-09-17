spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai",    "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan",  "heat_level": 6},
]

def get_names(spicy_foods):
    return [sf["name"] for sf in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [sf for sf in spicy_foods if sf["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for sf in spicy_foods:
        # ⚠️ utiliser des quotes simples dans l'f-string pour accéder aux clés
        texte = f'{sf["name"]} ({sf["cuisine"]}) | Heat Level: {"🌶" * sf["heat_level"]}'
        print(texte)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # retourne le premier qui matche (comme dans l’énoncé)
    return [sf for sf in spicy_foods if sf["cuisine"] == cuisine][0]

def print_spiciest_foods(spicy_foods):
    for sf in get_spiciest_foods(spicy_foods):
        texte = f'{sf["name"]} ({sf["cuisine"]}) | Heat Level: {"🌶" * sf["heat_level"]}'
        print(texte)

def get_average_heat_level(spicy_foods):
    # le lab attend un entier
    return int(sum(sf["heat_level"] for sf in spicy_foods) / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
