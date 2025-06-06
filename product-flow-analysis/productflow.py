"""
Warehouse Product Flow Visualization

This script uses matplotlib to plot a simple line chart comparing
incoming and outgoing products across weekdays. The goal is to
visualize product flow trends through the warehouse over a typical week.

Date: 2025 April
Author: JaqiKal
"""

import matplotlib.pyplot as plt

# Example data: incoming and outgoing products per weekday
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
incoming = [120, 150, 130, 170, 160]
outgoing = [100, 140, 120, 160, 180]

# Create the line chart
plt.plot(days, incoming, label="Incoming products", marker='s')
plt.plot(days, outgoing, label="Outgoing products", marker='o')

# Add title and labels
plt.title("Product flow through warehouse")
plt.xlabel("Day")
plt.ylabel("Number of products")

# Add legend and grid
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the chart
plt.show()
