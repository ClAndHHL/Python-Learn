import socket

s = socket.socket();
host = socket.gethostname();
port = 12344;
s.connect((host,port));
print s.recv(1024);
