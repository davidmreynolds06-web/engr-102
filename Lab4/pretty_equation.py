# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Blake Hammond
# David Reynolds
# Hunter Gilbert
# David Schug
# Section: 412/512
# Assignment: Lab Topic #4
# Date: 12 September 2025

# Pretty Equation 
from math import *
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

# What A might print
if A == 1:
	display_A = "x^2 "

elif A == -1:
	display_A = "- x^2 "

elif A == 0:
	display_A = ""

elif A < 0:
	display_A = f"- {abs(A)}x^2 "
	
else:
	display_A = f"{A}x^2 "

# What B might print
if A != 0:
	if B == 1:
		display_B = "+ x "

	elif B == -1:
		display_B = "- x "

	elif B == 0:
		display_B = ""
	
	elif B < 0:
		display_B = f"- {abs(B)}x "
	
	else:
		display_B = f"+ {B}x "

elif A == 0:
	if B == 1:
		display_B = "x "
	
	elif B == -1:
		display_B = "- x "
	
	elif B == 0:
		display_B = ""

	else:
		display_B = f"{B}x "

	
# What C might print
if B != 0:
	if C == 0:
		display_C = ""

	elif C < 0:
		display_C = f"- {abs(C)} "

	else:
		display_C = f"+ {C} "

elif B == 0:
	if C == 0:
		display_C = ""

	if C < 0:
		display_C = f"- {abs(C)} "
	
	else:
		display_C = f"{C} "

if C == 0:
	display_C = ""
	
print(f'The quadratic equation is {display_A + display_B + display_C}= 0')
