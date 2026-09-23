
from collections import Counter
from statistics import stdev
from statistics import mean
import os
from dotenv import load_dotenv
import requests
from pprint import pprint
import statistics 
import re

load_dotenv()
cle = os.getenv('CAT_API_KEY')

url = 'https://api.thecatapi.com/v1/breeds'
headers = {'x-api-key': cle}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data_cat = response.json()
except Exception as e:
    print(f'Échec de la requête : {e}')
    raise

bothweight_by_cat =[]
for cat in data_cat:
    weight = cat.get('weight', {})
    bothweight_by_cat.append(weight)
#print(bothweight_by_cat)
print(len(bothweight_by_cat))

allweights_cat_metric = []
for dataweight in bothweight_by_cat:
    metric_val = dataweight.get('metric', '')

    if bool(re.search(r'[0-9]', metric_val)):
        datasplit = metric_val.split('-')
        cat_mean_metric = (float(datasplit[0])+float(datasplit[1]))/2
        cat_mean_metric = round(cat_mean_metric,2)
        allweights_cat_metric.append(cat_mean_metric)
    else:
        imp_val = dataweight.get('imperial')
        int_impval = int(imp_val)
        allweights_cat_metric.append((int_impval*0.45))
print()
print(len(allweights_cat_metric))


def data_analyse_list(listdata):
    min_value  = min(listdata)
    max_value = max(listdata)
    mean_value = mean(listdata)
    median_value = statistics.median(listdata)
    stdev_value = stdev(listdata)
    return(f'''--- Value of your list ---
    \n\tMin value: {min_value:.2f}
    \n\tMax value: {max_value:.2f}
    \n\tMean value: {mean_value:.2f}
    \n\tMedian value: {median_value:.2f}
    \n\tStdev value: {stdev_value:.2f}
    ''')

print()
print(data_analyse_list(allweights_cat_metric))
print('=========================================================================\n')


lifespan_by_cat =[]
for cat in data_cat:
    lifespan = cat.get('life_span', '')
    if re.fullmatch(r'\s*\d+\s*-\s*\d+\s*',lifespan):
        separate_values = lifespan.split('-')
        mean_lifespan = (int(separate_values[0])+int(separate_values[1]))/2
        lifespan_by_cat.append(mean_lifespan)
    else:
        print('Please correct lifespan value of:')
        print(f'{cat['name']} lifespan current value: {lifespan}\n')

print(data_analyse_list(lifespan_by_cat))

print('=========================================================================\n')
country_cat =[]
for cat in data_cat:
    country = cat.get('origin', '')
    country_cat.append(country)


ranking_origin_country = Counter(country_cat).most_common(10)
pprint(ranking_origin_country)

#datasplit = nb.split('-')
#weight_metric.append(datasplit)       


