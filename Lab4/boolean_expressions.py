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

# boolean expressions

############ Part A ############ 

# Take user input and determine if it is true or false
a = (input("Enter True or False for a: "))
b = (input("Enter True or False for b: "))
c = (input("Enter True or False for c: "))

a_bool = ((a == "True") or (a == "T") or (a == "t")) or not ((a == "False") or (a == "F") or (a == "f"))
b_bool = ((b == "True") or (b == "T") or (b == "t")) or not ((b == "False") or (b == "F") or (b == "f"))
c_bool = ((c == "True") or (c == "T") or (c == "t")) or not ((c == "False") or (c == "F") or (c == "f"))

############ Part B ############ 


all_true = (a_bool and b_bool and c_bool)
one_true = (a_bool or b_bool or c_bool)

bool_all_true = bool(all_true)
bool_one_true = bool(one_true)

print(f"a and b and c: {bool_all_true}")
print(f"a or b or c: {bool_one_true}")


############ Part C ############ 
XOR = (a_bool or b_bool) and not(a_bool and b_bool)
bool_XOR = bool(XOR)
print(f"XOR: {bool_XOR}")
even = not ((a_bool and b_bool and not(c_bool)) or (a_bool and c_bool and not(b_bool)) or (b_bool and c_bool and not(a_bool)))
print("Odd number:", even)

############ Part D ############ 
