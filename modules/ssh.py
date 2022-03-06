from sys import stdin
from paramiko import SSHClient, AutoAddPolicy
import time


credentials = open("credentials.txt", "r").read()
credentials = credentials.split("\n")
host = credentials[0]
username = credentials[1]
password = credentials[2]
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(
    hostname=host,
    username=username,
    password=password
)

def sshExec(com):
    stdin, stdout, stederr = client.exec_command(str(com))
    time.sleep(0.5)
    return stdout.read().decode()

#client.close()
