from sys import stdin
from paramiko import SSHClient, AutoAddPolicy
import time

class Client:
    
    def __init__(self, credentials=None):
        self.credentials = open(str(credentials), "r").read().split("\n")
        self.host = self.credentials[0]
        self.username = self.credentials[1]
        self.password = self.credentials[2]
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(
            hostname=self.host,
            username=self.username,
            password=self.password
        )

    def command(self, com):

        stdin, stdout, stederr = self.client.exec_command(str(com))
        time.sleep(0.5)
        
        return stdout.read().decode()

    def commandExec(self, com):
        self.client.exec_command(str(com))
        time.sleep(0.5)
        
    def close(self):
        self.client.close()
        return

def sshExec(com, credentials):
        __credentials = open(str(credentials), "r").read().split("\n")
        __host = __credentials[0]
        __username = __credentials[1]
        __password = __credentials[2]
        __client = SSHClient()
        __client.set_missing_host_key_policy(AutoAddPolicy())
        __client.connect(
            hostname=__host,
            username=__username,
            password=__password
        )
        
        stdin, stdout, stederr = __client.exec_command(str(com))
        time.sleep(0.5)
        __client.close()
        return stdout.read().decode()
