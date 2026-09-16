print('\n ---- START SETS ----\n')

dog = {}

name = 'caem'
color = 'brown'
breed = 'cocker'
legs = 4
age = 1

dog['name'] = name
dog['color'] = color
dog['breed'] = breed
dog['legs'] = legs
dog['age'] = age
print(dog)
print()

student = {
    'first_name':'Lucas',
    'last_name':'Marie',
    'gender': 'Male',
    'age':25,
    'country':'France',
    'city':'Lyon',
    'is_married' : True,
    'skills':['Python', 'Excel', 'Ppt', 'Claude'],
    'address':{
        'street':'Rue centrale',
        'zipcode':'01700'
    }
    }
print(len(student))
skills = student.get('skills')
print(skills)
print(type(skills))
student['skills'].append('MacOS')
student['skills'].append('Linux')
print(skills)

listkey_stud = list(student.keys())
print(listkey_stud)
listvalue_stud = list(student.values())
print(listvalue_stud)
print()

tuple_stud = student.items()
print(tuple_stud)
print()

del student['gender']
print(student)

del student

print('\n ---- END SETS ----\n')