from flask import Flask,request
import requests
import random


app = Flask(__name__)
random.seed(random.randint(0, 1000000))

temporaryData = None

clients = {}
receiveFunction = lambda: None


@app.route('/', methods=['GET', 'POST'])

def main():
    global temporaryData, clients

    if request.method == "POST":

        temporaryData = request.json["data"]
        clientId = request.json["id"]

        on_receive(temporaryData, clientId, clients)

    elif request.method == "GET":
        pass
    return "None"
@app.route('/assign')
def idAssign():
    id=random.randint(10000000000000000,99999999999999999)
    clients[id] = "None"
    return str(id)
@app.route("/clear", methods=["POST"])
def clear_client_msg():
    clients[int(request.json["id"])] = "None"
    return "None"
@app.route("/<int:id>")
def client(id):
    if id in clients:
        return clients[id]
    return "None"
def remove_id(id):
    del clients[id]
def set_clients(client):
    global clients
    clients = client
def on_receive(data, clientId, clients):
    receiveFunction(data,clientId, clients)
def run():
    app.run(host='127.0.0.1', port=5000)