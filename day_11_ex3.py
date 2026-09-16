print('\n---START---\n')

number = 101
def is_prime(nb):
    '''which checks if a number is prime'''
    divi = [2,3,5,7]
    for div in divi:
        test = nb % div
        if test > 0:
            return 'PRIME'
        elif nb == 2:
            return 'PRIME'
        else:
            return 'NOT PRIME'
print(is_prime(number))
print()

unique = ['cat', 'dog', 'dog']
def isunique(animal):
    '''checks if all items are unique in the list'''
    for uni in animal:
        count = animal.count(uni)
        print(f'{uni}: {count}')
        if count > 1:
            return f'UNIQUE? {False}'
    else:
        return f'UNIQUE? {True}'
print(isunique(unique))
print()

unique = ['cat', 'dog', 'dog']
def same_data(liste):
    '''checks if all the items of the list are of the same data type'''
    premtype = type(liste[0])
    for uni in liste:
        if type(uni) != premtype:
            return f'Same type: {False}'
    return f'Same type: {True}'
print(same_data(unique))
print()


