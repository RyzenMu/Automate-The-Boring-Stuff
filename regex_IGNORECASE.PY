import re
message = " Why does A carrot so red Ear"
regex = re.compile(r'[aeiou]', re.IGNORECASE)
matching_object = regex.findall(message)
print(matching_object)