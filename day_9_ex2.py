print('\n ---- START CONDITIONAL ----\n')

agrade = (90,100)
bgrade = (80,89)
cgrade = (70,79)
dgrade = (60,69)
fgrade = (0,59)

graduation = {
    'A':agrade,
    'B':bgrade,
    'C':cgrade,
    'D':dgrade,
    'F':fgrade
}

while True:
    score = input('Enter your score: ')
    if score == 'quit':
        break

    intscore = int(score)
    if 0 <= intscore <= 100:
        for key, value in graduation.items():
            if value[0] <= intscore <= value[1]:
                print(f'\t--> Your grade: {key}\n')
                break
    else:
        print(f'\t--> Enter valid value\n')
            
            
#def find_grade(score):
    #'''Retourne la lettre correspondant au score'''
    #for letter, (low, high) in graduation.items():
        #if low <= score <= high:
            #return letter  
        
#try:
#    score = int(score)
#except ValueError:
#    print('\t--> Enter valid value\n')
#    continue 
        

   
    










print('\n ---- END CONDITIONAL ----\n')