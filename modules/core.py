import chat
import cry
from getpass import getuser
from threadpool import Pool

pool = Pool()

if getuser() == 'nyro':
    #pool.add(cpy.keyToServerCheck())
    pool.add(cry.keyToServerCheck)
    pool.initialize()
    
