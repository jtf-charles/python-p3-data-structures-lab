spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names=[spicy_food["name"] for spicy_food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spicy_food=[spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"]>5]
    return spicy_food

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        texte=f"{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {spicy_food["heat_level"]*"🌶"}"
        print(texte)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food=[spicy_food for spicy_food in spicy_foods if spicy_food["cuisine"]==cuisine]
    return spicy_food[0]

def print_spiciest_foods(spicy_foods):
    spicy_food_list=[spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"]>5]
    for spicy_food in spicy_food_list:
        texte=f"{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {spicy_food["heat_level"]*"🌶"}"
        print(texte)

def get_average_heat_level(spicy_foods):
    somme=0
    for spicy_food in spicy_foods:
        somme+=spicy_food["heat_level"]
    mean=somme/len(spicy_foods)
    return(mean)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
