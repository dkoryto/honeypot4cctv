import socket
import logging


def listen_port(port: int):  # Dodano parametr port
    """
    Nasłuchuje na określonym porcie i loguje próby połączenia

    Args:
        port (int): Numer portu do nasłuchiwania
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(5)
        logging.info(f"Nasłuchiwanie na porcie {port}")

        while True:
            client, address = sock.accept()
            logging.info(f"Próba połączenia na porcie {port} z adresu {address[0]}")
            client.close()

    except Exception as e:
        logging.error(f"Błąd podczas nasłuchiwania na porcie {port}: {str(e)}")
        return