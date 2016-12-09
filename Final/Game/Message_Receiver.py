#!/usr/bin/python3

# This is the Python 3.x client-sided message viewer script for a Chat Server.

from socket import socket, AF_INET, SOCK_STREAM, error

HOST = 'localhost'
PORT = 1337

serverAddress = (HOST, PORT)

Message_Socket = socket(family=AF_INET, type=SOCK_STREAM)

try:
    Message_Socket.connect(serverAddress)
    message = 'This is the message receiver JKwuP89?!234swWIpd'
    Message_Socket.send(message.encode(encoding='ascii'))
    while True:
        print('\n')
        recvMessage = Message_Socket.recv(1024)
        if not recvMessage:
            continue
        else:
            print(recvMessage.decode(encoding='ascii'))
except error:
    print('Sorry cannot connect to the Chat Server :(')
finally:
    Message_Socket.close()
