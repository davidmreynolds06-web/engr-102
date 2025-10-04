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

count = num1
sum = 0 
# Add and count.
while count <= num2:
    sum += count
    count += 1

print("The sum of all integers from", num1, "to", num2, "is", sum)