import logging
import time
from flask import Response

def get_system_status():
    return {"status": "OK", "camera_model": "Hikvision"}

def get_fake_snapshot():
    return Response(b"Fake Image Data", mimetype="image/jpeg")

def start_rtsp_stream():
    """
    Symuluje prosty serwer RTSP
    """
    logging.info("RTSP streaming started on port 554")
    while True:
        time.sleep(10)
        logging.info("RTSP: Oczekiwanie na połączenie")

def start_onvif_server():
    """
    Symuluje serwer ONVIF
    """
    logging.info("ONVIF server started on port 8080")
    while True:
        time.sleep(10)
        logging.info("Symulacja: Serwer ONVIF aktywny")