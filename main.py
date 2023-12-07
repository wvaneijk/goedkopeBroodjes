from flask import Flask, request, jsonify



import resolvers.recipeResolver


app = Flask(__name__)

@app.route('/recipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json

    data = client.records().insert("GoodFood", recipe_data)
    print("DATA: ", data)

    # Interpret the recipe
    response, status_code = resolvers.recipeResolver.resolve_recipe(data)

    # Here, you can further process, store, or respond with the interpretation
    # print(interpretation)

    return jsonify(response), status_code

@app.route('/goodfood', methods=['GET'])
def get_broodjes():
    data = client.data().query("GoodFood", {
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