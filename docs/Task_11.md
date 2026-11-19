# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_11_newton_secant.py` (given program), `code/Task_11_newton_secant_param_change.py` (changed parameter), `code/Task_11_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** the cash flows [-10,000, 3,000, 3,500, 4,000, 2,500] (initial investment then four yearly inflows). Newton starts at 10% with a derivative; Secant starts at 5% and 20%.
- **Mathematical operation:** find the rate r where net present value NPV(r) = sum of CF_t / (1 + r)^t equals zero. This rate is the internal rate of return (IRR).

## 2. Original program and output

Run with `python code/Task_11_newton_secant.py`.

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
```

## 3. Changing a parameter

**What I changed:** Reduced the inflows to [2,500, 3,000, 3,500, 3,000] (smaller and later cash).

```python
cash_flows = [-10000, 2500, 3000, 3500, 3000]   # was [-10000, 3000, 3500, 4000, 2500]
```

**Output after the change** (`code/Task_11_newton_secant_param_change.py`):

```text
IRR using Newton-Raphson: 7.436935%
IRR using Secant method: 7.436935%
NPV at Newton solution: 0.000000
```

**How the result changed and why:** The IRR fell from 11.542% to 7.437%. With a smaller total return, the discount rate that makes the investment break even is lower. Both methods still agreed and the NPV at the solution is 0.

## 4. Meaning of the output

Newton-Raphson and Secant both find an IRR of 11.542461%. This means the investment earns about 11.54% per year on the money tied up; if the investor's required return is below that, the project is worth doing. The NPV at the solution is 0.000000, which confirms the root.

## 5. Modified real-world case: True interest rate of a loan

### Assumptions and input data

- Borrow KES 100,000 and repay KES 9,500 per month for 12 months (illustrative figures).
- Find the monthly rate r such that 100,000 = present value of the 12 repayments. Newton, Secant and Bisection are compared.

### Program (`code/Task_11_modified.py`)

```python
"""Task 11 (modified): True monthly interest rate of a loan using Newton and Secant.
Assumption: borrow KES 100,000 and repay KES 9,500 per month for 12 months.
Find the monthly rate r where borrowed amount = present value of repayments."""
from scipy.optimize import root_scalar

P, pmt, n = 100_000.0, 9_500.0, 12

def f(r):
    return P - pmt * (1 - (1 + r) ** (-n)) / r

def df(r):
    h = 1e-8
    return (f(r + h) - f(r - h)) / (2 * h)

newton = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.005, x1=0.04, method="secant", xtol=1e-12)
bis = root_scalar(f, bracket=[0.0001, 0.2], method="bisect", xtol=1e-12)

r = newton.root
print(f"Monthly rate (Newton): {r:.6%}  in {newton.iterations} iterations")
print(f"Monthly rate (Secant): {secant.root:.6%}  in {secant.iterations} iterations")
print(f"Monthly rate (Bisect): {bis.root:.6%}  in {bis.iterations} iterations")
print(f"Annual nominal rate (12 x monthly): {12*r:.4%}")
print(f"Effective annual rate: {(1+r)**12 - 1:.4%}")
print(f"Total repaid: KES {pmt*n:,.0f}  -> interest paid: KES {pmt*n - P:,.0f}")
```

### Output

```text
Monthly rate (Newton): 2.075742%  in 4 iterations
Monthly rate (Secant): 2.075742%  in 6 iterations
Monthly rate (Bisect): 2.075742%  in 38 iterations
Annual nominal rate (12 x monthly): 24.9089%
Effective annual rate: 27.9589%
Total repaid: KES 114,000  -> interest paid: KES 14,000
```

### Interpretation

The monthly rate is 2.0757%, which is an annual nominal rate of 24.91% and an effective annual rate of 27.96%. Newton needed 4 iterations, Secant 6 and Bisection 38, so the derivative-based methods converge much faster. The total interest is KES 14,000 (14% of the principal), but the real rate is about 28% a year because the borrower repays part of the principal every month and so holds less money later. Checking the effective rate is how a borrower sees the real cost of a loan.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
