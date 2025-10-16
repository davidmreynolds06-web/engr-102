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
    print("Both sum to:", left_sum)
else: 
    print("Cannot split evenly")
# Split list
# Lab 7