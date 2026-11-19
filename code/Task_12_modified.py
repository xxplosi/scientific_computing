"""Task 12 (modified): Overlap of two cell-tower coverage areas.
Assumption: Tower 1 at (0, 0) with radius 5 km; Tower 2 at (6, 2) with radius 4 km.
The handover points are where both circles meet: two nonlinear equations."""
import numpy as np
from scipy.optimize import root

def equations(z):
    x, y = z
    return [x**2 + y**2 - 25,
            (x - 6)**2 + (y - 2)**2 - 16]

found = []
for guess in ([3.0, 4.0], [5.0, -1.0], [0.0, 0.0]):
    sol = root(equations, guess)
    print("Guess:", guess, "->", np.round(sol.x, 5),
          "| residual norm:", f"{np.linalg.norm(equations(sol.x)):.2e}",
          "| converged:", sol.success)
    if sol.success and not any(np.allclose(sol.x, f, atol=1e-6) for f in found):
        found.append(sol.x)

print("\nDistinct handover points (km):")
for p in found:
    print("  ", np.round(p, 4), "distance to tower 1:", round(np.hypot(*p), 4),
          "| to tower 2:", round(np.hypot(p[0]-6, p[1]-2), 4))
