import socket


HOST = '192.168.0.113'
PORT = 55555

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST,PORT))

SERVER.listen()

client, address = SERVER.accept()

while True:
    print(f"Connected to {address}")
    cmd_input = input("enter command: ")
    client.send(cmd_input.encode("utf-8"))
    print(client.recv(1024).decode('utf-8'))
