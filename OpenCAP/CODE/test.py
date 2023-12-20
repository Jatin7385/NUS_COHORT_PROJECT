import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

# Function to generate random data for the example
def generate_data():
    x = np.random.rand(5) * 10
    y = np.random.rand(5) * 10
    z = np.random.rand(5) * 10
    return x, y, z

# Set up the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter([], [], [], c='r', marker='o')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

plt.ion()  # Turn on interactive mode

# Real-time updating loop
for _ in range(50):  # Adjust the number of iterations as needed
    time.sleep(0.2)  # Simulate some data generation delay
    
    # Generate new data
    x, y, z = generate_data()

    # Update the scatter plot
    sc._offsets3d = (x, y, z)

    # Draw the updated plot
    plt.draw()
    plt.pause(0.1)

plt.ioff()  # Turn off interactive mode (optional)
plt.show()