Servidor e Cliente TCP/UDP com Threads
Este projeto implementa um servidor que lida com conexões TCP e mensagens UDP simultaneamente, utilizando Python e threads. O servidor escuta em duas portas distintas, processando múltiplas conexões TCP e mensagens UDP de forma eficiente.

Estrutura do Projeto
-servidor.py: Servidor que lida com conexões TCP e UDP.
-cliente.py: Cliente que permite enviar mensagens para o servidor usando TCP ou UDP.
-servidor_tcp.py (opcional): Servidor separado para conexões TCP.
-servidor_udp.py (opcional): Servidor separado para mensagens UDP.
Requisitos
-Python 3 instalado.
-Conhecimentos básicos de terminal/linha de comando.
Como Executar
Passo 1: Executar o Servidor
Abra um terminal e navegue até o diretório onde os arquivos estão salvos.
Execute o servidor combinado com o comando:
bash
Copiar código

python3 servidor.py
O servidor começará a escutar nas portas 5000 (TCP) e 5001 (UDP).
Passo 2: Usar o Cliente
Abra um novo terminal.
Execute o cliente:
bash
Copiar código
python3 cliente.py
Siga as instruções do cliente:
-Escolha o protocolo (TCP ou UDP).
-Digite a mensagem que deseja enviar ao servidor.
O cliente enviará a mensagem e exibirá a resposta do servidor.
Exemplo de Uso
-Cliente envia uma mensagem "Olá servidor!" usando TCP:
Resposta esperada: "TCP: Olá servidor!"
-Cliente envia uma mensagem "Ping" usando UDP:
Resposta esperada: "UDP: Ping"
Finalizando o Servidor
Para parar o servidor, volte ao terminal onde ele está rodando e pressione Ctrl + C.

Estrutura de Arquivos
-servidor.py: Servidor combinado TCP e UDP.
-cliente.py: Cliente para interagir com o servidor.
-servidor_tcp.py e servidor_udp.py: Servidores separados para cada protocolo (opcional).
-README.md: Este arquivo de instruções.
Contribuição
Sinta-se à vontade para fazer um fork e enviar pull requests com melhorias ou sugestões.
