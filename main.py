from flask import Flask, request, jsonify
from xata.client import XataClient

# xata = XataClient(db_name="pepper-en-zuur")
 

import resolvers.recipeResolver
import uuid

app = Flask(__name__)

client = XataClient(api_key="xau_iuTwIae5Qmg3NAMC6DvOURCTT2KMmHfm0", db_url="https://m-lalmohamed-s-workspace-t5jh8f.eu-central-1.xata.sh/db/pepper-en-zuur")


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