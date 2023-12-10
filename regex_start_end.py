import re
beginWithHelloRegex = re.compile(r'^Hel')
message = 'Hello World Hello Super girl'
matching_object = beginWithHelloRegex.findall(message)
print(matching_object)

endwithWorldRegex = re.compile(r'ld$')
message = "Hello World"
matching_object = endwithWorldRegex.findall(message)
print(matching_object)