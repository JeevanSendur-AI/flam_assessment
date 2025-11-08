import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# -----------------------------------------------------
#  Load data
# -----------------------------------------------------
data = pd.read_csv("xy_data_sorted.csv")
x_obs = data["x"].values
y_obs = data["y"].values
N = len(data)

# Construct t values (uniform from 6 to 60)
t = np.linspace(6, 60, N)

# -----------------------------------------------------
#  Define the model
# -----------------------------------------------------
def curve_model(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# -----------------------------------------------------
#  Define the residuals for least squares
# -----------------------------------------------------
def residuals(params, t, x_obs, y_obs):
    theta, M, X = params
    x_pred, y_pred = curve_model(t, theta, M, X)
    return np.concatenate([x_pred - x_obs, y_pred - y_obs])

# -----------------------------------------------------
#  Initial guess and parameter bounds
# -----------------------------------------------------
theta0 = np.deg2rad(20.0)
M0 = 0
X0 = 60
initial_guess = [theta0, M0, X0]

bounds = (
    [0.0, -0.05, 0.0],           # lower bounds
    [np.deg2rad(50.0), 0.05, 100.0]  # upper bounds
)

# -----------------------------------------------------
# Optimize the parameters
# -----------------------------------------------------
result = least_squares(residuals, initial_guess, args=(t, x_obs, y_obs), bounds=bounds)
theta_opt, M_opt, X_opt = result.x

# -----------------------------------------------------
# Compute fitted curve
# -----------------------------------------------------
x_fit, y_fit = curve_model(t, theta_opt, M_opt, X_opt)

# -----------------------------------------------------
#  Evaluate fit quality
# -----------------------------------------------------
L1_error = np.mean(np.abs(x_fit - x_obs) + np.abs(y_fit - y_obs))

print("\n=== OPTIMIZATION RESULTS ===")
print(f"Theta (radians): {theta_opt:.6f}")
print(f"Theta (degrees): {np.rad2deg(theta_opt):.6f}")
print(f"M: {M_opt:.6f}")
print(f"X: {X_opt:.6f}")
print(f"Mean L1 Error per point: {L1_error:.6f}")
print(f"Optimization success: {result.success}, message: {result.message}")

# -----------------------------------------------------
# Show fitted vs observed curve
# -----------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(x_obs, y_obs, s=10, alpha=0.5, label="Observed points")
plt.plot(x_fit, y_fit, 'r-', linewidth=1.8, label="Fitted curve")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Observed vs Fitted Curve")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------------------
# Output final parametric equation (LaTeX form)
# -----------------------------------------------------
latex_eq = (
    f"\\left(t\\cos({theta_opt:.6f})"
    f"-e^{{{M_opt:.6f}|t|}}\\sin(0.3t)\\sin({theta_opt:.6f})+{X_opt:.6f},"
    f"\\;42+t\\sin({theta_opt:.6f})+e^{{{M_opt:.6f}|t|}}\\sin(0.3t)\\cos({theta_opt:.6f})\\right)"
)

print("\nLaTeX equation for submission:\n")
print(latex_eq)
