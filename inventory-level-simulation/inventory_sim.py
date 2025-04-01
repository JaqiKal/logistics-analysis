"""
Inventory Simulation and Visualization

This script simulates daily warehouse inventory levels over a 10-day period 
based on incoming replenishments and outgoing customer orders. It uses matplotlib 
to visualize the inventory level, incoming stock, and outgoing flow. A reorder 
point line is also included to illustrate stock threshold awareness.

Date: 2025 April
Author: JaqKal
"""

import matplotlib.pyplot as plt

# Simulated date for 10 days
days = list(range(1, 11))  # Days 1 to 10
incoming = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]  # Incoming stock per day/replensishment
outgoing = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]  # Outgoing stock per day/customer orders

# Calculate inventory level per day
starting_inventory = 100
inventory = [starting_inventory]

for i in range(len(days)):
    new_level = inventory[-1] + incoming[i] - outgoing[i]
    inventory.append(max(new_level, 0)) # Ensure inventory doesn't go negative

# Remove the initial extra item for alignment
inventory = inventory[1:]

# Constants
reorder_point =  30

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(days, inventory, marker='o', label='Inventory Level', color='blue')    
plt.axhline(y=reorder_point, color='red', linestyle='--', label='Reorder Point')

# Optional: show incoming & outgoing as bar charts
plt.bar(days, incoming, alpha=0.5, label='Incoming Stock', color='green')
plt.bar(days, [-x for x in outgoing], label='Outgoing Stock', color='orange')

# Styling
plt.title("Inventory Level Over Time")
plt.xlabel("Day")
plt.ylabel("Units")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show or save
plt.show()
