import socket

_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
_socket.connect(('00:21:07:00:55:5F', 1))
_socket.send(b"0")


while True:
    print(_socket.recv(1024))


_socket.close()













