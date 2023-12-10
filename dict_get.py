myDict = {
    "name" : "samsung",
    "color" : "black",
    "price" : 11000,
    "os" : "android",
}

myVar = myDict.get('size', "found not")
print(myVar)
myVar = myDict.get('os', "not found")
print(myVar)