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
