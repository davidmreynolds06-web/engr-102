# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 2 (Independent)
# Date: 05 09 2025
import math
velo = 9
visc=0.0015
lin = 0.875
print("Reynolds number is", (velo * lin) / visc); #This prints the Reynolds number
thickness = 0.029
angle = 35
print("Wavelength is", 2 * thickness * math.sin((angle*math.pi)/180), "nm"); #This prints the wavelength
time = 10
P_Rate = 100
D_Rate = 2
Cons = 0.8
print("Production rate is", P_Rate / ((1 + Cons * D_Rate * time) ** (1 / Cons)), "barrels/day"); #This prints the barrel per day decay rate
I_Mass = 11000
F_Mass = 8300
E_Velo = 2029
print("Change of velocity is", E_Velo * math.log(I_Mass / F_Mass), "m/s"); #This prints the change in velocity