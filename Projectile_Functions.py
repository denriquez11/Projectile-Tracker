"""List of functions created to simplify code for projectile tracker application"""

def projectile_setup():
    print("Welcome to the Projectile Tracker! This program will calculate the time of flight, horizontal range, and maximum height of a projectile based on user input for launch velocity, launch height, and launch angle.")

    while True:
        try:
            launch_velocity = float(input("Enter initial launch velocity of projectile being launched (in m/s): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            launch_height = float(input("Enter initial launch height for projectile being launched (in meters): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            launch_angle = float(input("Enter launch angle for projectile being launched (in degrees above horizontal): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return launch_velocity, launch_height, launch_angle

def nonlinear_trajectory(angle_deg, velocity, x, launch_height): #Created by Prof Moreno w/in class slides
    import math
    g = 9.81  # acceleration due to gravity in m/s^2
    y = x * math.tan(math.radians(angle_deg)) - (g * x**2) / (2 * velocity**2 * math.cos(math.radians(angle_deg))**2) + launch_height
    return y
    
def time_of_flight(launch_velocity, launch_height, launch_angle): # Created by Daniel Enriquez Calderon
    import math
    g = 9.81  # acceleration due to gravity in m/s^2
    launch_angle_rad = math.radians(launch_angle) #convert degree angle into radians 
    # time = (2 * launch_velocity * math.sin(launch_angle_rad)) / g #formula to solve for time
    time = (launch_velocity * math.sin(launch_angle_rad) + math.sqrt((launch_velocity * math.sin(launch_angle_rad))**2 + 2 * g * launch_height)) / g
    return time #in seconds (s)
    
def horizontal_range(launch_velocity, launch_angle, time_of_flight):
    import math
    launch_angle_rad = math.radians(launch_angle)
    range = launch_velocity * math.cos(launch_angle_rad) * time_of_flight
    return range
    
def max_height(launch_velocity, launch_angle, launch_height):
    import math
    g = 9.81  # acceleration due to gravity in m/s^2
    launch_angle_rad = math.radians(launch_angle)
    height = (launch_velocity ** 2 * math.sin(launch_angle_rad) ** 2) / (2 * g) + launch_height
    return height
    
def velocity_at_time(launch_velocity, launch_angle, time):
    import math
    g = 9.81  # acceleration due to gravity in m/s^2
    launch_angle_rad = math.radians(launch_angle)
    velocity_x = launch_velocity * math.cos(launch_angle_rad)
    velocity_y = launch_velocity * math.sin(launch_angle_rad) - g * time
    return (velocity_x, velocity_y)
    
def position_at_time(launch_velocity, launch_angle, launch_height, time):
    import math
    g = 9.81  # acceleration due to gravity in m/s^2
    launch_angle_rad = math.radians(launch_angle)
    x = launch_velocity * math.cos(launch_angle_rad) * time
    y = launch_velocity * math.sin(launch_angle_rad) * time - (0.5 * g * time**2) + launch_height
    return (x, y)
