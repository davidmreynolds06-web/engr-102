# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 12
# Date: 19 11 2025

import numpy as np
import matplotlib.pyplot as plt

def main():
    # start point and matrix (use numpy for all operations)
    v = np.array([0.0, 1.0])
    M = np.array([[1.02, 0.095],
                  [-0.095, 1.02]])
    points = [v.copy()]

    # apply the matrix 250 times
    for _ in range(250):
        v = M @ v
        points.append(v.copy())

    pts = np.array(points)

    # plot
    plt.figure(figsize=(6,6))
    plt.plot(pts[:,0], pts[:,1], marker='.', linestyle='-', markersize=4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Outward spiral: repeated application of a rotation+scaling matrix')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()