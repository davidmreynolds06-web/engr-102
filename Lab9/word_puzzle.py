# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Deep Patel
#        Chris Voelkel
#        Karl Nolte
#        David Reynolds
# Section: 412
# Assignment: Lab Topic 9 word puzzle
# Date: 24 October 2025


# number 6 : function  main






def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")






# number 1 : function get_valid_characters


def get_valid_letters(puzzle):
    words = ""
    for c in puzzle:
        if not (c == "|" or c == "," or c == " "):
            words += c
    words = set(words)
    return "".join(words)


# number 2 : function  is_valuid_guess
def is_valid_guess(is_valid, guess):
    if len(guess) != 10:         # the length has to be 10
        return False
    if len(set(guess)) != 10:     # all characters have to be unique
        return False
    for char in guess:
        if char not in is_valid:      
            return False
    return True


# number 3 : function check_users_guess
def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == (quotient * divisor) + remainder:
        return True
    else:
        return False




# number 4 : function make_number
def make_number(word, valid_guess):
    number = ""
    for char in word:
        if char not in ["|", ",", " "]:
            number += str(valid_guess.index(char))
    return int(number)




# number 5: function make_numbers   (with an s)


def make_numbers(puzzle, user_guess):
    parts = puzzle.split(",")     # we are splitting the puzzle into pieces by the comma


    # here we are figuring out which part is which
    quotient_word = parts[0]           # first part before comma
    divisor_word = parts[1].split("|")[0] # part before | in 2nd
    dividend_word = parts[1].split("|")[1]   # part after |
    remainder_word = parts[-1].strip()            # last word in the puzzle which is our remainder


# now turn the words into numbers using the last function we made
    dividend = make_number(dividend_word, user_guess)
    quotient = make_number(quotient_word, user_guess)
    divisor = make_number(divisor_word, user_guess)
    remainder = make_number(remainder_word, user_guess)


    return dividend, quotient, divisor, remainder   # all returned as a tuple








def main():
    puzzle = input("Enter a word arithmetic puzzle: \n")    # asks for input
    print_puzzle(puzzle)    # printing it by calling the functioun to print


    valid_letters = get_valid_letters(puzzle)      # getting valid characters from the puzzle
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")  # asking for input for guess
   


    if not is_valid_guess(valid_letters, guess):    # chekcing if they guessed validly
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        return


    dividend, quotient, divisor, remainder = make_numbers(puzzle, guess) # making numbers from the words


    if check_user_guess(dividend, quotient, divisor, remainder):  # here we arew check if the guess is correct
        print("Good job!")
    else:
        print("Try again!")






if __name__ == '__main__':
    main()






    # RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA
    # TAKEOURSIM
