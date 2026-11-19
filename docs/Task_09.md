# Task 9: Eigenvalues and Eigenvectors

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_09_eigenvalues.py` (given program), `code/Task_09_eigenvalues_param_change.py` (changed parameter), `code/Task_09_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** the 4x4 adjacency matrix of a small undirected network with nodes A, B, C, D and links A-B, A-C, B-C, B-D, C-D.
- **Mathematical operations:** compute eigenvalues and eigenvectors with `np.linalg.eig`, pick the dominant (largest) eigenvalue, take its eigenvector, normalise it so the scores add to 1, and verify A v = lambda v.

## 2. Original program and output

Run with `python code/Task_09_eigenvalues.py`.

```text
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

## 3. Changing a parameter

**What I changed:** Added a link between A and D so that every node is connected to every other node.

```python
[0., 1., 1., 1.],   # row A: now linked to D
[1., 1., 1., 0.]    # row D: now linked to A
```

**Output after the change** (`code/Task_09_eigenvalues_param_change.py`):

```text
Dominant eigenvalue: 3.0
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 2.220446049250313e-16
```

**How the result changed and why:** The dominant eigenvalue rose from 2.5616 to exactly 3.0 and all four nodes now have the same importance (0.25 each). In a fully connected network every node has three links and a symmetric position, so no node can be more influential than another.

## 4. Meaning of the output

The dominant eigenvalue is 2.5616, and the eigenvector-based importance is 0.2808 for B and C and 0.2192 for A and D. B and C are more influential because each is linked to three other nodes, while A and D are linked to two. A and D have equal scores because they are in symmetric positions. The verification error (about 1.5e-15) confirms that A v = lambda v holds.

## 5. Modified real-world case: Which building or device matters most in a campus network?

### Assumptions and input data

- An invented topology of six nodes: Library, Lab, Admin, Hostel, Cafeteria and Gate, with eight undirected links (this is an assumed network, not real data).
- Eigenvector centrality is calculated with `np.linalg.eigh`, which is suited to symmetric matrices.

### Program (`code/Task_09_modified.py`)

```python
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
```

### Output

```text
Degree of each node: [3, 3, 4, 3, 2, 1]
Dominant eigenvalue: 2.9439
Admin      0.2213
Library    0.2023
Lab        0.1871
Hostel     0.1871
Cafeteria  0.1271
Gate       0.0752
Verification error: 2.603703785810335e-15
```

### Interpretation

Admin ranks first (0.2213) because it has the most links (degree 4). Library (0.2023) ranks above Lab and Hostel (0.1871 each) even though all three have degree 3, because Library is connected to the highly ranked Admin node. This shows that eigenvector centrality counts the importance of neighbours, not just the number of links. Gate has the lowest score (0.0752) because it has one link only. In a real network, the top nodes are the ones whose failure would hurt most.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
