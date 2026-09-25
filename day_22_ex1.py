
from csv import list_dialects
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

print()
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text()

displayed_datas = soup.find_all('div', class_='bu-stat-list')
tables = soup.find_all('section', class_='stat-section')

#table = tables[0]
#print(table.prettify()[:1500])
all_datas = {}
for table in tables:
    labels = table.find_all('h4', class_='stat-group-title')
    keys = table.find_all('span', class_='stat-label')
    values = table.find_all('span', class_='stat-figure')
    for l in labels:
        label = l.get_text()
        pair_key_value = {}
        for k, v in zip(keys, values):
            key = k.get_text()
            value = v.get_text()
            pair_key_value[key] = value
        all_datas[label] = pair_key_value


#pprint(all_datas)
#------------------------------------------------------
# highlight datas
for container in displayed_datas:
    section_title = container.find_previous_sibling('h4', class_='stat-group-title').get_text(strip=True)
    section_stats = {}

    for article in container.find_all('article', class_='bu-stat-single'):
        title = article.find('h3', class_='bu-stat-title').get_text(strip=True)
        value = article.find('div', class_='bu-stat-value-container').get_text(strip=True)
        section_stats[title] = value

    all_datas[section_title] = section_stats

with open('day_22json.json', 'w', encoding='utf-8') as bo:
    json.dump(all_datas, bo, ensure_ascii=False, indent = 4).     




   
#print(list_label)
    
        



print()