import re
message = "my number is 777-976-1004 and 354-357-3087"
reg = re.compile(r'\d\d\d')
result = reg.search(message)
print(result.group())