"""List of functions created to simplify code for projectile tracker application"""
import math

# Define constant vars
g = 9.81

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def projectile_setup():
    print("Welcome to the Projectile Tracker!")
    print("This program will calculate the time of flight, horizontal range, and maximum height of a projectile based on user input for launch velocity, launch height, and launch angle.\n\n")

    launch_velocity = get_float("Enter initial launch velocity of projectile being launched (in m/s): ")
    launch_height = get_float("Enter initial launch height for projectile being launched (in meters): ")
    launch_angle = get_float("Enter launch angle for projectile being launched (in degrees above horizontal): ")
    return launch_velocity, launch_height, launch_angle

def time_of_flight(launch_velocity, launch_height, launch_angle): # Created by Daniel Enriquez Calderon

    launch_angle_rad = math.radians(launch_angle) #convert degree angle into radians 
    # time = (2 * launch_velocity * math.sin(launch_angle_rad)) / g #formula to solve for time
    return (launch_velocity * math.sin(launch_angle_rad) + math.sqrt((launch_velocity * math.sin(launch_angle_rad))**2 + 2 * g * launch_height)) / g #time #in seconds (s)
    
def horizontal_range(launch_velocity, launch_angle, time_of_flight):

    return launch_velocity * math.cos(math.radians(launch_angle)) * time_of_flight #range
    
def max_height(launch_velocity, launch_angle, launch_height):

    angle_rad = math.radians(launch_angle)

    t_max = (launch_velocity * math.sin(angle_rad)) / g

    max_y = (launch_velocity**2 * math.sin(angle_rad)**2) / (2 * g) + launch_height
    max_x = (launch_velocity**2 * math.sin(2*angle_rad)) / (2 * g)

    return t_max, max_x, max_y
    
def velocity_at_time(launch_velocity, launch_angle, time):

    return launch_velocity * math.sin(math.radians(launch_angle)) - g * time

    
def position_at_time(launch_velocity, launch_angle, launch_height, time):

    launch_angle_rad = math.radians(launch_angle)
    x = launch_velocity * math.cos(launch_angle_rad) * time
    y = launch_velocity * math.sin(launch_angle_rad) * time - (0.5 * g * time**2) + launch_height
    return (x, y)