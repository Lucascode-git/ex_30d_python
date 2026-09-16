
from random import randint
from string import digits
from string import ascii_letters
import string
import random

def user_id_gen_by_user(characters, qty_ids):
    '''Write a function which generates a six digit/character random user id'''
    alphanum = list(ascii_letters + digits + digits)
    nb_ids =[]

    while len(nb_ids) < qty_ids:
        char_in_id = []
        
        for value in range(characters):
            char_in_id.append(random.choice(alphanum))
        
        finaluser = ''.join(char_in_id)
        nb_ids.append(finaluser)
    
    print('\n#output:')
    for id in nb_ids:
        print(f'#{id}')

    print()
    return nb_ids

#print('RAW DATA: ',user_id_gen_by_user(10,5))


def rgb_color_gen():
    '''It will generate rgb colors (3 values ranging from 0 to 255 each)'''
    rgblist = []
    for code in range(3):
        rgbcode = randint(0,255)
        codester = str(rgbcode)
        rgblist.append(codester)
    final = ','.join(rgblist)
    return f'# rgb({final})'

print(rgb_color_gen())