import socket

# Configurando o servidor TCP
HOST = '127.0.0.1'
PORT = 5000

# Criação do  socket TCP
server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_tcp.bind((HOST, PORT))
server_tcp.listen()

print("Servidor TCP ouvindo na porta 5000...")

while True:
    conn, addr = server_tcp.accept()
    print(f"Conexão estabelecida com {addr}")

    # Recebe a mensagem do cliente
    mensagem = conn.recv(1024).decode()
    print(f"Recebido (TCP): {mensagem}")

    # Envia a resposta com o prefixo "TCP:"
    resposta = "TCP:" + mensagem
    conn.send(resposta.encode())

    # Encerra a conexão
    conn.close()
