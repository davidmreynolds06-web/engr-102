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
# Assignment: Lab Topic #7
# Date: 8 October 2025
from colorama import Fore, Style

# Print user input rules
print("To play type a coordinate corresponding to the space you would like to place your piece on.")
print("Enter your space in the format row, column.")
print("For example if I wanted to place my piece on space 1 of row a, I would enter a1.")
print("If the space you want to take has already been played, you will be prompted to enter a different space.")
print("Enter the word 'stop' to end the game.\n")

# Initialize grid lists and take input
row_top = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
row_a = ["a", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_b = ["b", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_c = ["c", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_d = ["d", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_e = ["e", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_f = ["f", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_g = ["g", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_h = ["h", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
row_i = ["i", "○", "○", "○", "○", "○", "○", "○", "○", "○"]
full_grid = [row_top, row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i]


# Create list for the row letters so that we can use the index function to later covert to int
row = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i"]

# Overarching loop
count = 0

while True:

# For Blacks Turn
    if count % 2 == 0:

        # Print Grid
        x = 0
        y = 0
        while x <= 9:
            while y <= 9:
                print(full_grid[x][y], end=' ')
                y += 1
            print()
            x += 1
            y = 0

        # Get user input
        print("\nBlack to play")
        user_in = (input("What space would you like to take? "))
        print()

        # Check for stop
        if user_in == "stop":
            print("Thanks for playing!")
            break     

        # Find grid value   
        row_num = int(row.index(user_in[0:1]))
        column = int(user_in[1:2])

        # Check to make sure the input is correct, and ask for a new location if not
        while full_grid[row_num][column] == Fore.WHITE + Style.BRIGHT + "●" + Fore.RESET + Style.NORMAL or full_grid[row_num][column] == Fore.BLACK + Style.DIM + "●" + Fore.RESET + Style.NORMAL:
            print("That space has already been taken, try again.")
            user_in = (input("What space would you like to take? "))
            print()
            row_num = int(row.index(user_in[0:1]))
            column = int(user_in[1:2])

        # Place the users piece onto the board
        full_grid[row_num][column] = Fore.BLACK + Style.DIM + "●" + Fore.RESET + Style.NORMAL

        count += 1

# For Whites Turn
    elif count % 2 == 1:
        
        # Print Grid
        x = 0
        y = 0
        while x <= 9:
            while y <= 9:
                print(full_grid[x][y], end=' ')
                y += 1
            print()
            x += 1
            y = 0

        # Get user input
        print("\nWhite to play")
        user_in = (input("What space would you like to take? "))
        print()

        # Check for stop
        if user_in == "stop":
            print("Thanks for playing!")
            break

        # Find grid value
        row_num = int(row.index(user_in[0:1]))
        column = int(user_in[1:2])

        # Check to make sure the input is correct, and ask for a new location if not
        while full_grid[row_num][column] == Fore.WHITE + Style.BRIGHT + "●" + Fore.RESET + Style.NORMAL or full_grid[row_num][column] == Fore.BLACK + Style.DIM + "●" + Fore.RESET + Style.NORMAL:
            print("That space has already been taken, try again.")
            user_in = (input("What space would you like to take? "))
            print()
            row_num = int(row.index(user_in[0:1]))
            column = int(user_in[1:2])

        # Place the users piece onto the board
        full_grid[row_num][column] = Fore.WHITE + Style.BRIGHT + "●" + Fore.RESET + Style.NORMAL

        count += 1