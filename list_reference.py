list = [1, 2, 3, 4]
cp_list = list
cp_list[1] = 'Hello'
print(cp_list)
print(list) #there is only one list with several names 

list2 = list + [5, 6]
print(list2)
print(list) # list is a mutable value