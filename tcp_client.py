#

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
to = ("127.0.0.1", 60000)
client.connect(to)

req = b"Hello World"
client.send(req)
