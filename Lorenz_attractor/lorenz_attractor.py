'''
File: lorenz_solver.py
Project: lorenz_solver
File Created: Tuesday, 22nd August 2023 7:35:43 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Tuesday, 22nd August 2023 7:35:53 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
#TODO - OBTAIN BIFURCACTION DIAGRAM
'''

# ---------------------------------------------------------------------------- #
#                                   LIBRARIES                                  #
# ---------------------------------------------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------- #
#                                   CONSTANTS                                  #
# ---------------------------------------------------------------------------- #
NUM_STEPS = 10000

SIGMA = 10  # a
RHO = 28  # b
BETA = 8/3  # c
TIME_STEP = 0.01

# ---------------------------------------------------------------------------- #
#                            MATPLOTLIB LATEX CONFIG                           #
# ---------------------------------------------------------------------------- #
rc("font", **{"family": "serif", "serif": ["Computer Modern"], "size": 16})
rc("text", usetex=True)


def lorenz_system(
        t: float,
        state: tuple[float, float, float],
        sigma: float = SIGMA,
        rho: float = RHO,
        beta: float = BETA,
    ) -> np.ndarray:
    """Solves the lorenz equations
    
    The Lorenz equations are a system of ordinary differential equations that
    describe a chaotic dynamical system. They have applications in fluid dynamics,
    weather prediction, and chaos theory.
    
    Args:
        x (float, optional): Initial value for the x-coordinate. Defaults to 0.01.
        y (float, optional): Initial value for the y-coordinate. Defaults to 0.0.
        z (float, optional): Initial value for the z-coordinate. Defaults to 0.0.
        sigma (float, optional): Sigma parameter. Defaults to SIGMA.
        rho (float, optional): Rho parameter. Defaults to RHO.
        beta (float, optional): Beta parameter. Defaults to BETA.

    Returns:
        np.ndarray: An array containing the time derivatives of the input coordinates
            (dx, dy, dz) computed using the Lorenz equations at the given (x, y, z)
            coordinates.
    """
    # Equations
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = (x * (rho - z) - y)
    dz_dt = (x * y - beta * z)

    return [dx_dt, dy_dt, dz_dt]


def lorenz_solver(initial_state, sigma=SIGMA, rho=RHO, beta=BETA, dt=TIME_STEP, num_steps=NUM_STEPS):
    # Create solver object
    solver = solve_ivp(lorenz_system, (0, num_steps), initial_state, args=(sigma, rho, beta), dense_output=True)
    # Define time steps array
    t = np.arange(0, num_steps * dt, dt)
    # Integrate the Lorenz system
    trajectory = solver.sol(t)

    return trajectory



def main():
    # Initial state for x, y, z
    initial_state = (0.01, 0.0, 0.0)

    # Get Lorenz Attractor
    trajectory = lorenz_solver(initial_state=initial_state)
   
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    # The plot coloring idea is taken from:
    # https://scipython.com/blog/the-lorenz-attractor/
    s = 10
    cmap = plt.cm.plasma
    for i in range(0, NUM_STEPS-s, s):

        ax.plot(
            trajectory[0,i:i+s+1],
            trajectory[1,i:i+s+1],
            trajectory[2,i:i+s+1],
            color=cmap(i/NUM_STEPS),
            alpha=0.4
        )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.title("Lorenz Attractor")
    plt.savefig("example_lorenz_solver.png")


    # Bifurcation map
    num_rho_values = 500
    rho_values = np.linspace(start=0, stop=250, num=num_rho_values)
    num_steps = 200

    plt.figure(figsize=(10, 10))
    for rho in rho_values:
        # Initial state for x, y, z
        initial_state = (0.01, 0.0, 0.0)

        trajectory = lorenz_solver(initial_state=initial_state, rho=rho, num_steps=num_steps)  # Saves the last coor
        
        plt.scatter([rho for _ in range(len(trajectory[2,-100:]))], trajectory[2,-100:], c="black", marker='.', s=1, linewidths=0)

    plt.title("Lorenz bifurcation plot")
    plt.xlabel("$r$")
    plt.ylabel("$z$")
    plt.savefig("lorenz_bifurcation_plot_z.png")
# 

# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    main()