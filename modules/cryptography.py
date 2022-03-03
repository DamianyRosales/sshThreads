from keygenerator import key_generator

keygen = key_generator()

__server_key = open("key", "r").read(20)

def keyToServerCheck():
    if keygen.generate() == __server_key:
        print('ENTERED')
