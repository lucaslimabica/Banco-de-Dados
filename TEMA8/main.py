from flask import Flask, request, jsonify
from DatabaseManager import DatabaseManager

app = Flask(__name__) # Inicialização do Flask
db = DatabaseManager('sensors') # Inicialização do DatabaseManager

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    db.insert_data('my_table', data['columns'], data['values'])
    return jsonify({'status': 'success'}), 200

@app.route('/read', methods=['GET'])
def read():
    data = db.select_data('my_table', '*')
    return jsonify(data), 200

@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    db.update_data('my_table', data['set_column'], data['set_data'], data['where_column'], data['where_data'])
    return jsonify({'status': 'success'}), 200

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    db.delete_data('my_table', data['where_column'], data['where_data'])
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
