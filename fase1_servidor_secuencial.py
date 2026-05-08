import socket
import time
from datetime import datetime


HOST = "127.0.0.1"
PORT = 8000


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(5)
        print(f"[{timestamp()}] Servidor SECUENCIAL escuchando en {HOST}:{PORT}")
        print(f"[{timestamp()}] Solo se atiende UN cliente a la vez.\n")

        try:
            while True:
                # Bloqueante: espera aquí hasta que llegue una conexión.
                # Mientras duerme atendiendo al cliente 1, el cliente 2
                # queda represado en el backlog TCP del kernel.
                conn, addr = srv.accept()
                print(f"[{timestamp()}] Conexión aceptada de {addr[0]}:{addr[1]}")
                print(f"[{timestamp()}] Iniciando procesamiento (sleep 10s) ...")

                with conn:
                    time.sleep(10)  # simula trabajo pesado bloqueante
                    conn.sendall(b"OK - Procesado\n")
                    print(f"[{timestamp()}] Respuesta enviada a {addr[0]}:{addr[1]}. Conexión cerrada.\n")

        except KeyboardInterrupt:
            print(f"\n[{timestamp()}] Servidor detenido por el usuario.")


if __name__ == "__main__":
    main()
