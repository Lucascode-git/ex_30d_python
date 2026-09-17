
from string import ascii_uppercase
from functools import reduce

countriesli = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('\n--- MAP ---\n')

def upplist(alist):
    return alist.upper()
uppcountries = map(upplist, countriesli)
print(list(uppcountries))

def square(num):
    return num ** 2
square_numbers = map(square, numbers)
print(list(square_numbers))


print('\n--- FILTER ---\n')

def removeland(land_country):
    if 'land' in land_country:
        return False
    else:
        return True
landtest_countries = filter(removeland, countriesli)
print(list(landtest_countries))

def remove6char(char_country):
    countrylen = len(char_country)
    if countrylen >= 6:
        return False
    else: 
        return True
chartest_countries = filter(remove6char, countriesli)
print(list(chartest_countries))

def remove_e(ecountry):
    if ecountry[0] == 'E' or ecountry[0] == 'e':
        return False
    else:
        return True
no_ecountry = filter(remove_e, countriesli)
print(list(no_ecountry))


print('\n--- ALL 3 ---\n')

def cube(numlist):
    return numlist**3
def less100(numfun):
    if numfun <= 100:
        return True
    else: 
        return False
def sumnum(x,y):
    return x + y

odd_numbers = map(cube, numbers)
odd_numbers_less100 = filter(less100, odd_numbers)
sum_odd_nb_less100 = reduce(sumnum, odd_numbers_less100)
print(sum_odd_nb_less100)
# same but comprehension: 
result = reduce(sumnum, filter(less100, map(cube,numbers)))
print(result)

print('\nto know what happen above ^: ')
visu_odd_numbers = map(cube, numbers)
print(list(visu_odd_numbers))
visu_odd_numbers = map(cube, numbers)
visu_odd_numbers_less100 = filter(less100, visu_odd_numbers)
print(list(visu_odd_numbers_less100))


print('\n--- NB°9 ---\n')

def get_string_lists(intlist):
    return str(intlist)

str_numbers = map(get_string_lists, numbers)
print(list(str_numbers))

print('\n--- NB°10 ---\n')

def sumlist(x, y):
    return x + y

sum_numbers = reduce(sumlist, numbers)
print(sum_numbers)


print('\n--- NB°11 ---\n')

def sentencecount(x, y):
    return (x + ', ' + y)
sent_countries = reduce(sentencecount, countriesli[:-1])
print(f'{sent_countries} and {countriesli[-1]} are north European countries')


print('\n--- NB°12 ---\n')
from day_14_data import countries

def categorize_countries(pattern):
    '''Retourne les pays contenant le motif donné'''
    return [country for country in countries if pattern in country.lower()]
    # return list(filter(lambda country: pattern in country.lower(), countries))
print(categorize_countries('land'))


print('\n--- NB°13 ---\n')
import string

def returning_dictionary(listcountries):
    letters = list(ascii_uppercase)
    return {letter:len([country for country in listcountries if country[0] == letter]) for letter in letters}
test = returning_dictionary(countries)
print(test)


print('\n--- NB°14 ---\n')

def get_first_ten_countries(listc):
    return listc[:10]

print(get_first_ten_countries(countries))


print('\n--- NB°15 ---\n')

def slicer(nb):
    def get_last_ten_countries(listc):
        return listc[-nb:]
    return get_last_ten_countries

last10 = slicer(10)
last5 = slicer(5)
print(last10(countries))
print(last5(countries))









print()