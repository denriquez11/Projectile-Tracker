# Projectile Tracker – EGR115: Group 5
## Group Members
Josiah Dowell, Daniel Enriquez Calderon, Maccabee Meinig, Isabel Scalia, Gavin Sorenson

## Overview of the Project
The Projectile Tracker project calculates and plots the motion of any projectile based on user-provided inputs. The user chooses the initial launch velocity (meters per second), initial launch height (meters), and launch angle (in degrees above the horizontal). These inputs are used in a series of calculations found in the Projectile Functions branch to determine the projectile’s time of flight, horizontal range, and maximum height. The code simultaneously generates a visual plot based on the user inputs for the projectile’s trajectory using the Python library MATPLOTLIB, allowing the user to see the path of the projectile over time.

## Features of the Project
The code calculates these properties of the projectile:
- Time of Flight – total time the projectile remains in the air
- Maximum Height – highest vertical position reached
- Horizontal Range – total horizontal distance traveled
- Position at a Given Time – x and y coordinates during flight
- Velocity at a Given Time – horizontal and vertical velocity components

Along with that the code also accomplishes:
- Taking user inputs and generating the nonlinear trajectory of the projectile
- Plotting the path of the projectile using MATPLOTLIB

## Project Components
The Projectile Tracker Project is made up of two python files, the main code and the function library.

Projectile-Tracker.py (the main code) is designed to do these things:
1. Collect user inputs
2. Call calculation functions
3. Generate the trajectory points
4. Plotting the projectile motion graph

Projectile_Functions.py (the function library) contains these functions:
1. Projectile Setup
2. Nonlinear Trajectory
3. Time of Flight
4. Horizontal Range
5. Max Height
6. Position at Time
7. Velocity at Time

## Example Code Output
### Graph:
![Projectile Graph](PRESENTATION_GRAPH.png)

### User Inputs:
- Velocity: 43.5 m/s
- Launch Height: 7 m
- Launch Angle (degrees about the horizontal): 30°

## Physics Model
This project models projectile motion assuming:
- Gravity = 9.81 $m/s^2$
- There is no air resistance
- Two dimensional motion

The trajectory is calculated by using this equation:
$$
y = x\tan(\theta) - \frac{g x^2}{2 v^2 \cos^2(\theta)} + h
$$

Where:
- v  = initial launch velocity
- Θ = launch angle
- h  = launch height
- g  = gravity
