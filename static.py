# static typed
def add(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError("Both args must be int")
    return a+b
print(add(10,20))
print(add("a","b"))


# Duck typed
def add(a,b):
    return a+b
print(add(10,20))
print(add("a","b"))
