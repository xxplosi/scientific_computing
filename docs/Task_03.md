# Task 3: Mathematical Functions and Vectorization

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_03_vectorization.py` (given program), `code/Task_03_vectorization_param_change.py` (changed parameter), `code/Task_03_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** 1,000,000 simulated network latency values in milliseconds, drawn uniformly between 5 and 250 using a random generator with seed 42.
- **Mathematical operations:** convert ms to seconds (divide by 1000) and square each value. This is done two ways: a Python `for` loop and one vectorized NumPy expression. `timeit` measures how long each takes.

## 2. Original program and output

Run with `python code/Task_03_vectorization.py`.

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1329 s
Vectorized time: 0.0037 s
Approximate speed-up: 36.0x
```

## 3. Changing a parameter

**What I changed:** Reduced the number of measurements from 1,000,000 to 10,000 (`rng.uniform(5, 250, 10_000)`).

```python
latency_ms = rng.uniform(5, 250, 10_000)   # was 1_000_000
```

**Output after the change** (`code/Task_03_vectorization_param_change.py`):

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.0012 s
Vectorized time: 0.0000 s
Approximate speed-up: 51.2x
```

**How the result changed and why:** The loop time fell from 0.1329 s to 0.0012 s, roughly 100 times less, because there are 100 times fewer values. The vectorized time became too small to display (0.0000 s), so the printed speed-up (51.2x) is not reliable: the timer cannot measure such tiny durations accurately. The first five squared values are unchanged because the same seed produces the same first values. Lesson: vectorization benefits grow with data size, and speed-up figures should be measured on large inputs.

## 4. Meaning of the output

Both methods produce identical results, but the vectorized version ran about 36 times faster on one million values (0.0037 s versus 0.1329 s). NumPy performs the loop inside compiled C code instead of executing Python bytecode for every element. Exact timings differ between computers and between runs; the important point is the order-of-magnitude gap.

## 5. Modified real-world case: Fare calculation for 500,000 ride or delivery trips

### Assumptions and input data

- Fare = KES 100 base + KES 35 per km + KES 4 per minute.
- 500,000 trips with random distances (0.5 to 25 km) and durations (3 to 70 minutes), synthetic data with seed 7.
- Compare a Python loop with a vectorized expression.

### Program (`code/Task_03_modified.py`)

```python
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
```

### Output

```text
Trips: 500,000
Average fare: KES 692.13 | Min: 131.14 | Max: 1254.65
Total revenue: KES 346,067,098
Loop: 0.1038 s | Vectorized: 0.00273 s | Speed-up: 38x
```

### Interpretation

The average fare is KES 692.13, close to the hand estimate 100 + 35 x 12.75 + 4 x 36.5 = KES 692.25, which confirms the calculation. Total revenue is about KES 346 million for the 500,000 trips. The vectorized version was about 38 times faster than the loop, so for a system that prices millions of trips, vectorization keeps processing time small.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
