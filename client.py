import socket
s=socket.socket()
s.connect(('localhost',1234))
s.send(b"welcome to livewire")