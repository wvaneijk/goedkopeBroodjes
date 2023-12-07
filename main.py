from flask import Flask, request, jsonify
from xata.client import XataClient

# xata = XataClient(db_name="pepper-en-zuur")
import dbUtils
import resolvers.recipeResolver

app = Flask(__name__)

@app.route('/addrecipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json

    resolvedData, status_code = resolvers.recipeResolver.resolve_recipe(recipe_data)
    response = dbUtils.get_db_client().records().insert("GoodFood", resolvedData)
    return jsonify(response), status_code

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