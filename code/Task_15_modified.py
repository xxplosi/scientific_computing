"""Task 15 (modified): Acceleration of a bus from speed readings.
Assumption: speed (m/s) logged every 2 seconds while a bus leaves a stop and cruises.
Estimate acceleration with forward/central/backward differences and np.gradient."""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 22, 2, dtype=float)
v = np.array([0.0, 2.1, 4.6, 7.4, 9.9, 11.8, 13.0, 13.7, 14.0, 14.1, 14.1])

acc = np.zeros_like(v)
acc[0] = (v[1] - v[0]) / (t[1] - t[0])
acc[1:-1] = (v[2:] - v[:-2]) / (t[2:] - t[:-2])
acc[-1] = (v[-1] - v[-2]) / (t[-1] - t[-2])

check = np.gradient(v, t)
print("t (s) | speed (m/s) | acceleration (m/s^2)")
for ti, vi, ai in zip(t, v, acc):
    print(f"{ti:4.0f}  | {vi:6.1f}     | {ai:6.3f}")
print("Max difference vs np.gradient:", np.max(np.abs(acc - check)))
print(f"Peak acceleration: {acc.max():.3f} m/s^2 at t = {t[acc.argmax()]:.0f} s")

plt.plot(t, acc, marker="o")
plt.xlabel("Time (s)"); plt.ylabel("Acceleration (m/s^2)")
plt.title("Bus acceleration from speed readings"); plt.grid(True); plt.show()
