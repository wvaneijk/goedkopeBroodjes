def resolve_recipe(recipe_data):
    num_ingredients = count_ingredients(recipe_data.get('ingredients', []))
    estimated_prep_time = estimate_recipe_duration(recipe_data)
    return {
               'number_of_ingredients': num_ingredients,
               'estimated_preparation_time_minutes': estimated_prep_time,
               'name': recipe_data.get("name"),
               'bunType': recipe_data.get("bunType"),
               'recipe': recipe_data.get("recipe"),
               'price': recipe_data.get("price"),
               'ingredients': recipe_data.get("ingredients"),
               'number_of_ingredients': num_ingredients,
               'estimated_preparation_time_minutes': estimated_prep_time
           }, 200


def count_ingredients(ingredientsString):
    splitIngredients = ingredientsString.split(' ')
    return len(splitIngredients)


def estimate_recipe_duration(recipe_data):
    num_steps = len(recipe_data.get('steps', []))
    return num_steps * 5
