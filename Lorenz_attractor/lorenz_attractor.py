'''
File: lorenz_attractor.py
Project: Lorenz_attractor
File Created: Tuesday, 22nd August 2023 7:35:43 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Tuesday, 22nd August 2023 7:35:53 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
'''

# ---------------------------------------------------------------------------- #
#                                   LIBRARIES                                  #
# ---------------------------------------------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
#                                   CONSTANTS                                  #
# ---------------------------------------------------------------------------- #
MAX_ITERATIONS = 10000

SIGMA = 10  # a
RHO = 28  # b
BETA = 8/3  # c

x = 0.01
y = 0.0
z = 0.0

X = []
Y = []
Z = []
# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    for _ in range(MAX_ITERATIONS):
        dt = 0.01  # Time steps

        # Equations
        dx = (SIGMA * (y - x)) * dt
        dy = (x * (RHO - z) - y) * dt
        dz = (x * y - BETA * z) * dt

        x = x + dx
        y = y + dy
        z = z + dz

        X.append(x)
        Y.append(y)
        Z.append(z)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ax.plot(X, Y, Z, linewidth=0.5)
    plt.savefig("example_lorenz_attractor.png")