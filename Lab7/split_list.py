# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 7
# Date: 15 10 2025
num_list = [int(x) for x in input("Enter numbers: ").split()]

middle_index = len(num_list) // 2

first_half = num_list[:middle_index]
second_half = num_list[middle_index:] 

left_sum = 0
for num in first_half:
    left_sum += num

right_sum = 0
for num in second_half:
    right_sum += num

if left_sum == right_sum:
    print("Left:", first_half)
    print("Right:", second_half)
    print("Both sum to", left_sum)
elif left_sum > right_sum:
    second_half = [first_half[-1]] + second_half
    first_half = first_half[:-1]
    left_sum = 0
    for num in first_half:
        left_sum += num

    right_sum = 0
    for num in second_half:
        right_sum += num

    if left_sum == right_sum:
        print("Left:", first_half)
        print("Right:", second_half)
        print("Both sum to", left_sum)
    else: 
        print("Cannot split evenly")
elif right_sum > left_sum:
    first_half += [second_half[0]]
    second_half = second_half[1:]
    left_sum = 0
    for num in first_half:
        left_sum += num

    right_sum = 0
    for num in second_half:
        right_sum += num

    if left_sum == right_sum:
        print("Left:", first_half)
        print("Right:", second_half)
        print("Both sum to", left_sum)
    else: 
        print("Cannot split evenly")
    
# Split list
# Lab 7