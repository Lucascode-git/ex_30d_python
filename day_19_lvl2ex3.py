
import re
from collections import Counter
from pprint import pprint
import os

print('\n ----------- LVL 2 ------------------\n')
print(' ex 3 ------------------\n')


def text_to_compare(text1, text2):
    try:
        if os.path.isfile(text1):
            with open(text1, encoding='utf-8') as t1:
                text1_tocompare = t1.read()
        else:
            text1_tocompare = text1
        

        if os.path.isfile(text2):
            with open(text2, encoding='utf-8') as t2:
                text2_tocompare = t2.read()
        else:
            text2_tocompare = text2

        clean_text = f"[a-zA-Z]\w+(?:['-]\w+)*"
        clean_text1 = re.findall(clean_text, text1_tocompare.lower())
        clean_text2 = re.findall(clean_text, text2_tocompare.lower())

        both_text_cleaned = [clean_text1, clean_text2]

        stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', "he's", 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        remove_support_words = []
        for words in both_text_cleaned:
            if words not in stop_words:
                remove_support_words.append(words)
        
        list_both_text = remove_support_words[0] + remove_support_words[1]
        
        t1clean = set(remove_support_words[0])
        t2clean = set(remove_support_words[1])
        words_inboth_text = t1clean.intersection(t2clean)
        words_inone_text = set(list_both_text)
        
        jacquard_similarity = len(words_inboth_text) / len(words_inone_text)
        return jacquard_similarity


    except Exception as e:
        return f'Invalid text{e}'
    
print(text_to_compare('day_19_michelle.txt', 'day_19melina.txt'))









print()