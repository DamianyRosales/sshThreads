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
        salt=salt,
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
    return f.decrypt(word)

key = generateKey()
phraseEnc = ""

while True:

    option = input("Desea codificar o decodificar? (0/1) ")
    if option == "0":

        phrase = input("Ingrese la frase a codificar: ")
        phraseEnc = encodePhrase(phrase, key)
        print(phraseEnc)

    elif option == "1":

        decof = input("Ingrese la frase a decodificar: ")
        print(decodePhrase(phraseEnc, key))

__keygen = key_generator()
__server_key = sshExec(credentials='credentials.txt', com='cat /home/ayu/Documents/ConcurrentProject/finalproject/key')

def keyToServerCheck():
    a = __keygen.generate()
    while not a == __server_key:
        a = __keygen.generate()
    print('ENTERED')
