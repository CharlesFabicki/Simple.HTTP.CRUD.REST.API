# Flask API for Data Management

This is a simple Flask API that allows you to manage data records. You can perform CRUD (Create, Read, Update, Delete) operations on data records using this API.

## Setup

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Flask server by running:

    ```bash
    python HTTP_CRUD-Flask-API.py
    ```

## API Endpoints HOW DOES IT WORK?

### Retrieve Data (GET request): URL
```bash
http://127.0.0.1:5000/get_data
```
## USE BASH HERE

### Retrieve Data
```bash
curl http://127.0.0.1:5000/get_data
```
### Adding Data 
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Charles Fabicki", "age": 26}' http://127.0.0.1:5000/add_data
```
### Deleting All Data 
```bash
curl -X DELETE http://127.0.0.1:5000/delete_all_data
```
### Updating a Record (Assuming ID is 1):
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "age": 30}' http://127.0.0.1:5000/update_data/1
```
### Getting Specific Record by ID (Assuming ID is 2):
```bash
curl http://127.0.0.1:5000/get_data/2
```
### Adding Data with a Specific ID (Assuming ID is 5):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 35, "id": 5}' http://127.0.0.1:5000/add_data
```
### Deleting Specific Data by ID (Assuming ID is 3):
```bash
curl -X DELETE http://127.0.0.1:5000/delete_data/3
```
## Conclusion
This guide provides you with a quick reference on how to interact with your Flask API using cURL commands for various operations. Make sure your Flask server is running before executing these commands.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for details.

