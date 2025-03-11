import logging
import time
from datetime import datetime
import pytz


def monitor_requests():
    """
    Monitoruje i analizuje przychodzące żądania pod kątem potencjalnych ataków
    """
    logging.info("Uruchomiono monitor ataków")

    while True:
        try:
            # Tutaj można dodać bardziej zaawansowaną logikę analizy logów
            with open("honeypot.log", "r") as f:
                lines = f.readlines()
                for line in lines[-10:]:  # Sprawdź ostatnie 10 linii
                    if "POST" in line or "GET" in line:
                        timestamp = datetime.now(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")
                        logging.info(f"[{timestamp}] Wykryto potencjalną aktywność: {line.strip()}")

            time.sleep(60)  # Sprawdzaj co minutę

        except Exception as e:
            logging.error(f"Błąd w monitorze ataków: {str(e)}")
            time.sleep(60)  # W przypadku błędu, poczekaj minutę przed ponowną próbą