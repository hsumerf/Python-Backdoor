#!/usr/bin/env python
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.184.151",4444))
s.send("\n[+] Connection Established\n")
return_data = s.recv(1024)
print(return_data)
s.close()
