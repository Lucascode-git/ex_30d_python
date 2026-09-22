
import re
from collections import Counter
from pprint import pprint
import os
from day_19_stopwords import stop_words

print('\n ----------- LVL 2 ------------------\n')
print(' ex 3 ------------------\n')


def text_to_compare(text1, text2):
    ''' Return a list where values are the both texts '''
    try :
        textes = [text1, text2]
        list_both_texts = []
        for text in textes:
            if os.path.isfile(text):
                with open(text, encoding='utf-8') as t:
                    list_both_texts.append(t.read())
            else:
                list_both_texts.append(text)

        return list_both_texts

    except Exception as e:
        return f'INVALID INPUT : {e}'
        raise


def clean_text(list_texts):
    ''' Return a list where values are the both cleaned texts '''
    clean_char = r"[a-zA-Z]\w+(?:['-]\w+)*"
    clean_list_both_texts = []
    for text in list_texts:
        clean_list_both_texts.append(re.findall(clean_char, text.lower()))

    return clean_list_both_texts


def remove_support_words(listof_cleantexts):
    ''' '''
    set_stopwords = set(stop_words)
    set_list_cleantexts = []
    for text in listof_cleantexts:
        set_list_cleantexts.append(set(text))
    
    setlist_cleanstop_texts = []
    for text in set_list_cleantexts:
        setlist_cleanstop_texts.append( text.difference(set_stopwords) )
    return setlist_cleanstop_texts
    

def check_text_similarity(super_clean_texts):
    text1 = super_clean_texts[0]
    text2 = super_clean_texts[1]
    bothtext = list(text1) + list(text2)
    #print(len(text1), len(text2),len(bothtext))
    common_words_intexts = text1.intersection(text2)
    #print(len(common_words_intexts))
    #print(len(bothtext) - len(common_words_intexts))
    
    #jaccard = word in A and B / (word in A + word in B - word in A and B)
    jaccard_similarity = len(common_words_intexts) / (len(bothtext) - len(common_words_intexts))
    return jaccard_similarity

text_n1 = 'day_19_michelle.txt'
text_n2 = 'day_19melina.txt'

texts_to_list = text_to_compare(text_n1, text_n2)
clean_texts_list = clean_text(texts_to_list)
list_texts_cleanstop = remove_support_words(clean_texts_list)

jaccard_number = f'{(check_text_similarity(list_texts_cleanstop) * 100):.2f}%'
print(f'Jaccard similarity coeff between both text is: {jaccard_number}')









print()