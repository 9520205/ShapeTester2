#!/usr/bin/python

class ShapeTester:
    shapeL = 0
    shapeW = 0
    shapeH = 0
    shapeR = 0
    Y = True

    shapQues = input("Is your shape a 'box', sphere or pyramid? (input answer in lowercase) ")

    if (shapQues == "box"):
        L = shapeL + int(input("What is the length of your box? "))
        W = shapeW + int(input("What is the width of your box? "))
        H = shapeH + int(input("What is the height of your box? "))

        boxSa = str(L*W)
        boxVol = str(L*W*H)

        print(" ")
        print("The surface area of your box is: " + boxSa)
        print("The volume of your box is: " + boxVol)

    elif (shapQues == "sphere"):
        R = shapeR + int(input("What is the radius of your sphere? "))

        sphereSa = str(R*R*3.14*4)
        sphereVol = str(R*R*R*3.14*4/3)

        print(" ")
        print("The surface area of your sphere is: " + sphereSa)
        print("The volume of your sphere is: " + sphereVol)

    elif (shapQues == "pyramid"):
        pyrL = 0
        pyrW = 0
        pyrH = 0

        L = pyrL + int(input("What is the length of your pyramid? "))
        W = pyrW + int(input("What is the width of your pyramid? "))
        H = pyrH + int(input("What is the height of your pyramid? "))

        pyrVol = str(L*W*H/3)

        print(" ")
        print("The volume of your pyramid is: " + pyrVol)
        print("Surface area for this shape cannot be provided")
        
    else:

        print(" ")
        print("There was a mistype or an unrecognizable input. Please try again.")

    
