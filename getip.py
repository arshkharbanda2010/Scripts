import socket
import sys	
host=str(raw_input("Enter the url: "))
ip=socket.gethostbyname(host)
print(ip)

#usage:-

#python getip.py 
#<hostname>
