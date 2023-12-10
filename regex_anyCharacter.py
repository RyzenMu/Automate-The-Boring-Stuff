import re
# use . for any
message = 'i eat cat food for lunch'
regex = re.compile(r'.at')
matching_object = regex.findall(message)
print(matching_object)  