import createcredentials, communication
from ssh import Client
import cry
from getpass import getuser
from threadpool import Pool
from networkscanner import NScanner

pool = Pool()

client = Client('credentials.txt')
chat = communication.Interface(client)
nscanner = NScanner(client)

#pool.add(chat.establish)
#pool.add(nscanner.open_random_ports)
pool.add(nscanner.check_ports, 0,10)

for i in range(15):
    pool.add(nscanner.attack)

if getuser() == 'nyro':
    pool.add(cry.keyToServerCheck)

if getuser() == 'soupmctavish12':
    pass

if getuser() == 'emmanuel':
    pass

#client.close()
pool.initialize()
