import math

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

count = num1
sum = 0 
while count <= num2:
    sum += count
    count += 1

print("The sum of the integers from", num1, "to", num2, "is", sum)