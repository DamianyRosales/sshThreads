import createcredentials, communication
import cry
from getpass import getuser
from threadpool import Pool

pool = Pool()
chat = communication.Interface()

pool.add(chat.establish)
if getuser() == 'nyro':
    pool.add(cry.keyToServerCheck)
    pool.initialize()

if getuser() == 'soupmctavish12':
    pool.initialize()
