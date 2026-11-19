# Task 12: Polynomial and Nonlinear Equation Solving

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_12_nonlinear_equations.py` (given program), `code/Task_12_nonlinear_equations_param_change.py` (changed parameter), `code/Task_12_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** the circle x^2 + y^2 = 4, the parabola y = x^2 - 1, and two starting guesses [1, 1] and [-1, 1].
- **Mathematical operation:** write both equations as residuals that should equal zero and let `scipy.optimize.root` adjust (x, y) until both residuals are close to zero.

## 2. Original program and output

Run with `python code/Task_12_nonlinear_equations.py`.

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

## 3. Changing a parameter

**What I changed:** Enlarged the circle from radius 2 to radius 3 (x^2 + y^2 = 9).

```python
x**2 + y**2 - 9,   # was - 4
```

**Output after the change** (`code/Task_12_nonlinear_equations_param_change.py`):

```text
Initial guess: [1.0, 1.0]
Intersection: [1.83637723 2.37228132]
Residuals: [np.float64(-1.3891110484109959e-12), np.float64(1.4597212327771558e-12)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.83637723  2.37228132]
Residuals: [np.float64(-1.3855583347321954e-12), np.float64(1.4601653219870059e-12)]
Converged: True
```

**How the result changed and why:** The intersection points moved from (1.517, 1.303) and (-1.517, 1.303) to (1.836, 2.372) and (-1.836, 2.372). A larger circle meets the parabola further out and higher up. The residuals remained about 1e-12 and both solves converged.

## 4. Meaning of the output

The solver found two intersection points, (1.51749, 1.30278) and (-1.51749, 1.30278). They are mirror images because both curves are symmetric about the y-axis. Residuals of about 1e-13 show both equations are satisfied. Algebra confirms it: substituting x^2 = y + 1 gives y^2 + y - 3 = 0, so y = (-1 + sqrt(13))/2 = 1.3028; the other root y = -2.303 would need x^2 negative, so there is no real intersection there.

## 5. Modified real-world case: Handover points between two cell-tower coverage areas

### Assumptions and input data

- Tower 1 at (0, 0) with a coverage radius of 5 km; Tower 2 at (6, 2) with a radius of 4 km (assumed positions).
- The boundaries meet where both circle equations hold at once. Three different starting guesses are tried.

### Program (`code/Task_12_modified.py`)

```python
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
```

### Output

```text
Guess: [3.0, 4.0] -> [2.67531 4.22406] | residual norm: 3.55e-15 | converged: True
Guess: [5.0, -1.0] -> [ 4.67469 -1.77406] | residual norm: 1.78e-15 | converged: True
Guess: [0.0, 0.0] -> [2.67531 4.22406] | residual norm: 3.52e-14 | converged: True

Distinct handover points (km):
   [2.6753 4.2241] distance to tower 1: 5.0 | to tower 2: 4.0
   [ 4.6747 -1.7741] distance to tower 1: 5.0 | to tower 2: 4.0
```

### Interpretation

The two coverage circles meet at (2.675, 4.224) and (4.675, -1.774) km. The check shows each point is 5.0 km from Tower 1 and 4.0 km from Tower 2, so both equations hold. Different starting guesses found different solutions ([3, 4] and [0, 0] reach the first, [5, -1] reaches the second), which shows that a nonlinear system can have several solutions and the initial guess decides which one is found.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
