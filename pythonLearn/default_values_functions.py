# default Values
def add(x, y=2):  # y will be 4  by default, default arguments have to be at the end
    return x + y


print(add(x=7))
print(add(x=7, y=8))