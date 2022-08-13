import client

def on_receive(data):
    print(data)

client = client.Client("http://127.0.0.1:5000", on_receive=on_receive)
for i in range(10):
    client.send(i)
client.on_receive = on_receive