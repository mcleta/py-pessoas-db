from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://admin:admin@clustertest.1i6swo3.mongodb.net/?retryWrites=true&w=majority')
db = client['db-teste']
collection = db["pessoas"]

# Rota para recuperar dados (método GET)
@app.route('/pessoas', methods=['GET'])
def get_data():
    data = collection.find()

    result = []
    for item in data:
        result.append({
            'id': str(item['_id']),
            'name': item['name'],
            'age': item['age']
        })

    return jsonify(result)

# Rota para enviar dados (método POST)
@app.route('/pessoas', methods=['POST'])
def add_data():
    if not request.is_json:
        return jsonify({'error': 'Invalid JSON'}), 400

    name = request.json.get('name')
    age = request.json.get('age')

    data = {
        'name': name,
        'age': age
    }
    collection.insert_one(data)

    return jsonify({'message': 'Documento adicionado com sucesso!'})

# Executa o servidor Flask
if __name__ == '__main__':
    app.run()
