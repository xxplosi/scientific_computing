"""Task 7 (modified): Solar mini-grid circuit solved for 24 hourly source voltages.
Assumption: a 3-loop resistor network (mesh analysis). The resistance matrix R stays
the same, but the source voltage vector changes every hour as sunlight changes.
Factor R once with LU, then reuse it for all 24 hours."""
import numpy as np
import timeit
from scipy.linalg import lu_factor, lu_solve

R = np.array([[10.0, -2.0, 0.0],
              [-2.0,  8.0, -3.0],
              [0.0,  -3.0, 9.0]])

hours = np.arange(24)
sun = np.clip(np.sin((hours - 6) * np.pi / 12), 0, None)   # 0 at night, 1 at noon
V = np.column_stack([12 * sun, 6 * sun, 9 * sun])          # one source vector per hour

lu, piv = lu_factor(R)
currents = np.array([lu_solve((lu, piv), v) for v in V])

print("Hour 12 (noon) loop currents (A):", np.round(currents[12], 4))
print("Hour 3  (night) loop currents (A):", np.round(currents[3], 4))
print("Maximum residual over 24 hours:",
      max(np.linalg.norm(v - R @ i) for v, i in zip(V, currents)))


# Timing on a LARGER network (400 loops) with 300 different source vectors.
# For a tiny 3x3 matrix the Python overhead hides the benefit; for big systems it is large.
rng = np.random.default_rng(1)
n_big = 400
R_big = rng.uniform(-1, 1, (n_big, n_big))
R_big += np.diag(np.abs(R_big).sum(axis=1) + 1)       # make it diagonally dominant
V_big = rng.uniform(0, 12, (300, n_big))

t_direct = timeit.timeit(lambda: [np.linalg.solve(R_big, v) for v in V_big], number=1)
lu_big = lu_factor(R_big)
t_reuse = timeit.timeit(lambda: [lu_solve(lu_big, v) for v in V_big], number=1)
t_factor = timeit.timeit(lambda: lu_factor(R_big), number=1)

print(f"400x400 system, 300 source vectors:")
print(f"  np.linalg.solve each time : {t_direct:.3f} s")
print(f"  LU factor once + reuse    : {t_factor + t_reuse:.3f} s  (factor {t_factor:.3f} s + 300 solves {t_reuse:.3f} s)")
print(f"  Speed-up                  : {t_direct/(t_factor + t_reuse):.1f}x")
