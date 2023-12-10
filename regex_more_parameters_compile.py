import re
# to add m0re use Pipe | e.g re.DOTALL | re.IGNORECASE |re.VERBOSE
regex = re.compile(r'''
                   \d\d\d # area code
                   - # first dash
                   \d\d\d # first 3 digits
                   - # second dash
                   \d\d\d\d # second 4 digits
                   ''', re.VERBOSE | re.IGNORECASE | re.DOTALL)

message = 'My phone number is 735-816-9164'
matching_object = regex.findall(message)
print(matching_object)
