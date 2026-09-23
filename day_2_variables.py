# Day 2: 30 Days of python programming

print('---------------      ---------------')
# LEVEL 1 

firstname = 'Lucas'
lastname = 'Marie'
fullname = firstname + lastname
country = 'France'
city = 'Lyon'
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True
skills = ['excel', 'python', 'git']
info_about_me = {
    'firstname': 'Lucas',
    'lastname': 'Marie',
}
info_about_me['age'] = age

print(info_about_me)
print()

# LEVEL 2

len_first = len(firstname)
len_last = len(lastname)
len_diff = len_first - len_last
print(f'difference of character between first and last name is: {len_diff}')
print()

# num exercice
num_one = 9
num_two = 5

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = divmod(num_one, num_two)
variable_exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(remainder)
print(variable_exp)
print(floor_division)
print()

# circle
radius_circle_a = 30
pi = 3.14159

area_of_circle = (radius_circle_a **2) * pi
circum_of_circle = pi * radius_circle_a * 2

print(f'{area_of_circle:.2f}')
print(f'{circum_of_circle:.2f}')
print()

# user input
#prompt = "Insert the raduis to calculate the area: "

#while True:
    #radius_circle_a = input(prompt)
    #if radius_circle_a == 'quit':
        #break

    #try:
        #radius = float(radius_circle_a)
    #except ValueError:
        #print('Value not supported')
        #continue

    #if radius > 0:
        #area_of_circle = (radius **2) * pi
        #print(f'{area_of_circle:.2f}')
    #else:
        #print('Value not supported')

# build-in function full name
question_first = 'What is your first name? : ' 
question_last = 'What is your last name? : '
question_country = 'Where did you come from? : '
question_age = 'How old are you? : '

list_person = []
person = {}

while True:
    person = {}
    first = input(question_first)
    if first == 'quit':
        break
    else:
        person['first'] = first

    last = input(question_last)
    if last == 'quit':
        break
    else:
        person['last'] = last

    country = input(question_country)
    if country == 'quit':
        break
    else:
        person['country'] = country

    age = input(question_age)
    if last == 'quit':
        break
    else:
        person['age'] = age

    list_person.append(person)
    print(list_person)
    



print('-----   ---------------------   ----')