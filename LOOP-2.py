#WHILE LOOP

#print numbers
# i = 5
# while i>= 0:
#     i-= 1
#     print(i)
#namta
# n = input("Please enter a number: ")
# n = int(n)
# m = 1
# while m<= 10:
#     print(n, "x" , m, "=" , n*m)
#     m+= 1


#36 axis color circle
# import turtle
# turtle.color("red")
# turtle.speed(15)
# counter = 0
# while counter < 36:  #[360/10 = 36. as acircle is 360 degree]
#     for i in range(4): 
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     counter+= 1

# turtle.exitonclick()

#dotted square
import turtle

height = 5
width = 5

turtle.speed(2)

turtle.penup()

for y in range(height):
    for x in range (width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)        
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()