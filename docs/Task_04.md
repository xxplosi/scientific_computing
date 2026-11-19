# Task 4: Floating-Point Arithmetic and Numerical Errors

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_04_numerical_errors.py` (given program), `code/Task_04_numerical_errors_param_change.py` (changed parameter), `code/Task_04_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** the numbers 0.1, 0.2 and 0.3; the true value sqrt(2) versus the approximation 1.414; and small values x = 1e-4, 1e-8, 1e-12.
- **Mathematical operations:** exact equality versus tolerance comparison (`np.isclose`); absolute error = |true - approx|; relative error = absolute error / |true|; and two algebraically equal formulas for (sqrt(1+x) - 1)/x.

## 2. Original program and output

Run with `python code/Task_04_numerical_errors.py`.

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## 3. Changing a parameter

**What I changed:** Changed the approximation from 1.414 to 1.4142 and added an extra test value x = 1e-15.

```python
approx_value = 1.4142            # was 1.414
for x in [1e-4, 1e-8, 1e-12, 1e-15]:   # 1e-15 added
```

**Output after the change** (`code/Task_04_numerical_errors_param_change.py`):

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00001356
Relative error: 0.00095900%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
x=1e-15: direct=0.444089209850, stable=0.500000000000
```

**How the result changed and why:** A better approximation of sqrt(2) cut the absolute error from 0.00021356 to 0.00001356 (about 16 times smaller) and the relative error from 0.0151% to 0.00096%. For the unstable formula, the new value x = 1e-15 gave 0.444089 instead of the correct 0.5, an error of more than 11%, while the stable formula still returned 0.500000000000. So more digits in an approximation reduce truncation error, but a badly arranged formula can destroy accuracy even with exact inputs.

## 4. Meaning of the output

0.1 + 0.2 is stored as 0.30000000000000004 because 0.1 and 0.2 cannot be represented exactly in binary, so the exact test `==` returns False while `np.isclose` returns True. The direct formula for small x subtracts two almost equal numbers (sqrt(1+x) and 1), which loses significant digits (catastrophic cancellation): at x = 1e-12 it gives 0.50004445 instead of 0.5. The algebraically equivalent stable form 1/(sqrt(1+x)+1) avoids the subtraction and stays accurate.

## 5. Modified real-world case: Accumulated rounding error when adding KES 0.10 one million times

### Assumptions and input data

- A banking system adds a deposit of KES 0.10, one million times. The exact total is KES 100,000.00.
- Compare repeated float addition, `math.fsum`, and exact `Decimal` arithmetic.

### Program (`code/Task_04_modified.py`)

```python
"""Task 4 (modified): Rounding error when a banking system adds 10 cents 1,000,000 times.
Assumption: each deposit is KES 0.10. The exact total is KES 100,000.00.
Compare plain float addition, math.fsum and exact decimal arithmetic."""
import math
from decimal import Decimal
import numpy as np

n = 1_000_000
deposit = 0.10

float_total = 0.0
for _ in range(n):
    float_total += deposit

fsum_total = math.fsum([deposit] * n)
decimal_total = Decimal("0.10") * n
exact = 100_000.0

print(f"Float loop total : {float_total:.10f}")
print(f"math.fsum total  : {fsum_total:.10f}")
print(f"Decimal total    : {decimal_total}")
print(f"Absolute error (float loop): {abs(float_total - exact):.6e}")
print(f"Relative error (float loop): {abs(float_total - exact)/exact:.6e}")
print("float_total == 100000.0 ?", float_total == exact)
print("np.isclose(float_total, 100000.0) ?", np.isclose(float_total, exact))
```

### Output

```text
Float loop total : 100000.0000013329
math.fsum total  : 100000.0000000000
Decimal total    : 100000.00
Absolute error (float loop): 1.332883e-06
Relative error (float loop): 1.332883e-11
float_total == 100000.0 ? False
np.isclose(float_total, 100000.0) ? True
```

### Interpretation

The float loop ends at 100000.0000013329, an absolute error of about 1.3e-6 and a relative error of 1.3e-11. That is tiny, but the exact comparison `total == 100000.0` is False while `np.isclose` is True. `math.fsum` and `Decimal` both give exactly 100000. For money, the safe practice is to use Decimal or whole cents (integers) and never test float totals with `==`.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
