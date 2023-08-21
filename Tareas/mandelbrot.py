'''
File: mandelbrot.py
Project: Tareas
File Created: Friday, 18th August 2023 6:43:05 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Friday, 18th August 2023 6:43:14 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Mandelbrot set plot
'''

# ---------------------------------------------------------------------------- #
#                                   LIBRARIES                                  #
# ---------------------------------------------------------------------------- #

from cmath import isclose  # Complex comparison
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
#                                    CONFIG                                    #
# ---------------------------------------------------------------------------- #
rc("font", **{"family": "serif", "serif": ["Computer Modern"], "size": 16})
rc("text", usetex=True)

# ---------------------------------------------------------------------------- #
#                                   CONSTANTS                                  #
# ---------------------------------------------------------------------------- #
INITIAL_VALUE = 0 + 0j
RESOLUTION = 100
# COMPLEX_MESH = np.ogrid[-2: 2: RESOLUTION * 1j, -2: 2: RESOLUTION * 1j]
REAL = np.linspace(-2, 0.48, RESOLUTION)
IMAG = np.linspace(-1.12, 1.12, RESOLUTION)
# COMPLEX_MESH = np.meshgrid(X, Y)
# COMPLEX_MESH = np.ogrid[-2: 2: RESOLUTION * 1j, -2: 2: RESOLUTION * 1j]
ITERATIONS = 30 
EPSILON = 0.1
TOWARDS_INF = 4
# ---------------------------------------------------------------------------- #
#                             z_{n + 1} = z_n^2 + c                            #

#                                  If z_0 = 0                                  #

#                           z_1 = 0^2 + c; c = a + bi                          #
#                                 z_2 = c^2 + c                                #
#                             z_2 = (a + bi)^2 + c                             #
#                         z_2 = (a^2 + b^2) + 2abi + c                         #
# ---------------------------------------------------------------------------- #
def mandelbrot_set_equation(current_value: complex, c: complex) -> complex:
    a = current_value.real
    b = current_value.imag
    ac = c.real
    ab = c.imag

    next_a = a**2 - b**2
    next_b = 2*a*b

    next_value = complex(next_a + ac, next_b + ab)
    # next_value = complex(a**2 - b**2, 2*a*b) + c
    return next_value

def show_mandelbrot_set(real_range: np.ndarray, imag_range: np.ndarray):
    #TODO - FIX THIS FUNCTION. OVERFLOWS FOR SOME REASON
    # Iterating the mesh
    plt.figure(figsize=(15,10))
    for real in real_range:
        for imag in imag_range:
            # Complex variable
            c = complex(real, imag)
            count = 0  # Counter
            current_value = mandelbrot_set_equation(INITIAL_VALUE, c=c)
            while(count < ITERATIONS and abs(current_value.real + current_value.imag) < TOWARDS_INF):
                next_value = mandelbrot_set_equation(current_value=current_value, c=c)
                current_value = next_value
                count += 1
            if count == ITERATIONS:
                plt.scatter(real, imag, marker='x', color='black', s=0.5)
            else:
                plt.scatter(real, imag, marker='.', color='blue', s=0.5, alpha=0.3)

    plt.savefig("mandelbrot_test_me.png")



def run():
    pass


if __name__ == "__main__":
    # y, x = np.ogrid[-1.4: 1.4: RESOLUTION*1j, -1.8: 1: RESOLUTION*1j]
    # a_array = x + y*1j
    # z_array = np.zeros(a_array.shape)
    # iterations_till_divergence = ITERATIONS + np.zeros(a_array.shape)
    # print(f"{iterations_till_divergence=}")
    # for h in range(RESOLUTION):
        # for w in range(RESOLUTION):
            # z = z_array[h][w]
            # a = a_array[h][w]
            # for i in range(ITERATIONS):
                # z = z**2 + a
                # if z * np.conj(z) > 4:  # DE DONDE SALE ESE 4!!!!????
                    # iterations_till_divergence[h][w] = i
                    # break
# 
    # plt.imshow(iterations_till_divergence, cmap="viridis")
    # plt.savefig("mandelbrot_example.png")

    show_mandelbrot_set(REAL, IMAG)
    # run()
    # for i in COMPLEX_MESH[0]:
        # print(i)