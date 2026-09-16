

fruits = ['banana', 'orange', 'mango', 'lemon']

while True:
    print('IF NOT CLEAR YOUR FRUIT WILL NOT BE ADDED')
    in_fruits = input("Check if your fruit is in our list, if not we'll add it to: ")

    letter_fruit = in_fruits.isalpha()
    if letter_fruit == False:
        print('\nPLEASE ENTER A FRUIT NOT A NUMBER')
        continue

    if in_fruits == 'finish':
        print(f'\nvvvvv YOUR FRUITS: {fruits} vvvvv')
        break

    if in_fruits in fruits:
        print(f'\nxxx ALREADY IN: {fruits} xxx')
    
    elif in_fruits not in fruits:
        fruits.append(in_fruits)
        print(f'\t--> {in_fruits.upper()} ADDED TO THE LIST\n')
    
    
fruits = ['banana', 'orange', 'mango', 'lemon']











