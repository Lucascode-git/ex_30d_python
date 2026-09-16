print('\n ---- START CONDITIONAL ----\n')

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
autumn = (months[8:11])
winter = (months[-1], months[0], months[1])
spring = (months[2:5])
summer = (months[5:8])

while True:
    which_month = input('Which month are you searching for it season: ')
    if which_month == 'quit':
        break

    title_month = which_month.title()
    if title_month in months[8:11]:
        print(f'{title_month} is in AUTUMN')
    elif title_month in months[5:8]:
        print(f'{title_month} is in SUMMER')
    elif title_month in months[2:5]:
        print(f'{title_month} is in SPRING')
    else:
         print(f'{title_month} is in WINTER')
        









print('\n ---- END CONDITIONAL ----\n')
