import re

message = 'First Name : Al Last Name : Sterhart'
regex = re.compile(r'First Name : (.*) Last Name : (.*)')
matching_object = regex.findall(message)
print(matching_object)

message = '< To serve humand/ for dinner/'
greedyRegex = re.compile(r'<.*/')
matching_object = greedyRegex.findall(message)
print(matching_object)
lazyMatchRegex = re.compile(r'<.*?/')
matching_object = lazyMatchRegex.findall(message)
print(matching_object)