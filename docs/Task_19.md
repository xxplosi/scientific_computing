# Task 19: Numerical Optimization

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_19_optimization.py` (given program), `code/Task_19_optimization_param_change.py` (changed parameter), `code/Task_19_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** cost per unit A = 12 and B = 18; capacity per unit A = 100 and B = 170; required capacity at least 1000; non-negative amounts; start point [5, 3].
- **Mathematical operation:** minimise the cost 12x + 18y subject to 100x + 170y >= 1000 and x, y >= 0 using SLSQP; then search whole-server combinations.

## 2. Original program and output

Run with `python code/Task_19_optimization.py`.

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

## 3. Changing a parameter

**What I changed:** Reduced the cost of Type A from 12 to 8 (in both the objective and the integer search).

```python
return 8*x + 18*y      # was 12*x + 18*y
total_cost = 8*a + 18*b  # was 12*a + 18*b
```

**Output after the change** (`code/Task_19_optimization_param_change.py`):

```text
Optimization success: True
Type A allocation: 10.000
Type B allocation: 0.000
Total capacity: 1000.00
Minimum planning cost: 80.00
Best nearby integer solution: (80, 10, 0, 1000)
```

**How the result changed and why:** The optimal choice flipped from 5.882 units of Type B (cost 105.88) to 10 units of Type A and none of B (cost 80). Cost per unit of capacity is 18/170 = 0.106 for B and 12/100 = 0.120 for A originally, so B was cheaper; with A at 8 it becomes 8/100 = 0.080, so A wins. The whole-server answer also became exactly 10 A servers (cost 80) with no rounding loss.

## 4. Meaning of the output

The optimiser puts everything on Type B: 5.882 units giving exactly the required capacity of 1000 at a cost of 105.88, because B has the lower cost per unit of capacity. The constraint is tight (capacity equals the minimum). If whole servers are required, the best option is 6 Type B servers: capacity 1020 and cost 108, a little more expensive than the continuous result because you cannot buy 0.882 of a server.

## 5. Modified real-world case: Cheapest fertilizer mix for one acre (hypothetical prices)

### Assumptions and input data

- Fertilizer 1 (CAN-like): KES 3,500 per 50 kg bag, 26% nitrogen. Fertilizer 2 (DAP-like): KES 6,000 per 50 kg bag, 18% nitrogen and 46% P2O5. Prices and nutrient shares are assumptions for the exercise, not market data.
- The crop needs at least 20 kg of nitrogen and 9 kg of P2O5. Minimise the cost. Results from SLSQP are cross-checked with `linprog`.

### Program (`code/Task_19_modified.py`)

```python
"""Task 19 (modified): Cheapest fertilizer mix for one acre (hypothetical prices).
Assumption: Fertilizer 1 (CAN-like) costs KES 3,500 per 50 kg bag with 26% N.
Fertilizer 2 (DAP-like) costs KES 6,000 per 50 kg bag with 18% N and 46% P2O5.
The crop needs at least 20 kg N and 9 kg P2O5. Minimise cost (bags can be fractional)."""
import numpy as np
from scipy.optimize import minimize, linprog

cost_bag = np.array([3500.0, 6000.0])
scale = 1000.0   # work in thousands of KES so the solver is well scaled
N_kg = np.array([50 * 0.26, 50 * 0.18])
P_kg = np.array([0.0, 50 * 0.46])

res = minimize(lambda z: cost_bag @ z / scale, x0=[1.5, 0.5], method="SLSQP",
               bounds=[(0, None), (0, None)],
               constraints=[{"type": "ineq", "fun": lambda z: N_kg @ z - 20.0},
                            {"type": "ineq", "fun": lambda z: P_kg @ z - 9.0}])

print("SLSQP success:", res.success)
print(f"Bags of fertilizer 1: {res.x[0]:.3f} | Bags of fertilizer 2: {res.x[1]:.3f}")
print(f"N supplied: {N_kg @ res.x:.2f} kg | P2O5 supplied: {P_kg @ res.x:.2f} kg")
print(f"Minimum cost: KES {res.fun*scale:,.2f}")

lp = linprog(cost_bag, A_ub=-np.vstack([N_kg, P_kg]), b_ub=-np.array([20.0, 9.0]), bounds=[(0, None)] * 2)
print(f"Cross-check with linprog: bags = {np.round(lp.x, 3)}, cost = KES {lp.fun:,.2f}")

best = None
for a in range(0, 8):
    for b in range(0, 8):
        if N_kg @ [a, b] >= 20 and P_kg @ [a, b] >= 9:
            c = cost_bag @ [a, b]
            if best is None or c < best[0]:
                best = (float(c), a, b)
print("Best whole-bag combination (cost, bags1, bags2):", best)
```

### Output

```text
SLSQP success: True
Bags of fertilizer 1: 1.268 | Bags of fertilizer 2: 0.391
N supplied: 20.00 kg | P2O5 supplied: 9.00 kg
Minimum cost: KES 6,784.28
Cross-check with linprog: bags = [1.268 0.391], cost = KES 6,784.28
Best whole-bag combination (cost, bags1, bags2): (9500.0, 1, 1)
```

### Interpretation

The cheapest mix is 1.268 bags of fertilizer 1 and 0.391 bags of fertilizer 2, giving exactly 20 kg of N and 9 kg of P2O5 at a cost of KES 6,784.28. Both nutrient constraints are tight (met exactly), and `linprog` gives the same answer, which confirms the SLSQP result. If only whole bags can be bought, the best choice is 1 bag of each at KES 9,500, which costs more than the continuous optimum because of rounding.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
