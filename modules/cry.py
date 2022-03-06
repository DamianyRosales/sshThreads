from keygenerator import key_generator
from ssh import sshExec

__keygen = key_generator()
__server_key = sshExec('cat /home/ayu/Documents/ConcurrentProject/finalproject/key')

def keyToServerCheck():
    a = __keygen.generate()
    while not a == __server_key:
        a = __keygen.generate()
    print('ENTERED')
