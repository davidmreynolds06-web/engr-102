# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 3 (Independent)
# Date: 11 09 2025
import math
print("This program calculates the Reynolds number given velocity, length, and viscosity")
print("Please enter the velocity (m/s):")
velo = int(input()) #This takes in the velocity
print("Please enter the length (m):")
lin = float(input()) #This takes in the length
print("Please enter the viscosity (m^2/s):")
visc = float(input()) #This takes in the viscosity
rey_num = int((velo * lin) / visc)
print("Reynolds number is", rey_num) #This prints the Reynolds number
print()
print("This program calculates the wavelength given distance and angle")
print("Please enter the distance (nm):")
thickness = float(input()) #This takes in the distance
print("Please enter the angle (degrees):")
angle = int(input()) #This takes in the angle
wave_len = float(2 * thickness * math.sin((angle*math.pi)/180))
print(f"Wavelength is {wave_len:.4f} nm") #This prints the wavelength
print()
print("This program calculates the production rate given time, initial rate, and decline rate")
print("Please enter the time (days):")
time = int(input()) #This takes in the time
print("Please enter the initial rate (barrels/day):")
i_rate = int(input()) #This takes in the initial rate
print("Please enter the decline rate (1/day):")
d_rate = int(input()) #This takes in the decline rate
constant = 0.8
p_rate = float(i_rate / ((1 + constant * d_rate * time) ** (1 / constant)))
print(f"Production rate is {p_rate:.2f} barrels/day") #This prints the barrel per day decay rate
print()
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
print("Please enter the initial mass (kg):")
i_mass = int(input()) #This takes in the initial mass
print("Please enter the final mass (kg):")
f_mass = int(input()) #This takes in the final mass
print("Please enter the exhaust velocity (m/s):")
e_velo = int(input()) #This takes in the exhaust velocity
c_velo = float(e_velo * math.log(i_mass / f_mass))
print(f"Change of velocity is {c_velo:.1f} m/s") #This prints the change in velocity