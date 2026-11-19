"""Task 6 (modified): Service marketplace job mix.
Assumption: two job types. Type A takes 2 hours and pays KES 1,500;
Type B takes 3 hours and pays KES 2,500. In one week the team logged
38 working hours and KES 30,000 of payouts. How many jobs of each type?"""
import numpy as np

A = np.array([[2.0, 3.0],
              [1500.0, 2500.0]])
b = np.array([38.0, 30000.0])

jobs = np.linalg.solve(A, b)
residual = b - A @ jobs

print(f"Type A jobs: {jobs[0]:.2f}")
print(f"Type B jobs: {jobs[1]:.2f}")
print("Check A @ jobs:", A @ jobs)
print("Residual norm:", np.linalg.norm(residual))
print("Determinant of A:", round(np.linalg.det(A), 2))
print("Condition number:", round(np.linalg.cond(A), 2))
