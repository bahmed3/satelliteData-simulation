from math import sqrt, pi

# Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2, gravitational constant
M = 5.9722e24  # kg, mass of Earth
R = 6371e3  # m, radius of Earth
r = R + 35786e3  # m, altitude of geostationary orbit

def calculate_new_position(old_position, velocity, time_step):
    # Calculating orbital velocity
    velocity = sqrt(G * M / r)
    
    # Calculating angular velocity (omega)
    omega = velocity / r
    
    # Calculating change in angle (delta_theta)
    delta_theta = omega * time_step
    
    # Calculating new position
    new_position = old_position + delta_theta
    
    # Keeping angle between 0 and 2*pi
    new_position = new_position % (2 * pi)
    
    return new_position

def calculate_temperature(distance_to_sun):
    # Simple temperature model based on distance to sun
    return 300 / sqrt(distance_to_sun / 1.496e11)