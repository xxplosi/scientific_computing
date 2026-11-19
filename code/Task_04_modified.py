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
