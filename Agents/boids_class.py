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
    position: np.ndarray(shape=(1, 2), dtype=np.float32)
    # x', y'
    velocity: np.ndarray(shape=(1, 2), dtype=np.float32)
    # Visual range
    radius: int = 3


@dataclass
class Playground:
    shape: tuple[int, int]
    world: np.ndarray = field(init=False)
    n_agents: int = 10
    agents: list[Boid] = field(init=False, default_factory=lambda: [])
    # Check out Kfish.org/BOIDS/Pseudocode.html
    coherence_factor: float = 8
    separation_radius: float = 2
    alignment_factor: float = 100

    def __post_init__(self):
        self.__init_agents()
        self.world = np.zeros(shape=self.shape, dtype=np.uint8)

    def __init_agents(self):
        for _ in range(self.n_agents):
            # Random positions and velocity
            x = np.random.uniform(0, self.shape[0])
            y = np.random.uniform(0, self.shape[1])
            # TODO Make the movement smoother
            dx = np.random.uniform(-1, 1)
            dy = np.random.uniform(-1, 1)

            self.agents.append(
                Boid(position=np.array([x, y]), velocity=np.array([dx, dy]))
            )

    def __clear_world(self):
        # Clears world
        self.world = np.zeros(shape=self.shape, dtype=np.uint8)

    def __update_world(self, boid: Boid):
        self.world[int(boid.position[0]), int(boid.position[1])] = 1

    def __handle_borders(self, boid: Boid):
        # Out of x bounds
        if boid.position[0] < 0:
            boid.position[0] = self.shape[0] - 1
        elif boid.position[0] > self.shape[0] - 1:
            boid.position[0] = 0
        # Out of y bounds
        if boid.position[1] < 0:
            boid.position[1] = self.shape[1] - 1
        elif boid.position[1] > self.shape[1] - 1:
            boid.position[1] = 0


    def __cohesion_rule(self, myself: Boid, neighbors: list[Boid]):
        # print(f"{len(neighbors)=}")
        new_velocity = np.array([0, 0], dtype=np.float32)
        for neighbor in neighbors:
            # print(f"{neighbor.velocity=}")
            new_velocity += neighbor.velocity

        new_velocity = new_velocity / len(neighbors)

        return (new_velocity - myself.velocity) / self.coherence_factor


    def __align_rule(self, myself: Boid, neighbors: list[Boid]) -> np.ndarray:    
        new_position = np.array([0, 0], dtype=np.float32)
        for neighbor in neighbors:
                new_position += neighbor.position

        new_position = new_position / len(neighbors)

        return (new_position - myself.position) / self.alignment_factor


    def __separation_rule(self, myself: Boid, neighbors: list[Boid]):
        vector_c = np.array([0, 0], dtype=np.float32)
        for neighbor in neighbors:
            distance_to_neighbor = self.__distance_to_neighbor(myself, neighbor)
            # print(f"distance_to_neighbor: {distance_to_neighbor}")
            if distance_to_neighbor < self.separation_radius:
                vector_c += (myself.position - neighbor.position)
                # print(f"{vector_c=}")

        return vector_c

    
    def __distance_to_neighbor(self, myself: Boid, neighbor: Boid):
        return np.linalg.norm(myself.position - neighbor.position)


    def __count_neighbors(self, myself: Boid) -> list[Boid]:
        neighbors = []
        for boid in self.agents:
            if boid is not myself:
                # Calculate distance
                neighbors.append(boid)

        # neighbors = list(filter(
            # lambda neighbor: True if self.__distance_to_neighbor(myself, neighbor) < self.separation_radius else False,
            # neighbors,
        # ))
        # print(f"{neighbors=}")
        # print(f"{len(neighbors)=}")
        return neighbors

    def __simple_movement(self, boid):
        boid.position += np.array([1, 1])
        self.__handle_borders(boid)

    def __move_agents(self, boid):
        # Counts neighbors
        neighbors = self.__count_neighbors(boid)
        # self.check_collision(boid, neighbors)
        # Applys rules and calculates velocity
        v1 = self.__separation_rule(boid, neighbors)
        v2 = self.__align_rule(boid, neighbors)
        v3 = self.__cohesion_rule(boid, neighbors)

        # Updates velocity and position
        # print(f"{boid.position=}")
        boid.velocity += v1 + v2 + v3
        boid.velocity = np.clip(boid.velocity, -1, 1)
        # print(f"{boid.velocity=}")
        # boid.velocity += v1
        boid.position += boid.velocity
        # print(f"{boid.position=}")

        # Boundary handling
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

    def check_collision(self, myself, neighbors):
        for neighbor in neighbors:
            if np.all(myself.position == neighbor.position):
                print("COLLISION DETECTED")

    def run_simulation(self):
        while True:
            # Updates boids
            for boid in self.agents:
                # Apply rules to obtain velocities modifications
                # Apply velocity and update positions
                self.__move_agents(boid)
                # self.__simple_movement(boid)
                self.__update_world(boid)
            # Prints world
            self.__show_world()
            sleep(0.1)
            # Clears for next iter
            self.__clear_world()
            self.__clear_screen()


def main():
    playground = Playground(shape=(50, 50), n_agents=50)
    playground.run_simulation()


if __name__ == "__main__":
    main()
