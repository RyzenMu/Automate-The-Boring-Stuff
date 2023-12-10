import re
message = 'The adventures of batman'
message1 = 'The adventures of batwoman'
regex = re.compile(r'bat(wo)?man')
result = regex.search(message)
print(result.group())
result1 = regex.search(message1)
print(result1.group())