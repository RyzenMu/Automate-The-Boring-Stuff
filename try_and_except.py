
def div(num):
    try:
        print(65/num)
    except ZeroDivisionError:
        print('Koo moo tai')
        
div(9)
div(0)
div(6)  

print('Enter the number of cats')
cats = (input())
try:
    if int(cats) >= 4:
        print("You have" + " "+ str(cats) + " cats")
    else:
        print("You have less vcats")    
except ValueError:
    print('Please a number')          