# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 4 (Independent)
# Date: 18 09 2025
import math

day = int(input("Please enter a positive value for day: "))
gadget_count = 0
if day < 0:
    print("You entered an invalid number!")
elif day < 11:
    gadget_count = day * 10
    print(f"The sum total number of gadgets produced on day {day} is {gadget_count}")
elif day == 11:
    gadget_count = 100 + 11
    print(f"The sum total number of gadgets produced on day {day} is {gadget_count}")
elif day > 11 and day < 50:
    gadget_count = 100 + ((1/2) * (11 + day) * (day - 10))
    print(f"The sum total number of gadgets produced on day {day} is {gadget_count:.0f}")
elif day >= 50 and day < 101:
    gadget_count = 100 + 990 + (50 * (day - 49))
    print(f"The sum total number of gadgets produced on day {day} is {gadget_count:.0f}")
else:
    gadget_count = 100 + 990 + 1