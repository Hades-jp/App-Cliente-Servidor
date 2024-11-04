import socket

HOST = '127.0.0.1'

while True:
    # Escolhendo o protocolo e a mensagem
    protocolo = input("Digite o protocolo (TCP ou UDP): ").strip().upper()
    mensagem = input("Digite a mensagem para o servidor: ")

    if protocolo == 'TCP':
        PORT = 5000
        # Criação do socket TCP e conxão com o servidor
        client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_tcp.connect((HOST, PORT))

        # Envia a mensagem
        client_tcp.send(mensagem.encode())
        resposta = client_tcp.recv(1024).decode()

        print("Resposta do servidor:", resposta)

        # Encerra o socket
        client_tcp.close()

    elif protocolo == 'UDP':
        PORT = 5001
        # Cria o socket UDP
        client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Envia a mensagem
        client_udp.sendto(mensagem.encode(), (HOST, PORT))
        resposta, _ = client_udp.recvfrom(1024)

        print("Resposta do servidor:", resposta.decode())
    
    else:
        print("Protocolo inválido! Escolha TCP ou UDP.")
