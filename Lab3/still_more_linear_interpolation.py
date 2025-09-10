# Linear Interpolation
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Blake Hammond
# David Reynolds
# Hunter Gilbert
# David Schug
# Section: 412/512
# Assignment: Lab Topic #3
# Date: 9 September 2025

# Prompt user to input initial time and locations
from math import *
time_1 = float(input("Enter time 1: "))
x_first = float(input("Enter the x position of the object at time 1: "))
y_first = float(input("Enter the y position of the object at time 1: "))
z_first = float(input("Enter the z position of the object at time 1: "))
time_2 = float(input("Enter time 2: "))
x_final = float(input("Enter the x position of the object at time 2: "))
y_final = float(input("Enter the y position of the object at time 2: "))
z_final = float(input("Enter the z position of the object at time 2: "))
print()

# Find 3 times between the two originals
middle_time = (time_1 + time_2)/2
time_3 = (middle_time + time_1)/2
time_4 = (middle_time + time_2)/2

x3 = (x_final - x_first) / (time_2 - time_1) * (time_3 - time_1) + x_first
y3 = (y_final - y_first) / (time_2 - time_1) * (time_3 - time_1) + y_first
z3 = (z_final - z_first) / (time_2 - time_1) * (time_3 - time_1) + z_first

x_middle = (x_final - x_first) / (time_2 - time_1) * (middle_time - time_1) + x_first
y_middle = (y_final - y_first) / (time_2 - time_1) * (middle_time - time_1) + y_first
z_middle = (z_final - z_first) / (time_2 - time_1) * (middle_time - time_1) + z_first

x4 = (x_final - x_first) / (time_2 - time_1) * (time_4 - time_1) + x_first
y4 = (y_final - y_first) / (time_2 - time_1) * (time_4 - time_1) + y_first
z4 = (z_final - z_first) / (time_2 - time_1) * (time_4 - time_1) + z_first

# Print results
print(f"At time {time_1:.2f} seconds the object is at ({x_first:.3f}, {y_first:.3f}, {z_first:.3f})")
print(f"At time {time_3:.2f} seconds the object is at ({x3:.3f}, {y3:.3f}, {z3:.3f})")
print(f"At time {middle_time:.2f} seconds the object is at ({x_middle:.3f}, {y_middle:.3f}, {z_middle:.3f})")
print(f"At time {time_4:.2f} seconds the object is at ({x4:.3f}, {y4:.3f}, {z4:.3f})")
print(f"At time {time_2:.2f} seconds the object is at ({x_final:.3f}, {y_final:.3f}, {z_final:.3f})")