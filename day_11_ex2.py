print('\n---START---\n')
def evens_and_odds(number):
    '''It takes a positive integer as parameter and it counts number of evens and odds in the number'''
    evensnum = list(range(0,number+1,2))
    oddsnum = list(range(1,number,2))
    leneven = len(evensnum)
    lenodd = len(oddsnum)
    return f'The number of evens are {leneven}.\nThe number of odds are {lenodd}.\n'
print(evens_and_odds(9))

def factorial(factor):
    '''it takes a whole number as a parameter and it return a factorial of the number'''
    total = 1
    for value in range(1, factor+1):
        total = total * value
    return total
print(factorial(5))
print()

numbers = [5,10,6,20]
def calculate_mean(onelist):
    totale = 0
    for nb in onelist:
        totale += nb
    lenone = len(onelist)
    return totale / lenone
print(calculate_mean(numbers))
print()

def greet(name = False):
    if name:
        return f'Hello, {name.title()}!'
    else:
        return 'Hello, Guest!'
print(greet('clem'))
print()

def show_args(**kwargs):
    '''take an arbitrary number of named arguments and print their names and values'''
    listargs = []
    for k, v in kwargs.items():
        strtoargs = f'{k}: {v}'
        listargs.append(strtoargs)
        result = ', '.join(listargs)
    return 'Received: ' + result

print(show_args(name="Alice", age=30, city="New York"))
print()