"""
File: mapeo_logistico.py
Project: Tareas
File Created: Wednesday, 9th August 2023 5:21:44 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Thursday, 10th August 2023 6:31:03 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
"""


# SECTION - LIBRARIES
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import seaborn as sns

# !SECTION

# SECTION - CONFIG
# Use LaTeX throughout the figure for consistency
# rc("font", **{"family": "serif", "serif": ["Computer Modern"], "size": 16})
# rc("text", usetex=True)

# !SECTION


# SECTION - FUNCTIONS
# Logistic mapping equation
def logistic_mapping(r: float, x_current: float) -> float:
    """Logistic mapping function that describes population growth.

    Args:
        r (float): growth factor.
        x_current (float): current population size.

    Returns:
        x_next (float): next population size.
    """
    x_next = r * x_current * (1 - x_current)
    return x_next


# !SECTION


# SECTION - MAIN
if __name__ == "__main__":
    # Initial constants
    r_list = np.linspace(start=0, stop=5, num=5)  # Growth rate
    x_current_list = np.linspace(
        start=0, stop=1, num=100
    )  # Current population init values in percentage

    # Function vectorization with numpy
    vlogistic_mapping = np.vectorize(logistic_mapping)

    # Logistic mapping function plot for different growth rates
    plt.figure(figsize=(10, 10), layout="tight")

    for idx, r in enumerate(r_list):
        x_next_list = vlogistic_mapping(
            r=r, x_current=x_current_list
        )  # Next population value in percentage
        sns.lineplot(x=x_current_list, y=x_next_list, label=f"{r=}")

    plt.title("Logistic map function: $x_{n+1} = r x_n (1 - x_n)$", size=15)
    plt.xlabel("$x_n \in [0, 1]$", size=15)
    plt.ylabel("$x_{n+1}$", size=15)
    plt.savefig("logistic_map_function_plot.png", dpi=300)
