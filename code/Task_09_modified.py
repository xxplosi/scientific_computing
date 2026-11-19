"""Task 9 (modified): Which device matters most in a campus network?
Assumption (invented topology): 6 nodes. Library(L), Lab(B), Admin(A), Hostel(H),
Cafeteria(C), Gate(G). Links are undirected. Eigenvector centrality ranks nodes."""
import numpy as np

nodes = ["Library", "Lab", "Admin", "Hostel", "Cafeteria", "Gate"]
edges = [(0,1),(0,2),(0,3),(1,2),(1,4),(2,3),(2,5),(3,4)]

A = np.zeros((6, 6))
for i, j in edges:
    A[i, j] = A[j, i] = 1

vals, vecs = np.linalg.eigh(A)          # symmetric matrix -> real eigenvalues
lam = vals[-1]
v = np.abs(vecs[:, -1])
score = v / v.sum()

print("Degree of each node:", A.sum(axis=1).astype(int).tolist())
print(f"Dominant eigenvalue: {lam:.4f}")
for name, s in sorted(zip(nodes, score), key=lambda t: -t[1]):
    print(f"{name:10s} {s:.4f}")
print("Verification error:", np.linalg.norm(A @ vecs[:, -1] - lam * vecs[:, -1]))
