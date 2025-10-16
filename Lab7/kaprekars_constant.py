# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 7
# Date: 15 10 2025
n = int(input("Enter a four-digit integer: "))
count = 0

while n != 6174 and count < 7:
    print(f"{n} >", end=" ")
    num_str = str(n).zfill(4)
    asc_digits = ''.join(sorted(num_str))
    desc_digits = asc_digits[::-1]
    n = int(desc_digits) - int(asc_digits)
    count += 1
print(n, end="")

print(f"\nKaprekar's constant reached in {count} steps.")
# Kaprekar's constant