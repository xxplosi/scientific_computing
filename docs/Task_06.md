# Task 6: Solution of Systems of Linear Equations

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_06_linear_systems.py` (given program), `code/Task_06_linear_systems_param_change.py` (changed parameter), `code/Task_06_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** coefficient matrix A = [[4, 2], [8, 12]] (CPU and memory per server type) and the observed totals b = [20, 72].
- **Mathematical operation:** solve A x = b for x = [number of Type A servers, number of Type B servers] with `np.linalg.solve`, then check the residual b - A x.

## 2. Original program and output

Run with `python code/Task_06_linear_systems.py`.

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## 3. Changing a parameter

**What I changed:** Changed the observed totals from [20, 72] to [32, 112].

```python
b = np.array([32.0, 112.0])   # was [20.0, 72.0]
```

**Output after the change** (`code/Task_06_linear_systems_param_change.py`):

```text
Type A servers: 5
Type B servers: 6
Verification A @ solution: [ 32. 112.]
Residual: [0. 0.]
Residual norm: 0.0
```

**How the result changed and why:** The solution changed from 3 Type A and 4 Type B servers to 5 Type A and 6 Type B servers. The matrix A did not change, so the answer depends linearly on b: more resource usage means more active servers. The residual remained 0, so the new solution fits both equations exactly.

## 4. Meaning of the output

The result is 3 Type A and 4 Type B servers. Check: 4(3) + 2(4) = 20 CPU units and 8(3) + 12(4) = 72 GB of memory, which match the totals. The residual is zero, so the solution is exact (up to round-off).

## 5. Modified real-world case: Job mix in a service marketplace

### Assumptions and input data

- Type A job: 2 hours of work and KES 1,500 payout. Type B job: 3 hours and KES 2,500.
- In one week the team logged 38 working hours and KES 30,000 of payouts. Find the number of jobs of each type.

### Program (`code/Task_06_modified.py`)

```python
"""Task 6 (modified): Service marketplace job mix.
Assumption: two job types. Type A takes 2 hours and pays KES 1,500;
Type B takes 3 hours and pays KES 2,500. In one week the team logged
38 working hours and KES 30,000 of payouts. How many jobs of each type?"""
import numpy as np

A = np.array([[2.0, 3.0],
              [1500.0, 2500.0]])
b = np.array([38.0, 30000.0])

jobs = np.linalg.solve(A, b)
residual = b - A @ jobs

print(f"Type A jobs: {jobs[0]:.2f}")
print(f"Type B jobs: {jobs[1]:.2f}")
print("Check A @ jobs:", A @ jobs)
print("Residual norm:", np.linalg.norm(residual))
print("Determinant of A:", round(np.linalg.det(A), 2))
print("Condition number:", round(np.linalg.cond(A), 2))
```

### Output

```text
Type A jobs: 10.00
Type B jobs: 6.00
Check A @ jobs: [   38. 30000.]
Residual norm: 0.0
Determinant of A: 500.0
Condition number: 17000.03
```

### Interpretation

The solution is 10 Type A jobs and 6 Type B jobs (check: 2x10 + 3x6 = 38 hours and 1500x10 + 2500x6 = 30,000 KES). The determinant is 500, so the system has exactly one solution. The condition number is about 17,000, which is large partly because the two rows are on very different scales (hours versus shillings); it warns that small errors in the recorded payouts could change the answer noticeably.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
