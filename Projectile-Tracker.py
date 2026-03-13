"""Projectile Tracker by Group 5 for Dennis Moreno's EGR115 at ERAU Sping 2026"""
import numpy as np
import Projectile_Functions as pro12
import matplotlib.pyplot as plt


def main():

    launch_velocity, launch_height, launch_angle = pro12.projectile_setup() #runs custom function to gather user input data

    if launch_velocity == "exit" or launch_height == "exit" or launch_angle == "exit":  # Check if the user wants to exit the program
        print("Exiting program...")
        exit()

    time_of_flight = pro12.time_of_flight(launch_velocity, launch_height, launch_angle) #runs fn to calculate tof
    horizontal_range = pro12.horizontal_range(launch_velocity, launch_angle, time_of_flight) #runs fn to calc range
    t_max, max_x, max_y = pro12.max_height(launch_velocity, launch_angle, launch_height) #runs fn to calc max height

    times = np.linspace(0, time_of_flight, 200)

    pointsX, pointsY = pro12.position_at_time(launch_velocity, launch_angle, launch_height, times)
    velocity = pro12.velocity_at_time(launch_velocity, launch_angle, times)

    plt.figure(num = 1, figsize = (13,4))
    plt.plot(pointsX, pointsY, color = 'red', linewidth = 1, label = 'Projectile Path')

    plt.scatter(max_x, max_y, color='blue', label='Max Height', zorder=3)

    plt.annotate(f"Max Height ({max_x:.2f}, {max_y:.2f})",
             (max_x, max_y),
             textcoords="offset points",
             xytext=(0,-20),
             ha='center')
    
    plt.scatter(horizontal_range, 0, color='green', label='Final Position', zorder=3)

    plt.annotate(f"Final pos ({horizontal_range:.2f}, {0:.2f})",
             (horizontal_range, 0),
             textcoords="offset points",
             xytext=(-80,-5),
             ha='center')
    
    plt.xlabel('X (meters)')
    plt.ylabel('Y (meters)')
    plt.title('Projectile Tracker')
    plt.grid(True) # Setting up the background of the graph
    plt.legend()
    plt.show()

    plt.figure(num = 2, figsize = (13,4))
    plt.plot(times, pointsY, color = 'red', linewidth = 1, label = 'Projectile Path')

    plt.scatter(t_max, max_y, color='blue', label='Max Height', zorder=3)
    plt.annotate(f"Max Height ({max_x:.2f}, {max_y:.2f})",
             (t_max, max_y),
             textcoords="offset points",
             xytext=(0,-20),
             ha='center')

    plt.xlabel('t (seconds)')
    plt.ylabel('Y (meters)')
    plt.title('Projectile Tracker')
    plt.grid(True) # Setting up the background of the graph
    plt.legend()
    plt.show()

    

    plt.figure(num = 3, figsize = (13,4))
    plt.plot(times, velocity, color = 'red', linewidth = 1, label = 'Projectile Path')
    plt.xlabel('t (seconds)')
    plt.ylabel('v (meters/second)')
    plt.title('Projectile Tracker')
    plt.grid(True) # Setting up the background of the graph
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()