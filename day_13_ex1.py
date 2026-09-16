print('\n---START---\n')

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
onlyneg = [i for i in numbers if i <= 0]
print(onlyneg)

print

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listcombine = [stock for list in list_of_lists for stock in list]
print(listcombine)
print()

allnb =[]
for nb in range(0,11):
    calc = [nb]
    for number in range(0,6):
        cal = nb ** number
        calc.append(cal)
    allnb.append(tuple(calc))
        
#print(allnb)


listcomp = [tuple([nb]+[(nb**number) for number in range(0,6)]) for nb in range(0,11)] 
print(listcomp)
print()

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatcount = [[value[0].upper(), value[0][:3].upper(), value[1].upper()] for pair in countries for value in pair] 
#[list(value) for pair in countries for value in pair] 
print(flatcount)
print()

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
fulllist = []
dictcount = {}
for cc in countries:
    cc = dict(cc)
    for count, cap in cc.items():
        dictcount['country']=count
        dictcount['city']=cap
        fulllist.append(dictcount)

print(fulllist)

compfull = [{'country':countcap[0].upper(), 'city':countcap[1].upper()} for cc in countries for countcap in cc]
print(compfull)
print()

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flatnames = [f'{name[0]} {name[1]}' for full in names for name in full]
print(flatnames)
print()

def linear(x):
    return lambda n: x ** x + n * x + 2
funct = linear(1)(3)
print(f'linear: {funct}')




print(f'\n--- END ---\n')