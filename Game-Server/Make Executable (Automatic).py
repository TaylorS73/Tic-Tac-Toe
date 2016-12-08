import sys
import os

filePath = str.replace(sys.executable, 'pythonw.exe', 'python.exe')

if 'Python27' in filePath:
    filePath = str.replace(filePath, 'Python27', 'Python35-32')


f = open('Run Server.bat', 'w')

f.write('@echo off' + '\n')

f.write('COLOR 3E' + '\n')

f.write(os.path.normpath(filePath) + ' ' + 'Game_Server.py' + '\n')

f.write('PAUSE' + '\n')

f.close()


f = open('Run Client.bat', 'w')

f.write('@echo off' + '\n')

f.write('COLOR 3E' + '\n')

f.write(os.path.normpath(filePath) + ' ' + 'Game_Client.py' + '\n')

f.write('PAUSE' + '\n')
f.close()
