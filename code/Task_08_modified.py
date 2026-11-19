"""Task 8 (modified): Temperature along a metal rod with 9 interior points.
Assumption: left end held at 150 C, right end at 30 C, steady state, equal spacing.
Compare Jacobi and Gauss-Seidel convergence for a bigger system."""
import numpy as np
import matplotlib.pyplot as plt

n = 9
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n); b[0] = 150.0; b[-1] = 30.0

def jacobi(A, b, tol=1e-6, max_iter=5000):
    D = np.diag(A); R = A - np.diagflat(D)
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        xn = (b - R @ x) / D
        e = np.linalg.norm(xn - x, np.inf); errs.append(e); x = xn
        if e < tol: break
    return x, errs

def gauss_seidel(A, b, tol=1e-6, max_iter=5000):
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        e = np.linalg.norm(x - old, np.inf); errs.append(e)
        if e < tol: break
    return x, errs

xj, ej = jacobi(A, b)
xg, eg = gauss_seidel(A, b)
exact = np.linalg.solve(A, b)

print("Exact temperatures:", np.round(exact, 3))
print(f"Jacobi iterations: {len(ej)}, max error vs exact: {np.max(np.abs(xj-exact)):.2e}")
print(f"Gauss-Seidel iterations: {len(eg)}, max error vs exact: {np.max(np.abs(xg-exact)):.2e}")

plt.semilogy(ej, label="Jacobi"); plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change")
plt.title("Rod temperature: convergence (9 points)")
plt.legend(); plt.grid(True); plt.show()
