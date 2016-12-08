import os

filePath = input('Please input your Python 3.5.2 installation directory: ')

filePath = filePath + os.path.normpath('/python.exe')

print(filePath)

f = open('Run Server.bat', 'w')

f.write('@echo off' + '\n')

f.write('COLOR 3E' + '\n')

f.write(filePath + ' ' + 'Game_Server.py' + '\n')

f.write('PAUSE' + '\n')

f.close()


f = open('Run Client.bat', 'w')

f.write('@echo off' + '\n')

f.write('COLOR 3E' + '\n')

f.write(filePath + ' ' + 'Game_Client.py' + '\n')

f.write('PAUSE' + '\n')

f.close()
