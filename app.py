import os
import logging
import threading
from flask import Flask
from auth.login import handle_login
from camera import get_system_status, get_fake_snapshot, start_rtsp_stream, start_onvif_server
from network import listen_port
from attack_monitor import monitor_requests
from telegram_bot import start_telegram_bot
from config import NETWORK_CONFIG, CAMERA_MODEL, HONEYPOT_NAME

app = Flask(__name__)
logging.basicConfig(filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s")


@app.route("/")
def home():
    return f"{CAMERA_MODEL.capitalize()} Camera Honeypot - {HONEYPOT_NAME} - IP: {NETWORK_CONFIG['IP']}"


@app.route("/doc/page/login.asp", methods=["GET", "POST"])
def login():
    return handle_login()


@app.route("/ISAPI/System/status")
def system_status():
    return get_system_status()


@app.route("/ISAPI/Streaming/channels/101/picture")
def fake_snapshot():
    return get_fake_snapshot()


if __name__ == "__main__":
    threads = [
        threading.Thread(target=listen_port, args=(22,), daemon=True),
        threading.Thread(target=listen_port, args=(443,), daemon=True),
        threading.Thread(target=listen_port, args=(554,), daemon=True),
        threading.Thread(target=listen_port, args=(8080,), daemon=True),
        threading.Thread(target=monitor_requests, daemon=True),
        threading.Thread(target=start_telegram_bot, daemon=True),
        threading.Thread(target=start_rtsp_stream, daemon=True),
        threading.Thread(target=start_onvif_server, daemon=True)
    ]

    for thread in threads:
        thread.start()

    app.run(host="0.0.0.0", port=80)
