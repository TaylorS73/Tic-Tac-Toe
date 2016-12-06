import importlib
menuChoice = 0
menuCount = 0


while True:

    print('╔═════════════════════════════════════════════════╗')
    print('║                                                 ║')
    print('║                 Tic-Tac-Toe                     ║')
    print('║                                                 ║')
    print('║    Hello please choose an option:               ║')
    print('║                                                 ║')
    print('║     [1]  Single Player Mode                     ║')
    print('║                                                 ║')
    print('║     [2]  Multi-Player Mode                      ║')
    print('║                                                 ║')
    print('║     [3]  Exit Game                              ║')
    print('║                                                 ║')
    print('║                                                 ║')
    print('╚═════════════════════════════════════════════════╝')

    menuChoice = int(input('-> '))

    if menuChoice == 1 and menuCount == 0:
        menuChoice = 0
        menuCount = 1
        import SinglePlayer
    elif menuChoice == 1 and menuCount == 1:
        importlib.reload(module=SinglePlayer)
    elif menuChoice == 2:
        print('You have chosen option number 2')
        break
    elif menuChoice == 3:
        break
    else:
        print('Sorry. There is no such option!')
