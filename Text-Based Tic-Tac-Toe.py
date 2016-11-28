import time, sys
from random import randint

pos1 = ' '
pos2 = ' '
pos3 = ' '
pos4 = ' '
pos5 = ' '
pos6 = ' '
pos7 = ' '
pos8 = ' '
pos9 = ' '

grid = {1:pos1, 2:pos2, 3:pos3, 4:pos4, 5:pos5, 6:pos6, 7:pos7, 8:pos8, 9:pos9}

haveWonO = False
haveWonX = False

counter = 0
def gameAI():

#this will lay out the grid for the tic tac toe game      
    if ((grid[2] == 'X' and grid[3] == 'X') or (grid[4] == 'X' and grid[7] == 'X') or (grid[5] == 'X' and grid[9] == 'X')) and grid[1] != 'O':
        return 1
    elif ((grid[1] == 'X' and grid[3] == 'X') or (grid[5] == 'X' and grid[8] == 'X')) and grid[2] != 'O':
        return 2
    elif ((grid[1] == 'X' and grid[2] == 'X') or (grid[6] == 'X' and grid[9] == 'X') or (grid[5] == 'X' and grid[7] == 'X')) and grid[3] != 'O':
        return 3
    elif ((grid[1] == 'X' and grid[7] == 'X') or (grid[5] == 'X' and grid[6] == 'X')) and grid[4] != 'O':
        return 4
    elif ((grid[1] == 'X' and grid[9] == 'X') or (grid[2] == 'X' and grid[8] == 'X') or (grid[3] == 'X' and grid[7] == 'X') or (grid[4] == 'X' and grid[6] == 'X')) and grid[5] != 'O':
        return 5
    elif ((grid[3] == 'X' and grid[9] == 'X') or (grid[4] == 'X' and grid[5] == 'X')) and grid[6] != 'O':
        return 6
    elif ((grid[1] == 'X' and grid[4] == 'X') or (grid[3] == 'X' and grid[5] == 'X') or (grid[8] == 'X' and grid[9] == 'X')) and grid[7] != 'O':
        return 7
    elif ((grid[2] == 'X' and grid[5] == 'X') or (grid[7] == 'X' and grid[9] == 'X')) and grid[8] != 'O':
        return 8
    elif ((grid[1] == 'X' and grid[5] == 'X') or (grid[3] == 'X' and grid[6] == 'X') or (grid[7] == 'X' and grid[8] == 'X')) and grid[9] != 'O':
        return 9
        
    while True:
        randInt = randint(1, 9)

        if grid[randInt] == 'X' or grid[randInt] == 'O':
            continue
        else:
            grid[randInt] = 'O'
            break
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

print ('\n' + 'This is how the Tic-Tac-Toe grid looks like (starting from position 1 [top-left] all the way to position 9 [bottom-right]):')

drawGrid()

while haveWonO == False or haveWonX == False:

    if counter > 8:
        break
    else:
        player = int(input("Player 1's turn. Please input where you want to place the 'X': "))
        grid[player] = 'X'
        drawGrid()
        if ((grid[1] == 'X' and grid[2] == 'X' and grid[3] == 'X')
        or (grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X')
        or (grid[1] == 'X' and grid[5] == 'X' and grid[9] == 'X')
        or (grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X')
        or (grid[3] == 'X' and grid[6] == 'X' and grid[9] == 'X')
        or (grid[3] == 'X' and grid[5] == 'X' and grid[7] == 'X')
        or (grid[4] == 'X' and grid[5] == 'X' and grid[6] == 'X')
        or (grid[7] == 'X' and grid[8] == 'X' and grid[9] == 'X')):
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
        grid[computer] = 'O'
        drawGrid()
        if ((grid[1] == 'O' and grid[2] == 'O' and grid[3] == 'O')
        or (grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O')
        or (grid[1] == 'O' and grid[5] == 'O' and grid[9] == 'O')
        or (grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O')
        or (grid[3] == 'O' and grid[6] == 'O' and grid[9] == 'O')
        or (grid[3] == 'O' and grid[5] == 'O' and grid[7] == 'O')
        or (grid[4] == 'O' and grid[5] == 'O' and grid[6] == 'O')
        or (grid[7] == 'O' and grid[8] == 'O' and grid[9] == 'O')):
            haveWonX = True
            break
        counter += 1

if haveWonO == True:
    print ('Congratulations Player 1 won!')
elif haveWonX == True:
    print ('Congratulations Player 2 won!')
elif counter == 9:
    print('It is a tie!')
