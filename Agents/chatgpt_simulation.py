import random
import math
import os
import time

# Constants for the simulation
WIDTH = 80
HEIGHT = 24
NUM_BOIDS = 20
MAX_SPEED = 2.0
BOID_RADIUS = 1.5
COHESION_DISTANCE = 10
SEPARATION_DISTANCE = 5
ALIGNMENT_DISTANCE = 15

class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = random.uniform(-1, 1)
        self.velocity_y = random.uniform(-1, 1)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def apply_rules(self, boids):
        # Rule 1: Cohesion - Move towards the center of mass of nearby boids
        center_x, center_y = 0, 0
        count = 0
        for boid in boids:
            if boid != self:
                distance = math.sqrt((self.x - boid.x)**2 + (self.y - boid.y)**2)
                if distance < COHESION_DISTANCE:
                    center_x += boid.x
                    center_y += boid.y
                    count += 1
        if count > 0:
            center_x /= count
            center_y /= count
            self.velocity_x += (center_x - self.x) / 100
            self.velocity_y += (center_y - self.y) / 100

        # Rule 2: Separation - Avoid collisions with nearby boids
        move_x, move_y = 0, 0
        for boid in boids:
            if boid != self:
                distance = math.sqrt((self.x - boid.x)**2 + (self.y - boid.y)**2)
                if distance < SEPARATION_DISTANCE:
                    move_x += (self.x - boid.x)
                    move_y += (self.y - boid.y)
        self.velocity_x += move_x
        self.velocity_y += move_y

        # Rule 3: Alignment - Align velocity with nearby boids
        avg_velocity_x, avg_velocity_y = 0, 0
        count = 0
        for boid in boids:
            if boid != self:
                distance = math.sqrt((self.x - boid.x)**2 + (self.y - boid.y)**2)
                if distance < ALIGNMENT_DISTANCE:
                    avg_velocity_x += boid.velocity_x
                    avg_velocity_y += boid.velocity_y
                    count += 1
        if count > 0:
            avg_velocity_x /= count
            avg_velocity_y /= count
            self.velocity_x += (avg_velocity_x - self.velocity_x) / 8
            self.velocity_y += (avg_velocity_y - self.velocity_y) / 8

        # Limit the speed
        speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if speed > MAX_SPEED:
            self.velocity_x = (self.velocity_x / speed) * MAX_SPEED
            self.velocity_y = (self.velocity_y / speed) * MAX_SPEED

    def wrap_around(self):
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Create boids
boids = [Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range(NUM_BOIDS)]

try:
    while True:
        clear_screen()
        for boid in boids:
            boid.apply_rules(boids)
            boid.move()
            boid.wrap_around()
            x, y = int(boid.x), int(boid.y)
            print(f"\033[{y+1};{x+1}H@", end='')  # Print boid at position (x, y)
        time.sleep(0.1)  # Sleep for 50 milliseconds to control the animation speed

except KeyboardInterrupt:
    pass  # Exit the simulation
