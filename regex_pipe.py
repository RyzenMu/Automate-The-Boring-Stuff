import re
message = "batman. batmobile lost a wheel, batbat is a bat of a bat"
regex = re.compile(r'bat(man|mobile|bat)')
matching_object = regex.findall(message)
print(matching_object)
regex = re.compile(r'bat(man|mobile|bat)')
matching_object = regex.search(message)
print(matching_object.group())
