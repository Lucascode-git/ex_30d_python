from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('\n--- MAP ---\n')

def upp(onelist):
    upping = onelist.upper()
    return upping

countries_upp = map(upp, countries)
print(list(countries_upp))

countupp_lambda = map(lambda name: name.upper(), countries)
print(list(countupp_lambda))


print('\n--- FILTER ---\n')

def oddnumber(numlist):
    if numlist % 2 == 0:
        return False
    else:
        return True

testodd = filter(oddnumber, numbers)
print(list(testodd))


print('\n--- REDUCE ---\n')
def sumlist(x, y):
    return x + y

sumnumbers = reduce(sumlist, numbers)
print(sumnumbers)


print('\n--- FOR ---\n')

def allcountries(countlist):
    for country in countlist:
        print(country)

allcountries(countries)












print()