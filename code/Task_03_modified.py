"""Task 3 (modified): Ride/delivery fare calculation for 500,000 trips.
Assumption: fare = base fee + per-km rate * distance + per-minute rate * time (KES),
distances and times are random (synthetic). Compare a Python loop with NumPy."""
import numpy as np
import timeit

rng = np.random.default_rng(7)
n = 500_000
distance_km = rng.uniform(0.5, 25, n)
minutes = rng.uniform(3, 70, n)

BASE, PER_KM, PER_MIN = 100.0, 35.0, 4.0   # KES

def loop_version():
    fares = []
    for d, m in zip(distance_km, minutes):
        fares.append(BASE + PER_KM * d + PER_MIN * m)
    return fares

def vector_version():
    return BASE + PER_KM * distance_km + PER_MIN * minutes

loop_t = timeit.timeit(loop_version, number=1)
vec_t = timeit.timeit(vector_version, number=5) / 5
fares = vector_version()

print(f"Trips: {n:,}")
print(f"Average fare: KES {fares.mean():.2f} | Min: {fares.min():.2f} | Max: {fares.max():.2f}")
print(f"Total revenue: KES {fares.sum():,.0f}")
print(f"Loop: {loop_t:.4f} s | Vectorized: {vec_t:.5f} s | Speed-up: {loop_t/vec_t:.0f}x")
