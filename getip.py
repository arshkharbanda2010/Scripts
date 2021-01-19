import socket
import sys	
host=str(raw_input())
ip=socket.gethostbyname(host)
print(ip)