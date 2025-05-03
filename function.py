def add(n1,n2):
    return n1+n2
n1 = float(input("take a input: "))
n2 = float(input("take other input: "))
result = add(n1, n2)
print(result)

m = 12
n = 23
print(add(m, n))

print(add(2.5, 9))

import turtle

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0
while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()


import turtle

def draw_triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
        

turtle.exitonclick()


import turtle

def draw_triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)  

draw_triangle(100)  
turtle.exitonclick()
 
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
