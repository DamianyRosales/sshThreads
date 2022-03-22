from keygenerator import key_generator
from ssh import sshExec
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generateKey():
    password = b"674X-MD2F-0G47-Q9VZ"
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        #salt=salt,
        salt=b'z/\x94\x0bK\x8e\x83\xd6\xf3\xf7\x9f1\xb0\xf1U\x12',
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key



def getKeyInFile():
    with open('key', 'rb') as f:
        return f.read()


def encodePhrase(word, secret):
    f = Fernet(secret)
    wordToEncrypt = word.encode('utf-8')
    return f.encrypt(wordToEncrypt)


def decodePhrase(word, secret):
    f = Fernet(secret)
    word = word.encode('utf-8')
    return f.decrypt(word)

key = generateKey()

__keygen = key_generator()
__server_key = sshExec(credentials='credentials.txt', com='cat /home/ayu/Documents/ConcurrentProject/finalproject/key')

def keyToServerCheck():
    a = __keygen.generate()
    while not a == __server_key:
        a = __keygen.generate()
    print('ENTERED')
