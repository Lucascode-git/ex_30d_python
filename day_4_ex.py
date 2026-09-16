# EX 1 to 
print('\n---- START ----')
print('Thirty' + ' ' +'Days' + ' ' + 'Of' + ' ' + 'Python')
space = ' '
coding_for_all = 'Coding' + space + 'For' + space + 'All'
print(coding_for_all)
print()

company_v = coding_for_all
print(company_v)
print(len(company_v))
print(company_v.upper())
print(company_v.lower())
print(company_v.capitalize(), '/', company_v.title(), '/', company_v.swapcase())
print(company_v[7:])
print(company_v.find('Coding'))
print()

company_new = company_v.replace('Coding', 'Python')
print(company_v)
company_ev = company_new.replace('All', 'Everyone')
print(company_new.replace('All', 'Everyone'))
print(company_new.split(' '))
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

print()
print(company_v[0])
print(f"'{company_v[10]}'")
print(company_ev)
acronyme_pfev = company_ev[0] + company_ev[7] + company_ev[11:13]
print(acronyme_pfev)
acronyme_cfa = company_v[0] + company_v[7] + company_v[11:]
print(acronyme_cfa) 
print()

print(company_v.index('C'))
print(company_v.index('F'))
print(company_v.rindex('l'))
print()

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
first_because = sentence.index('because')
last_because = sentence.rindex('because')
last_because = int(last_because + len('because'))
becauses = sentence[first_because:last_because]
print(sentence)
print(becauses)
print(sentence.replace(becauses, 'because'))
print()

print(company_v.startswith('Coding'))
print(company_v.startswith('coding'))
print()

trailingspaces = '   Coding For All      '
start = trailingspaces.index('C')
end = trailingspaces.rindex('l')
trailingspaces = trailingspaces[start:(end + 1)]
print(trailingspaces)
print()

test = '30DaysOfPython'
test2 = 'thirty_days_of_python'
print(test.isidentifier())
print(test2.isidentifier())
print()

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultat = '/ '.join(python_libraries)
print()

print('I am enjoying this challenge.\nI just wonder what is next.')

print('\nNAME\tAGE\tCOUNTRY\tCITY')
print('Lucas\t25\tFrance\tLyon')
print()

radius = 10
area = 3.14 * radius ** 2

print(f'The area of a circle with radius {radius} is {(radius*area):.0f} meters square.')
print()

a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
