import re
message = "my phone no is 770, 538, and 247, wherie 185 is his number"
regex = re.compile(r'\d\d\d')


# search method
result = regex.search(message)
print(result.group())

#findall method
reult= regex.findall(message)
print(reult)

