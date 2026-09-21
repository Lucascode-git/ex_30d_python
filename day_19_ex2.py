import json
from collections import Counter
from pprint import pprint


print('\n ------ EX 2 ----------')

with open('day_19_countriesdata.json', encoding='utf-8') as listc:
    countries_datas = json.load(listc)

def most_spoken_languages(data, top):
    all_spoken_languages = []

    for country in data:
        languages = country.get('languages', [])
        for language in languages:
            all_spoken_languages.append(language)

    stat_language = Counter(all_spoken_languages)
    language_qty_speakers = stat_language.most_common()

    top_sorted_speakers = language_qty_speakers[:top]
    return top_sorted_speakers

pprint(most_spoken_languages(countries_datas, 3))


print('\n ------ EX 2 ----------')


def most_populated_countries(data_list, top_to_display):
    pair_country_pop = []
    info_country = 'name'
    info_popu = 'population'

    for country in data_list:
        get_country = country.get(info_country, '')
        get_popu = country.get(info_popu, 0)
        pair_country_pop.append({ 'country':get_country, info_popu:get_popu })

    sorted_by_popu = sorted(pair_country_pop, key= lambda country: country['population'], reverse= True)
    top_sorted_popu = sorted_by_popu[:top_to_display]
    return top_sorted_popu

pprint(most_populated_countries(countries_datas, 5))






print()