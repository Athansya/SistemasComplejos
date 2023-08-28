'''
File: cellular_automata_1d.py
Project: SistemasComplejos
File Created: Sunday, 27th August 2023 1:27:16 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Sunday, 27th August 2023 1:27:21 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 1-Dimensional Cellular Automata Generator. Uses Wolfram's
original rules [0-255] to update the state of each cells. Saves a 'png'
file with the result.
'''

import matplotlib.pyplot as plt
import numpy as np
import argparse


def parse_arguments():
    # Parsing command line options
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    # Description
    # Optional
    parser.add_argument(
        "number_of_cells",
        type=int,
        help="Number of cells in the 1D World. Default is 100.",
        default=100
        )
    parser.add_argument(
        "generations",
        type=int,
        help="Number of generations to produce. Default is 100",
        default=100
    )
    parser.add_argument(
        "rule",
        type=int,
        choices=range(1,256),
        metavar="rule [1-255]",
        help="Set of rules for updating the cells. Default is 90.",
        default=90
    )

    args = parser.parse_args()
    
    # Assign variables
    num_cells = args.number_of_cells
    generations = args.generations
    rule = args.rule

    # Converts integer to binary str representation of len 8
    rule = format(rule, '08b')

    print(f"Number of cells: {num_cells}")
    print(f"Generations: {generations}")
    print(f"Rule: {rule}")

    return num_cells, generations, rule


def apply_rule(rule, left_neighbor, cell, right_neighbor):
    if cell:
        if left_neighbor:
            if right_neighbor:  # 111
                return int(rule[0])
            return int(rule[1])  # 110
        elif right_neighbor:
            return int(rule[4])  # 011
        else:
            return int(rule[5])  # 010
    else:
        if left_neighbor:
            if right_neighbor:
                return int(rule[2])  # 101
            return int(rule[3])  # 100
        elif right_neighbor:
            return int(rule[6])  # 001
        else:
            return int(rule[7])  # 000



if __name__ == "__main__":
    # Read command line arguments
    NUM_CELLS, GENERATIONS, RULE = parse_arguments()

    # Create world and initialize
    WORLD = np.zeros(shape=(NUM_CELLS + 1 if NUM_CELLS % 2 == 0 else NUM_CELLS))
    WORLD[len(WORLD) // 2] = 1
    OLD_WORLD = WORLD.copy()
    # print("OLD_WORLD:")
    # print(OLD_WORLD)

    # Generations
    for gen in range(GENERATIONS):
        NEW_WORLD = np.zeros_like(OLD_WORLD)
        for i in range(1, len(OLD_WORLD) - 1):
            NEW_WORLD[i] = apply_rule(RULE, OLD_WORLD[i-1], OLD_WORLD[i], OLD_WORLD[i+1])
        WORLD = np.vstack([WORLD, NEW_WORLD])  # ADD GEN TO WORLD
        OLD_WORLD = np.copy(NEW_WORLD)
        # print(f"NEW WORLD GEN {gen}:")
        # print(NEW_WORLD)

    plt.imshow(WORLD, cmap='binary')
    # plt.axes('off')
    plt.title(f"Rule {int(RULE, 2)}")
    plt.axis('off')
    plt.savefig(f"1D_automata_rule_{int(RULE, 2)}.png")