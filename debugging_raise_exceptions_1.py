"""
**************
*            *
*            *
************** 

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception ("Please enter only one character")
    if (width < 2) or (height < 2):
        raise Exception ("The width and height should be greater than 2")
    print(symbol * width)
    for i in range (height-2):
        print(symbol + (' '*(width-2))+symbol)
    print(symbol * width) 
    
boxPrint("*", 1, 1)             