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