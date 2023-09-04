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
#TODO Refactor code to make Cell class immutable
"""
from copy import deepcopy
from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import numpy as np


@dataclass(slots=True)
class Cell:
    """Class for storing the state of a cell
    Args:
        state (int): state of the cell. Default 0.
    """

    state: int = 0

    def __repr__(self) -> str:
        return str(self.state)


@dataclass(slots=True)
class CA:
    """Class for creating a cellular automata
    Args:
        world_dim (tuple[int, int]): Dimensions MxN of the world grid.
        states (dict[str, int]): Valid states for the cell
    """

    world_dim: tuple[int, int]
    states: dict[str, int] = field(default_factory=lambda: {"0": 0, "1": 1})
    gen: int = field(init=False, default=0)
    world: list[list[Cell]] = field(init=False)
    new_world: list[list[Cell]] = field(init=False)

    def __post_init__(self) -> None:
        self.world = [
            [Cell() for _ in range(self.world_dim[1] + 1)]
            for _ in range(self.world_dim[0] + 1)
        ]
        self.new_world = deepcopy(self.world)

    def set_cell_value(self, row_index: int, col_index: int, value: int) -> None:
        """Sets the state of a cell.

        Args:
            row_index (int): row position of cell in world grid.
            col_index (int): column position of cell in world grid.
            value (int): new state value.
        """
        self.world[row_index][col_index].state = value

    def show_world(self) -> None:
        """Prints the world grid"""
        for row in self.world:
            print(*row)

    def show_world_pretty(self) -> None:
        """Pretty print of world grid"""
        state_to_char = " #"

        for row in self.world:
            print(*[state_to_char[cell.state] for cell in row])

    def apply_rules(self, row_index: int, col_index: int) -> int:
        """Applies solidification rules for a 2D cellular automata.

        Args:
            row_index (int): row position in world grid.
            col_index (int): col position in world grid.

        Returns:
            int: new cell's state.
        """
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

    def game_of_life_rules(self, row_index: int, col_index: int) -> int:
        """Applies Conway's game of life rules for 2D cellular automata.

        Args:
            row_index (int): _description_
            col_index (int): _description_

        Returns:
            int: _description_
        """
        # Conway's rules
        # 1 with 2 or 3 -> 1 else -> 0
        # 0 with 3 -> 1 else 0

        neighborhood_sum = 0 - self.world[row_index][col_index].state
        # Live cell
        if self.world[row_index][col_index].state == self.states["1"]:
            for row in self.world[row_index - 1 : row_index + 2]:
                neighborhood_sum += sum(
                    cell.state for cell in row[col_index - 1 : col_index + 2]
                )
            if neighborhood_sum == 2 or neighborhood_sum == 3:
                # Keeps living
                return self.states["1"]
            else:
                # Dies
                return self.states["0"]
        else:  # Dead cell
            for row in self.world[row_index - 1 : row_index + 2]:
                neighborhood_sum += sum(
                    cell.state for cell in row[col_index - 1 : col_index + 2]
                )
            if neighborhood_sum == 3:
                # Revives
                return self.states["1"]
            else:
                # Still dead
                return self.states["0"]

    def update_world(self, generations: int = 10) -> None:
        """Updates world grid using a set of rules

        Args:
            generations (int, optional): Number of generations. Defaults to 10.
        """
        for _ in range(1, generations + 1):
            for row_index in range(1, self.world_dim[0]):
                for col_index in range(1, self.world_dim[1]):
                    # Solidification rules
                    self.new_world[row_index][col_index].state = self.apply_rules(
                        row_index, col_index
                    )
                    # Game of life rules
                    # self.new_world[row_index][col_index].state = self.game_of_life_rules(
                    # row_index, col_index
                    # )
            # Update worlds!
            self.world = deepcopy(self.new_world)
            self.gen += 1  # Update gen counter

    def world_to_numpy(self) -> np.ndarray:
        """Converts world grid to numpy array.

        Returns:
            np.ndarray: converted world grid.
        """
        return np.array([[cell.state for cell in row] for row in self.world])

    def save_world_to_image(
        self,
        title: str | None = None,
        filename: str | None = None
    ) -> None:
        """Saves the world state as 'png' image.

        Args:
            title (str, optional): Image title. Defaults to None.
            filename (str, optional): file name. Defaults to None.
        """
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


def main():
    # CA init
    ROWS, COLS = 501, 501
    ca = CA(world_dim=(ROWS, COLS))
    ca.set_cell_value(ROWS // 2, COLS // 2, 1)
    # Updates CA and saves images
    for _ in range(10):
        ca.update_world()
        ca.save_world_to_image(filename=f"ca_solification_rules_gen_{ca.gen}.png")


if __name__ == "__main__":
    main()
