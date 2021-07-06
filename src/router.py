from database import *
from models.color import Color
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# GET REQUESTS

@app.route('/colors')
@app.route('/color')
def colors():
    favorite = request.args.get('favorite', '')
    if favorite.lower() == 'true':
        colors = get_colors_by_favorite(True)
        return jsonify({'colors': colors})
    elif favorite.lower() == 'false':
        colors = get_colors_by_favorite(False)
        return jsonify({'colors': colors})
    else:
        colors = get_colors()
        # return jsonify(colors)
        return jsonify({'colors': colors})


@app.route('/color/<int:id>')
def color(id):
    color = get_color(id)
    if color is None:
        return jsonify({'Response': 'Not Found'})
    return jsonify(color)


# POST REQUEST

@app.route('/color', methods=['POST'])
@app.route('/colors', methods=['POST'])
def new_color():
    name = request.json['name']
    rgb = request.json['rgb']
    fav = request.json['favorite']
    c = Color()
    c.name = name; c.rgb = rgb; c.favorite = fav;
    if add_color(c) == 1:
        return jsonify({"Response":"Success"})
    else:
        return jsonify({"Response":"Color name already exists"})

# PUT REQUEST

@app.route('/color', methods=['PUT'])
@app.route('/colors', methods=['PUT'])
def update_color():
    id = request.json['id']
    name = request.json['name']
    rgb = request.json['rgb']
    fav = request.json['favorite']
    c = Color()
    c.id = id; c.name = name; c.rgb = rgb; c.favorite = fav;
    if update(c) == 1:
        return jsonify({"Response":"Success"})
    else:
        return jsonify({"Response":"Name already exists"})


#DELETE REQUEST

@app.route('/color', methods=['DELETE'])
@app.route('/colors', methods=['DELETE'])
def delete_color():
    id = request.json['id']
    if delete(id) == 1:
        return jsonify({"Response":"Success"})
    else:
        return jsonify({"Response":"Not found"})


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0", port=5000)