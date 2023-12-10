import re
message = "he said hahahahahahahahaha"
regex = re.compile(r'(ha){3,6}?')
matching_object = regex.search(message)
print(matching_object.group())