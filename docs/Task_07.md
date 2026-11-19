# Task 7: Gaussian Elimination and LU Decomposition

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_07_gaussian_lu.py` (given program), `code/Task_07_gaussian_lu_param_change.py` (changed parameter), `code/Task_07_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** a fixed 3x3 coefficient matrix A and three different right-hand-side vectors b (three sets of measurements).
- **Mathematical operations:** factor A once into permuted lower and upper triangular matrices (PA = LU) with `lu_factor`, then solve each b by forward and back substitution with `lu_solve`; compare with `np.linalg.solve` and check the residual norm.

## 2. Original program and output

Run with `python code/Task_07_gaussian_lu.py`.

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

## 3. Changing a parameter

**What I changed:** Changed the first diagonal entry of A from 4 to 6.

```python
[6.0, -1.0, 0.0],   # was [4.0, -1.0, 0.0]
```

**Output after the change** (`code/Task_07_gaussian_lu_param_change.py`):

```text
Measurement set 1
Solution: [3.25396825 4.52380952 4.84126984]
Residual norm: 3.552713678800501e-15

Measurement set 2
Solution: [3.46031746 4.76190476 4.58730159]
Residual norm: 0.0

Measurement set 3
Solution: [3.19047619 5.14285714 5.38095238]
Residual norm: 4.351167857633658e-15

Direct solution for first set: [3.25396825 4.52380952 4.84126984]
```

**How the result changed and why:** The solution for the first measurement set changed from [5, 5, 5] to about [3.254, 4.524, 4.841]. A larger diagonal entry means the first unknown contributes more to equation 1, so a smaller value is needed to produce the same measurement; the change then spreads to the other unknowns through the off-diagonal coupling. The residual norm stayed near 1e-15, so the LU solution is still accurate.

## 4. Meaning of the output

For the first measurement set the exact solution is [5, 5, 5] (check: 4(5) - 5 = 15, -5 + 20 - 5 = 10, -5 + 15 = 10). The other two sets give different solutions with the same factorization. Residual norms are around 1e-15, which is round-off level, and the LU answer agrees with the direct solver. The factorization is the expensive step and is done once.

## 5. Modified real-world case: Solar mini-grid circuit solved for 24 hourly source voltages

### Assumptions and input data

- Three-loop resistor network analysed by mesh analysis: R x I = V, where R is fixed and V changes each hour.
- The source voltages follow sunlight: zero at night and highest at noon (12 V, 6 V and 9 V in the three loops at noon).
- A larger 400-loop network with 300 source vectors is timed to show when LU reuse pays off.

### Program (`code/Task_07_modified.py`)

```python
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
```

### Output

```text
Hour 12 (noon) loop currents (A): [1.5455 1.7273 1.5758]
Hour 3  (night) loop currents (A): [0. 0. 0.]
Maximum residual over 24 hours: 2.6645352591003757e-15
400x400 system, 300 source vectors:
  np.linalg.solve each time : 0.457 s
  LU factor once + reuse    : 0.012 s  (factor 0.002 s + 300 solves 0.010 s)
  Speed-up                  : 38.2x
```

### Interpretation

At noon the loop currents are about 1.55 A, 1.73 A and 1.58 A; at night all currents are zero because there is no source voltage. The largest residual over 24 hours is about 3e-15, so every hourly solution is accurate. In the large 400x400 timing test, factoring once and reusing the factors was dozens of times faster than calling `np.linalg.solve` for every vector (timing varies per machine). With a tiny 3x3 matrix the difference is not noticeable; LU reuse matters when the matrix is big and is reused many times.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
