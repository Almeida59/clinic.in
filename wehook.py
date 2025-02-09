from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7567604688:AAECILv30v6FhA2W-Z-8uG98V32lmybmSVg"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Log para inspecionar o payload recebido
        print("Payload recebido: ", request.data)

        # Carrega o JSON recebido
        payload = request.get_json(force=True)
        print("JSON Decodificado: ", payload)

        # Extrai informações da mensagem
        chat_id = payload['message']['chat']['id']
        received_text = payload['message']['text']

        # Envia uma resposta automática
        send_message(chat_id, f"Você disse: {received_text}")

        return "OK", 200
    except Exception as e:
        print(f"Erro no webhook: {e}")
        return "Erro no webhook", 500

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
