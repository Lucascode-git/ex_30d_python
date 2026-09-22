l1 = [5,8,9]
l2 = [10,34,5]

ltot = [l1, l2]
print(ltot)

test = []
for list in ltot:
    
    test.append(list)
print(test)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3', 'item5'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1))
