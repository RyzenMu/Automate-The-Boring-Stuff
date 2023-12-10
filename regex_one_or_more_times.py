# the search-value must conatin atleast one or more times
import re
message = 'the adventures of batwoman'
regex = re.compile(r'bat(wo)+man')
matching_object = regex.search(message)
print(matching_object.group())