
import re
from collections import Counter
from pprint import pprint
import os

print('\n ----------- LVL 2 ------------------\n')

with open('day_19_emailbig.txt', 'r') as em:
    text = em.read()
    
from_mail = r'From (\S+@\S+)+'
only_from_mail = re.findall(from_mail, text)
#print(only_from_mail)

print('\n ex 2 ------------------\n')



def find_most_common_words(text_file, top_words):
    try:
        if os.path.isfile(text_file): 
            with open(text_file, encoding='utf-8') as bob:
                string_text = bob.read()
        else:
            string_text = text_file

        words = r"\w+(?:['-]\w+)*"
        only_words = re.findall(words, string_text.lower())

        counter_words = Counter(only_words)
        sorted_qty_word = [(value, key) for key, value in counter_words.most_common(top_words)]
        return sorted_qty_word

    except Exception as e:
        return f'Invalid Input: {e}'


pprint(find_most_common_words('day_19_obama.txt', 10))

print()