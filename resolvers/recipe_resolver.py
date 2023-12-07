import dbUtils


def createRecipeMutation(recipe_data):
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

def addRecipe(recipe_data):
    response, responseCode = createRecipeMutation(recipe_data)
    if responseCode is not 200:
        raise ValueError("There is something wrong with the recipe mutation")
    return dbUtils.get_db_client().records().insert("GoodFood", response)


def updateRecipe(recipe_id, recipe_data):
    if recipe_id is None:
        return {"no ID is provided"}, 400
    response, responseCode = createRecipeMutation(recipe_data)
    if responseCode is not 200:
        raise ValueError("There is something wrong with the recipe mutation")
    return dbUtils.get_db_client().records().update("GoodFood", recipe_id, response)

def count_ingredients(ingredientsString):
    splitIngredients = ingredientsString.split(' ')
    return len(splitIngredients)


def estimate_recipe_duration(recipe_data):
    num_steps = len(recipe_data.get('steps', []))
    return num_steps * 5

def get_all_sandwiches():
    return dbUtils.get_db_client().data().query("GoodFood", {
        "columns": [
            "id",
            "name",
        ]
    })

def get_sandwich_by_id(id):
    return dbUtils.get_db_client().records().get("GoodFood", id)

def search_by_query(searchQuery):
    return dbUtils.get_db_client().data().query("GoodFood", { "filter": { "name": { "$contains" : searchQuery } } })