import random

# sensors.py
def add_sensor_noise(true_value):
    noise = random.gauss(0, 1)  # Gaussian noise with mean 0 and standard deviation 1
    return true_value + noise