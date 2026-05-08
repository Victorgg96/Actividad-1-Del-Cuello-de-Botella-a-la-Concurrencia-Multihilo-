import socket
import time
from datetime import datetime


HOST = "127.0.0.1"
PORT = 8000


def timestamp():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]  # milisegundos


def main():
    print(f"[{timestamp()}] Conectando a {HOST}:{PORT} ...")
    inicio = time.perf_counter()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[{timestamp()}] Conexión establecida. Enviando mensaje ...")
        s.sendall(b"hola\n")

        respuesta = s.recv(1024)
        fin = time.perf_counter()

    latencia = fin - inicio
    print(f"[{timestamp()}] Respuesta recibida: {respuesta.decode().strip()!r}")
    print(f"[{timestamp()}] Latencia total: {latencia:.2f} s")


if __name__ == "__main__":
    main()
