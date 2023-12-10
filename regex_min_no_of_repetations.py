import re
message = "rorororororr boat"
regex = re.compile(r'(ro){2,4}')
matching_objects = regex.search(message)
print(matching_objects.group())
