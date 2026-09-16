print('\n---- START LVL 1 LISTS ----')

empty_list = []
list5items = ['nike', 'tiempo', 180, 46, 0]

len5items =len(list5items)
print(len5items)
midlle_list = int(len5items/2)
print(midlle_list)
print(list5items[0], list5items[midlle_list], list5items[-1])

mixed_data_types = ['Lucas', 25, 1.77, 2, 'Clémence']
print()

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
len_it = len(it_companies)
print(f'Number of companies: {len_it}')

middle_itlist = int(len_it/2)
print(middle_itlist)
print(it_companies[0], it_companies[middle_itlist], it_companies[-1])
print()

it_companies[4] = 'OFM'
print(it_companies)
print()

#11
it_companies.append('IBM')
print(it_companies)
#12
it_companies.insert(middle_itlist, 'NVIDIA')
print(it_companies)
print()

#13
company_to_upp = 'Google'
position = it_companies.index(company_to_upp)
company_upp = it_companies[position].upper()
it_companies[position] = company_upp
print(it_companies)
print()

it_join = ' / '.join(it_companies)
print(it_join)
print()

check_company = 'Snapchat'
inside_list = check_company in it_companies
print(inside_list)
print()

#16 / #17
print(it_companies)
dup_it_companies = it_companies.copy()
dup_it_companies.sort()
print(dup_it_companies)
dup_it_companies.sort(reverse=True)
print(dup_it_companies)
print()

#18
first3_comp = it_companies[:3]
last3_comp = it_companies[-3:]
print(f'{first3_comp}\n{last3_comp}')
print()
#20
it_companies.append('Snapchat')
recalc_len_comp = len(it_companies)
odd_or_even = recalc_len_comp % 2
print(odd_or_even)
half_list = int(recalc_len_comp/2)
print(it_companies)
if odd_or_even == 1:
    print(it_companies[half_list : half_list + 1])
else:
    print(it_companies[half_list - 1 : half_list + 1])
print()

#21
del it_companies[0]
print(it_companies)
print()
#22
if odd_or_even == 1:
    del it_companies[half_list : half_list + 1]
else:
    del it_companies[half_list - 1 : half_list + 1]
print(it_companies)
print()
#23
it_companies.remove('Snapchat')
print(it_companies)
print()

#24-25
it_companies.clear()
print(it_companies)
del it_companies

#26-27
print('\n-------------------------------------')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_and_back = front_end + back_end
print(front_and_back)
full_stack = front_and_back


print('\n---- END LVL 1 LISTS ----')

print('\n---- START LVL 2 LISTS ----\n')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(ages)
min_age = ages[0]
max_age = ages[-1]
print(f'\nMin age: {min_age}')
print(f'Max age: {max_age}')

len_ages = len(ages)
median_age = int(len_ages/2)
even_test = len_ages % 2
if even_test == 0:
    print(f'Median age: {ages[median_age-1:median_age+1]}')
else:
    print(f'Median age: {ages[median_age:median_age+1]}')

total_ages = sum(ages)
average_age = total_ages / len_ages
print(f'Average age: {average_age}')

range_ages = max_age - min_age
print(f'Range of the ages: {range_ages}')
print()

min_minus_avg = min_age - average_age
max_minus_avg = max_age - average_age
if max_minus_avg < abs(min_minus_avg):
    print(f'Most of valuse are ABOVE average:\ndistribution values > average: {max_minus_avg}\ndistribution < average: {abs(min_minus_avg)}')
elif max_minus_avg > abs(min_minus_avg):
    print(f'Most of valuse are BELOW average:\ndistribution values < average: {abs(min_minus_avg)}\ndistribution > average: {max_minus_avg}')

print('\n---- END LVL 2 LISTS ----\n')

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
  
  
]
print('---- COUNTRY EX ----\n')
len_countries = len(countries)
print(len_countries)
half_countries = int(len_countries/2)
print(half_countries)
evenodd = len_countries % 2
print(evenodd)

if evenodd == 1:
    contry1 = countries[0:half_countries+1]
    country2 = countries[half_countries+1:]

elif evenodd == 0:
    contry1 = countries[0:half_countries]
    country2 = countries[half_countries:]

#print(contry1)
print()
#print(country2)
print(len(contry1))
print(len(country2))
print()

list_coun3 = ['China', 'Russia', 'United States', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = list_coun3
first3count = ch,ru,us
print(list(first3count))
print(scandic)
print()

position_coun3 =[]
for country in list_coun3:
    position = countries.index(country)
    position_coun3.append(position)
print(position_coun3)
    
for position in position_coun3:
    find_country = countries[position]
    print(find_country)
print('\n---- END COUNTRY EX ----\n')