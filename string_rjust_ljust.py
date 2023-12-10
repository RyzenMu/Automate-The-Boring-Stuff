str = 'hello'
str_rjust = str.rjust(10)
str_ljust = str.ljust(10)

print(str_ljust)
print(str_rjust)

str_rjust = str.rjust(20, '*')
print(str_rjust)

#center
str_center = str.center(20, '-')
print(str_center)