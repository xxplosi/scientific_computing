# Task 16: Numerical Integration

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_16_numerical_integration.py` (given program), `code/Task_16_numerical_integration_param_change.py` (changed parameter), `code/Task_16_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** smart-meter power readings (kW) every two hours from 0 to 12 hours: [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9].
- **Mathematical operation:** energy = integral of power over time, estimated with the trapezoidal rule and with Simpson's rule.

## 2. Original program and output

Run with `python code/Task_16_numerical_integration.py`.

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

## 3. Changing a parameter

**What I changed:** Raised the peak reading at hour 6 from 1.8 kW to 3.0 kW.

```python
power_kw = np.array([0.8, 1.0, 1.4, 3.0, 1.6, 1.2, 0.9])   # peak was 1.8
```

**Output after the change** (`code/Task_16_numerical_integration_param_change.py`):

```text
Energy using trapezoidal rule: 18.100 kWh
Energy using Simpson's rule: 19.000 kWh
Difference between estimates: 0.900 kWh
```

**How the result changed and why:** The trapezoidal estimate rose from 15.700 to 18.100 kWh and Simpson's from 15.800 to 19.000 kWh, so the difference between the two grew from 0.100 to 0.900 kWh. A sharper peak means more curvature; the trapezoidal rule cuts straight across the top, while Simpson's rule follows the curve with parabolas, so the two methods disagree more.

## 4. Meaning of the output

About 15.7 to 15.8 kWh of energy is used in the 12 hours. The trapezoidal rule joins readings with straight lines (check: 2 x (0.4 + 1.0 + 1.4 + 1.8 + 1.6 + 1.2 + 0.45) = 15.7). Simpson's rule fits parabolas through groups of three points and gives a slightly higher value, 15.8 kWh. The difference is only 0.1 kWh, so with smooth data both methods agree well.

## 5. Modified real-world case: Total water volume from a river-flow sensor

### Assumptions and input data

- Flow rate (m^3/s) logged every 3 hours for 24 hours (9 readings, synthetic data), with a rise to 9.8 m^3/s at 12:00.
- Volume = integral of the flow rate over time, with time converted to seconds.

### Program (`code/Task_16_modified.py`)

```python
"""Task 16 (modified): Total water volume from a river-flow sensor.
Assumption: flow rate (m^3/s) recorded every 3 hours for a day (9 readings, synthetic).
Volume = integral of flow rate over time. Compare trapezoid and Simpson."""
import numpy as np
from scipy.integrate import simpson

t_hours = np.arange(0, 25, 3, dtype=float)
flow = np.array([4.0, 3.6, 3.9, 6.5, 9.8, 8.2, 5.6, 4.5, 4.1])   # m^3/s

t_sec = t_hours * 3600
vol_trap = np.trapezoid(flow, t_sec)
vol_simp = simpson(flow, x=t_sec)

print(f"Volume (trapezoid): {vol_trap:,.0f} m^3  = {vol_trap/1e6:.3f} million m^3")
print(f"Volume (Simpson)  : {vol_simp:,.0f} m^3  = {vol_simp/1e6:.3f} million m^3")
print(f"Difference        : {abs(vol_simp-vol_trap):,.0f} m^3 ({abs(vol_simp-vol_trap)/vol_simp:.2%})")
print(f"Average flow over the day: {vol_simp/86400:.3f} m^3/s")
```

### Output

```text
Volume (trapezoid): 498,420 m^3  = 0.498 million m^3
Volume (Simpson)  : 496,440 m^3  = 0.496 million m^3
Difference        : 1,980 m^3 (0.40%)
Average flow over the day: 5.746 m^3/s
```

### Interpretation

The volume is about 498,420 m^3 (trapezoid) or 496,440 m^3 (Simpson), roughly half a million cubic metres in the day. The two methods differ by 1,980 m^3 (0.4%). The average flow is 5.746 m^3/s. Because readings are only every 3 hours, a short flood peak between readings could be missed, so the sampling interval limits the accuracy of any integration method.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
