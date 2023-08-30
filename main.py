import pygame
import math
import time
import random
from physics import calculate_new_position, calculate_temperature

# Initialize Pygame
pygame.init()
my_font = pygame.font.SysFont('arial', 20)

# Constants
window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Satellite Simulation')

# Load and scale images
earth = pygame.image.load('earth.png')
scaled_earth = pygame.transform.scale(earth, (300, 300))
satellite = pygame.image.load('satellite.png')
scaled_satellite = pygame.transform.scale(satellite, (40, 40))

# Initial satellite state
position = 0  # initial angle in radians
velocity = 0.01  # Updated velocity for demonstration

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update position and temperature
    position += 0.01  # Temporarily set a fixed increment to make sure the satellite moves
    distance_to_sun = 1.496e11 + random.uniform(-1e9, 1e9)
    temperature = calculate_temperature(distance_to_sun)

    # Clear screen
    win.fill((0, 0, 0))

    # Draw Earth and satellite
    earth_rect = scaled_earth.get_rect(center=(window_width // 2, window_height // 2))
    win.blit(scaled_earth, earth_rect)

    satellite_x = window_width // 2 + math.cos(position) * 100
    satellite_y = window_height // 2 + math.sin(position) * 100

    satellite_rect = scaled_satellite.get_rect(center=(satellite_x, satellite_y))
    win.blit(scaled_satellite, satellite_rect)

    # Draw text for position and temperature
    position_text = my_font.render(f"Position: {position:.2f} rad", True, (0, 0, 128))
    temperature_text = my_font.render(f"Temperature: {temperature:.2f} K", True, (0, 0, 128))




    win.blit(position_text, (satellite_x + 50, satellite_y))
    win.blit(temperature_text, (satellite_x + 50, satellite_y + 20))

    pygame.display.update()
    time.sleep(1)
