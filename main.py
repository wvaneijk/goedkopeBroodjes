from flask import Flask, request, jsonify
from xata.client import XataClient
 
import resolvers.recipeResolver
import uuid

app = Flask(__name__)

client = XataClient(api_key="xau_Y7lWdYj8v7Go6CJsreuLnBBHsBPwH1Vt3", db_url="https://m-lalmohamed-s-workspace-t5jh8f.eu-central-1.xata.sh/db/pepper-en-zuur")

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
def get_all_broodjes():
    data = client.data().query("GoodFood", {
    "columns": [
        "id",
        "name",
    ]
    })
    print(data)
    
    return jsonify({
        "message": "Available broodjes",
        "data": data
    }), 200

@app.route('/broodjes/<id>', methods=['GET'])
def get_specific_broodje(id):
    data = client.records().get("GoodFood", id)
    print(data)
    return data

@app.route('/broodjes', methods=['GET'])
def get_broodjes():
    searchQuery = request.args.get('search')
    data = client.data().query("GoodFood", { "filter": { "name": { "$contains" : searchQuery } } }) 
    return data

if __name__ == '__main__':
    app.run(debug=True)