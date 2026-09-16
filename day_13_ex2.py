print('\n---START---\n')

employees = [
    {'name': 'alice martin', 'role': 'developer', 'salary': 52000, 'years': 3},
    {'name': 'bob durand', 'role': 'designer', 'salary': 45000, 'years': 1},
    {'name': 'clara petit', 'role': 'developer', 'salary': 61000, 'years': 7},
    {'name': 'david roux', 'role': 'manager', 'salary': 72000, 'years': 5},
    {'name': 'emma blanc', 'role': 'developer', 'salary': 48000, 'years': 2},
]

uppname = [person['name'].upper() for person in employees]
print(uppname)

devname = [person['name'] for person in employees if person['role']=='developer']
print(devname)

senior = [f'{person['name']} ({person['role']})' for person in employees if person['years']>=5]
print(senior)

inisal = [(f'{person['name'].split()[0][0].upper()}{person['name'].split()[1][0].upper()}',person['salary']) for person in employees]
print(inisal)

aug5 = {person['name']:(person['salary']*1.05) for person in employees if person['role']=='developer'}
print(aug5)



print(f'\n--- END ---\n')