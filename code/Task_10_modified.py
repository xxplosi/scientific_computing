"""Task 10 (modified): Break-even point of a phone-repair shop using bisection.
Assumption (KES per month): revenue = 1,500 per repair.
Cost = 60,000 fixed + 400 per repair + 0.8*n^1.5 (extra staff/overtime cost grows with volume).
Break-even is where profit(n) = revenue - cost = 0."""
import numpy as np
import matplotlib.pyplot as plt

def profit(n):
    revenue = 1500 * n
    cost = 60000 + 400 * n + 0.8 * n**1.5
    return revenue - cost

def bisection(f, a, b, tol=1e-6):
    assert f(a) * f(b) < 0, "Need a sign change"
    steps = 0
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(a) * f(m) <= 0: b = m
        else: a = m
        steps += 1
    return (a + b) / 2, steps

n_star, steps = bisection(profit, 10, 500)
print(f"Break-even repairs per month: {n_star:.3f}  (found in {steps} bisection steps)")
print(f"Round up to whole repairs: {int(np.ceil(n_star))}")
print(f"Profit at break-even: {profit(n_star):.6f} KES")
print(f"Profit at 200 repairs: {profit(200):,.0f} KES")

n = np.linspace(10, 500, 300)
plt.plot(n, profit(n)); plt.axhline(0, linewidth=0.8); plt.axvline(n_star, linestyle="--")
plt.xlabel("Repairs per month"); plt.ylabel("Profit (KES)")
plt.title("Break-even point of a repair shop"); plt.grid(True); plt.show()
