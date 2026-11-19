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
