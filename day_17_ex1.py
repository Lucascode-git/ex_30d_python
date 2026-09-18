from statistics import *

print('\n-Start---------------------\n')

print('\n-Ex 1---------------------\n')
def safe_divide(a, b):
    return a / b

try :
    a = 10
    b = 3
    dixto = safe_divide(a, 0)
    print(dixto)     
except Exception as e:
    print(e)

print('\n-Ex 2---------------------\n')

from statistics import mean

def stats(first, *middle, last):
    return {'first':first, 'last':last, 'mean middle numbers':mean(middle)}

scores = [88, 92, 75, 64, 99, 81, 70]
first, *middle, last = scores
print(stats(first, last=last, *middle))
print()

first, *rest, last = scores
print(rest)


print('\n-Ex 3---------------------\n')

def build_url(base, **params):
    language = [base]
    other = []
    for key in params:
        if key =='q':
            language.append(f'{key}={params[key]}')
        else:
            continue
    joinlang = '?'.join(language)

    other = [joinlang]
    for key in params:
        if key !='q':
            other.append(f'{key}={params[key]}')
        else:
            continue
    joinother = '&'.join(other)

    return joinother

print(build_url('https://api.example.com/search', q='python', page=2, sort='date'))
print()

def buildurl2(url, **kwargs):
    pair = [f'{key}={value}' for key, value in kwargs.items()]
    return url + '?' + '&'.join(pair)

print(buildurl2('https://api.example.com/search', q='python', page=2, sort='date'))


print('\n-Ex 4---------------------\n')

frontend = ['HTML', 'CSS', 'JavaScript']
backend = ['Python', 'Django']
tools = ['Git', 'Docker']

skills = ['Fullstack'] + [*frontend] + [*backend] + [*tools]
print(skills)
print()

profile = {'name': 'Lucas', 'role': 'developer'}
location = {'city': 'Lyon', 'country': 'France'}

full_profile = {**profile, **location}
print(full_profile)


print('\n-Ex 5---------------------\n')

names = ['alice', 'bob', 'clara', 'david']
roles = ['developer', 'designer', 'developer', 'manager']
years = [3, 1, 7, 5]


def build_team(names, roles, years):
    fulllist =[]
    for index, (n, r, y) in enumerate(zip(names, roles, years), start= 1):
        fulllist.append({'rank':index, 'name':n, 'role':r, 'years':y})
        
    return fulllist
print(build_team(names, roles, years))


print('\n-Exercises: Day 17---------------------\n')

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
fi, sw, no, de, ic, *rest = names
nordic_countries = fi, sw, no, de, ic
print(nordic_countries)
ru = list(rest[-1:])
print(ru)

print('\n-End---------------------\n')
