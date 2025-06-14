import random
import requests

# Simular estado do ar baseado no nível de poluentes
def gerar_dado():
    nivel = random.randint(10, 150)  # em µg/m³

    if nivel < 50:
        estado_ar = "Bom"
        estado_visita = "Apto"
    elif nivel < 100:
        estado_ar = "Moderado"
        estado_visita = "Parcialmente Apto"
    else:
        estado_ar = "Ruim"
        estado_visita = "Inapto"

    return {
        "estado_ar": estado_ar,
        "nivel_poluentes": f"{nivel} µg/m³",
        "estado_visita": estado_visita
    }

# Enviar para a API
def enviar_para_api(dado):
    url = "http://localhost:5000/dados_ar"
    response = requests.post(url, json=dado)
    print("Enviado:", response.status_code, response.json())

if __name__ == "__main__":
    for _ in range(5):  # Envia 5 registros
        dado = gerar_dado()
        enviar_para_api(dado)
