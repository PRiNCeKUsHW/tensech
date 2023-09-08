from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to simulate the Pantry key-value store
pantry_store = {}

# Create (POST) endpoint to add key-value pairs to Pantry
@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.json
    pantry_id = data.get('b6057d6b-762a-4a1e-8724-2eab6a74a6e4')
    basket_key = data.get('https://getpantry.cloud/apiv1/pantry/b6057d6b-762a-4a1e-8724-2eab6a74a6e4/basket/tensech3')
    value = data.get('value')
    
    if pantry_id not in pantry_store:
        pantry_store[pantry_id] = {}
    
    pantry_store[pantry_id][basket_key] = value
    return jsonify({'message': 'Item added successfully'}), 201

# Read (GET) endpoint to retrieve the value associated with a specified basket key
@app.route('/get-item', methods=['GET'])
def get_item():
    pantry_id = request.args.get('b6057d6b-762a-4a1e-8724-2eab6a74a6e4')
    basket_key = request.args.get('https://getpantry.cloud/apiv1/pantry/b6057d6b-762a-4a1e-8724-2eab6a74a6e4/basket/tensech3')
    
    if pantry_id in pantry_store and basket_key in pantry_store[pantry_id]:
        value = pantry_store[pantry_id][basket_key]
        return jsonify({'value': value}), 200
    
    return jsonify({'message': 'Item not found'}), 404

# List Baskets (GET) endpoint to list all baskets under a specified Pantry
@app.route('/list-baskets', methods=['GET'])
def list_baskets():
    pantry_id = request.args.get('b6057d6b-762a-4a1e-8724-2eab6a74a6e4')
    
    if pantry_id in pantry_store:
        baskets = list(pantry_store[pantry_id].keys())
        return jsonify({'baskets': baskets}), 200
    
    return jsonify({'message': 'Pantry not found'}), 404

# Update (PUT) endpoint to update the value associated with a specified basket key
@app.route('/update-item', methods=['PUT'])
def update_item():
    data = request.json
    pantry_id = data.get('b6057d6b-762a-4a1e-8724-2eab6a74a6e4')
    basket_key = data.get('https://getpantry.cloud/apiv1/pantry/b6057d6b-762a-4a1e-8724-2eab6a74a6e4/basket/tensech3')
    new_value = data.get('newValue')
    
    if pantry_id in pantry_store and basket_key in pantry_store[pantry_id]:
        pantry_store[pantry_id][basket_key] = new_value
        return jsonify({'message': 'Item updated successfully'}), 200
    
    return jsonify({'message': 'Item not found'}), 404

# Delete (DELETE) endpoint to delete a specific basket by providing Pantry ID and basket key
@app.route('/delete-item', methods=['DELETE'])
def delete_item():
    pantry_id = request.args.get('b6057d6b-762a-4a1e-8724-2eab6a74a6e4')
    basket_key = request.args.get('https://getpantry.cloud/apiv1/pantry/b6057d6b-762a-4a1e-8724-2eab6a74a6e4/basket/tensech3')
    
    if pantry_id in pantry_store and basket_key in pantry_store[pantry_id]:
        del pantry_store[pantry_id][basket_key]
        return '', 204
    
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
