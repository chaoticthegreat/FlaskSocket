import server

def on_receive(data, clientId, clients):
    print(data, clientId)

server.on_receive = on_receive
server.run()