from os import remove
import re

print('\n ------ EX 1 ----------')



with open('day_19_obama.txt') as bob:

    obama = {}
    text = bob.read()

    lines = text.splitlines()
    noempty_lines = [sen for sen in lines if sen.strip()]
    obama['lines'] = len(noempty_lines)

    words_fil = r"\w+(?:['-]\w+)*"
    words_ob = re.findall(words_fil, text)
    obama['words'] = len(words_ob)


with open('day_19_michelle.txt') as mio:
    
    michelle = {}
    text = mio.read()
    
    lines = text.splitlines()
    nb_lines = [line for line in lines if line.strip()]
    michelle['lines'] = len(noempty_lines)

    real_words = r"\w+(?:['-]\w+)*"
    words_mi = re.findall(real_words, text)
    michelle['words'] = len(words_mi)

#------------------------------------------------------------------
writters = ['BARACK OBAMA', 'MICHELLE OBAMA']
info_texts = [obama, michelle]

writter_winfos = [{k:v} for k, v in zip(writters, info_texts)]


print(writter_winfos)

    





print('\n ------ EX 2 ----------')







print()

