#  Step 1: Install necessary libraries (run in notebook cell)
!pip install pulp matplotlib numpy

#  Step 2: Import libraries
from pulp import LpMaximize, LpProblem, LpVariable, value
import matplotlib.pyplot as plt
import numpy as np

#  Step 3: Define the Linear Programming Model
model = LpProblem("Product_Mix_Optimization", LpMaximize)

# Decision Variables
x1 = LpVariable("P1_units", lowBound=0, cat='Continuous')  # Product 1
x2 = LpVariable("P2_units", lowBound=0, cat='Continuous')  # Product 2

# Objective Function: Maximize profit
model += 40 * x1 + 30 * x2, "Total_Profit"

# Constraints
model += 2 * x1 + 1 * x2 <= 100, "Machine_Hours"
model += 1 * x1 + 1 * x2 <= 80,  "Labor_Hours"

#  Step 4: Solve the Model
model.solve()

#  Step 5: Display Results
print("Status:", model.status)
print("Optimal Production Plan:")
print(f" Produce {x1.varValue:.2f} units of Product 1")
print(f" Produce {x2.varValue:.2f} units of Product 2")
print(f"Maximum Profit: ₹{value(model.objective):.2f}")

#  Step 6: Plot Feasible Region and Optimal Point
x_vals = np.linspace(0, 60, 400)
y1 = 100 - 2 * x_vals        # From 2x1 + x2 <= 100
y2 = 80 - 1 * x_vals         # From x1 + x2 <= 80

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label='2x1 + x2 ≤ 100 (Machine)', color='blue')
plt.plot(x_vals, y2, label='x1 + x2 ≤ 80 (Labor)', color='green')

# Shade feasible region
plt.fill_between(x_vals, np.minimum(y1, y2), where=(y1>=0) & (y2>=0), color='lightgrey', alpha=0.5)

# Plot optimal solution
plt.plot(x1.varValue, x2.varValue, 'ro', label='Optimal Solution (Max Profit)')
plt.text(x1.varValue + 1, x2.varValue, f"({x1.varValue:.0f}, {x2.varValue:.0f})", color='red')

plt.xlabel("Product 1 Units (x1)")
plt.ylabel("Product 2 Units (x2)")
plt.title("Feasible Region and Optimal Solution")
plt.xlim((0, 60))
plt.ylim((0, 80))
plt.grid(True)
plt.legend()
plt.show()

output:
Status: 1
Optimal Production Plan:
 Produce 20.00 units of Product 1
 Produce 60.00 units of Product 2
Maximum Profit: ₹2600.00    

                
