#!/usr/bin/python3

# This is the Python 3.x client-sided script for a Chat Server.

from socket import socket, AF_INET, SOCK_STREAM, error

HOST = 'localhost'
PORT = 1337

serverAddress = (HOST, PORT)

Client_Socket = socket(family=AF_INET, type=SOCK_STREAM)

try:
    Client_Socket.connect(serverAddress)
    recvMessage = Client_Socket.recv(1024)
    print(recvMessage.decode(encoding='ascii'))

    userName = input('Please enter your name: ')
    userName = userName.encode(encoding='ascii')
    Client_Socket.send('Name: '.encode(encoding='ascii') + userName)

    while True:
        print('\n')
        message = input('{}: '.format(userName.decode(encoding='ascii')))
        Client_Socket.send(message.encode(encoding='ascii'))
except error:
    print('Sorry cannot connect to the Chat Server :(')
finally:
    Client_Socket.close()
