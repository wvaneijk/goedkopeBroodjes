from flask import Flask, request, jsonify
import dbUtils
import resolvers.recipe_resolver

app = Flask(__name__)

db_client = dbUtils.get_db_client()

@app.route('/addRecipe', methods=['POST'])
def add_recipe():
    recipe_data = request.json
    return jsonify(resolvers.recipe_resolver.addRecipe(recipe_data))


@app.route('/updateRecipe/<id>', methods=['PUT'])
def update_recipe(id):
    recipe_data = request.json
    return jsonify(resolvers.recipe_resolver.updateRecipe(id, recipe_data))


@app.route('/goodfood', methods=['GET'])
def get_all_sandwiches():
    response = jsonify(resolvers.recipe_resolver.get_all_sandwiches())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/sandwiches/<id>', methods=['GET'])
def get_specific_sandwich(id):
    response = jsonify(resolvers.recipe_resolver.get_sandwich_by_id(id))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/sandwiches', methods=['GET'])
def search_by_query():
    searchQuery = request.args.get('search')
    response = resolvers.recipe_resolver.search_by_query(searchQuery)
    return response

if __name__ == '__main__':
    app.run(debug=True)
