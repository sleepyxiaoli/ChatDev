import logging
import requests
import os
from flask import Flask, send_from_directory, request, jsonify
import argparse
import socket

app = Flask(__name__, static_folder='static')
app.logger.setLevel(logging.ERROR)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
messages = []
port = [8000]  # Default port


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def send_msg(role, text):
    try:
        data = {"role": role, "text": text}
        response = requests.post(
            f"http://127.0.0.1:{port[-1]}/send_message", json=data)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send message: {e}")
        return False


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chain_visualizer")
def chain_visualizer():
    return send_from_directory("static", "chain_visualizer.html")


@app.route("/replay")
def replay():
    return send_from_directory("static", "replay.html")


@app.route("/get_messages")
def get_messages():
    return jsonify(messages)


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data or 'role' not in data or 'text' not in data:
        return jsonify({"error": "Invalid request"}), 400

    role = data.get("role")
    text = data.get("text")
    avatarUrl = find_avatar_url(role)

    message = {"role": role, "text": text, "avatarUrl": avatarUrl}
    messages.append(message)
    return jsonify(message), 200


def find_avatar_url(role):
    role = role.replace(" ", "%20")
    avatar_filename = f"avatars/{role}.png"
    static_path = os.path.join(app.static_folder, avatar_filename)

    # Check if avatar actually exists
    if not os.path.exists(static_path):
        return "/static/avatars/default.png"  # Fallback to default avatar

    return f"/static/{avatar_filename}"


if __name__ == "__main__":
    print(f"Attempting to start server on port {port[-1]}...")  # 调试信息
    try:
        app.run(host='0.0.0.0', port=port[-1], debug=True)  # 强制指定参数
    except Exception as e:
        print(f"Failed to start server: {e}")  # 捕获异常
