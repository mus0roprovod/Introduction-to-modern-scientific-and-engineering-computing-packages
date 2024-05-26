import numpy as np
import matplotlib.pyplot as plt

def madcoc(speed, angle, scale_factor, x_start, y_start, z_start):
    initial_radius = np.hypot(x_start, y_start) * scale_factor
    angle_rad = np.deg2rad(angle)
    initial_theta = angle_rad
    time_points = np.linspace(0, 100, 1000)
    radius = initial_radius - (initial_radius / 100) * time_points
    theta = initial_theta + (2 * np.pi / 100) * time_points
    height = initial_radius - radius
    x_coords = radius * np.cos(theta)
    y_coords = radius * np.sin(theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_coords, y_coords, height)
    ax.scatter(0, 0, initial_radius, color='y', s=30)
    ax.legend()
    plt.show()


