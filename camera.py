import logging
import time
import subprocess
from flask import Response

def get_system_status():
    return {"status": "OK", "camera_model": "Hikvision"}

def get_fake_snapshot():
    return Response(b"Fake Image Data", mimetype="image/jpeg")

def start_rtsp_stream():
    logging.info("RTSP streaming started on port 554")
    cmd = [
        "ffmpeg", "-re", "-stream_loop", "-1", "-i", "sample.mp4",
        "-vcodec", "copy", "-f", "rtsp", "rtsp://0.0.0.0:554/live"
    ]
    subprocess.run(cmd)

def start_onvif_server():
    logging.info("ONVIF server started on port 8080")
    while True:
        time.sleep(10)  # Simulated ONVIF response