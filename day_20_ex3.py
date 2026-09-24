
from collections import Counter
import json
from pprint import pprint

with open('day_20_countrieslong.json', encoding='utf-8') as co:
    countries = json.load(co)

def countries_by_area(list_countries, top=10):
    ''' Return a liste of tuple that rank countries in the list by their area '''
    list_country_area = []
    for country in list_countries:
        name = country.get('name', '')
        area = country.get('area', '0')
        area = int(area)
        list_country_area.append((name, area))

    sorted_country_byarea = sorted(list_country_area, key= lambda item: item[1], reverse=True)
    top_area = sorted_country_byarea[:top]
    return top_area

print('\n--- ex 1 ---------------------')
pprint(countries_by_area(countries, 5))


print('\n--- ex 2 ---------------------')
def languages_info(list_contries, top=10):
    all_languages = []
    for country in list_contries:
        languages = country.get('languages',[])
        for language in languages:
            name = language.get('name', {})
            all_languages.append(name)
    
    sorted_top_languages = Counter(all_languages).most_common(top)

    print(f'Total number of languages: {len(set(all_languages))}')
    return sorted_top_languages

pprint(languages_info(countries))


