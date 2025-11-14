# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Deep Patel
#        Chris Voelkel
#        Karl Nolte
#        David Reynolds
# Section: 412
# Assignment: Lab Topic 12
# Date: 10 November 2025
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material




import numpy as np


# a
list_A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]   # creating list with 12 elements between 0 and 11




list_B = [0, 1, 2, 3, 4, 5, 6, 7]  # 8 elements
 


list_C = [0, 1, 2, 3, 4, 5]  # 6 elements


# making the lists into arrays based on size
A = np.array(list_A).reshape(3,4)


B = np.array(list_B).reshape(4,2)


C = np.array(list_C).reshape(2,3)


# b - printing with spaces
print(A)
print()
print(B)
print()
print(C)
print()


# c
# dot is product of 2 arrays
D = A.dot(B).dot(C)


# d
print(D)
print()


# e


E = np.sqrt(D)/2    # using sqrt function on D , each elemt
print(E)
