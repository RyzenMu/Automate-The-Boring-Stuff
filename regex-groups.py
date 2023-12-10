import re
message = 'my phone number is 864-852-8642'
regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matching_object = regex.search(message) 
print(matching_object.group())
print(matching_object.group(1))
print(matching_object.group(2))