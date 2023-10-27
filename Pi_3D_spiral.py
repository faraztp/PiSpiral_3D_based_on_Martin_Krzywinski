from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp
import matplotlib.cm as cm

# Step 1: Obtain Pi Digits
mp.dps = 500  # Number of decimal places
pi_digits = str(mp.pi)[2:]  # Get Pi digits, removing the "3."

# Step 2: Initialize Variables
num_segments = len(pi_digits)
theta_increment = 0.05  # Smaller angle increment for smoothness
a, b = 0, 0.05  # Constants for Archimedean Spiral

# Create a colormap for full spectrum of colors
colors = cm.rainbow(np.linspace(0, 1, 10))

# Step 3: Initialize Spiral Parameters
theta = 0
x, y, z = 0, 0, 0

# Create a new 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make axis panes transparent
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

# Turn off the axis lines and ticks
ax.set_axis_off()

# Calculate coordinates based on Archimedean Spiral equation
def calculate_spiral_coords(theta, a, b):
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Infinite loop for continuous spiral
while True:
    for i in range(num_segments):
        digit = int(pi_digits[i])

        # Get color from the colormap
        color = colors[digit]

        # Calculate the next coordinates
        x_new, y_new = calculate_spiral_coords(theta, a, b)

        # Calculate the next z-coordinate based on the digit
        z_new = z + digit * 0.01  # Smaller z-increment for smoothness

        # Draw the segment with a thinner line
        ax.plot([x, x_new], [y, y_new], [z, z_new], color=color, linewidth=0.5)

        # Update current position and angle
        x, y, z = x_new, y_new, z_new
        theta += theta_increment

        # Pause to visualize the drawing
        plt.pause(0.01)

    # Clear the axis for the next loop
    ax.clear()
    ax.set_axis_off()

# Show the Pi Spiral
plt.show()
