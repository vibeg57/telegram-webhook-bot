from flask import Flask, request, jsonify

app = Flask(__name__)

# Главное меню и ответы
menu = {
    "История": "Лазурное — уютный поселок на берегу Черного моря...",
    "Домоводство": "Советы по уюту и экономии в доме...",
    'IT для "чайников"': "Простые советы по работе с компьютером и смартфоном.",
    "FAQ": "Здесь вы можете получить ответы на часто задаваемые вопросы.",
    "О боте": "Бот — помощник сайта vibegnews.tilda.ws"
}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message', '').strip()

    if user_message in menu:
        reply_text = menu[user_message]
    else:
        reply_text = (
            "Привет! Выберите раздел меню:\n"
            "- История\n"
            "- Домоводство\n"
            '- IT для "чайников"\n'
            "- FAQ\n"
            "- О боте"
        )

    # Формируем ответ с текстом и кнопками (если платформа поддерживает)
    response = {
        "reply": reply_text,
        "buttons": list(menu.keys())  # Кнопки с названиями разделов
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
