import createcredentials
import communication
import cry
from getpass import getuser
from threadpool import Pool

pool = Pool()
chat = communication.Interface()

if getuser() == 'nyro':
    pool.add(cry.keyToServerCheck)
    pool.add(chat.establish)
    pool.initialize()

if getuser() == 'soupmctavish12':
    pool.add(chat.establish)
    pool.initialize()
