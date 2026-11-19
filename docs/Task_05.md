# Task 5: Matrix Algebra and Matrix Operations

**Course:** BIT 2118 Scientific Computing  
**Student:** Michael Asilwa (Admission No: BSCCS/2024/56330, GitHub: xxplosi)  
**Files:** `code/Task_05_matrix_algebra.py` (given program), `code/Task_05_matrix_algebra_param_change.py` (changed parameter), `code/Task_05_modified.py` (my real-world case)

## 1. Inputs and mathematical operation

- **Input data:** the four corners of a unit square as a 4x2 array, a rotation angle of 45 degrees, and a scaling matrix that stretches x by 2.0 and y by 1.5.
- **Mathematical operations:** build the rotation matrix R and scaling matrix S, combine them with matrix multiplication T = R @ S, transform every point with `points @ T.T`, and compute the determinant of T.

## 2. Original program and output

Run with `python code/Task_05_matrix_algebra.py`.

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

## 3. Changing a parameter

**What I changed:** Changed the rotation angle from 45 degrees to 90 degrees.

```python
angle = np.deg2rad(90)   # was 45
```

**Output after the change** (`code/Task_05_matrix_algebra_param_change.py`):

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.22464680e-16 -1.50000000e+00]
 [ 2.00000000e+00  9.18485099e-17]]
Transformed points:
 [[ 0.00000000e+00  0.00000000e+00]
 [ 1.22464680e-16  2.00000000e+00]
 [-1.50000000e+00  2.00000000e+00]
 [-1.50000000e+00  9.18485099e-17]]
Determinant: 2.9999999999999996
```

**How the result changed and why:** The transformation matrix became approximately [[0, -1.5], [2, 0]] and the corner (1, 0) moved to (0, 2) instead of (1.414, 1.414). The determinant stayed 3.0 because rotation never changes area, so the area factor is still 2.0 x 1.5 = 3. The very small numbers such as 1.2e-16 are floating-point round-off from cos(90 degrees) and should be read as zero.

## 4. Meaning of the output

The unit square is first stretched to 2 wide by 1.5 tall and then rotated 45 degrees, so the corner (1, 0) goes to (1.414, 1.414). The determinant 3.0 equals the area scale factor: the new shape has 3 times the original area (1 becomes 3). A positive determinant also means the shape is not flipped (no reflection).

## 5. Modified real-world case: Transforming a banner on a phone screen

### Assumptions and input data

- A rectangular banner of 200 x 100 pixels with its corner at the origin.
- Transformation order: scale to 60% then rotate 30 degrees then shear horizontally by 0.3 (T = shear @ rotation @ scale).

### Program (`code/Task_05_modified.py`)

```python
"""Task 5 (modified): Transforming a rectangular app icon/banner on a phone screen.
Assumption: banner corners in pixels. We rotate by 30 degrees, shrink to 60%,
then shear horizontally, using a combined 2x2 transformation matrix."""
import numpy as np

banner = np.array([[0.0, 0.0], [200.0, 0.0], [200.0, 100.0], [0.0, 100.0]])

theta = np.deg2rad(30)
rotation = np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta),  np.cos(theta)]])
scale = np.diag([0.6, 0.6])
shear = np.array([[1.0, 0.3],
                  [0.0, 1.0]])

T = shear @ rotation @ scale
new_banner = banner @ T.T

print("Transformation matrix:\n", np.round(T, 4))
print("Transformed corners:\n", np.round(new_banner, 2))
print("Determinant:", round(np.linalg.det(T), 4))
print("Original area:", 200 * 100)
print("New area (original x determinant):", round(200 * 100 * np.linalg.det(T), 1))
```

### Output

```text
Transformation matrix:
 [[ 0.6096 -0.1441]
 [ 0.3     0.5196]]
Transformed corners:
 [[  0.     0.  ]
 [121.92  60.  ]
 [107.51 111.96]
 [-14.41  51.96]]
Determinant: 0.36
Original area: 20000
New area (original x determinant): 7200.0
```

### Interpretation

The combined matrix has determinant 0.36. This equals 0.6 x 0.6 (scaling) x 1 (rotation) x 1 (shear), because rotation and shear do not change area. The banner's area therefore changes from 20,000 to 7,200 pixels squared, which matches 20,000 x 0.36. One matrix multiplication moved all four corners consistently, which is how graphics systems transform shapes and icons.

---
*Note: numbers marked as timings (Tasks 3 and 7) depend on the computer and change slightly from run to run. All other results are reproducible with the fixed random seeds in the code.*
