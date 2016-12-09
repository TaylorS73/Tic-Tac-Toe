<<<<<<< HEAD
#!/usr/bin/python3

# This is the Python 3.x client-sided script for a Chat Server.

from socket import socket, AF_INET, SOCK_STREAM, error

# this will allow the user to enter in X and O into the grid spaces

grid = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

playerType = ''

opponent = ''

counter = 0


def drawGrid():

        print('\t')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + grid[1], grid[2] + ' ', grid[3] + ' '))
        print('       ║       ║       ')
        print(' ══════╬═══════╬═══════')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + grid[4], grid[5] + ' ', grid[6] + ' '))
        print('       ║       ║       ')
        print(' ══════╬═══════╬═══════')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + grid[7], grid[8] + ' ', grid[9] + ' '))
        print('       ║       ║       ' + '\n')

def checkWin(player):
    if ((grid[1] == player and grid[2] == player and grid[3] == player)
    or (grid[1] == player and grid[4] == player and grid[7] == player)
    or (grid[1] == player and grid[5] == player and grid[9] == player)
    or (grid[2] == player and grid[5] == player and grid[8] == player)
    or (grid[3] == player and grid[6] == player and grid[9] == player)
    or (grid[3] == player and grid[5] == player and grid[7] == player)
    or (grid[4] == player and grid[5] == player and grid[6] == player)
    or (grid[7] == player and grid[8] == player and grid[9] == player)):
        return True


HOST = 'localhost'
PORT = 12345

serverAddress = (HOST, PORT)

Client_Socket = socket(family=AF_INET, type=SOCK_STREAM)

try:
    Client_Socket.connect(serverAddress)
    Client_Socket.send('Ready'.encode(encoding='ascii'))
    while True:
        if counter > 8:
            print('It is a tie!')
            input('Please press any key to exit.')
            break
        elif checkWin(playerType) == True:
                print('You have won!')
                input('Please press any key to exit.')
                break
        elif checkWin(opponent) == True:
                print('You have lost!')
                input('Please press any key to exit.')
                break
        recvMessage = Client_Socket.recv(1024)
        if recvMessage.decode(encoding='ascii') == 'X':
            playerType = 'X'
            opponent = 'O'
        elif recvMessage.decode(encoding='ascii') == 'O':
            playerType = 'O'
            opponent = 'X'
        elif recvMessage.decode(encoding='ascii') == 'Your Turn.':
            userInput = int(input("Your turn. Please input where you want to place the '{}': ".format(playerType)))
            Client_Socket.send(str(userInput).encode(encoding='ascii'))
            grid[userInput] = playerType
            drawGrid()
            counter += 1
        for i in range(10):
            if recvMessage.decode(encoding='ascii') == ascii(i):
                if playerType == 'X':
                    pos = recvMessage.decode(encoding='ascii')
                    grid[int(pos)] = opponent
                    drawGrid()
                    counter += 1
                elif playerType == 'O':
                    pos = recvMessage.decode(encoding='ascii')
                    grid[int(pos)] = opponent
                    drawGrid()
                    counter += 1

except error:
    print('Sorry cannot connect to the Chat Server :(')
=======
#!/usr/bin/python3

# This is the Python 3.x client-sided script for a Chat Server.

from socket import socket, AF_INET, SOCK_STREAM, error

# this will allow the user to enter in X and O into the grid spaces

grid = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

playerType = ''

opponent = ''

counter = 0


def drawGrid():

        print('\t')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + grid[1], grid[2] + ' ', grid[3] + ' '))
        print('       ║       ║       ')
        print(' ══════╬═══════╬═══════')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + grid[4], grid[5] + ' ', grid[6] + ' '))
        print('       ║       ║       ')
        print(' ══════╬═══════╬═══════')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + grid[7], grid[8] + ' ', grid[9] + ' '))
        print('       ║       ║       ' + '\n')

def checkWin(player):
    if ((grid[1] == player and grid[2] == player and grid[3] == player)
    or (grid[1] == player and grid[4] == player and grid[7] == player)
    or (grid[1] == player and grid[5] == player and grid[9] == player)
    or (grid[2] == player and grid[5] == player and grid[8] == player)
    or (grid[3] == player and grid[6] == player and grid[9] == player)
    or (grid[3] == player and grid[5] == player and grid[7] == player)
    or (grid[4] == player and grid[5] == player and grid[6] == player)
    or (grid[7] == player and grid[8] == player and grid[9] == player)):
        return True


HOST = 'localhost'
PORT = 12345

serverAddress = (HOST, PORT)

Client_Socket = socket(family=AF_INET, type=SOCK_STREAM)

try:
    Client_Socket.connect(serverAddress)
    Client_Socket.send('Ready'.encode(encoding='ascii'))
    while True:
        if counter > 8:
            print('It is a tie!')
            input('Please press any key to exit.')
            break
        elif checkWin(playerType) == True:
                print('You have won!')
                input('Please press any key to exit.')
                break
        elif checkWin(opponent) == True:
                print('You have lost!')
                input('Please press any key to exit.')
                break
        recvMessage = Client_Socket.recv(1024)
        if recvMessage.decode(encoding='ascii') == 'X':
            playerType = 'X'
            opponent = 'O'
        elif recvMessage.decode(encoding='ascii') == 'O':
            playerType = 'O'
            opponent = 'X'
        elif recvMessage.decode(encoding='ascii') == 'Your Turn.':
            userInput = int(input("Your turn. Please input where you want to place the '{}': ".format(playerType)))
            Client_Socket.send(str(userInput).encode(encoding='ascii'))
            grid[userInput] = playerType
            drawGrid()
            counter += 1
        for i in range(10):
            if recvMessage.decode(encoding='ascii') == ascii(i):
                if playerType == 'X':
                    pos = recvMessage.decode(encoding='ascii')
                    grid[int(pos)] = opponent
                    drawGrid()
                    counter += 1
                elif playerType == 'O':
                    pos = recvMessage.decode(encoding='ascii')
                    grid[int(pos)] = opponent
                    drawGrid()
                    counter += 1

except error:
    print('Sorry cannot connect to the Chat Server :(')
>>>>>>> origin/master
