import numpy as np
import matplotlib.pyplot as plt    # Libraries for math calculation and graph plotting.
from solvers import jacobi,apply_boundary_conditions  # Math Functions

# User Input Section

print("\n2D Laplace Equation Solver using Iterative Methods\n")
N = int(input("\n[-]Enter grid size N (e.g. 50): "))
max_iter = int(input("\n[-]Enter maximum iterations (e.g. 5000): "))
tol = float(input("\n[-]Enter tolerance (e.g. 1e-6): "))
omega = float(input("\n[-]Enter SOR relaxation factor omega (e.g. 1.7): "))

# Initial Grid

u0 = np.zeros((N, N))
u0 = apply_boundary_conditions(u0)

