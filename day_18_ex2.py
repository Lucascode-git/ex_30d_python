import re

#def is_valid_variable(vari):
#    '''Vérifie si une string est un nom de variable Python valide'''
#    return bool(re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', vari))

def is_valid_variable(vari):
    first_char = r'^[a-zA-Z_]'
    middle = r'[a-zA-Z0-9_]'

    match_num = re.findall(first_char, vari)
    match_middle = re.findall(middle, vari)
          
    if len(match_num) > 0 and len(match_middle) == len(vari):
        return True
    else: 
        return False
        
text = '1first_name'
test_var = is_valid_variable(text)
print(test_var)