import pprint
myStr = 'It was a bright winter day in april'

count = {}

for character in myStr.upper():
    count.setdefault(character, 0)
    count[character] = count[character] +1
    
pprint.pprint(count)    