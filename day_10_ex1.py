
print('\n ---- START LOOPS----\n')

list010 = []
for value in range(11,0,-1):
    list010.append(value)
print(list010)

#count = 10
#while count > 0:
#    count = count-1
#    print(count)
print()

diez = '#'
while len(diez) < 8:
    print(diez)
    diez = diez + '#'
print()

diez2 ='# '
ref = 0

while ref < 9:
    ref = ref + 1
    while len(diez2) < 16:
        diez2 = diez2 + '# '
    
    else:
        print(diez2)
print()

debut = 0
while debut < 11:
    print(f'{debut} x {debut} = {debut*debut}')
    debut = debut + 1
else:
    print('Finish\n')
    
    

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)
print()

evennum = []
oddnum = []
zerohund = range(0,101)
for number in zerohund:
    test = (number % 2) == 0
    if test == True: 
        evennum.append(number) 
    else: 
        oddnum.append(number) 
else:      
    print(evennum)
    print(oddnum)
print()

total = 0
for value in range(0,101):
    total += value
print(f'sum: {total}')

eventotal = 0
oddtotal = 0
for number in range(0,101):
    test = (number % 2) == 0
    if test == True: 
        eventotal = eventotal + number
    else:
        oddtotal = oddtotal + number
print(f'sum even: {eventotal}')
print(f'sum odd: {oddtotal}')





print('\n ---- END LOOPS ----\n')