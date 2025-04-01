"""
Transport Cost Breakdown Visualization

This script compares transport costs across 5 delivery routes by separating
fixed and variable cost components. The chart helps illustrate which routes
are most cost-efficient or have a high variable share.

Date: 2025 April
Author: JaqKal
"""
import matplotlib.pyplot as plt

# Route names
routes = ["Route A", "Route B", "Route C", "Route D", "Route E"]

# Simulated transport costs (SEK)
fixed_costs = [1200, 1000, 1300, 1100, 900]
variable_cost = [800, 1200, 900, 1100, 1000]

# Total for reference (optional)
total_costs = [f + v for f, v in zip(fixed_costs, variable_cost)]

# Plotting stacked bar chart
plt.figure(figsize=(10, 6))
plt.bar(routes, fixed_costs, label="Fixed Cost", color="skyblue")
plt.bar(
    routes,
    variable_cost,
    bottom=fixed_costs,
    label="Variable Cost",
    color="orange"
)

# Styling
plt.title('Transport Cost per Route (SEK)')
plt.ylabel('SEK')
plt.xlabel('Delivery Route')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()

# Show chart
plt.show()
