import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("xy_data_sorted.csv")

# Create figure
plt.figure(figsize=(8, 6))

# Draw connecting lines first
plt.plot(data["x"], data["y"], '-', color='red', linewidth=1.2, label='Connecting lines')

# Draw scatter points on top
plt.scatter(data["x"], data["y"], s=10, color='blue', alpha=0.7, label='Points')

# Labels and grid
plt.title("Reconstructed Continuous Curve from Sorted Data")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Equal scale: 1 unit on x = 1 unit on y
plt.gca().set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()
