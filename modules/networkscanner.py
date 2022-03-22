import socket
from random import randint

class NScanner:

    def __init__(self, client):
        self.client = client
        self.credentials = open('credentials.txt', 'r').read().split('\n')
        self.ip = self.credentials[0]
        self.openports = []

    def check_ports(self, start, end):
        if start == 450:
            start = 0
            end = 0
        portsfile = open('portslog.txt', 'a')
        for port in range(start,end):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((self.ip, port))
                if result == 0:
                    if port not in self.openports:
                        self.openports.append(port)
                        portsfile.write(str(port))
                else:
                    if port in self.openports:
                        with open('portslog.txt', 'r') as f:
                            lines = f.readlines()
                        with open('portslog.txt', 'w') as f:
                            for line in lines:
                                if line.strip('\n') != str(22):
                                    f.write(line)

                sock.close()
            except: pass
        portsfile.close()
        self.check_ports(start+10, end+10)

    def open_random_ports(self):
        while True:
            port = randint(0,450)
            if not port == 22:
                com = 'sudo ufw allow' + str(port)
                self.client.command(com)
                print('open'+port)

