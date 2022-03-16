import os
from getpass import getuser
from datetime import datetime
from threading import Thread

class Interface:
    
    def __init__(self, client):
        self.cuser = getuser()
        self.client = client

    def getLOGS(self):

        logs = self.client.command('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
        
        while True:
            logs2 = self.client.command('cat /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')

            if not logs2 == logs:
                logs = logs2 
                os.system('clear')
                print(str(logs))

    def establish(self):
        msg = ''
        msg2 = ''
        Thread(target=self.getLOGS).start()
        while not msg2 == 'exit()':

            userid = self.cuser + '>'
            now = datetime.now()
            msg2 = input(userid)
            if not msg2 == 'exit()':
                msg = now.strftime("%d/%m/%Y %H:%M:%S") + ' ' + userid + msg2
                com = "sed -i -e '$a" + str(msg) + "' /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs"
                #sshExec(com)
                self.client.command(com)

    def reset(self):
        self.client.command('rm /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
        self.client.command('cat /home/ayu/Documents/ConcurrentProject/finalproject/logtemplate > /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')

