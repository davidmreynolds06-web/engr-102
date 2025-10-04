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
# Take user input for side length and number of layers
side_leg = float(input("Enter the side length in meters: "))
layer_amnt = float(input("Enter the number of layers: "))

# Number of cubes per side per layer, this will be used to restate side_cube_amnt
side_cube_amnt = layer_amnt

# Initialize Variables | side_at = side area total | top_at = top area total | bot_at = bottom area total |
side_at = 0
top_at = 0
bot_at = 0

# Compute side surface area
while (side_cube_amnt > 0):
    side_area = (4 * ((side_leg ** 2) * (side_cube_amnt)))
    side_cube_amnt -= 1
    side_at += side_area

# Set side cube amount back to its initial value
side_cube_amnt = layer_amnt

# Compute top surface area
while (side_cube_amnt > 0):
    top_area = (side_leg ** 2) * (side_cube_amnt ** 2)
    side_cube_amnt -= 1
    top_at += top_area
    
# Set side cube amount back to its initial value
# Subtruct 1 since we are not removing the bottom area of the lowest layer
side_cube_amnt = layer_amnt - 1

# Compute bottom surface area which will be removed from the top
while (side_cube_amnt > 0):
    bot_area = (side_leg ** 2) * (side_cube_amnt ** 2)
    side_cube_amnt -= 1   
    bot_at += bot_area    
surf_area = (side_at + (top_at - bot_at))
print(f"You need {surf_area:.2f} m^2 of gold foil to cover the pyramid")
