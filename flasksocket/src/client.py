import requests
from threading import Thread
import time

class Client:
    def __init__(self, server,on_receive=lambda data: None,time_delay=0.1):
        self.server = server
        self.id = requests.get(server + "/assign").text
        self.on_receive = on_receive
        self.time_delay = time_delay
        self.data = ""
        # self.clear()
    def on_receive_server(self):
        while True:
            data = self.receive()
            if data != "None":
                self.on_receive(data)
                self.clear()
            time.sleep(self.time_delay)
    def clear(self):
        requests.post(self.server + "/clear", json={"id": self.id})

    def send(self, data):
        requests.post(self.server, json={"id": self.id, "data": data})

    def receive(self):
        self.data = requests.get(self.server + "/" + self.id).text
        return self.data

    def __repr__(self):
        return f"Client({self.id})"

    def __str__(self):
        return f"Client({self.id})"
    def start(self):
        Thread(target=self.on_receive_server, daemon=True).start()
        

    # def __del__(self):
    #     requests.post(self.server + "/remove", json={"id": self.id})