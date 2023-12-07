from flask import Flask, request, jsonify
from xata.client import XataClient

# xata = XataClient(db_name="pepper-en-zuur")


import resolvers.recipeResolver

app = Flask(__name__)

client = XataClient(api_key="xau_iuTwIae5Qmg3NAMC6DvOURCTT2KMmHfm0", db_url="https://m-lalmohamed-s-workspace-t5jh8f.eu-central-1.xata.sh/db/pepper-en-zuur")


@app.route('/addRecipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json

    response, status_code = resolvers.recipeResolver.resolve_recipe(recipe_data)

    return jsonify(response), status_code

    return jsonify({
        "message": "Recipe received and interpreted",
        "id": interpretation['id'],
        "interpretation": interpretation
    }), 200

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
    # resp = xata.data().query("GoodFood")
    # broodjes = response.json
    # print(broodjes)
    return jsonify({
        "message": "Available broodjes",
        "data": data
    }), 200

# @app.route('')

if __name__ == '__main__':
    app.run(debug=True)