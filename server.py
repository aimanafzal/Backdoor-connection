import socket

HOST = '127.0.0.1'
PORT = 8081

new_port = input('Inpt Host Port (Blank if default')

if (new_port != "\n"):
    REMOTE_PORT = new_port

# BINDING THE IP TO THE PORT
# CREATING A SOCKET

server = socket.socket()
server.bind((HOST, PORT))

# STARTING THE LISTENER
print('[+] Server Started')
print('[+] Listening For the Client Connection...')
server.listen()

client, client_addr = server.accept()
print(f'[+] {client_addr} Client Connected to the Server')

# SENDING AND RECEIVING COMMANDS IN AN INFINITE LOOP
while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
