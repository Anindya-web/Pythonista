#get inputs for side lengths
slen1 = float(input("enter the side length 1: "))
slen2 = float(input("enter the side length 2: "))
slen3 = float(input("enter the side length 3: "))
slen4 = float(input("enter the side length 4: "))

#check if opposite sides are equal
if (slen1 == slen3) and (slen2 == slen4):
    #check if all sides are equal length:
    if slen1 == slen2 and slen2 == slen3 and slen3 == slen4:
        print("It's a square.")
    else:
        print("It's a rectangle.")

