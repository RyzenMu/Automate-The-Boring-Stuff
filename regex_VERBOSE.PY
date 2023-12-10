import re
regex = re.compile(r'''
                   \d\d\d # area code
                   - # first dash
                   \d\d\d # first 3 digits
                   - # second dash
                   \d\d\d\d # second 4 digits
                   ''', re.VERBOSE)

message = 'My phone number is 735-816-9164'
matching_object = regex.findall(message)
print(matching_object)
