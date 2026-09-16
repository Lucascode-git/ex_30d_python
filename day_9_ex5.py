print('\n ---- START CONDITIONAL LVL 3 ----\n')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python',],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


def eligible(info_person):
    '''Find if a person eligible : maried and live in Finland / + return this contions with his full name'''
    if_fin = 'Finland' == info_person['country']
    return info_person['country'] == 'Finland' and info_person['is_married']

def find_middle(info_skills):
    '''Find the middle skill in the skills list'''
    lenskills = len(info_skills)
    middleskill = int(lenskills/2)
    oddeven = lenskills % 2
    if oddeven == 1:
        return f'Middle skill is: {info_skills[middleskill]}'
    elif oddeven == 0 and info_skills == 2:
        return f'Middle skill are: {info_skills[middleskill]} / {info_skills[middleskill+1]}'
    else:
        return f'Middle skill are: {info_skills[middleskill-1]} / {info_skills[middleskill]}'

def get_dev_title(skills):
    '''Find what kind of dev have applied'''
    profile = {
        'backend': ['Node','Python','MongoDB'],
        'frontend': ['JavaScript','React'],
        'full stack': ['React','Node','MongoDB'],
        'front/back/full': ['JavaScript','React','Node','Python','MongoDB']
    }
    for title, required in profile.items():
        if sorted(skills) == sorted(required):
            return f'He/She is a {title} developer'
    return 'Unknown title'

            
skills = person.get('skills', [])
print(skills)
print()

if skills:
    middle_skill = find_middle(skills)
    print(middle_skill)

    if 'Python' in skills:
        print('\nThe candidate have PYTHON in is technical bag\n')
    else:
        print('\nThe candidate DOES NOT have PYTHON in is technical bag\n')

    dev_title = get_dev_title(skills)
    print(dev_title)
    
else:
    print('No skill listed, so no middle skill')

is_eligible = eligible(person)
if is_eligible :
    print(f'\n{person['first_name']} {person['last_name']} lives in Finland. He is married.')
else:
    print(f'\n{person['first_name']} {person['last_name']} is NOT eligible')







print('\n ---- END CONDITIONAL LVL 3 ----\n')

#if 'skills' in info_person.keys():
    #    for key, list in info_person.items():
    #        if key == 'skills':
    #            return(list)
    #elif 'skills' not in info_person.keys():
    #    return('No skill listed')



#if 'country' in info_person.keys() and 'is_married' in info_person.keys():
    #    if info_person['country'] == 'Finland' and info_person['is_married'] == True:
    #        sentence = f'{info_person['first_name']} {info_person['last_name']} lives in Finland. He is married.'
    #        return sentence
    #    else:
    #        sentence = f'{info_person['first_name']} {info_person['last_name']} DOES NOT LIVE IN FIN OR IS NOT MARRIED'
    #        return sentence
    #else:
    #    return 'Be sure that you have enter info in: country/is_married'



#    copy_skills = skills.copy()
 #   copy_skills.sort()
#
 #   back_end = ['Node','Python','MongoDB']
  #  front_end = ['JavaScript','React']
   # full_stack = ['React','Node','MongoDB']
    #everything_dev = ['JavaScript','React','Node','Python','MongoDB']

#    back_end.sort()
 #   front_end.sort()
  #  full_stack.sort()
   # everything_dev.sort()

#    if copy_skills == back_end:
 #       return 'He/She is a backend developer'
  #  elif copy_skills == front_end:
   #     return 'He/She is a frontend developer'
#    elif copy_skills == full_stack:
 #       return 'He/She is a fullstack developer'
  #  elif copy_skills == everything_dev:
   #     return'He/She is a frontend/backend/fullstack developer'
    #else:
    #    return 'Unknown title'