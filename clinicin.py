from flask import Flask, request
import telebot
import os

# Configurações principais
TELEGRAM_TOKEN = "7567604688:AAECILv30v6FhA2W-Z-8uG98V32lmybmSVg"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Inicializa o app Flask
app = Flask(__name__)

# Função para lidar com mensagens recebidas e enviar respostas predefinidas
def processar_mensagem(mensagem):
    """
    Retorna uma resposta predefinida baseada na mensagem recebida.
    """
    mensagem = mensagem.lower()
    if "olá" in mensagem or "oi" in mensagem:
        return "Olá! Como posso ajudar você hoje?"
    elif "marcar consulta" in mensagem:
        return "Claro! Por favor, me informe o seu nome completo e a especialidade desejada."
    elif "horário" in mensagem:
        return "Estamos disponíveis de segunda a sexta, das 8h às 18h."
    else:
        return "Desculpe, não entendi sua solicitação. Poderia reformular?"

# Manipulador de mensagens do bot Telegram
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    """
    Recebe mensagens dos usuários e responde com base em regras predefinidas.
    """
    user_id = message.chat.id
    incoming_msg = message.text.strip()
    
    print(f"Mensagem recebida de {user_id}: {incoming_msg}")
    
    # Obtém resposta predefinida
    resposta = processar_mensagem(incoming_msg)
    
    # Envia a resposta ao usuário
    bot.send_message(user_id, resposta)

# Rota do webhook para integração com o Telegram
@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Recebe atualizações do Telegram via Webhook e as processa.
    """
    try:
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "", 200
    except Exception as e:
        print(f"Erro no webhook: {e}")
        return "Erro no webhook", 500

# Inicialização do app Flask
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
