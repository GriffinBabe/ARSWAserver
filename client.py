class Client():

    def __init__(self,username,address,socket,clients):
        self.username=username
        self.online=True
        self.address = address
        self.socket = socket
        self.clients = clients #Other clients

    def sendData(self,data): #Sends the data to this user
        self.socket.sendto(data,self.address)

    """
    def sendDataTo(self,data,address): #Sends the data to a particular user
        self.socket.sendto(data,address)
        
    def sendDataToAll(self,data): #Sends the data to all users but this user
        for client in self.clients:
            if client != self:
                self.sendDataTo(data,client.address)
    """
