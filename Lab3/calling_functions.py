# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 3 (Independent)
# Date: 11 09 2025

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here
print("Please enter the side length:")
side_length = float(input())
area_triangle = (sqrt(3)/4) * (side_length ** 2)
printresult('triangle', side_length, area_triangle)
area_square = side_length ** 2
printresult('square', side_length, area_square)
area_pentagon = (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * (side_length ** 2)
printresult('pentagon', side_length, area_pentagon)
area_hexagon = (3 * sqrt(3) / 2) * (side_length ** 2)
printresult('hexagon', side_length, area_hexagon)
area_dodecagon = 3 * (2 + sqrt(3)) * (side_length ** 2)
printresult('dodecagon', side_length, area_dodecagon)