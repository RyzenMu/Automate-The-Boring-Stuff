# * is used for one or more times
import re
message = 'batwowowoman batwoman'
regex = re.compile(r'bat(wo)*man')
matching_object = regex.search(message)
print(matching_object.group())