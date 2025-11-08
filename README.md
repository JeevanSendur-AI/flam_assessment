# flam_assessment
Assessment done by Jeevan Sendur G for FLAM for the role of Research and development engineer-AI
# Just Run 'python param_fitting_v1.py'

Desmos Link: https://www.desmos.com/calculator/vlcjl6hlq5

Unknown Variables recovered:

θ deg = 30.091366 degrees, 0.525193 rad ;
M = 0.029880 ;
X = 55.013786

Equation in latex: "\left(t*\cos(0.525193)-e^{0.029880\left|t\right|}\cdot\sin(0.3t)\sin(0.525193)+55.013786,\;42+\ t*\sin(0.525193)+e^{0.029880\left|t\right|}\cdot\sin(0.3t)\cos(0.525193)\right)"


# Steps Followed
# 1. Data visualization: 
Plotted the data given in CSV, but noticed that the line in between subsequent datapoints were not in order

# 2. Data Sorting: 
Sorted the data with respect to increasing order of x values, as y is not incremental and followed a wave pattern.

# 3. Re-plotting:
Plotted the sorted data again (with connecting lines).
Verified that the curve was now continuous and smooth.

# 4. Parameter Estimation:
Used the given equations for x(t),y(t).
Defined a loss function comparing model predictions vs. actual points.
Used scipy.optimize.least_squares to find best-fit values for θ, M, and X.

# 5. Optimization Results:
Mean L1 error per point = 0.305275

# 6. Validation:
Plotted the fitted curve using these parameters.
Observed a perfect overlap between fitted and actual points.

# 7. Desmos Plot:
Used the final fitted equation in Desmos for visual verification.
The Desmos plot matched the Python plot exactly.

# Conclusion:
Successfully reverse-engineered the missing parameters.
Achieved a near-perfect fit with minimal error.

