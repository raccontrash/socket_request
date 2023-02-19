import socket

# just a exercise

# defining target
target_host = "www.instagram.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: instagram.com\r\n\r\n")

# receive some data
responde = client.recv(4096)

print(responde)
