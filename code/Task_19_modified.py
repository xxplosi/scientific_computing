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
