# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab1 Topic 6
# Date: 03 10 2025
import math

n = int(input("Enter a value for n: "))
n0 = n
n1 = 0
n2 = 0
n3 = 0
n4 = 0
count = 0
sum = 0

for j in range(1, n + 1):
    n1 += 1
    sum += n1

n3 = sum/105

# Find the balancing number.
while n2 != sum:
    n0 += 1
    n2 += n0
    count += 1
    if n2 > sum:
        break
n4 = n2/105

if n3 == n4:
    print(f"{n} is a co-balancing number with r={count}")
else:
    print(f"{n} is not a co-balancing number")