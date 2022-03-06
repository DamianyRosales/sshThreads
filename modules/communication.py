from ssh import sshExec
import os
from getpass import getuser
from datetime import datetime

class Interface():
    
    cuser = getuser()
    
    def getLOGS(self):
        
        logs = sshExec('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
        print(logs)

    def establish(self):
        msg = ''
        msg2 = ''
        while not msg2 == 'exit()':
            userid = self.cuser + '>'
            os.system('clear')
            self.getLOGS()
            now = datetime.now()
            msg2 = input(userid)
            if not msg2 == 'exit()':
                msg = now.strftime("%d/%m/%Y %H:%M:%S") + userid + msg2
                com = "sed -i -e '$a" + str(msg) + "' /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs"
                sshExec(com)

host = input('ip>')
if not host == '1':
    username = input('host>') + "\n"
    password = input('password>') + "\n"

    credentials = open("credentials.txt", "w+")
    credentials.write(host + "\n")
    credentials.write(username)
    credentials.write(password)

    credentials.close()
