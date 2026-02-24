from flask import Flask, jsonify, request, render_template

# Create Flask app
app = Flask(__name__)

data = [
    {'id': 1, 'name': 'The Great Gatsby'},
    {'id': 2, 'name': 'To Kill a Mockingbird'},
    {'id': 3, 'name': '1984'},
    {'id': 4, 'name': 'The Alchemist'},
    {'id': 5, 'name': 'Atomic Habits'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': data})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)

    if item:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'message': 'Invalid request'}), 400

    new_item = {
        'id': len(data) + 1,
        'name': request.json['name']
    }

    data.append(new_item)

    return jsonify({
        'message': 'Item added successfully',
        'item': new_item
    }), 201


# Run the application
if __name__ == '__main__':
    app.run(debug=True)