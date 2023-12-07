import uuid


def resolve_recipe(recipe_data):
    title = recipe_data.get("name", "")
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
               'uuid': recipe_uuid,
               'resolved_data': {
                   'bunType': recipe_data.get('bunType', ''),
                   'original_id': recipe_data.get('id', ''),
                   'ingredients': recipe_data.get('ingredients', ''),
                   'name': title,
                   'price': recipe_data.get('price', 0),
                   'xata': recipe_data.get('xata', {}),
                   'estimated_prep_time': estimated_prep_time,
                   'num_ingredients': num_ingredients
               }
           }, 200
