print('\n---- START TUPLE ----\n')

tuple1 = ()
tuple2 = ('clémence', 'lorik', 'muriel','gisele')
tuple3 = ('mickael', 'nicole')
tuple4 = tuple2 + tuple3
print(tuple4)
print(len(tuple4))
morefam = ('chloé', 'patrick')
fullfam = tuple4 + morefam

fullfam = tuple1
print(fullfam)
print()

fruits = ('mango', 'pineapple', 'apple')
vegetables = ('zuchini', 'brocoli', 'bean')
meat = ('chicken', 'beef')
food_stuff_tp = fruits + vegetables + meat
print(food_stuff_tp)

list_food = list(food_stuff_tp)
print(list_food)
print()

len_food = len(food_stuff_tp)
middle_food = int(len_food/2)
oddeven = len_food % 2
if oddeven == 1:
    print(food_stuff_tp[middle_food : middle_food + 1])
else: 
    print(food_stuff_tp[middle_food - 1 : middle_food + 1])

first3 = food_stuff_tp[:3]
last3 = food_stuff_tp[-3:]
print(first3)
print(last3)

del food_stuff_tp
print()

country_to_check1 = 'Estonia'
country_to_check2 = 'Iceland'
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
does_nordic1 = country_to_check1 in nordic_countries
does_nordic2 = country_to_check2 in nordic_countries
print(does_nordic1, does_nordic2)


print('\n---- END TUPLE ----\n')