#!/usr/bin/python3

# This is the Python 3.x server-sided script for a Chat Server.

from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread, currentThread

messageReceiver = []

nameDict = {}


def clientHandler():
    connection, clientAddr = Server_Socket.accept()
    print('{} is connected to the Chat Server.'.format(clientAddr))
    connection.send((
                     '\n' + 'Thank you for connecting' +
                     ' to the Chat Server.'
                    ).encode(encoding='ascii'))
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            if 'Name: ' in data.decode(encoding='ascii'):
                userName = data.decode(encoding='ascii')
                userName = str(userName)
                userName = str.replace(userName, 'Name: ', '')
                nameDict[str(clientAddr)] = userName
            print('Received Message: {}'.format(data.decode(encoding='ascii')))
            if data.decode(encoding='ascii') == 'This is the message receiver JKwuP89?!234swWIpd':
                messageReceiver.append(connection)
            for receiver in messageReceiver:
                if receiver == connection:
                    continue
                else:
                    if 'Name: ' not in data.decode(encoding='ascii'):
                        client = str(clientAddr).encode(encoding='ascii')
                        receiver.send(nameDict[client] + '> '.encode(encoding='ascii') + data)
        except error:
            print('{} disconnected from the chat server.'.format(clientAddr))
            break

HOST = 'localhost'
PORT = 1337

serverAddress = (HOST, PORT)

Server_Socket = socket(family=AF_INET, type=SOCK_STREAM)

Server_Socket.bind(serverAddress)

print("Chat Server has started on host '{}' (on port: {})".format(HOST, PORT))

Server_Socket.listen(7)

messageThread = Thread(name='Message_Thread', target=clientHandler)
messageThread.start()

th1 = Thread(target=clientHandler)
th2 = Thread(target=clientHandler)
th3 = Thread(target=clientHandler)
th4 = Thread(target=clientHandler)
th5 = Thread(target=clientHandler)
th6 = Thread(target=clientHandler)

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()


while True:
    if th1.isAlive() is False:
        th1 = Thread(target=clientHandler)
        th1.start()
    elif th2.isAlive() is False:
        th2 = Thread(target=clientHandler)
        th2.start()
    elif th3.isAlive() is False:
        th3 = Thread(target=clientHandler)
        th3.start()
    elif th4.isAlive() is False:
        th4 = Thread(target=clientHandler)
        th4.start()
    elif th5.isAlive() is False:
        th5 = Thread(target=clientHandler)
        th5.start()
    elif th6.isAlive() is False:
        th6 = Thread(target=clientHandler)
        th6.start()

Server_Socket.close()
