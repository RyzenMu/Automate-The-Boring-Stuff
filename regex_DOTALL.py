import re 

message = "Robocop is a hollyeood movie \n where robots perform \n for real"
regex = re.compile(r'.*', re.DOTALL)
matching_object = regex.findall(message)
print(matching_object)