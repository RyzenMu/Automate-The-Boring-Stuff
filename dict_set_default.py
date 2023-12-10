myDict = {
    "name" : "samsung",
    "color" : "black",
    "price" : 11000,
    "os" : "android",
}

myDict.setdefault('size', 5.5)
myDict.setdefault('os', 'windows')

print(myDict.values())