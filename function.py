#function is a block of code which performs the specified task
# "def" keyword is used to declare a function in python
def fun_1():
    print("This is my first function")
fun_1()

#arguments in function
def fun_2(color):
    print("Colors:",color)
fun_2("pink")
fun_2("blue")
fun_2("red")

#"pass" statement is if a function does not have any definition
def fun_3():
    pass

#----Exercise----
#1.Write a function called calculate_area that takes base and height as an input and returns and area of a 
# triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height
import math
def calculate_area(base,height):
    area = (1/2)*base*height
    return area

base=int(input("Enter base: "))
height=int(input("Enter height: "))
area=calculate_area(base,height)

print("Area:",area)

#2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". 
# Based on shape type it will calculate area. Equation of rectangle's area is,
#rectangle area=length*width
#If no shape is supplied then it should take triangle as a default shape
def calculate_area1(base1,height1,shape="triangle"):
    if shape == "triangle":
        area1 = (1/2)*base1*height1
    elif shape == "rectangle":
        area1 = base1*height1
    else:
        print("Invalid shape")
        return
    return area1

base1=int(input("Enter base: "))
height1=int(input("Enter height: "))
shape=input("Enter shape (triangle or rectangle, default is triangle): ")

area1=calculate_area1(base1,height1,shape)
if area1:
    print("Area of the shape: ",area1)

#3.Write a function called print_pattern that takes integer number as an argument and prints following pattern 
# if input number is 3,
# *
# **
# ***
#if input is 4 then it should print
# *
# **
# ***
# ****
#Basically number of lines it prints is equal to that number.
def print_pattern(num):
    for i in range(1,num+1):
        print("*"*i)

num=int(input("Enter the number: "))
print_pattern(num)