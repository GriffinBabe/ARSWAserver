import socket
from client import Client


def adduser(username, address):
    for client in clients:
        if client.username == username:
            return
    clients.append(Client(username, address))
    print('New client detected with username: ' + username)


def parse(data, so):
    print(data)
    so.sendTo(data, address)


so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = ('localhost', 2055)  # 2055 is the game port
so.bind(serverAddress)

clients = []

while True:
    print('Waiting for clients to log in...')
    data, address = so.recv(4096)
    parse(data)
