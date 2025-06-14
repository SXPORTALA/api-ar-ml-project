import requests

url = 'http://localhost:5000/dados_ar'

estado_ar = input("Digite o estado do ar: ")
nivel_poluentes = input("Digite o nível de poluentes (ex: 50 µg/m³): ")
estado_visita = input("Digite o estado para visita (ex: Apto/Inapto): ")

dados = {
    "estado_ar": estado_ar,
    "nivel_poluentes": nivel_poluentes,
    "estado_visita": estado_visita
}

resposta = requests.post(url, json=dados)

if resposta.status_code == 201:
    print("✅ Registro adicionado com sucesso!")
    print(resposta.json())
else:
    print("❌ Erro ao adicionar registro:")
    print(resposta.status_code, resposta.text)
