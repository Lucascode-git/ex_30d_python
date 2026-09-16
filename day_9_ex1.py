print('\n ---- START CONDITIONAL ----\n')


#while True: 
    #age = input('Entre your age: ')
    #strage = str(age)
    #intage = int(age)
    #if strage == 'quit':    
        #break

    #elif intage > 18:
        #sentence = 'You are old enough to drive.'
        #print(sentence)
      
    #elif intage < 18:
        #sentence = f'You need {18 - intage} more years to learn to drive.'
        #print(sentence)

#myage = 25
#while True:
    #yourage = input('Enter your age: ')
    #stryourage = str(yourage)
    #intyourage = int(yourage)

    #if stryourage == 'quit':
        #break

    #diffage = intyourage - myage
    #if intyourage > myage:
        #if diffage == 1:
        #    print(f'You are {diffage} year older than me.')
        #elif diffage > 1:
        #    print(f'You are {diffage} years older than me.')
#
#    elif intyourage < myage:
#        if diffage == -1:
 #           print(f'You are {abs(diffage)} year younger than me.')
  #      elif diffage < -1:
   #         print(f'You are {abs(diffage)} years younger than me.')

#    elif intyourage == myage:
#        print('We have the same age')

while True :

    one = input('Enter number one: ')
    two = input('Enter number two: ')
    strone = str(one)
    strtwo = str(two)
    if strone == 'quit' or strtwo == 'quit':
        break

    intone = int(one)
    inttwo =int(two)

    if intone > inttwo:
        print(f'{intone} is greater than {inttwo}')
    elif intone < inttwo:
        print(f'{intone} is smaller than {inttwo}')
    elif intone == inttwo:
        print(f'{intone} is equal to {inttwo}')

    










print('\n ---- END CONDITIONAL ----\n')
