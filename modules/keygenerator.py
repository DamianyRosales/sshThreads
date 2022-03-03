from random import randint

class key_generator():

    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'

    def generate(self):
        key = ''
        for i in range(16):
            if i%4 == 0 and i != 0: key += '-'
            if randint(0,1) == 0:
                l = list(self.letters)
                key += l[randint(0,len(l)-1)]
            else:
                n = list(self.numbers)
                key += n[randint(0,len(n)-1)]
        return key.upper()
