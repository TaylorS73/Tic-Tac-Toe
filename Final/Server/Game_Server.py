#!/usr/bin/python3

from socket import socket, AF_INET, SOCK_STREAM, error
from threading import Thread

# clientList = [client1, client2]
# gameRoom['Room-1'] = clientList
# clientList.clear()
# gameRoom = {'Room-1': [client1, client2]}

clientList = []

gameRoom = {}


def clientHandler():
    count = 0
    connection, clientAddr = Server_Socket.accept()

    if len(clientList) == 0:
        clientList.append(connection)
    elif len(clientList) == 1 and clientList[0] != connection:
        clientList.append(connection)
        clientList[0].send('X'.encode(encoding='ascii'))
        clientList[0].send('Your Turn.'.encode(encoding='ascii'))
        clientList[1].send('O'.encode(encoding='ascii'))
        count += 1
        gameRoom['Room-{}'.format(len(gameRoom)+1)] = clientList.copy()
        clientList.clear()

    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            else:
                if data.decode(encoding='ascii') == 'Game has ended.':
                    for room in gameRoom:
                        if gameRoom[room][0] == connection:
                            gameRoom[room][1].send(data)
                        elif gameRoom[room][1] == connection:
                            gameRoom[room][0].send(data)
                for i in range(1, 10):
                    if data.decode(encoding='ascii') == ascii(i):
                        for room in gameRoom:
                            if gameRoom[room][0] == connection:
                                gameRoom[room][1].send(data)
                                gameRoom[room][1].send("Your Turn.".encode(encoding='ascii'))
                            elif gameRoom[room][1] == connection:
                                gameRoom[room][0].send(data)
                                gameRoom[room][0].send("Your Turn.".encode(encoding='ascii'))
        except error:
            print('{} disconnected from the game server.'.format(clientAddr))
            break

HOST = 'localhost'
PORT = 12345

serverAddress = (HOST, PORT)

Server_Socket = socket(family=AF_INET, type=SOCK_STREAM)

Server_Socket.bind(serverAddress)

print("Game Server has started on host '{}' (on port: {})".format(HOST, PORT))

numOfAllowedClients = 10

Server_Socket.listen(numOfAllowedClients)

threadDict = {}

for i in range(numOfAllowedClients):
    threadDict['Thread{}'.format(i)] = Thread(target=clientHandler)
    threadDict['Thread{}'.format(i)].start()
    print(threadDict['Thread{}'.format(i)])

while True:
    for thread in threadDict:
        if threadDict[thread].isAlive() is False:
            threadDict[thread] = Thread(target=clientHandler)
            threadDict[thread].start()
