from collections import Counter
import re
from pprint import pprint

print('\n ----------- LVL 2 ------------------')
print(' ex 5 -------------------------------\n')

with open('day_19_ROMEOJU.txt', encoding='utf-8') as rj:
    text = rj.read()

    remove_char = r"\w+(?:['-]\w+)*"
    start = text.find('Dramatis Personae') 
    end = text.find('THE END')

    text_ro = text[start:end]

    list_words = re.findall(remove_char, text_ro.lower())

    occu_words = Counter(list_words)
    top10 = occu_words.most_common(10)
    pprint(top10)


print('\n ----------- LVL 2 ------------------')
print(' ex 6 -------------------------------\n')
import csv
with open('hacker_news.csv', encoding='utf-8') as hk:
    csv_reader = csv.reader(hk, delimiter=',')
    csv_all_row = []
    for row in csv_reader:
        csv_all_row.append(row)
    

def find_python_lines(listdatas, filter_word, not_in = False):
    filter_lines = []
    for line in listdatas:
        textline = ','.join(line)
        lowtext = textline.lower()
        if not_in:
            if filter_word in lowtext and not_in not in lowtext:
                filter_lines.append(line)
        else:
            if filter_word in lowtext:
                filter_lines.append(line)

    return f'Qty of lines with {filter_word} (avoid?: {not_in}): {len(filter_lines)}'

qty_lines_python = find_python_lines(csv_all_row, 'java', 'javascript')
print(qty_lines_python)
          
print()
