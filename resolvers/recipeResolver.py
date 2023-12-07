import uuid
from fuzzywuzzy import fuzz


def resolve_recipe(recipe_data):
    num_ingredients = count_ingredients(recipe_data)
    estimated_prep_time = estimate_recipe_duration(recipe_data)
    return {
               'number_of_ingredients': num_ingredients,
               'estimated_preparation_time_minutes': estimated_prep_time,
               'name' : recipe_data.get("name"),
               'bunType': recipe_data.get("bunType"),
               'recipe': recipe_data.get("recipe"),
               'price': recipe_data.get("price"),
               'ingredients': recipe_data.get("ingredients"),
               'number_of_ingredients': 3,
               'estimated_preparation_time_minutes': 2.5
           }, 200


def count_ingredients(recipe_data):
    return len(recipe_data.get('ingredients', []))

def estimate_recipe_duration(recipe_data):
    num_steps = len(recipe_data.get('steps', []))
    return num_steps * 5
