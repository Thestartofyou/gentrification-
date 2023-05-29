import matplotlib.pyplot as plt
import numpy as np

# Sample data representing car count and demographic information
# Format: (x, y, car_count, demographic_score)
data = [
    (1, 1, 10, 0.8),
    (2, 2, 5, 0.6),
    (3, 3, 15, 0.9),
    (4, 4, 8, 0.7),
    (5, 5, 12, 0.85),
    # Add more data points...
]

def calculate_hotness(car_count, demographic_score):
    # Define a formula to calculate hotness based on car count and demographic score
    return car_count * demographic_score

# Extract data points
x = [d[0] for d in data]
y = [d[1] for d in data]

# Calculate hotness for each data point
hotness = [calculate_hotness(d[2], d[3]) for d in data]

# Create a scatter plot with hotness as the color
plt.scatter(x, y, c=hotness, cmap='hot', s=100)
plt.colorbar(label='Hotness')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Hot Zones')

# Add annotations to indicate car count and demographic score
for i, d in enumerate(data):
    plt.annotate(f'{d[2]} cars, {d[3]:.2f}', (d[0], d[1]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
