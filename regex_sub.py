# the sub method find and replace the objects

import re 
message = "Agent Bob gave sceret documents to Agent Murphy"
regex = re.compile(r'Agent \w+')
matching_object = regex.findall(message)
print(matching_object)
new_message = regex.sub('REDACTED', message)
print(new_message)

# A**** B****
regex = re.compile(r'Agent (\w)\w+')
matching_object = regex.findall(message)
print(matching_object)
new_message = regex.sub(r'Agent \1****', message)
print(new_message)
