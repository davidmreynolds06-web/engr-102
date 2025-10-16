# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 7
# Date: 15 10 2025
n = int(input("Enter a four-digit integer: "))
num = n
count = 0

while num != 6174 and count < 7:
    print(f"{num} >", end=" ")
    num_str = str(n).zfill(4)
    asc_digits = ''.join(sorted(num_str))
    desc_digits = asc_digits[::-1]
    num = int(desc_digits) - int(asc_digits)
    count += 1
print(num, end="")

print(f"\n{n} reaches 6174 via Kaprekar's routine in {count} steps.")
# Kaprekar's constant