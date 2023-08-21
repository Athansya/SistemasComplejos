"""
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
"""

# ---------------------------------------------------------------------------- #
#                                   LIBRARIES                                  #
# ---------------------------------------------------------------------------- #

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
INITIAL_VALUE = 0 + 0j  # z_0
REAL_RANGE = 1000
IMAG_RANGE = 1000
REAL = np.linspace(-2, 0.48, REAL_RANGE)
IMAG = np.linspace(-1.12, 1.12, IMAG_RANGE)
MAX_ITERATIONS = 30
TOWARDS_INF = 4


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #
def quadratic_map_equation(current_value: complex, c: complex) -> complex:
    """Computes de quadratic map equation given a current value (z_n) and
    a complex constant (c).

    z_{n + 1} = z_n^2 + c

    E.g.
    If z_0 = 0

    z_1 = 0^2 + c; c = a + bi
    z_2 = c^2 + c
    z_2 = (a + bi)^2 + c
    z_2 = (a^2 + b^2) + 2abi + c

    Args:
        current_value (complex): current value z_n.
        c (complex): constant complex value c.

    Returns:
        next_value complex:
    """
    # Squaring a complex causes an error, but we can avoid it by simplifying the
    # operation -> complex^2 = (a^2 - b^2) + (2 * a * b)i
    next_a = current_value.real**2 - current_value.imag**2  # Real part
    next_b = 2 * current_value.real * current_value.imag  # Imaginary part

    next_value = complex(next_a, next_b) + c  # Computes z_{n+1}
    return next_value


def obtain_mandelbrot_set(
    real_values: np.ndarray = REAL,
    imag_values: np.ndarray = IMAG,
    max_iterations: int = MAX_ITERATIONS,
) -> np.ndarray:
    """Obtains the Mandelbrot set for a given set of 'c' values.

    Args:
        real_values (np.ndarray): real component of c.
        imag_values (np.ndarray): imaginary component of c.

    Returns:
        complex_plane (np.ndarray): Mandelbrot set complex plane matrix
        color coded by the number of iterations.
    """
    # Generates complex plane array
    complex_plane = (
        np.zeros(shape=(len(imag_values), len(real_values))) + max_iterations
    )  # The sum initiates coloring
    # Iterates 'c' values in the plane
    for id_i, imag in enumerate(imag_values):
        for id_r, real in enumerate(real_values):
            c = complex(real, imag)
            current_value = INITIAL_VALUE  # z_0
            # Computes the quadric map
            for iteration in range(max_iterations):
                # z_{n + 1} = z_n^2 + c
                current_value = quadratic_map_equation(current_value=current_value, c=c)
                # Checks if orbit exploded or not to draw
                if (current_value.real**2 + current_value.imag**2) >= TOWARDS_INF:
                    # Assigns color based on iteration
                    complex_plane[id_i][id_r] = iteration
                    break

    return complex_plane


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    mandelbrot_complex_plane = obtain_mandelbrot_set()
    plt.imshow(mandelbrot_complex_plane, cmap="viridis")
    plt.title("Mandelbrot Set")
    plt.xlabel("$\\Re$")
    plt.ylabel("$C$")
    plt.savefig("mandelbrot_set_plot.png")
