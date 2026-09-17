
print('\n--- START ---\n')

from day_14_countries_data import allcountriesinfo


def get_list_sortedbyinfo(listc):
    def sortby(info):
        return sorted([country for country in listc], key= lambda tri: tri[info])[:3]
    return sortby

print('\n--- CLOSURE ---')
sortcountries = get_list_sortedbyinfo(allcountriesinfo)

print(sortcountries('name'))
print()
print(sortcountries('capital'))
print()
print(sortcountries('population'))

print('\n--- LANGUAGES ---\n')

#total = [lang for country in allcountriesinfo for lang in country.get('languages', [])]
#test = {info: total.count(info) for info in total}

def ranking_countries(listcount):
    total = [lang for country in listcount for lang in country.get('languages', [])]

    pairing = {}
    for lang in total:
        pairing[lang] = pairing.get(lang, 0) + 1

    def topcountry(number):
        sortedlang = sorted(pairing.items(), key= lambda item:item[1], reverse=True)[:number]
        return sortedlang
    return topcountry


list_torank = ranking_countries(allcountriesinfo)
topchoosen = list_torank(5)
print(topchoosen)


print('\n--- most populated countries ---\n')
def rankcountries(listc):
    popu = {country['name']: country['population'] for country in listc}
    def nbintop(number):
        ranking = sorted(popu.items(), key= lambda item: item[1], reverse=True)[:number]
        return ranking
    return nbintop

list_to_rank = rankcountries(allcountriesinfo)
choosen_top = list_to_rank(10)

print(choosen_top)











print('\n--- END ---\n')