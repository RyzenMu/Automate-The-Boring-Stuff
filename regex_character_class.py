import re
message = 'I am a man of age thity'
regex = re.compile(r'[aeiou]')# (a|e|i|o|u)
matching_object = regex.findall(message)
print(matching_object)

#not character - ^
#find all consonants
message = 'I am a man of age thity'
regex = re.compile(r'[^aeiou]')# (^a|e|i|o|u)
matching_object = regex.findall(message)
print(matching_object)
