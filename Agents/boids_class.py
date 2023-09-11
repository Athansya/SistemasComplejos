"""
File: voids_class.py
Project: Agents
File Created: Sunday, 10th September 2023 3:30:43 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Sunday, 10th September 2023 3:30:56 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
"""
from dataclasses import dataclass, field
import numpy as np
from os import system
from time import sleep


@dataclass
class Boid:
    """
    Class representing boids.

    Attributes:
        position (np.ndarray): Array representing the positions of the boids in the x, y coordinates.
        velocity (np.ndarray): Array representing the velocities of the boids in the x', y' coordinates.
    """

    # x, y
    position: np.ndarray
    # x', y'
    velocity: np.ndarray
    # Visual range
    radius: int = 3


@dataclass
class Playground:
    shape: tuple[int, int]
    world: np.ndarray = field(init=False)
    n_agents: int = 10
    agents: list[Boid] = field(init=False, default_factory=lambda: [])
    num_neighbors: int = 5
    separation_factor: int = 5
    coherence_factor: int = 5

    def __post_init__(self):
        self.__init_agents()
        self.world = np.zeros(shape=self.shape, dtype=np.uint8)

    def __init_agents(self):
        for _ in range(self.n_agents):
            # Random positions and velocity
            x = np.random.randint(0, self.shape[0])
            y = np.random.randint(0, self.shape[1])
            # TODO Make the movement smoother
            dx = np.random.randint(-1, 1)
            dy = np.random.randint(-1, 1)

            self.agents.append(
                Boid(position=np.array([x, y]), velocity=np.array([dx, dy]))
            )

    def __clear_world(self):
        # Clears world
        self.world = np.zeros(shape=self.shape, dtype=np.uint8)
        # Fills world with boids

    def __update_world(self, boid: Boid):
        self.world[boid.position[0], boid.position[1]] = 1

    def __handle_borders(self, boid: Boid):
        # Out of x bounds
        if boid.position[0] < 1:
            boid.position[0] = self.shape[0] - 1
        elif boid.position[0] > self.shape[0] - 2:
            boid.position[0] = 0
        # Out of y bounds
        if boid.position[1] < 1:
            boid.position[1] = self.shape[1] - 1
        elif boid.position[1] > self.shape[1] - 2:
            boid.position[1] = 0


    def __cohesion_rule(self, myself: Boid, neighbors: list[Boid]):
        new_position = np.array([0, 0])
        for neighbor in neighbors[:self.num_neighbors]:
            new_position += neighbor.position

        new_velocity = (new_position - myself.position) // self.coherence_factor + 1
        myself.position += new_velocity
        myself.velocity += new_position


    def __align_rule(self, myself: Boid, neighbors: list[Boid]):    
        new_position = np.array([0, 0])
        for neighbor in neighbors[:self.num_neighbors]:
                new_position += neighbor.velocity

        new_velocity = new_position // self.num_neighbors + 1
        myself.velocity = new_velocity
        myself.position += new_velocity


    def __separation_rule(self, myself: Boid, neighbors: list[Boid]):
        new_position = np.array([0, 0])
        for neighbor in neighbors[:self.num_neighbors]:
            if self.__distance_to_neighbor(myself, neighbor) < self.separation_factor:
                new_position += (myself.position - neighbor.position) + 1

        myself.velocity = new_position
        myself.position += new_position 

    
    def __distance_to_neighbor(self, myself: Boid, neighbor: Boid):
        return np.linalg.norm(myself.position - neighbor.position)


    def __count_neighbors(self, myself: Boid) -> int:
        neighbors = []
        for boid in self.agents:
            if np.all(boid.position != myself.position):
                # Calculate distance
                neighbors.append(boid)

        # neighbors = filter(
            # lambda neighbor: distance_to_neighbor(myself, neighbor) <= myself.radius,
            # neighbors,
        # )
        return neighbors

    def __move_agents(self, boid):
        # Moves boids
        # boid.position += boid.velocity
        neighbors = self.__count_neighbors(boid)
        self.__separation_rule(boid, neighbors)
        self.__align_rule(boid, neighbors)
        self.__cohesion_rule(boid, neighbors)

        self.__handle_borders(boid)

    def __show_world(self):
        state_to_char = " *"

        for row in self.world:
            # print(row)
            print(*[state_to_char[state] for state in row])
        pass

    def __clear_screen(self):
        system("clear")
        print(
            "-" * (self.shape[1] - 7) + "Boid Simulation" + "-" * (self.shape[1] - 7),
            sep="\n\n",
        )

    def run_simulation(self):
        while True:
            # Updates boids
            for boid in self.agents:
                self.__move_agents(boid)
                self.__update_world(boid)
            # Prints world
            self.__show_world()
            sleep(1)
            # Clears for next iter
            self.__clear_world()
            self.__clear_screen()


def main():
    playground = Playground(shape=(20, 20), n_agents=100)
    playground.run_simulation()


if __name__ == "__main__":
    main()
