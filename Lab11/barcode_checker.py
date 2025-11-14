# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 11
# Date: 13 11 2025

def is_valid_barcode(code: str) -> bool:
    if len(code) != 13 or not code.isdigit():
        return False
    # first 12 digits split into odd/even positions (0-based)
    first_sum = sum(int(code[i]) for i in range(0, 12, 2))
    second_sum = sum(int(code[i]) for i in range(1, 12, 2))
    total = second_sum * 3 + first_sum
    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(code[12])