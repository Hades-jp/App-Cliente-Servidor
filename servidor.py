import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'
TCP_PORT = 5000
UDP_PORT = 5001

def handle_tcp_connection(conn, addr):
    print(f"Conexão TCP estabelecida com {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            mensagem = data.decode()
            print(f"Recebido (TCP): {mensagem} de {addr}")
            resposta = "TCP:" + mensagem
            conn.sendall(resposta.encode())
    except ConnectionResetError:
        print(f"Conexão TCP com {addr} foi fechada inesperadamente.")
    finally:
        conn.close()
        print(f"Conexão TCP com {addr} encerrada.")

def handle_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, UDP_PORT))
    print(f"Servidor UDP ouvindo na porta {UDP_PORT}...")

    while True:
        data, addr = udp_socket.recvfrom(1024)
        mensagem = data.decode()
        print(f"Recebido (UDP): {mensagem} de {addr}")
        resposta = "UDP:" + mensagem
        udp_socket.sendto(resposta.encode(), addr)

def tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST, TCP_PORT))
    tcp_socket.listen()
    print(f"Servidor TCP ouvindo na porta {TCP_PORT}...")

    while True:
        conn, addr = tcp_socket.accept()
        tcp_thread = threading.Thread(target=handle_tcp_connection, args=(conn, addr))
        tcp_thread.start()

if __name__ == "__main__":
    udp_thread = threading.Thread(target=handle_udp)
    udp_thread.start()

    tcp_server()
