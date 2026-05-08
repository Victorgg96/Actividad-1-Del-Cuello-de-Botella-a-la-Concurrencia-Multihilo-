import socket
import threading
import time
from datetime import datetime


HOST = "127.0.0.1"
PORT = 8000


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def manejar_cliente(conn, addr):
    hilo = threading.current_thread().name
    print(f"[{timestamp()}] [{hilo}] Atendiendo a {addr[0]}:{addr[1]}")
    print(f"[{timestamp()}] [{hilo}] Iniciando procesamiento (sleep 10s) ...")

    with conn:
        time.sleep(10)  # ocurre en su propio hilo; no bloquea al hilo principal
        conn.sendall(b"OK - Procesado\n")
        print(f"[{timestamp()}] [{hilo}] Respuesta enviada a {addr[0]}:{addr[1]}. Conexión cerrada.\n")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(5)
        print(f"[{timestamp()}] Servidor CONCURRENTE escuchando en {HOST}:{PORT}")
        print(f"[{timestamp()}] Modelo: un hilo por cliente (thread-per-client).\n")

        try:
            while True:
                # El hilo principal solo hace accept(); delega inmediatamente.
                conn, addr = srv.accept()
                t = threading.Thread(
                    target=manejar_cliente,
                    args=(conn, addr),
                    daemon=True,  # muere cuando el proceso principal termina
                )
                t.start()
                print(f"[{timestamp()}] [MainThread] Hilo lanzado: {t.name} para {addr[0]}:{addr[1]}")

        except KeyboardInterrupt:
            print(f"\n[{timestamp()}] Servidor detenido por el usuario.")


if __name__ == "__main__":
    main()
