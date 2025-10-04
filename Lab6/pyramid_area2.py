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
from math import*

# get the variables needed to calculate
side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))



# cal the total area using an artihmatic sequence

area = (3 * layers * layers + 2 * layers) * (side_length ** 2)

print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")