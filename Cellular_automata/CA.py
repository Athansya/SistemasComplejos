"""
File: CA.py
Project: Cellular_automata
File Created: Wednesday, 30th August 2023 10:20:17 am
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Wednesday, 30th August 2023 10:40:38 am
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Simple cellular automata class.
"""
from copy import deepcopy
from dataclasses import dataclass, field
import matplotlib.pyplot as plt
from numpy import array, ndarray


@dataclass()
class Cell:
    """Class for storing the state of a cell"""

    state: int = 0
    # _state: int = 0

    # @property
    # def state(self) -> int:
    # return self._state
    #
    # @state.setter
    # def state(self, value: int) -> None:
    # self._state = value

    def __add__(self, other) -> int:
        return self.state + other.state

    def __repr__(self) -> str:
        return str(self.state)


@dataclass
class CA:
    world_dim: tuple[int, int]
    states: dict[str, int] = field(default_factory=lambda: {"0": 0, "1": 1})
    gen: int = field(init=False, default=0)

    def __post_init__(self):
        self.world = [
            [Cell() for _ in range(self.world_dim[1])] for _ in range(self.world_dim[0])
        ]
        self.new_world = deepcopy(self.world)

    def set_cell_value(self, row_index: int, col_index: int, value: int):
        self.world[row_index][col_index].state = value

    def show_world(self):
        for row in self.world:
            print(*row)

    def apply_rules(self, row_index, col_index) -> int:
        # Solidification rules
        # Case 1. State == 1 -> 1
        if self.world[row_index][col_index].state == self.states["1"]:
            return 1
        # Case 2. State == 0 and && neighorhood sum == 1 or 2 -> 1
        # Init sum without taking central into account
        neighborhood_sum = 0 - self.world[row_index][col_index].state
        # Walk through Van Moore Neighborhood
        for row in self.world[row_index - 1 : row_index + 2]:
            neighborhood_sum += sum(
                cell.state for cell in row[col_index - 1 : col_index + 2]
            )
        if neighborhood_sum == 1 or neighborhood_sum == 2:
            return self.states["1"]
        else:
            return self.states["0"]

    def update_world(self, generations: int = 10):
        for _ in range(1, generations + 1):
            for row_index in range(1, self.world_dim[0]):
                for col_index in range(1, self.world_dim[1]):
                    self.new_world[row_index][col_index].state = self.apply_rules(
                        row_index, col_index
                    )
            # Update worlds!
            self.world = deepcopy(self.new_world)
            self.gen += 1  # Update gen counter

    def world_to_numpy(self) -> ndarray:
        return array([[cell.state for cell in row] for row in self.world])

    def save_world_to_image(self, title: str = None, filename: str = None):
        img = self.world_to_numpy()
        plt.imshow(img, cmap="binary")
        plt.axis("off")
        if title is not None:
            plt.title(f"{title}")
        else:
            plt.title(f"Cellular Automata - Gen {self.gen}")
        if filename is not None:
            plt.savefig(f"{filename}.png")
        else:
            plt.savefig(f"ca_{self.gen}.png")
        



if __name__ == "__main__":
    # CA init
    ROWS, COLS = 101, 101
    ca = CA(world_dim=(ROWS, COLS))
    ca.set_cell_value(ROWS//2, COLS//2, 1)
    # Updates CA and saves images
    for _ in range(8):
        ca.update_world()
        ca.save_world_to_image(
            filename=f"ca_solification_rules_gen_{ca.gen}.png"
        )