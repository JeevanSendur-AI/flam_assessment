import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("xy_data.csv")

# Sort by x coordinate
data_sorted = data.sort_values(by="x").reset_index(drop=True)

# Save to a new CSV
data_sorted.to_csv("xy_data_sorted.csv", index=False)

# Plot the reconstructed order
plt.figure(figsize=(8, 6))
plt.scatter(data["x"], data["y"], s=8, alpha=0.4, label="Original (unordered)")
plt.plot(data_sorted["x"], data_sorted["y"], '-', lw=1.5, color='red', label="Sorted by x")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Curve Sorted by X (Reconstructed Order)")
plt.grid(True)
plt.tight_layout()
plt.show()
