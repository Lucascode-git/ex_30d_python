
print()

with open('/Users/procode/Code/a_ex_30d_python/day_19_obama.txt') as ob:
    text = ob.read()
    listwords = text.split(' ')
    lentext = len(listwords)
    print(lentext)
    line_count = text.splitlines()
    print(line_count)
