from flask import Flask, request, jsonify

import resolvers.recipeResolver
import uuid

app = Flask(__name__)


@app.route('/recipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json

    # Interpret the recipe
    interpretation = resolvers.recipeResolver.resolve_recipe(recipe_data)

    # Here, you can further process, store, or respond with the interpretation
    print(interpretation)

    return jsonify({
        "message": "Recipe received and interpreted",
        "id": interpretation['id'],
        "interpretation": interpretation
    }), 200


if __name__ == '__main__':
    app.run(debug=True)