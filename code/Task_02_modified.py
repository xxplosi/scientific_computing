"""Task 2 (modified): Greenhouse temperature monitoring for tomato farming.
Assumption: 24 hourly sensor readings (synthetic) from an IoT sensor in a greenhouse.
Tomatoes grow best between 18 C and 30 C, so hours outside that band are flagged."""
import numpy as np

greenhouse_c = np.array([
    17.2, 16.8, 16.5, 16.4, 16.9, 18.3,
    21.0, 24.5, 27.8, 30.6, 32.4, 33.8,
    34.5, 34.1, 33.0, 31.2, 28.9, 26.1,
    23.7, 21.8, 20.4, 19.2, 18.4, 17.6
])

LOW, HIGH = 18.0, 30.0

mean_t, min_t, max_t = greenhouse_c.mean(), greenhouse_c.min(), greenhouse_c.max()
too_hot = greenhouse_c > HIGH          # boolean mask, no loop
too_cold = greenhouse_c < LOW
hours = np.arange(24)

print(f"Mean: {mean_t:.2f} C | Min: {min_t:.2f} C | Max: {max_t:.2f} C")
print(f"Hours above {HIGH} C: {too_hot.sum()} -> hours {hours[too_hot].tolist()}")
print(f"Hours below {LOW} C: {too_cold.sum()} -> hours {hours[too_cold].tolist()}")
print(f"Hours inside the safe band: {(~too_hot & ~too_cold).sum()} of 24")
print(f"Peak temperature in Kelvin: {max_t + 273.15:.2f} K")
