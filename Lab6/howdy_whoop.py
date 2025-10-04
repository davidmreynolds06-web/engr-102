# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab1 Topic 6
# Date: 03 10 2025
import math

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

count = 1

# Loop it.
while count <= 100:
    if count % num1 == 0 and count % num2 == 0:
        print("Howdy Whoop")
    elif count % num1 == 0:
        print("Howdy")
    elif count % num2 == 0:
        print("Whoop")
    else:
        print(count)
    count += 1