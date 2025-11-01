# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 10
# Date: 31 10 2025
def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

num1 = input("Enter the first Roman numeral: ")
num2 = input("Enter the second Roman numeral: ")

# Convert Roman numerals to integers
int1 = roman_to_int(num1)
int2 = roman_to_int(num2)

if int1 < int2:
    print(f"{num1} is less than {num2}.")
elif int1 > int2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")