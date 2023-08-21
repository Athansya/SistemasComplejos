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
REAL_RESOLUTION = 1000
IMAG_RESOLUTION = 1000
# COMPLEX_MESH = np.ogrid[-2: 2: RESOLUTION * 1j, -2: 2: RESOLUTION * 1j]
REAL = np.linspace(-2, 0.48, REAL_RESOLUTION)
IMAG = np.linspace(-1.12, 1.12, IMAG_RESOLUTION)
# COMPLEX_MESH = np.meshgrid(X, Y)
# COMPLEX_MESH = np.ogrid[-2: 2: RESOLUTION * 1j, -2: 2: RESOLUTION * 1j]
MAX_ITERATIONS = 30 
TOWARDS_INF = 4
COMPLEX_MESH = np.zeros(shape=(len(IMAG), len(REAL))) + MAX_ITERATIONS
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
    plt.figure(figsize=(15,10))
    for id_i, imag in enumerate(imag_range):
        for id_r, real in enumerate(real_range):
            # Complex variable
            c = complex(real, imag)
            current_value = INITIAL_VALUE
            for iteration in range(MAX_ITERATIONS):
                current_value = mandelbrot_set_equation(current_value=current_value, c=c)
                if (current_value.real**2 + current_value.imag**2) >= TOWARDS_INF:
                    COMPLEX_MESH[id_i][id_r] = iteration
                    break
            # else:
                # plt.scatter(real, imag, marker='.', color='blue', s=0.5, alpha=0.3)

    plt.imshow(COMPLEX_MESH, cmap='viridis')
    plt.savefig("mandelbrot_test_me_2.png")


def run():
    pass


if __name__ == "__main__":
    # y, x = np.ogrid[-1.4: 1.4: REAL_RESOLUTION*1j, -1.8: 1: REAL_RESOLUTION*1j]
    # print(f"{y.shape}")
    # a_array = x + y*1j
    # z_array = np.zeros(a_array.shape)
    # iterations_till_divergence = MAX_ITERATIONS + np.zeros(a_array.shape)
    # print(f"{iterations_till_divergence=}")
    # for h in range(RESOLUTION):
        # for w in range(RESOLUTION):
            # z = z_array[h][w]
            # a = a_array[h][w]
            # for i in range(MAX_ITERATIONS):
                # z = z**2 + a
                # if z * np.conj(z) > 4:  # DE DONDE SALE ESE 4!!!!????
                    # iterations_till_divergence[h][w] = i
                    # break
# 
    # plt.imshow(iterations_till_divergence, cmap="viridis")
    # plt.savefig("mandelbrot_example.png")

    print(f"{COMPLEX_MESH.shape}")
    show_mandelbrot_set(REAL, IMAG)
    # run()
    # for i in COMPLEX_MESH[0]:
        # print(i)