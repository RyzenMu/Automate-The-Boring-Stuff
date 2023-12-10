import re
message = ' my phone numbers are 536-863-8736, 735-925-8616, 936-136-8436'
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matching_object = regex.findall(message)
print(matching_object)