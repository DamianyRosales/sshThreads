import os
from getpass import getuser
from datetime import datetime
from threading import Thread
import cry
from ssh import sshExec

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
                for i in logs.split('\n'):
                    try:
                        i = str(cry.decodePhrase(i, cry.key))
                        i =  i[:0] + i[0+1:] 
                        i =  i[:0] + i[0+1:]
                        lastComma = len(i)-1
                        i =  i[:lastComma] + i[lastComma+1:]
                        print(i)
                    except: pass

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
                msg = cry.encodePhrase(msg, cry.key)
                msg = str(msg)
                msg =  msg[:0] + msg[0+1:]
                com = "sed -i -e '$a" + msg + "' /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs"
                
                self.client.command(com)

    def reset(self):
        self.client.commandExec('rm /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')
        self.client.command('cat /home/ayu/Documents/ConcurrentProject/finalproject/logtemplate > /home/ayu/Documents/ConcurrentProject/finalproject/chatlogs')

