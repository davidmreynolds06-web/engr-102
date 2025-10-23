# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 8
# Date: 22 10 2025
let_num = {'a': '4', 'e': '3', 'o': '0', 's': '5', 't': '7'} #dictionary mapping letters to numbers
text = input("Enter some text: ")
leet_text = ""
for char in text: #iterate through each character in the input text
    leet_text += let_num.get(char, char) #replace the character with its leet equivalent if it exists
print(f"In leet speak, \"{text}\" is: {leet_text}")