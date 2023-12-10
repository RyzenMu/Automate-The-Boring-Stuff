import copy

list = [2, 4, 6]
list_new = copy.deepcopy(list)
list_new[1] = 'Hello'
print(list)
print(list_new)
