from flask import Flask, request, jsonify

import resolvers.recipeResolver
import uuid

app = Flask(__name__)

@app.route('/recipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json

    response, status_code = resolvers.recipeResolver.resolve_recipe(recipe_data)

    return jsonify(response), status_code


if __name__ == '__main__':
    app.run(debug=True)