
def sum(**para):
    tot = 0
    for key, value in para.items():
        tot += value
        print(type(tot))
    print(tot)
        
        
sum(a=3, b=6, c=9, d=6)    


print(sum)

    
         