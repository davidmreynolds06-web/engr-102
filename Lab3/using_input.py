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
velo = float(input("Please enter the velocity (m/s): ")) #This takes in the velocity
lin = float(input("Please enter the length (m): ")) #This takes in the length
visc = float(input("Please enter the viscosity (m^2/s): ")) #This takes in the viscosity

rey_num = int(((velo * lin) / visc) + 0.5) #This calculates the Reynolds number

print("Reynolds number is", rey_num) #This prints the Reynolds number
print()
print("This program calculates the wavelength given distance and angle")
thickness = float(input("Please enter the distance (nm): ")) #This takes in the distance
angle = float(input("Please enter the angle (degrees): ")) #This takes in the angle
wave_len = float(2 * thickness * math.sin((angle*math.pi)/180))
print(f"Wavelength is {wave_len:.4f} nm\n") #This prints the wavelength
print("This program calculates the production rate given time, initial rate, and decline rate")
time = float(input("Please enter the time (days): ")) #This takes in the time
i_rate = float(input("Please enter the initial rate (barrels/day): ")) #This takes in the initial rate
d_rate = float(input("Please enter the decline rate (1/day): ")) #This takes in the decline rate
constant = 0.8
p_rate = float(i_rate / ((1 + constant * d_rate * time) ** (1 / constant)))

print(f"Production rate is {p_rate:.2f} barrels/day\n") #This prints the barrel per day decay rate

print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
i_mass = float(input("Please enter the initial mass (kg): ")) #This takes in the initial mass
f_mass = float(input("Please enter the final mass (kg): ")) #This takes in the final mass
e_velo = float(input("Please enter the exhaust velocity (m/s): ")) #This takes in the exhaust velocity
c_velo = float(e_velo * math.log(i_mass / f_mass))
print(f"Change of velocity is {c_velo:.1f} m/s") #This prints the change in velocity