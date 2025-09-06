# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 2 (Independent)
# Date: 05 09 2025
import math
t0 = 12
x0 = 8
y0 = 6
z0 = 7
t3 = 85
x3 = -5
y3 = 30
z3 = 9
t1 = 30
x1 = ((x3-x0)/(t3-t0))*(t1-t0)+x0
y1 = ((y3-y0)/(t3-t0))*(t1-t0)+y0
z1 = ((z3-z0)/(t3-t0))*(t1-t0)+z0
print("At time 30.0 seconds:")
print("x1 =", x1, "m")
print("y1 =", y1, "m")
print("z1 =", z1, "m")
t2 = 37.5
x2 = ((x3-x0)/(t3-t0))*(t2-t0)+x0
y2 = ((y3-y0)/(t3-t0))*(t2-t0)+y0
z2 = ((z3-z0)/(t3-t0))*(t2-t0)+z0
print("At time 37.5 seconds:")
print("x2 =", x2, "m")
print("y2 =", y2, "m")
print("z2 =", z2, "m")
#This is a little much