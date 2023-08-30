'''
File: game_of_life.py
Project: Images
File Created: Wednesday, 30th August 2023 1:25:00 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Wednesday, 30th August 2023 1:25:04 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Conway's Game of Life.
'''

from CA import CA
from numpy import uint8
import PIL
# from os import system
# from time import sleep

if __name__ == "__main__":
    # CA init
    ROWS, COLS = 30, 37
    ca = CA(world_dim=(ROWS, COLS))

    # Glider gun initialization
    cell_positions = [
        (5, 1),
        (5, 2),
        (6, 1),
        (6, 2),
        (3, 13),
        (3, 14),
        (4, 12),
        (4, 16),
        (5, 11),
        (5, 17),
        (6, 11),
        (6, 15),
        (6, 17),
        (6, 18),
        (7, 11),
        (7, 17),
        (8, 12),
        (8, 16),
        (9, 13),
        (9, 14),
        (1, 25),
        (2, 23),
        (2, 25),
        (3, 21),
        (3, 22),
        (4, 21),
        (4, 22),
        (5, 21),
        (5, 22),
        (6, 23),
        (6, 25),
        (7, 25),
        (3, 35),
        (3, 36),
        (4, 35),
        (4, 36)
    ]

    for x, y in cell_positions:
        ca.set_cell_value(x, y, value=1)

    # Create GIF
    images = []
    for _ in range(100):
        images.append(PIL.Image.fromarray((ca.world_to_numpy()*255).astype(uint8)))
        ca.update_world(generations=1)
        # Show on terminal
        # system("clear")
        # print(f"Game of Life - Gen {ca.gen}\n")
        # ca.show_world_pretty()
        # sleep(0.5)
    images[0].save(
        "game_of_life_glider_gun.gif",
        save_all=True,
        append_images=images[1:],
        duration=300,
        loop=0
    )