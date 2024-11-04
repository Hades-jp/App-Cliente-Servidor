import socket

# Configurando o servidor UDP
HOST = '127.0.0.1'
PORT = 5001

# Criação do socket UDP
server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_udp.bind((HOST, PORT))

print("Servidor UDP ouvindo na porta 5001...")

while True:
    # Recebe a mensagem do cliente
    mensagem, addr = server_udp.recvfrom(1024)
    mensagem = mensagem.decode()
    print(f"Recebido (UDP) de {addr}: {mensagem}")

    # Envia a resposta com o prefixo "UDP:"
    resposta = "UDP:" + mensagem
    server_udp.sendto(resposta.encode(), addr)
