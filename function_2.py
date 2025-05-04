def myfnc(x):      #local variable x
    print("inside myfnc", x)
    x = 10
    print("inside myfnc", x)

x = 20 
myfnc(x)
print(x)

def myfnc(y):
    print("y =", y)
    print("x =", x)

x = 20 
myfnc(x)

def myfnc(y):
    print("y =", y)
    print("x =", x)

x = 20
myfnc(x)
print("y:", y)

def myfnc(y=10):
    print("y =", y)
x = 20
myfnc(x)
myfnc()


# def myfnc(x, y=10, z):
#     print("x =", x, "y=", y "z=", z)
# x = 5
# y = 6
# z = 8
# myfnc(x,y,z)

def myfnc(x=3, y=10, z=8):
    print("x =", x, "y =", y, "z =", z)
x = 5
y = 6
z = 8
myfnc(x,y,z)

def myfnc(x,z, y=10):
    print("x =", x, "y =", y, "z =", z)

myfnc(x = 1, y = 2, z = 5)
a = 5
b = 6
myfnc(x = a, z = b)
a = 2
b = 9
c = 17
myfnc(y = a, z = b, x = c)

def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

result = add_numbers([1, 30, 4.6, 9.2, 4, 7, 24, 34])
print(result)
