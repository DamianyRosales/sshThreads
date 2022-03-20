import createcredentials, communication
from ssh import Client
import cry
from getpass import getuser
from threadpool import Pool

pool = Pool()

client = Client('credentials.txt')
chat = communication.Interface(client)
pool.add(chat.establish)
if getuser() == 'nyro':
    pass
    #pool.add(cry.keyToServerCheck)

if getuser() == 'soupmctavish12':
    pass

#client.close()
pool.initialize()
