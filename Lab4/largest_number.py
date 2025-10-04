# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 4 (Independent)
# Date: 18 09 2025
x = float(input("Enter number 1: "))#This takes in the first number
y = float(input("Enter number 2: "))#This takes in the second number
z = float(input("Enter number 3: "))#This takes in the third number

largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z

print(f"The largest number is {largest}")