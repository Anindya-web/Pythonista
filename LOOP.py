#WHILE LOOP
#kaan dhore uthbos kora
kotobaar = 0
while (kotobaar<10):
    print('Ek baar uthbosh krchi')
    kotobaar+= 1

# Festival Wish
eidwish = 0
while (eidwish < 5):
    print("EID MUBARAK")
    eidwish+= 1

pujawish = 0
while (pujawish < 5):
    print("মায়ের আশীর্বাদ যেন আপনার জীবনের পথ থেকে সমস্ত বাধা অপসারণ করতে পারে। শুভ মহালয়া!")
    pujawish+= 1


#FOR LOOP
#apple counter
for apple_count in range(10):
    print("Ekjon ke apple dichi")
    apple_count+= 1
    
#addition counter
addition_num = 0
for addition_num in range(10):
    addition_num = addition_num+1
print("The total sum is:  ",addition_num)


# number output from 1 to 20
n = 1
for n in range(21):
   print(n)

# number output from 36 to 64
for n in range(36,64):
    print(n)

#summation of 1  to 100
sum = 0
for n in range (1,101):
   sum = sum + n
print(sum)

#square with turtle
import turtle
turtle.shape("turtle")
turtle.speed(1)
for value in range(4):
  turtle.forward(100)
  turtle.left(90)

turtle.exitonclick()

#large number printer
n = [6, 1, 3, 0, 9, 3, 2, 5]
L_N = n[0]
for n in n:
   if n > L_N:
       L_N = n
print(L_N)

#list of reminder by 5
result = 0
for num in range(100):
   if num % 5 == 0:
       print(num)
       result+= num
print("Sum is: ", result)        

#using for loop
result = 0
for num in range(5,101,5):
   print(num)
   result+= num
print("Sum is: ", result)

#Dashline drawing

import turtle

turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()

#nested loop
#square
import turtle
turtle.shape("turtle")
turtle.speed(1)

for side_L in range(50, 100, 10):
    for i in range(4):
        turtle.forward(side_L)
        turtle.left(90)

turtle.exitonclick()

# loop in list
saarc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
for country in saarc:
    print(country, "is a member of SAARC")
                                            
li = list(range(11))
print(li)
li = list(range(2,21,2))
print(li)