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
import matplotlib.pyplot as plt

# SECTION - CONSTANTS
r = 2.6  # Growth rate

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



#
x = [i for i in range(10)]
y = [np.random.randint(low=0, high=10) for i in x]

plt.figure(figsize=(10, 10), layout="tight")
plt.scatter(x, y)
plt.show()
plt.savefig("example.png", dpi=300)


# SECTION - MAIN
if __name__ == "__main__":

    