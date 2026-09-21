import re 
from collections import Counter
print()

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

character = r'[a-zA-Z]'
char_to_remov = r'[%@#&!?$€:;/]'

cleaned_text = re.sub(char_to_remov, '', sentence)
print(cleaned_text)

char = re.findall(character, cleaned_text)
print()

counts = Counter(char).most_common()
# [(num, cha) for cha, num in Counter(char).most_common()] --> reverse key, value
print(counts)
print()

all_char =[]
c = []
for ch in char:
    if ch not in c:
        all_char.append((char.count(ch), ch))
        c.append(ch)
sortedchar = sorted(all_char, reverse=True)
print(sortedchar)

print()