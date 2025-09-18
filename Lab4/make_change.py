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
# Assignment: Lab Topic #4
# Date: 12 September 2025

# Make Change

# Take input for payment and output cost and change
payment = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

input_change = (payment - cost)
print(f"You received ${input_change:.2f} in change. That is...")

input_adjusted = int((payment * 100) - (cost * 100))

# Determine Quarters
if (input_adjusted >= 25):
    quarters = int(f"{(input_adjusted // 25)}")
    if(quarters > 1):
        print(f"{quarters:.0f} quarters")
    else:
        print(f"{quarters:.0f} quarter")
else: quarters = 0

change_after_quarters = int(f"{(input_adjusted % 25)}")

# Determine Dimes
if(change_after_quarters >= 10):
    dimes = int(f"{(change_after_quarters // 10)}")
    if(dimes > 1):      
        print(f"{dimes:.0f} dimes")
    else:
        print(f"{dimes:.0f} dime")
else: dimes = 0

change_after_dimes = int(f"{(change_after_quarters % 10)}")

# Determine Nickels
if(change_after_dimes >= 5):
    nickels = int(f"{(change_after_dimes // 5)}")
    if(nickels > 1):
        print(f"{nickels:.0f} nickels")
    else:
        print(f"{nickels:.0f} nickel")
else: nickels = 0

change_after_nickels = int(f"{(change_after_dimes % 5)}")

# Determine Pennies
if(change_after_nickels >= 1):
    pennies = int(f"{(change_after_nickels // 1)}")
    if(pennies > 1):
        print(f"{pennies:.0f} pennies")
    else:
        print(f"{pennies:.0f} penny")
else: pennies = 0
