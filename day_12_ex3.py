from random import randint
from string import digits
import random
import string

print('\n---START---\n')

infouser = ['lucas', 'bleu', 25, 2]

def shuffle_list(liste):
    newnblist = liste.copy()
    random.shuffle(newnblist)
    return newnblist

print(shuffle_list(infouser))
print(infouser)
print('\n------\n')





def shuffle_number():
    '''returns an array of seven random numbers in a range of 0-9'''
    nb = 7
    numliste = list(range(10))
    random.shuffle(numliste)
    return numliste[:nb]
    

print(shuffle_number())



print(f'\n--- END ---\n')
