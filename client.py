class Client():

    def __init__(self,username,address,socket,clients,color,character):
        self.username=username
        self.color = color
        self.character = character
        self.online=True
        self.address = address
        self.socket = socket
        self.clients = clients #Other clients
        print("New client created. Username: "+self.username+".")

    def sendData(self,data): #Sends the data to this user
        #print("To ["+self.address[0]+"]: "+data.decode("utf-8"))
        self.socket.sendto(data,self.address)

    def informplayers(self): #Inform the freshly connected player all the players that came before
        for client in self.clients:
            if client != self:
                stringdata = "CO@"+client.username+"@"+client.color+"@"+client.character+"@"+str(0)+"@"+str(0)
                data = stringdata.encode("utf-8")
                self.sendData(data)
