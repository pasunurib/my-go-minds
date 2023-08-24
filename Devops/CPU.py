import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize lists to store data
cpu_percentages = []
memory_percentages = []

# Set up the figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('CPU and Memory Utilization')

# Create initial empty plots
line1, = ax1.plot([], [], label='CPU %')
line2, = ax2.plot([], [], label='Memory %')
lines = [line1, line2]

# Set up the axes labels and legends
ax1.set_ylabel('CPU Utilization (%)')
ax2.set_ylabel('Memory Utilization (%)')
ax2.set_xlabel('Time (s)')
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')

# Function to update the plots
def update(frame):
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent

    cpu_percentages.append(cpu_percent)
    memory_percentages.append(memory_percent)

    time_points = list(range(len(cpu_percentages)))

    for line, data in zip(lines, [cpu_percentages, memory_percentages]):
        line.set_data(time_points, data)
        line.axes.set_xlim(0, max(time_points))
        line.axes.set_ylim(0, 100)

    return lines

# Create an animation
ani = FuncAnimation(fig, update, blit=True, interval=1000)

# Show the plot
plt.tight_layout()
plt.show()
