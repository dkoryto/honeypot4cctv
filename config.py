import os
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Konfiguracja sieci
NETWORK_CONFIG = {
    'IP': os.getenv('HONEYPOT_IP', '0.0.0.0'),
    'SUBNET': os.getenv('HONEYPOT_SUBNET', '255.255.255.0'),
    'GATEWAY': os.getenv('HONEYPOT_GATEWAY', '192.168.1.1')
}

# Konfiguracja kamery
CAMERA_MODEL = os.getenv('CAMERA_MODEL', 'hikvision')
HONEYPOT_NAME = os.getenv('HONEYPOT_NAME', 'Camera-01')

# Konfiguracja Telegrama
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')