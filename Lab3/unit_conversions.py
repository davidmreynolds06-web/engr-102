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

from math import*

x = input("Please enter the quantity to be converted: ")
x_float = float(x)
x_str = f"{x_float:.2f}"
newton = x_float*4.44822
newton_str = f"{newton:.2f}"
print(x_str, "pounds force is equivalent to", newton_str, "newtons")
meter = x_float * 3.28084
meter_str = f"{meter:.2f}"
print(x_str, "meters is equivalent to", meter_str, "feet" )
atmosphere = x_float * 101.325
atom_str = f"{atmosphere:.2f}"
print(x_str, "atmospheres is equivalent to", atom_str, "kilopascals" )
btu = x_float*3.41214163
btu_str = f"{btu:.2f}"
print(x_str, "watts is equivalent to",btu_str, "BTU per hour" )
gpm = x_float * 60 * 0.264172052
gpm_str = f"{gpm:.2f}"
print(x_str, "liters per second is equivalent to",gpm_str,"US gallons per minute" )
temp = x_float * (9/5) +32
temp_str = f"{temp:.2f}"
print(x_str, "degrees Celsius is equivalent to",temp_str, "degrees Fahrenheit" )
#bruh
