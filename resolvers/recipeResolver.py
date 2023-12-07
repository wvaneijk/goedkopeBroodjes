import uuid

def resolve_recipe(recipe_data):
    # Count ingredients
    num_ingredients = len(recipe_data.get('ingredients', []))

    # Estimate preparation time (simple example: 10 minutes per step)
    num_steps = len(recipe_data.get('steps', []))
    estimated_prep_time = num_steps * 10

    # Basic categorization based on keywords in name or description
    keywords = {
        'dessert': ['cookie', 'cake', 'dessert', 'sweet'],
        'main course': ['steak', 'pasta', 'salad', 'pizza'],
        # Add more categories and keywords as needed
    }
    recipe_uuid = str(uuid.uuid4())
    category = 'others'
    name_description = recipe_data.get('name', '') + ' ' + recipe_data.get('description', '')
    for cat, keyws in keywords.items():
        if any(kw in name_description.lower() for kw in keyws):
            category = cat
            break

    return {
        'number_of_ingredients': num_ingredients,
        'estimated_preparation_time_minutes': estimated_prep_time,
        'category': category,
        'id': recipe_uuid
    }, 200

