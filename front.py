import threading
from flask_cors import CORS
from flask import Flask, request, jsonify
import send

app = Flask(__name__)
CORS(app)


@app.route('/send-message-one', methods=['POST'])
def send_message_one():
    data = request.get_json()

    username = data.get('username')
    description = data.get('description')
    decision = data.get('decision')

    send.send_one(username, description, decision)

    return jsonify({'message': 'Сообщение отправлено'})


@app.route('/send-message-all', methods=['POST'])
def send_message_all():
    data = request.get_json()

    description = data.get('description')
    decision = data.get('decision')

    t = threading.Thread(target=send.send_all, args=(description, decision))
    t.start()

    return jsonify({'message': 'Сообщение получено, будет отправлено'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
