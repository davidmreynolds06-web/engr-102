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
# Assignment: Lab Topic #6
# Date: 1 October 2025
from math import * 

# User input for x
x = float(input("Enter a value for x: "))

# Verify user value is correct and reprompt if incorrect
while ((x <= 0) or (x > 2)):
    x = float(input("Out of range! Try again: "))

# User input for tolerance
tol = float(input("Enter the tolerance: "))

# Initialize Variables
ln_approx = 0.0
vari_term = 1

# Calculate the natural logarithm using Taylor series expansion
while True:
    term = ((-1) ** (vari_term + 1)) * (((x - 1) ** vari_term) / vari_term)
    # Increase power and divisor every loop
    vari_term += 1
    # End sequence when tolerance is larger than the next term
    if abs(term) < tol:
        break
    ln_approx += term 

print(f"ln({x}) is approximately {ln_approx}")
print(f"ln({x}) is exactly {log(x)}")
# Evaluate difference
if log(x) > ln_approx:
    print(f"The difference is {log(x) - ln_approx}")
else: print(f"The difference is {ln_approx - log(x)}")