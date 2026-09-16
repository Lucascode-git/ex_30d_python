print('\n ---- START SETS ----\n')
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


set_comp = set(it_companies)
print(set_comp)
print(len(set_comp))
print()
set_comp.add('Twitter')
print(set_comp)
set_comp.update(['Nvidia', 'TSMC', 'Anthropic'])
print(set_comp)

set_comp.remove('Twitter')
# discard = no error if company not in list 
set_comp.discard('Snapchat')
print(set_comp)
print()

aandb = A.union(B)
print(aandb)
intersect_ab = A.intersection(B)
print(intersect_ab)
a_sub_b = A.issubset(B)
print(f'A subset of B: {a_sub_b}')

#A.update(B)
#print(A)
#B.update(A)
#print(B)

sym_diff_ab = A.symmetric_difference(B)
print(sym_diff_ab)
del A
del B
print()

setage = set(age)
lenlist = len(age)
lenset = len(setage)
print(lenlist, lenset)
print(lenlist > lenset)
print()

sentence = 'I am a teacher and I love to inspire and teach people'
senlist = sentence.split(' ')
print(senlist)

uniqueword = []
for word in senlist:
    if senlist.count(word) < 2:
        uniqueword.append(word)
    else:
        continue

print(f'\nList of unique word contain {len(uniqueword)} word:\n{uniqueword}')




print('\n ---- END SETS ----\n')