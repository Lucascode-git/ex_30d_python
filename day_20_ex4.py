from bs4 import BeautifulSoup
import requests

url = 'https://fr.wikipedia.org/wiki/Ligue_des_champions_de_l%27UEFA'
headers = {'User-Agent': 'MonProjet/1.0 (lf16code@gmail.com)'}

response = requests.get(url, headers=headers)
texte = response.text

soup = BeautifulSoup(texte, 'html.parser')
tables = soup.find_all('table',class_='wikitable alternance')


#for index, table in enumerate(tables):
    #print(index)
    #print(table.get_text(strip=True)[:100])
    #print()


table = tables[0]
rows = table.find_all('tr')
firest_row = rows[0].get_text()
columns_list = firest_row.split('\n')

test = []
for row in rows:
    r = row.get_text()
    test.append(r.split('\n'))
print(test)





print()