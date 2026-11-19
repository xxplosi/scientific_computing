# Task 2: NumPy Arrays and Numerical Computation

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_02_numpy_arrays.py` (given program), `code/Task_02_numpy_arrays_param_change.py` (changed parameter), `code/Task_02_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** one NumPy array `temperatures_c` holding 24 hourly temperature readings in degrees Celsius (from 18.5 C at hour 0 to 19.0 C at hour 23).
- **Mathematical operations:** mean = (sum of all readings) / 24; minimum; maximum; and the element-wise conversion F = 1.8 x C + 32 applied to the whole array at once (vectorized, no loop).

## 2. Original program and output

Run with `python code/Task_02_numpy_arrays.py`.

```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

## 3. Changing a parameter

**What I changed:** Added 5 C to every reading (a hotter day) with `temperatures_c = temperatures_c + 5`.

```python
temperatures_c = temperatures_c + 5   # CHANGE: every reading is 5 C hotter
```

**Output after the change** (`code/Task_02_numpy_arrays_param_change.py`):

```text
Daily mean temperature: 28.12 C
Minimum temperature: 22.50 C
Maximum temperature: 34.40 C
First six Fahrenheit readings: [74.3  73.4  73.04 72.5  73.22 75.2 ]
```

**How the result changed and why:** The mean, minimum and maximum each moved up by exactly 5 C (23.12 to 28.12, 17.50 to 22.50, 29.40 to 34.40), and the first Fahrenheit reading rose from 65.3 F to 74.3 F, which is 5 x 1.8 = 9 F. The spread (max minus min) stayed 11.90 C. So adding a constant shifts the location statistics but does not change how spread out the readings are.

## 4. Meaning of the output

The day is mild: the average temperature is 23.12 C, the coolest reading (17.50 C) occurs in the early morning and the warmest (29.40 C) around midday/early afternoon. The Fahrenheit array shows the same pattern on a different scale (the first six readings are about 64 to 66 F). NumPy let us compute all of this with single expressions instead of writing loops over 24 values.

## 5. Modified real-world case: Greenhouse temperature monitoring for tomatoes

### Assumptions and input data

- 24 hourly readings from an IoT temperature sensor in a greenhouse (synthetic data created for this exercise).
- Tomatoes are assumed to grow best between 18 C and 30 C, so readings outside that band are flagged.
- Boolean masks (`greenhouse_c > 30`) replace loops for counting and locating the bad hours.

### Program (`code/Task_02_modified.py`)

```python
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
```

### Output

```text
Mean: 24.21 C | Min: 16.40 C | Max: 34.50 C
Hours above 30.0 C: 7 -> hours [9, 10, 11, 12, 13, 14, 15]
Hours below 18.0 C: 6 -> hours [0, 1, 2, 3, 4, 23]
Hours inside the safe band: 11 of 24
Peak temperature in Kelvin: 307.65 K
```

### Interpretation

The mean is 24.21 C, but the day swings from 16.40 C to 34.50 C. Seven hours (hours 9 to 15) are above 30 C and six hours (0 to 4 and 23) are below 18 C, so only 11 of 24 hours are inside the safe band. In practice the farmer would need ventilation or shade around midday and some heating or covering at night. The mean alone (24.21 C) would have hidden this problem, which is why the min, max and the masks matter.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
