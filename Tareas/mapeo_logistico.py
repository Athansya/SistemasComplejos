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
from matplotlib import rc  # Enable Latex Figures
import matplotlib.pyplot as plt
import seaborn as sns

# !SECTION

# SECTION - MATPLOTLIB LATEX CONFIG
rc("font", **{"family": "serif", "serif": ["Computer Modern"], "size": 16})
rc("text", usetex=True)

# !SECTION


# SECTION - FUNCTIONS
# Logistic mapping equation
def logistic_map_eq(r: float, x_current: float) -> float:
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
    # SECTION - DEFINITIONS
    # Initial values
    r_list = np.linspace(start=0, stop=4, num=5)  # Growth rate
    x_current_list = np.linspace(
        start=0, stop=1, num=100
    )  # Current population init values in percentage

    # Function vectorization with numpy
    vlogistic_map_eq = np.vectorize(logistic_map_eq)

    # !SECTION

    # SECTION - 2D & 3D PLOT
    # Logistic mapping function plot for different growth rates
    fig = plt.figure(figsize=(20, 10), layout="tight")
    fig.suptitle("Logistic map function: $x_{n+1} = r x_n (1 - x_n)$", size=15)
    ax_0 = fig.add_subplot(1, 2, 1)
    ax_1 = fig.add_subplot(1, 2, 2, projection="3d")

    for idx, r in enumerate(r_list):
        x_next_list = vlogistic_map_eq(
            r=r, x_current=x_current_list
        )  # Next population value in percentage x_{n+1}
        x_next_2_list = vlogistic_map_eq(r=r, x_current=x_next_list)  # x_{n+2}
        # 2D Plot
        sns.lineplot(ax=ax_0, x=x_current_list, y=x_next_list, label=f"{r=}")
        # 3D Plot
        ax_1.plot(x_next_list, x_current_list, x_next_2_list, label=f"{r=}")

    ax_0.set_title("2D")
    ax_0.set_xlabel("$x_n$", size=15)
    ax_0.set_ylabel("$x_{n+1}$", size=15)
    ax_1.legend()
    ax_1.invert_xaxis()
    ax_1.set_title("3D")
    ax_1.set_ylabel("$x_n$", size=15)
    ax_1.set_xlabel("$x_{n+1}$", size=15)
    ax_1.set_zlabel("$x_{n+2}$", size=15)
    # plt.savefig("logistic_map_function_plot.png", dpi=300)  # Uncomment to save figure

    # !SECTION

    # SECTION - FIXED POINTS
    # Fixed points are points where f(x) = x. For example, in the previous plot, 0 is a fixed point.
    # Let's see how does the function looks like after iterating n times.
    x_current = 0.5
    r = 0.1
    n_iterations = 10
    x_n_list = [x_current]

    for n in range(n_iterations):
        x_next = logistic_map_eq(r=r, x_current=x_current)
        x_n_list.append(x_next)
        x_current = x_next

    plt.figure(figsize=(10, 10))
    sns.lineplot(
        x=[i for i in range(len(x_n_list))],
        y=x_n_list,
        marker=".",
        markersize=15,
        mfc="r",
    )
    plt.title(f"Fixed point(s) for r = {r}")
    # plt.savefig(f"fixed_point_for_r_{r}.png", dpi=300)  # Uncomment to save figure
    # It approaches 0!

    # What about multiple values for r?
    r_list = np.sort(np.random.uniform(low=0, high=4.001, size=10))
    # print(f"r = {r}")

    fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(20, 10), layout="tight")
    for id_row, ax_row in enumerate(axs):  # Figure rows
        # print(f"{id_row=}")
        for id_col, _ in enumerate(ax_row):  # Figure cols
            # print(f"{id_col=}")
            x_current = 0.5
            x_n_list = [x_current]
            r = r_list[id_row * axs.shape[1] + id_col]  # Obtains growth rate

            for n in range(n_iterations):  # Logistic map eq
                x_next = logistic_map_eq(r=r, x_current=x_current)
                x_n_list.append(x_next)
                x_current = x_next

            sns.lineplot(
                ax=axs[id_row][id_col],
                x=[i for i in range(len(x_n_list))],
                y=x_n_list,
                marker=".",
                markersize=15,
                mfc="r",
            )

            axs[id_row][id_col].set_title(f"$r$ = {r}")
            axs[id_row][id_col].set_xlabel(f"$n$")
            axs[id_row][id_col].set_ylabel(f"$x_n$")

            del x_n_list

    plt.suptitle("Fixed points for different values of $r$")
    # plt.savefig("multiple_r_values.png", dpi=300)  # Uncomment to save figure
    # There are different and sometimes multiple fixed points for a given value of r

    # !SECTION

    # SECTION - BIFURCTATION PLOT
    # Another way to analyze how the fixed points change is using a bifurcation plot:
    # !TODO Add parallel method to plot multiple points
    r_list = np.linspace(start=0, stop=4, num=100)
    n_iterations = 100

    fig = plt.figure(figsize=(10,10))

    for r in r_list:
        x_current = 0.5
        for n in range(n_iterations):
            x_next = logistic_map_eq(r=r, x_current=x_current)
            x_current = x_next
        for n in range(n_iterations):
            x_next = logistic_map_eq(r=r, x_current=x_current)
            x_current = x_next
            plt.scatter(r, x_next, c="black", s=5)

    plt.title("Bifurcation plot")
    plt.xlabel("$r$")
    plt.ylabel("$x$")
    plt.savefig("bifurcation_plot.png", dpi=300)