from flask import Flask, request, jsonify
import dbUtils
import resolvers.recipe_resolver

app = Flask(__name__)


@app.route('/addRecipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json
    return jsonify(resolvers.recipe_resolver.addRecipe(recipe_data))


@app.route('/updateRecipe/<id>', methods=['PUT'])
def update_recipe(id):
    recipe_data = request.json
    return jsonify(resolvers.recipe_resolver.updateRecipe(id, recipe_data))


@app.route('/goodfood', methods=['GET'])
def get_broodjes():
    data = dbUtils.get_db_client().data().query("GoodFood", {
        "columns": [
            "id",
            "name",
            "bunType",
            "recipe",
            "price",
            "ingredients"
        ]
    })
    print(data)

    return jsonify({
        "message": "Available broodjes",
        "data": data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
