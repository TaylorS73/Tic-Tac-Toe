import importlib
menuChoice = 0
menuCount = 0


while True:

    print('╔═════════════════════════════════════════════════╗')
    print('║                                                 ║')
    print('║                                                 ║')
    print('║    Hello please choose what you want to do:     ║')
    print('║                                                 ║')
    print('║                                                 ║')
    print('║     Single Player Mode [1]                      ║')
    print('║                                                 ║')
    print('║     Multi-Player Mode  [2]                      ║')
    print('║                                                 ║')
    print('║     Exit Game          [3]                      ║')
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
