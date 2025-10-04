import math

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

count = 1

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