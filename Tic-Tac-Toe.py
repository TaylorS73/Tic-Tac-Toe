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

print ('\n' + 'This is how the Tic-Tac-Toe grid looks like (starting from position 1 [top-left] all the way to position 9 [bottom-right]):')

drawGrid()

