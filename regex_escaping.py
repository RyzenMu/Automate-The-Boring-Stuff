import re
# use backslash to escape ?, *. +

message = 'Waht is the value?*+to'
regex = re.compile(r'\?\*\+')
matching_object = regex.search(message)
print(matching_object.group())
