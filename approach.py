def add(a,b):
    return a+b
def sum(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return"Division by zero not allowed"
x=int(input("Enter 1st value:")
y=int(input("Enter 2nd value:")
print("Addition:",add(x,y))
