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
import matplotlib.pyplot as plt






# 1


x = np.linspace(-2.0,2.0,100)


f1, f2 = 2, 6


y1 = (1 / (4 * f1)) * x**2
y2 = (1 / (4 * f2)) * x**2


# starting plot
plt.figure(figsize=(7,5))
plt.plot(x, y1, color = "purple", linewidth = 2.0, label = "f = 2")
plt.plot(x, y2, color = "yellow", linewidth = 2.0, label = "f = 6")
plt.title("Parabola plots with varying focal length")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(False)
plt.show()










# 2


x = np.linspace(-4.0,4.0,25)
y = 2 * x**3 + 3*x**2 -11*x - 6      # cubic polynomial


# starting the plotting


plt.figure(figsize=(7,5))
plt.plot(x, y, "*", linewidth = 2, markersize=6 , label ="Plot of cubic polynomial")
plt.title("Plot of cubic polynomial")
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)
plt.show()








#3
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y_sin = np.sin(x)
y_cos = np.cos(x)




fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))


# sine subplot
ax1.plot(x, y_sin, color = "purple", linewidth = 2.0, label="sin(x)")
ax1.set_ylabel("y=sin(x)")
ax1.grid(True)
ax1.legend()
# cosine subplot
ax2.plot(x, y_cos, color = "green", linewidth = 2, label = "cos(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y=cos(x)")
ax2.grid(True)
ax2.legend()


fig.suptitle("Plot of cos(x) and sin(x)", fontsize=14, fontweight="bold", y=0.97)


plt.tight_layout(rect = [0,0,1,0.95])
plt.show()
