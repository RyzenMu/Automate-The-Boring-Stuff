import re
message = 'rororororo boat '
regex = re.compile(r'(ro){3}')
matching_object = regex.search(message)
print(matching_object.group()) 