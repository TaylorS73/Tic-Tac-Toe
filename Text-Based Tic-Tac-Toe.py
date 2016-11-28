import time, sys
from random import randint
#this will allow the user to enter in X and O into this grid spaces
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
#if player has three Xs in a row haveWonX will become true triggering the if statement and the bottom on the code 
haveWonO = False
haveWonX = False

counter = 0 # the counter counts how many moves there have been. If there has been 9 moves it has to be a tie.
def gameAI():

'''this will lay out the grid for the tic tac toe game'''   
    if ((gridDict[2] == 'X' and gridDict[3] == 'X') or (gridDict[4] == 'X' and gridDict[7] == 'X') or (gridDict[5] == 'X' and gridDict[9] == 'X')) and gridDict[1] != 'O':
        return 1
    elif ((gridDict[1] == 'X' and gridDict[3] == 'X') or (gridDict[5] == 'X' and gridDict[8] == 'X')) and gridDict[2] != 'O':
        return 2
    elif ((gridDict[1] == 'X' and gridDict[2] == 'X') or (gridDict[6] == 'X' and gridDict[9] == 'X') or (gridDict[5] == 'X' and gridDict[7] == 'X')) and gridDict[3] != 'O':
        return 3
    elif ((gridDict[1] == 'X' and gridDict[7] == 'X') or (gridDict[5] == 'X' and gridDict[6] == 'X')) and gridDict[4] != 'O':
        return 4
    elif ((gridDict[1] == 'X' and gridDict[9] == 'X') or (gridDict[2] == 'X' and gridDict[8] == 'X') or (gridDict[3] == 'X' and gridDict[7] == 'X') or (gridDict[4] == 'X' and gridDict[6] == 'X')) and gridDict[5] != 'O':
        return 5
    elif ((gridDict[3] == 'X' and gridDict[9] == 'X') or (gridDict[4] == 'X' and gridDict[5] == 'X')) and gridDict[6] != 'O':
        return 6
    elif ((gridDict[1] == 'X' and gridDict[4] == 'X') or (gridDict[3] == 'X' and gridDict[5] == 'X') or (gridDict[8] == 'X' and gridDict[9] == 'X')) and gridDict[7] != 'O':
        return 7
    elif ((gridDict[2] == 'X' and gridDict[5] == 'X') or (gridDict[7] == 'X' and gridDict[9] == 'X')) and gridDict[8] != 'O':
        return 8
    elif ((gridDict[1] == 'X' and gridDict[5] == 'X') or (gridDict[3] == 'X' and gridDict[6] == 'X') or (gridDict[7] == 'X' and gridDict[8] == 'X')) and gridDict[9] != 'O':
        return 9
        
    while True:
        randInt = randint(1, 9)

        if gridDict[randInt] == 'X' or gridDict[randInt] == 'O':
            continue
        else:
            gridDict[randInt] = 'O'
            break
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

print ('\n' + 'This is how the Tic-Tac-Toe grid looks like (starting from position 1 [top-left] all the way to position 9 [bottom-right]):')

drawGrid()

while haveWonO == False or haveWonX == False:

    if counter > 8:
        break
    else:
        player = int(input("Player 1's turn. Please input where you want to place the 'X': "))
        gridDict[player] = 'X'
        drawGrid()
        if ((gridDict[1] == 'X' and gridDict[2] == 'X' and gridDict[3] == 'X')
        or (gridDict[1] == 'X' and gridDict[4] == 'X' and gridDict[7] == 'X')
        or (gridDict[1] == 'X' and gridDict[5] == 'X' and gridDict[9] == 'X')
        or (gridDict[2] == 'X' and gridDict[5] == 'X' and gridDict[8] == 'X')
        or (gridDict[3] == 'X' and gridDict[6] == 'X' and gridDict[9] == 'X')
        or (gridDict[3] == 'X' and gridDict[5] == 'X' and gridDict[7] == 'X')
        or (gridDict[4] == 'X' and gridDict[5] == 'X' and gridDict[6] == 'X')
        or (gridDict[7] == 'X' and gridDict[8] == 'X' and gridDict[9] == 'X')):
            haveWonO = True
            break
        counter += 1


    if counter > 8:
        break
    else:
        print ("This is the computer's turn.")
        print ('\n')
        time.sleep(0.5)
        sys.stdout.write('Thinking')
        time.sleep(0.2)
        sys.stdout.write('.')
        time.sleep(0.2)
        sys.stdout.write('.')
        time.sleep(0.2)
        sys.stdout.write('.')
        time.sleep(0.2)
        sys.stdout.write('.')
        time.sleep(0.2)
        sys.stdout.write('.')

        print ('\n')
        
        computer = gameAI()
        gridDict[computer] = 'O'
        drawGrid()
        if ((gridDict[1] == 'O' and gridDict[2] == 'O' and gridDict[3] == 'O')
        or (gridDict[1] == 'O' and gridDict[4] == 'O' and gridDict[7] == 'O')
        or (gridDict[1] == 'O' and gridDict[5] == 'O' and gridDict[9] == 'O')
        or (gridDict[2] == 'O' and gridDict[5] == 'O' and gridDict[8] == 'O')
        or (gridDict[3] == 'O' and gridDict[6] == 'O' and gridDict[9] == 'O')
        or (gridDict[3] == 'O' and gridDict[5] == 'O' and gridDict[7] == 'O')
        or (gridDict[4] == 'O' and gridDict[5] == 'O' and gridDict[6] == 'O')
        or (gridDict[7] == 'O' and gridDict[8] == 'O' and gridDict[9] == 'O')):
            haveWonX = True
            break
        counter += 1

if haveWonO == True:
    print ('Congratulations Player 1 won!')
elif haveWonX == True:
    print ('Congratulations Player 2 won!')
elif counter == 9:
    print('It is a tie!')
