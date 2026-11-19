"""Task 18 (modified): SIR epidemic model solved with solve_ivp.
Assumption: population 10,000, 10 initially infected, infection rate beta = 0.4/day,
recovery rate gamma = 0.1/day (so R0 = beta/gamma = 4). Simulate 120 days."""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

N, beta, gamma = 10_000.0, 0.4, 0.1

def sir(t, y):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]

sol = solve_ivp(sir, (0, 120), [N - 10, 10, 0], t_eval=np.linspace(0, 120, 481), rtol=1e-8, atol=1e-8)
S, I, R = sol.y
peak = I.argmax()

print("Solver success:", sol.success)
print(f"R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak infections: {I[peak]:.0f} people on day {sol.t[peak]:.1f}")
print(f"Total ever infected by day 120: {R[-1] + I[-1]:.0f} ({(R[-1]+I[-1])/N:.1%})")
print(f"Population conserved? S+I+R at end = {S[-1]+I[-1]+R[-1]:.4f}")

plt.plot(sol.t, S, label="Susceptible"); plt.plot(sol.t, I, label="Infected"); plt.plot(sol.t, R, label="Recovered")
plt.xlabel("Day"); plt.ylabel("People"); plt.title("SIR epidemic model")
plt.legend(); plt.grid(True); plt.show()
