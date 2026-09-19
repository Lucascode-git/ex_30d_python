import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = r'[a-zA-Z]+'
matchwords = re.findall(words, paragraph)
#print(matchwords)
print()

pairdouble =[]
word = []
for oneword in matchwords:
    if oneword not in word:
        count = matchwords.count(oneword)
        pairing = (count, oneword)
        pairdouble.append(pairing)
        word.append(oneword)
    
sortedone = sorted(pairdouble, key= lambda pair: pair[0], reverse=True)
#print(sortedone)
print()

sentence = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
numbers = r'-?\d+'

points = re.findall(numbers, sentence)
sorted_points = []
for num in points:
    sorted_points.append(int(num))

sorted_points = sorted(sorted_points)
print(sorted_points)
distance = max(sorted_points) - min(sorted_points)
print(distance)









print()

