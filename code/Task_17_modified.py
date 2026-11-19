"""Task 17 (modified): Logistic population growth solved with Euler's method.
Assumption: a user community grows dP/dt = r*P*(1 - P/K) with r = 0.5 per month,
carrying capacity K = 10,000 users and P(0) = 200. Compare three step sizes."""
import numpy as np
import matplotlib.pyplot as plt

r, K, P0, T = 0.5, 10_000.0, 200.0, 24.0

def euler(h):
    t = np.arange(0, T + h, h)
    P = np.zeros_like(t); P[0] = P0
    for i in range(len(t) - 1):
        P[i + 1] = P[i] + h * r * P[i] * (1 - P[i] / K)
    return t, P

exact = lambda t: K / (1 + (K / P0 - 1) * np.exp(-r * t))

for h in (4.0, 1.0, 0.25):
    t, P = euler(h)
    print(f"h = {h:<5}: P(24) = {P[-1]:9.2f} | exact = {exact(24):9.2f} | max error = {np.max(np.abs(P-exact(t))):8.2f}")

tt = np.linspace(0, T, 300)
plt.plot(tt, exact(tt), "k", label="Exact")
for h in (4.0, 1.0, 0.25):
    t, P = euler(h); plt.plot(t, P, marker="o", markersize=3, label=f"Euler h={h}")
plt.xlabel("Months"); plt.ylabel("Users"); plt.title("Logistic growth with Euler's method")
plt.legend(); plt.grid(True); plt.show()
