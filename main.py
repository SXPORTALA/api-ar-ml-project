from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'registro.json')


# Carrega dados do arquivo ou inicia lista vazia
def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=4)

# GET - todos os registros
@app.route('/dados_ar', methods=['GET'])
def listar_dados():
    dados = carregar_dados()
    return jsonify(dados)

# GET - registro específico
@app.route('/dados_ar/<int:id>', methods=['GET'])
def obter_dado(id):
    dados = carregar_dados()
    for item in dados:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({'erro': 'Registro não encontrado'}), 404

# POST - adicionar novo registro
@app.route('/dados_ar', methods=['POST'])
def adicionar_dado():
    dados = carregar_dados()
    novo = request.get_json()

    if not all(k in novo for k in ['estado_ar', 'nivel_poluentes', 'estado_visita']):
        return jsonify({'erro': 'Campos obrigatórios: estado_ar, nivel_poluentes, estado_visita'}), 400

    novo['id'] = len(dados) + 1
    dados.append(novo)
    salvar_dados(dados)
    return jsonify(novo), 201

# Inicia servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

