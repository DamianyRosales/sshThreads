from ssh import sshExec
import os
from getpass import getuser
from datetime import datetime
from threading import Thread

class Interface():
    
    cuser = getuser()
    
    def getLOGS(self):

        logs = sshExec('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
        while True:
            logs2 = sshExec('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
            if not logs2 == logs:
                logs = logs2 
                os.system('clear')
                print(logs)

    def establish(self):
        msg = ''
        msg2 = ''
        Thread(target=self.getLOGS).start()
        #logs = sshExec('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
        while not msg2 == 'exit()':

            #logs2 = sshExec('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
            #if not logs2 == logs:
                #logs = logs2
                #os.system('clear')
                #print(logs)
            userid = self.cuser + '>'
            now = datetime.now()
            msg2 = input(userid)
            if not msg2 == 'exit()':
                msg = now.strftime("%d/%m/%Y %H:%M:%S") + ' ' + userid + msg2
                com = "sed -i -e '$a" + str(msg) + "' /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs"
                sshExec(com)

