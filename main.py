from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/recipe', methods=['POST'])
def add_recipe():
    # Get the JSON data sent in the POST request
    recipe_data = request.json

    # Implement your logic here (e.g., save to database)
    # For this example, we'll just print it
    print(recipe_data)

    # Return a response
    return jsonify({"message": "Recipe received successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)