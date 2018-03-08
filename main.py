import socket
from client import Client

def sendback(data):
    """Sends the message back to all the users"""
    for client in clients:
        client.sendData(data)

def parse(data,socket,address):
    """We define first the HEAD code, the head is at the beginning of each packet and means the type
    of information de packet holds, the BODY is the information and the type depends on the HEAD.
    The multiple BODY elements are divided by "-" """

    PLAYER_CONNECTION = "CO" #1 is the username
    PLAYER_DISCONNECTION = "DC"

    stringdata = data.decode("utf-8")
    #print("From ["+str(address[0])+"]: "+stringdata)
    listdata = stringdata.split("-")
    head = listdata[0]

    if head == PLAYER_CONNECTION: #The body, just after the HEAD is the username
        print("New player connected: "+listdata[1])
        client = Client(listdata[1],address,socket,clients,listdata[2],listdata[3]) #TODO: Checkout if clients is a object link or a new object in Client
        clients.append(client)
        client.informplayers()

    if head == PLAYER_DISCONNECTION: #The body, just after the HEAD is the username
        print("Player disconnected: "+listdata[1])
        for client in clients:
            if client.username == listdata[1]:
                clients.remove(client)
                break

    #In other cases, the server doesn't do anything but sends the information back to all other users, since the server is just a hub.

    sendback(data)




so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = ("localhost", 2055)  # 2055 is the game port
so.bind(serverAddress)

clients = []

print("Server online...")

while True:
    data, address = so.recvfrom(4096)
    parse(data,so,address)