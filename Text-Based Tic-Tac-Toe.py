pos1 = ' '
pos2 = ' '
pos3 = ' '
pos4 = ' '
pos5 = ' '
pos6 = ' '
pos7 = ' '
pos8 = ' '
pos9 = ' '

gridDict = {1:pos1, 2:pos2, 3:pos3, 4:pos4, 5:pos5, 6:pos6, 7:pos7, 8:pos8, 9:pos9}


def drawGrid():

        print('\t')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + gridDict[1], gridDict[2] + ' ', gridDict[3] + ' '))
        print('       ║       ║       ')
        print(' ══════╬═══════╬═══════')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + gridDict[4], gridDict[5] + ' ', gridDict[6] + ' '))
        print('       ║       ║       ')
        print(' ══════╬═══════╬═══════')
        print('       ║       ║       ')
        print('   %s  ║   %s  ║   %s  ' % (' ' + gridDict[7], gridDict[8] + ' ', gridDict[9] + ' '))
        print('       ║       ║       ' + '\n')

def gameAI(playerFirst):
    from random import randint
    
    if playerFirst == False:
        return 5
    else:   
        if ((gridDict[2] == 'O' and gridDict[3] == 'O') or (gridDict[4] == 'O' and gridDict[7] == 'O') or (gridDict[5] == 'O' and gridDict[9] == 'O')) and gridDict[1] != 'X':
            return 1
        elif ((gridDict[1] == 'O' and gridDict[3] == 'O') or (gridDict[5] == 'O' and gridDict[8] == 'O')) and gridDict[2] != 'X':
            return 2
        elif ((gridDict[1] == 'O' and gridDict[2] == 'O') or (gridDict[6] == 'O' and gridDict[9] == 'O') or (gridDict[5] == 'O' and gridDict[7] == 'O')) and gridDict[3] != 'X':
            return 3
        elif ((gridDict[1] == 'O' and gridDict[7] == 'O') or (gridDict[5] == 'O' and gridDict[6] == 'O')) and gridDict[4] != 'X':
            return 4
        elif ((gridDict[1] == 'O' and gridDict[9] == 'O') or (gridDict[2] == 'O' and gridDict[8] == 'O') or (gridDict[3] == 'O' and gridDict[7] == 'O') or (gridDict[4] == 'O' and gridDict[6] == 'O')) and gridDict[5] != 'X':
            return 5
        elif ((gridDict[3] == 'O' and gridDict[9] == 'O') or (gridDict[4] == 'O' and gridDict[5] == 'O')) and gridDict[6] != 'X':
            return 6
        elif ((gridDict[1] == 'O' and gridDict[4] == 'O') or (gridDict[3] == 'O' and gridDict[5] == 'O') or (gridDict[8] == 'O' and gridDict[9] == 'O')) and gridDict[7] != 'X':
            return 7
        elif ((gridDict[2] == 'O' and gridDict[5] == 'O') or (gridDict[7] == 'O' and gridDict[9] == 'O')) and gridDict[8] != 'X':
            return 8
        elif ((gridDict[1] == 'O' and gridDict[5] == 'O') or (gridDict[3] == 'O' and gridDict[6] == 'O') or (gridDict[7] == 'O' and gridDict[8] == 'O')) and gridDict[9] != 'X':
            return 9
        
        while True:
            randInt = randint(1, 9)

            if gridDict[randInt] == 'O' or gridDict[randInt] == 'X':
                continue
            else:
                gridDict[randInt] = 'X'
                break

drawGrid()

print ('\n' + 'This is how the Tic-Tac-Toe grid looks like (starting from position 1 [top-left] all the way to position 9 [bottom-right]):')

haveWonO = False
haveWonX = False

counter = 0

while haveWonO == False or haveWonX == False:

    if counter > 8:
        break
    else:
        player1 = int(input("Player 1's turn. Please input where you want to place the 'O': "))
        gridDict[player1] = 'O'
        drawGrid()
        if ((gridDict[1] == 'O' and gridDict[2] == 'O' and gridDict[3] == 'O')
        or (gridDict[1] == 'O' and gridDict[4] == 'O' and gridDict[7] == 'O')
        or (gridDict[1] == 'O' and gridDict[5] == 'O' and gridDict[9] == 'O')
        or (gridDict[2] == 'O' and gridDict[5] == 'O' and gridDict[8] == 'O')
        or (gridDict[3] == 'O' and gridDict[6] == 'O' and gridDict[9] == 'O')
        or (gridDict[3] == 'O' and gridDict[5] == 'O' and gridDict[7] == 'O')
        or (gridDict[4] == 'O' and gridDict[5] == 'O' and gridDict[6] == 'O')
        or (gridDict[7] == 'O' and gridDict[8] == 'O' and gridDict[9] == 'O')):
            haveWonO = True
            break
        counter += 1
        
    if counter > 8:
        break
    else: 
        player2 = gameAI(True)
        gridDict[player2] = 'X'
        drawGrid()
        if ((gridDict[1] == 'X' and gridDict[2] == 'X' and gridDict[3] == 'X')
        or (gridDict[1] == 'X' and gridDict[4] == 'X' and gridDict[7] == 'X')
        or (gridDict[1] == 'X' and gridDict[5] == 'X' and gridDict[9] == 'X')
        or (gridDict[2] == 'X' and gridDict[5] == 'X' and gridDict[8] == 'X')
        or (gridDict[3] == 'X' and gridDict[6] == 'X' and gridDict[9] == 'X')
        or (gridDict[3] == 'X' and gridDict[5] == 'X' and gridDict[7] == 'X')
        or (gridDict[4] == 'X' and gridDict[5] == 'X' and gridDict[6] == 'X')
        or (gridDict[7] == 'X' and gridDict[8] == 'X' and gridDict[9] == 'X')):
            haveWonX = True
            break
        counter += 1


