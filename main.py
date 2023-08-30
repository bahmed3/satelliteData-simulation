import pygame
import math
import time
import random
from physics import calculate_new_position, calculate_temperature
# from mqtt_helper import publish_to_mqtt  # Uncomment if you have MQTT setup

# Initialize Pygame
pygame.init()

# Constants
window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Satellite Simulation')

# Load and scale images
earth = pygame.image.load('earth.png')
scaled_earth = pygame.transform.scale(earth, (300, 300))  # Scale the image to 300x300 pixels
satellite = pygame.image.load('satellite.png')
scaled_satellite = pygame.transform.scale(satellite, (40, 40))  # Scale the image to 50x50 pixels

# Initial satellite state
position = 0  # initial angle in radians
velocity = 0.001  # just a value for demonstration, can be calculated as in your physics module
theta = 0  # Initialize angle to 0 radians

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update position and temperature
    position = calculate_new_position(position, velocity, 1)
    distance_to_sun = 1.496e11 + random.uniform(-1e9, 1e9)
    temperature = calculate_temperature(distance_to_sun)

    # Update theta (angle)
    theta += 0.01  # Increment angle

    # Print data to console
    print(f"New position: {position}")
    print(f"Temperature: {temperature}")

    # Publish to MQTT
    # publish_to_mqtt('satellite/position', position)  # Uncomment if you have MQTT setup
    # publish_to_mqtt('satellite/temperature', temperature)  # Uncomment if you have MQTT setup

    # Clear screen
    win.fill((0, 0, 0))

    # Draw Earth and satellite
    earth_rect = scaled_earth.get_rect(center=(window_width // 2, window_height // 2))
    win.blit(scaled_earth, earth_rect)

    satellite_x = window_width // 2 + math.cos(theta) * 100  # Use theta for cos and sin
    satellite_y = window_height // 2 + math.sin(theta) * 100  # Use theta for cos and sin

    satellite_rect = scaled_satellite.get_rect(center=(satellite_x, satellite_y))
    win.blit(scaled_satellite, satellite_rect)

    pygame.display.update()
    time.sleep(1)
