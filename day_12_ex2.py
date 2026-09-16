from string import digits
from random import randint
from string import ascii_letters
import string
import random

print('\n---START---\n')

def list_of_hexa_colors():
    '''returns any number of hexadecimal colors in an array (six hexadecimal written after #.) 
    With only 0-9 and first 6 letters of the alphabet'''
    full_hexa_symbol = list('0123456789abcdef')
    nb_of_char = 6

    hexa_code = []
    for value in range(nb_of_char):
        hexa_code.append(random.choice(full_hexa_symbol))
    final_hexa_code = '#' + ''.join(hexa_code)
    return final_hexa_code

print(list_of_hexa_colors())
print()


def random_rgb_colors():
    '''returns any number of RGB colors in an array (3 values ranging from 0 to 255 each).'''
    rgb_onecode_len = 3

    rgb_code = []
    for value in range(rgb_onecode_len):
        code_str_random = str(randint(0,255))
        rgb_code.append(code_str_random)

    full_rgb_code = ', '.join(rgb_code)
    final_rgb_code = f'rgb({full_rgb_code})'
    return final_rgb_code

print(random_rgb_colors())

print(f'\n--- CALL 2 FUNCTIONS ---\n')


def generate_colors(type, qty):
    '''return hexa ('hexa) or rgb ('rgb) colors depend of the 'type' called eand qty the number of color codes needed'''
    colors_asked = []

    if type == 'hexa':
        for nb in range(qty):
            hexa_code = list_of_hexa_colors()
            colors_asked.append(hexa_code)
        return colors_asked

    elif type == 'rgb':
        for nb in range(qty):
            rgb_code = random_rgb_colors()
            colors_asked.append(rgb_code)
        return colors_asked
        
    else:
        return "Please enter a valid color type ('rgb' or 'hexa')"

# EXAMPLE LISTE COMPREHENSION:
#   generators = {'hexa': list_of_hexa_colors, 'rgb': list_of_rgb_colors}

#   if color_type not in generators:
#       return "Please enter a valid color type ('rgb' or 'hexa')"

#   generator = generators[color_type]
#   return [generator() for _ in range(qty)]

color_type_call = 'rgb'
qty_colors = 4
print(generate_colors(color_type_call,qty_colors))

print(f'\n--- END ---\n')
