import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for Lowe's services/products
lowes_data = [
    {'id': 1, 'service': 'Appliances', 'product': 'Cooktops', 'city': 'Arlington Heights', 'zipcode': '60005'},
    {'id': 2, 'service': 'Bathroom', 'product': 'Bathroom Remodeling', 'city': 'Naperville', 'zipcode': '60564'},
    {'id': 3, 'service': 'Exterior Home', 'product': 'Fencing', 'city': 'Northbrook', 'zipcode': '60062'},
    {'id': 4, 'service': 'Flooring', 'product': 'Carpet', 'city': 'Carol Stream', 'zipcode': '60188'},
    {'id': 5, 'service': 'Kitchen', 'product': 'Cabinets', 'city': 'Bolingbrook', 'zipcode': '60490'},
    {'id': 6, 'service': 'Kitchen', 'product': 'Countertops', 'city': 'Northbrook', 'zipcode': '60062'},
    {'id': 7, 'service': 'Exterior Home', 'product': 'Gutters', 'city': 'Bolingbrook', 'zipcode': '60490'},
    {'id': 8, 'service': 'Bathroom', 'product': 'Sinks & Faucets', 'city': 'Northbrook', 'zipcode': '60062'},
    {'id': 9, 'service': 'Appliances', 'product': 'Dishwashers', 'city': 'Arlington Heights', 'zipcode': '60005'},
    {'id': 10, 'service': 'Flooring', 'product': 'Hardwood Flooring', 'city': 'Carol Stream', 'zipcode': '60188'},
    {'id': 11, 'service': 'Bathroom', 'product': 'Toilets', 'city': 'Naperville', 'zipcode': '60564'},
    {'id': 12, 'service': 'Kitchen', 'product': 'Garbage Disposals', 'city': 'Bolingbrook', 'zipcode': '60490'},
    {'id': 13, 'service': 'Flooring', 'product': 'Tile Flooring', 'city': 'Naperville', 'zipcode': '60564'},
    {'id': 14, 'service': 'Appliances', 'product': 'Refrigerators', 'city': 'Arlington Heights', 'zipcode': '60005'},
    {'id': 15, 'service': 'Exterior Home', 'product': 'Roofing', 'city': 'Carol Stream', 'zipcode': '60188'}
]

# Home route
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Lowe's Home Improvement API</h1>
<p>A prototype API for Lowe's services and products.</p>'''

# Endpoint to return all data
@app.route('/api/v1/resources/lowes/all', methods=['GET'])
def api_all():
    return jsonify(lowes_data)

# Endpoint to return data by ID
@app.route('/api/v1/resources/lowes', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    for entry in lowes_data:
        if entry['id'] == id:
            results.append(entry)

    return jsonify(results)

# Endpoint to filter by service
@app.route('/api/v1/resources/lowes/service', methods=['GET'])
def api_service():
    if 'service' in request.args:
        service = request.args['service']
    else:
        return "Error: No service field provided. Please specify a service."

    results = [entry for entry in lowes_data if entry['service'].lower() == service.lower()]
    return jsonify(results)

# Endpoint to filter by product
@app.route('/api/v1/resources/lowes/product', methods=['GET'])
def api_product():
    if 'product' in request.args:
        product = request.args['product']
    else:
        return "Error: No product field provided. Please specify a product."

    results = [entry for entry in lowes_data if entry['product'].lower() == product.lower()]
    return jsonify(results)

# Endpoint to filter by city
@app.route('/api/v1/resources/lowes/city', methods=['GET'])
def api_city():
    if 'city' in request.args:
        city = request.args['city']
    else:
        return "Error: No city field provided. Please specify a city."

    results = [entry for entry in lowes_data if entry['city'].lower() == city.lower()]
    return jsonify(results)
# Endpoint to add a new service/product
@app.route('/api/v1/resources/lowes/service', methods=['POST'])
def add_service():
    new_service = request.get_json()

    if not all(k in new_service for k in ('id', 'service', 'product', 'city', 'zipcode')):
        return jsonify({"error": "Missing fields"}), 400

    lowes_data.append(new_service)
    
    return jsonify(new_service), 201  # 201 Created

# Endpoint to update an existing service/product
@app.route('/api/v1/resources/lowes/service/<int:id>', methods=['PUT'])
def update_service(id):
    service_to_update = next((entry for entry in lowes_data if entry['id'] == id), None)
    
    if service_to_update is None:
        return jsonify({"error": "Service not found"}), 404

    updated_data = request.get_json()
    service_to_update.update(updated_data)

    return jsonify(service_to_update), 200  # 200 OK

# Endpoint to delete a service/product
@app.route('/api/v1/resources/lowes/service/<int:id>', methods=['DELETE'])
def delete_service(id):
    global lowes_data  # Modify the global variable

    service_to_delete = next((entry for entry in lowes_data if entry['id'] == id), None)
    
    if service_to_delete is None:
        return jsonify({"error": "Service not found"}), 404

    lowes_data = [entry for entry in lowes_data if entry['id'] != id]
    
    return jsonify({"message": "Service deleted"}), 200  # 200 OK


# Run the app
if __name__ == "__main__":
    app.run()
