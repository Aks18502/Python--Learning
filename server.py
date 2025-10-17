import socket
s=socket.socket()
s.bind(('localhost',1234))
s.listen()
conn,_=s.accept();
print(conn.recv(1024).decode())