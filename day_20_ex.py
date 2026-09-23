
from collections import Counter
import re
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from day_19_stopwords import stop_words

def convert_html_to_list(url):
    ''' Return a text version of the extract from the html url '''
    response = requests.get(url)
    html_to_text = response.text

    soup = BeautifulSoup(html_to_text, 'html.parser')
    text = soup.get_text()

    return text


def find_most_used_words(list_words, top = 10):
    ''' Print most used word in a text without stop words, defaut value: top 10 '''
    filter_word = r"\w+(?:[-']\w+)*"
    words_in_list = re.findall(filter_word, list_words.lower())
    
    stop = set(stop_words)
    list_text_without_stop = [word for word in words_in_list if word not in stop]
    
    top_used_words = Counter(list_text_without_stop).most_common(top)
    
    return top_used_words

romeojuliet_text = convert_html_to_list('https://shakespeare.mit.edu/romeo_juliet/full.html')
most_used_wordin = find_most_used_words(romeojuliet_text)
pprint(most_used_wordin)

    

