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
    name_list = []
    for food in spicy_foods:
        name_list.append(food["name"])
    return name_list

def get_spiciest_foods(spicy_foods):
    spiciest_food_list = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food_list

def print_spicy_foods(spicy_foods):
    chili_pepper = "🌶"
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * chili_pepper}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food_dict = next((food for food in spicy_foods if food["cuisine"] == cuisine))
    return spicy_food_dict

def print_spiciest_foods(spicy_foods):
    chili_pepper = "🌶"
    spiciest_food_list = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spiciest_food_list:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * chili_pepper}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    average_heat_level = total_heat_level / 3
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods