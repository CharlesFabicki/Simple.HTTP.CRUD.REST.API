import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load last used unique_id from file or start from 1
try:
    with open('unique_id.txt', 'r') as file:
        unique_id = int(file.read())
except FileNotFoundError:
    unique_id = 1

data_store = []
data_file = 'data.json'


# Function for saving data to a JSON file
def save_data_to_file(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)


# Function for loading data from a JSON file
def load_data_from_file():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save the current unique_id to a file
def save_unique_id():
    with open('unique_id.txt', 'w') as file:
        file.write(str(unique_id))


# Endpoint for adding data
@app.route('/add_data', methods=['POST'])
def add_data():
    global unique_id, data_store
    new_data = request.json

    # Verify that required fields are present (Validation)
    if 'name' not in new_data or 'age' not in new_data:
        return jsonify({"error": "Name and age fields are required"}), 400

    # Assign unique identifier and increment it (Unique Identifiers)
    new_data['id'] = unique_id
    unique_id += 1

    data_store.append(new_data)
    save_data_to_file(data_store)  # Save data to JSON file
    save_unique_id()  # Save the updated unique_id
    return jsonify({"message": "Data has been successfully added!"})


# Endpoint for retrieving all data
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)


# Endpoint for deleting data
@app.route('/delete_data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    global data_store
    data_store = [data for data in data_store if data['id'] != data_id]
    save_data_to_file(data_store)  # Save data to JSON file
    return jsonify({"message": "Data has been successfully deleted!"})


# Endpoint for deleting all data
@app.route('/delete_all_data', methods=['DELETE'])
def delete_all_data():
    global data_store
    data_store = []  # Clear the data_store list
    save_data_to_file(data_store)  # Save data to JSON file
    return jsonify({"message": "All data has been successfully deleted!"})


# Endpoint for retrieving a single record by ID
@app.route('/get_data/<int:data_id>', methods=['GET'])
def get_single_data(data_id):
    record = next((data for data in data_store if data['id'] == data_id), None)
    if record:
        return jsonify(record)
    else:
        return jsonify({"error": "Record not found"}), 404


# Endpoint for updating data
@app.route('/update_data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    global data_store
    updated_data = request.json

    # Find the record by ID
    record_index = next((index for index, data in enumerate(data_store) if data['id'] == data_id), None)

    if record_index is not None:
        data_store[record_index].update(updated_data)
        save_data_to_file(data_store)  # Save updated data to JSON file
        return jsonify({"message": "Data has been successfully updated!"})
    else:
        return jsonify({"error": "Record not found"}), 404


if __name__ == '__main__':
    data_store = load_data_from_file()  # Load data from JSON file on startup
    app.run(debug=True)

# HOW DOES IT WORK?
# 1.
# # Retrieve Data (GET request): URL
# # http://127.0.0.1:5000/get_data
# 2.
# # Retrieve DataBASH
# # curl http://127.0.0.1:5000/get_data
# 3.
# # Adding Data BASH
# # curl -X POST -H "Content-Type: application/json" -d '{"name": "Charles Fabicki", "age": 26}' http://127.0.0.1:5000/add_data
# 4.
# # Deleting All Data BASH
# # curl -X DELETE http://127.0.0.1:5000/delete_all_data
# 5.
# # Updating a Record (Assuming ID is 1):
# # curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "age": 30}' http://127.0.0.1:5000/update_data/1
# 6.
# # Getting Specific Record by ID (Assuming ID is 2):
# # curl http://127.0.0.1:5000/get_data/2
# 7.
# # Adding Data with a Specific ID (Assuming ID is 5):
# # curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 35, "id": 5}' http://127.0.0.1:5000/add_data
# 8.
# # Deleting Specific Data by ID (Assuming ID is 3):
# # curl -X DELETE http://127.0.0.1:5000/delete_data/3
