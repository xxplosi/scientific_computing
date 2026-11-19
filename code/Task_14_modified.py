"""Task 14 (modified): Growth curve of weekly app sign-ups.
Assumption: 10 weeks of synthetic sign-up counts that grow roughly exponentially.
Fit y = a*exp(b*week) and use it to forecast week 12."""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

weeks = np.arange(1, 11, dtype=float)
signups = np.array([52, 61, 70, 86, 99, 121, 140, 171, 199, 238], dtype=float)

def model(x, a, b):
    return a * np.exp(b * x)

(a, b), cov = curve_fit(model, weeks, signups, p0=[50, 0.1])
pred = model(weeks, a, b)
rmse = np.sqrt(np.mean((signups - pred) ** 2))
ss_res = np.sum((signups - pred) ** 2)
ss_tot = np.sum((signups - signups.mean()) ** 2)

print(f"Fitted model: y = {a:.2f} * exp({b:.4f} * week)")
print(f"Weekly growth rate: {np.exp(b)-1:.2%}   | doubling time: {np.log(2)/b:.2f} weeks")
print(f"RMSE: {rmse:.2f} sign-ups | R^2: {1 - ss_res/ss_tot:.4f}")
print(f"Forecast for week 12: {model(12, a, b):.0f} sign-ups")

x = np.linspace(1, 12, 200)
plt.scatter(weeks, signups, label="Observed"); plt.plot(x, model(x, a, b), label="Exponential fit")
plt.xlabel("Week"); plt.ylabel("Sign-ups"); plt.title("Growth of weekly sign-ups")
plt.legend(); plt.grid(True); plt.show()
