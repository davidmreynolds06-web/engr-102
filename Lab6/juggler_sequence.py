# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab1 Topic 6
# Date: 03 10 2025
import math

num = int(input("Enter a positive integer: "))

count = 0

print("The Juggler sequence starting at", num, "is:")

while num != 1:
    print(f"{num}, ", end="")
    if num % 2 == 0:
        num = int(math.sqrt(num))
    else:
        num = int((math.sqrt(num)) ** 3)
    count += 1

print("1")
print("It took", count, "iterations to reach 1.")