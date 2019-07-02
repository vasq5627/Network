# import socket library
import socket               
 
# create socket object
host = ''
# reserve a port on your computer
port = 1200  
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         

# Next bind to the port, coming from other computers on the network
socket.bind((host, port))        

# socket into listening mode
socket.listen(1)     
addr, connections = socket.accept()
print ('connected by' , addr)           
 
# a loop until we interrupt it 
while True:
 data = connections.recv(1024)
 if not data: break
 connections.sendall(data)
connections.close()
