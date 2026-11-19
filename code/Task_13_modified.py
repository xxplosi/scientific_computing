"""Task 13 (modified): Estimating a missing solar-panel reading.
Assumption: hourly power output (kW) of a small solar panel, synthetic data.
The 13:00 reading is "lost"; we estimate it from the other hours and compare
with the true value (which we kept aside) to test the interpolation methods."""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16], dtype=float)
power = np.array([0.9, 1.7, 2.5, 3.1, 3.4, 3.3, 2.9, 2.2, 1.3])

missing_hour, true_value = 13.0, 3.3
keep = hours != missing_hour

linear = interp1d(hours[keep], power[keep])
cubic = CubicSpline(hours[keep], power[keep])

print(f"True 13:00 reading        : {true_value:.3f} kW")
print(f"Linear estimate           : {float(linear(13.0)):.3f} kW  (error {abs(float(linear(13.0))-true_value):.3f})")
print(f"Cubic-spline estimate     : {float(cubic(13.0)):.3f} kW  (error {abs(float(cubic(13.0))-true_value):.3f})")
print(f"Cubic estimate at 10:30   : {float(cubic(10.5)):.3f} kW")

t = np.linspace(8, 16, 200)
plt.scatter(hours[keep], power[keep], label="Measured")
plt.scatter([13], [true_value], marker="x", s=80, label="Lost reading (true)")
plt.plot(t, linear(t), label="Linear"); plt.plot(t, cubic(t), label="Cubic spline")
plt.xlabel("Hour of day"); plt.ylabel("Power (kW)")
plt.title("Recovering a missing solar reading"); plt.legend(); plt.grid(True); plt.show()
