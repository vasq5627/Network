# Import socket module
import socket               

#getting the host
host = socket.gethostname()
#getting the portname
port = 1200

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
socket.connect((host,port))
socket.sendall(b'Hello')
#gathering the data
data = socket.recv(1024)
#closing our socket
socket.close()
#printing the message
print('recieved', repr(data))
