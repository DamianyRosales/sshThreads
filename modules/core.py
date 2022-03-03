from sys import argv
from threadpool import Pool

pool = Pool()


for user in argv:
    if user == 'damiany':
        pool.add()

