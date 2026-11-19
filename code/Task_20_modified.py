"""Task 20 (modified): Will a delivery take longer than 45 minutes?
Assumption (synthetic): waiting for pickup ~ Exponential(mean 8 min); riding time
~ Normal(mean 20, sd 5); handover ~ Uniform(2, 6) minutes. Simulate 200,000 deliveries."""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
N = 200_000
wait = rng.exponential(8.0, N)
ride = np.clip(rng.normal(20.0, 5.0, N), 0, None)
handover = rng.uniform(2.0, 6.0, N)
total = wait + ride + handover

late = total > 45
p = late.mean()
se = np.sqrt(p * (1 - p) / N)

print(f"Mean delivery time: {total.mean():.2f} min | median: {np.median(total):.2f} min")
print(f"90th percentile: {np.percentile(total, 90):.2f} min")
print(f"P(delivery > 45 min): {p:.4%}  (standard error about {se:.4%})")
print(f"Late deliveries: {late.sum()} of {N}")

plt.hist(total, bins=80, density=True)
plt.axvline(45, color="r", linestyle="--", label="45-minute limit")
plt.xlabel("Total delivery time (min)"); plt.ylabel("Density")
plt.title("Monte Carlo simulation of delivery times"); plt.legend(); plt.grid(True); plt.show()
