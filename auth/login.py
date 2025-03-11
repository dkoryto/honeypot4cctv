import logging
from flask import request, jsonify
from datetime import datetime
import pytz


def handle_login():
    """
    Obsługuje próby logowania do honeypota i zapisuje je w logach
    """
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    ip_address = request.remote_addr

    # Logowanie próby logowania
    timestamp = datetime.now(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")
    logging.warning(f"[{timestamp}] Próba logowania z IP {ip_address} - Login: {username}, Hasło: {password}")

    # Zawsze zwracaj błąd logowania
    response = {
        "error": {
            "code": "unauthorized",
            "message": "Invalid username or password"
        }
    }

    return jsonify(response), 401