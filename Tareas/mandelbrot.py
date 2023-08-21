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
RESOLUTION = 1000
COMPLEX_MESH = np.ogrid[-2: 2: RESOLUTION * 1j, -2: 2: RESOLUTION * 1j]
ITERATIONS = 30 
EPSILON = 0.1
# ---------------------------------------------------------------------------- #
#                             z_{n + 1} = z_n^2 + c                            #
# ---------------------------------------------------------------------------- #
def mandelbrot_set_equation(current_value: complex, c: complex) -> complex:
    next_value = current_value**2 + c
    return next_value

def show_mandelbrot_set(mesh: list):
    # Iterating the mesh
    plt.figure(figsize=(15,10))
    for row in mesh[0]:
        for col in mesh[1]:
            for real in row:
                # print(f"{real=}")
                for imaginary in col:
                    # Complex variable
                    c = complex(real, imaginary)
                    print(f"{c=}")
                    count = 0  # Counter
                    current_value = mandelbrot_set_equation(INITIAL_VALUE, c=c)
                    next_value = mandelbrot_set_equation(current_value=current_value, c=c)
                    while(count < ITERATIONS and not isclose(next_value, current_value, rel_tol=EPSILON)):
                        current_value = next_value
                        next_value = mandelbrot_set_equation(current_value=current_value, c=c)
                        count += 1
                    if count == ITERATIONS:
                        plt.scatter(real, imaginary, marker='x', color='black', s=0.5)
                    else:
                        plt.scatter(real, imaginary, marker='.', color='blue', s=0.5, alpha=0.3)


    plt.savefig("mandelbrot_test.png")



def run():
    pass

def show_mesh(mesh: np.ndarray):
    plt.figure(figsize=(15,10))
    plt.scatter(COMPLEX_MESH[0], COMPLEX_MESH[1], c='blue', s=0.5)
    plt.savefig("mesh_example.png")
    

if __name__ == "__main__":
    y, x = np.ogrid[-1.4: 1.4: RESOLUTION*1j, -1.8: 1: RESOLUTION*1j]
    a_array = x + y*1j
    z_array = np.zeros(a_array.shape)
    iterations_till_divergence = ITERATIONS + np.zeros(a_array.shape)
    print(f"{iterations_till_divergence=}")
    for h in range(RESOLUTION):
        for w in range(RESOLUTION):
            z = z_array[h][w]
            a = a_array[h][w]
            for i in range(ITERATIONS):
                z = z**2 + a
                if z * np.conj(z) > 4:  # DE DONDE SALE ESE 4!!!!????
                    iterations_till_divergence[h][w] = i
                    break

    plt.imshow(iterations_till_divergence, cmap="viridis")
    plt.savefig("mandelbrot_example.png")

    # print(f"{a_array.shape=}")
    # print(f"{y=}")
    # print(f"{x=}")
    # show_mesh(COMPLEX_MESH)
    # show_mandelbrot_set(mesh=COMPLEX_MESH)
    # run()
    # for i in COMPLEX_MESH[0]:
        # print(i)