from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = 'sensors.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Exemplo de rota para obter todas as unidades
@app.route('/units', methods=['GET'])
def get_units():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Unit')
    units = cursor.fetchall()
    conn.close()
    return jsonify({'units': [dict(unit) for unit in units]})

# Exemplo de rota para adicionar uma nova unidade
@app.route('/units', methods=['POST'])
def add_unit():
    data = request.get_json()
    name = data['name']
    description = data['description']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Unit (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Unit added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
