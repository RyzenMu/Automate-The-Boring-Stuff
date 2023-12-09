# args - non keyword arguments
# kwargs - keyword arguments

def aFunc(*pa): # example of args
    for p in pa:
        print(p)
 
aFunc('jh', 'kjh', 123, 97) 

def anotherFunc(**pas):
    for key, value in pas.items():
        print(key, end='')
        print(value)
        
anotherFunc(p1='123', p2='kjh', p3='ju7')        