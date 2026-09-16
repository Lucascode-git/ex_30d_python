def add_two_numbers(a,b):
    sum = a + b
    return sum
print(add_two_numbers(3,4))

def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_circle(10))

def convert_celsuis(cel):
    fahrenheit = (cel*9/5) + 32
    return fahrenheit
print(convert_celsuis(20))

def check_season(month):
    seasons = {
        'winter':['dec', 'jan', 'feb'],
        'spring':['mar', 'apr', 'may'],
        'summer':['jun', 'jul', 'aug'],
        'autumn':['sep', 'oct', 'nov']
        }
    for season , months in seasons.items():
        if month in months:
            return season
    else:
        return 'enter a valid month'
print(check_season('may'))


listetest = [10,30,60,80,130,180]

def print_liste(liste):
    resultat = []
    for valeur in liste:
        resultat.append(valeur)
    return resultat
print(print_liste(listetest))

revliste = [1,2,3,4,5]
def reverte(listrev):
    return sorted(listrev, reverse=True)
print(reverte(revliste))


ville = ['lyon', 'greer', 'miami']
def capitalize_list_items(villeliste):
    capville = []
    for city in villeliste:
        city = city.title()
        capville.append(city)
    return capville
print(capitalize_list_items(ville))


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(food, arg=False):
    if arg:
        food.append(arg)
        return food
    else:
        return food
print(add_item(food_stuff, 'Meat'))


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item(vege, remov = False):
    if remov and remov in vege:
        vege.remove(remov)
        return vege
    else:
        return vege
print(remove_item(food_stuff))


def sum_of_numbers(number):
    max = number
    while number > 0:
        number = number - 1
        max += number    
    return max
print(sum_of_numbers(10))

print('\n----------------\n')

def sum_of_oddeven(num):
    total = 0
    for value in range(num+1,0,-2):
        value = value - 1
        total += value
    return total
print(sum_of_oddeven(11))
print()

emptylist = []
def is_empty(testlist):
    if testlist:
        return False
    else:
        return True
print(is_empty(emptylist))
print()

def greet(name = False):
    if name:
        return f'Hello, {name.title()}!'
    else:
        return 'Hello, Guest!'
print(greet('clem'))
print()

def show_args(**args):
    '''take an arbitrary number of named arguments and print their names and values'''
    for key, value in args.items():
        print(key, value)

show_args(name="Alice", age=30, city="New York")

