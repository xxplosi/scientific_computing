# BIT 2118 Scientific Computing: Group Work (individual submission)

**Student:** Michael Asilwa  
**Admission No:** BSCCS/2024/56330  
**Institution:** Mount Kenya University (Thika campus), Bachelor of Computer Science  
**Unit:** BIT 2118 Scientific Computing  
**GitHub:** [xxplosi](https://github.com/xxplosi)

Individual GitHub repository of **Michael Asilwa** (`xxplosi`) for the BIT 2118 Scientific Computing group work, Tasks 2 to 20.

For every task the repository contains:

1. the **given program** (`code/Task_XX_<name>.py`),
2. a **parameter-change version** (`code/Task_XX_<name>_param_change.py`) with the change explained,
3. a **modified real-world program** (`code/Task_XX_modified.py`) with its own assumptions, input data, output and interpretation,
4. a **write-up** (`docs/Task_XX.md`) covering inputs and operation, the output in words, the parameter change, and the modified case.

## Tasks

| Task | Topic | Given program | Modified program | Write-up |
|---|---|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | [code/Task_02_numpy_arrays.py](code/Task_02_numpy_arrays.py) | [code/Task_02_modified.py](code/Task_02_modified.py) | [docs/Task_02.md](docs/Task_02.md) |
| 3 | Mathematical Functions and Vectorization | [code/Task_03_vectorization.py](code/Task_03_vectorization.py) | [code/Task_03_modified.py](code/Task_03_modified.py) | [docs/Task_03.md](docs/Task_03.md) |
| 4 | Floating-Point Arithmetic and Numerical Errors | [code/Task_04_numerical_errors.py](code/Task_04_numerical_errors.py) | [code/Task_04_modified.py](code/Task_04_modified.py) | [docs/Task_04.md](docs/Task_04.md) |
| 5 | Matrix Algebra and Matrix Operations | [code/Task_05_matrix_algebra.py](code/Task_05_matrix_algebra.py) | [code/Task_05_modified.py](code/Task_05_modified.py) | [docs/Task_05.md](docs/Task_05.md) |
| 6 | Solution of Systems of Linear Equations | [code/Task_06_linear_systems.py](code/Task_06_linear_systems.py) | [code/Task_06_modified.py](code/Task_06_modified.py) | [docs/Task_06.md](docs/Task_06.md) |
| 7 | Gaussian Elimination and LU Decomposition | [code/Task_07_gaussian_lu.py](code/Task_07_gaussian_lu.py) | [code/Task_07_modified.py](code/Task_07_modified.py) | [docs/Task_07.md](docs/Task_07.md) |
| 8 | Iterative Methods for Linear Systems | [code/Task_08_iterative_linear.py](code/Task_08_iterative_linear.py) | [code/Task_08_modified.py](code/Task_08_modified.py) | [docs/Task_08.md](docs/Task_08.md) |
| 9 | Eigenvalues and Eigenvectors | [code/Task_09_eigenvalues.py](code/Task_09_eigenvalues.py) | [code/Task_09_modified.py](code/Task_09_modified.py) | [docs/Task_09.md](docs/Task_09.md) |
| 10 | Root Finding: Bisection and Fixed-Point Methods | [code/Task_10_bisection_fixed_point.py](code/Task_10_bisection_fixed_point.py) | [code/Task_10_modified.py](code/Task_10_modified.py) | [docs/Task_10.md](docs/Task_10.md) |
| 11 | Root Finding: Newton-Raphson and Secant Methods | [code/Task_11_newton_secant.py](code/Task_11_newton_secant.py) | [code/Task_11_modified.py](code/Task_11_modified.py) | [docs/Task_11.md](docs/Task_11.md) |
| 12 | Polynomial and Nonlinear Equation Solving | [code/Task_12_nonlinear_equations.py](code/Task_12_nonlinear_equations.py) | [code/Task_12_modified.py](code/Task_12_modified.py) | [docs/Task_12.md](docs/Task_12.md) |
| 13 | Interpolation | [code/Task_13_interpolation.py](code/Task_13_interpolation.py) | [code/Task_13_modified.py](code/Task_13_modified.py) | [docs/Task_13.md](docs/Task_13.md) |
| 14 | Curve Fitting and Approximation | [code/Task_14_curve_fitting.py](code/Task_14_curve_fitting.py) | [code/Task_14_modified.py](code/Task_14_modified.py) | [docs/Task_14.md](docs/Task_14.md) |
| 15 | Numerical Differentiation | [code/Task_15_numerical_differentiation.py](code/Task_15_numerical_differentiation.py) | [code/Task_15_modified.py](code/Task_15_modified.py) | [docs/Task_15.md](docs/Task_15.md) |
| 16 | Numerical Integration | [code/Task_16_numerical_integration.py](code/Task_16_numerical_integration.py) | [code/Task_16_modified.py](code/Task_16_modified.py) | [docs/Task_16.md](docs/Task_16.md) |
| 17 | Ordinary Differential Equations: Euler Method | [code/Task_17_euler_ode.py](code/Task_17_euler_ode.py) | [code/Task_17_modified.py](code/Task_17_modified.py) | [docs/Task_17.md](docs/Task_17.md) |
| 18 | Numerical Solution of ODEs Using SciPy | [code/Task_18_scipy_ode.py](code/Task_18_scipy_ode.py) | [code/Task_18_modified.py](code/Task_18_modified.py) | [docs/Task_18.md](docs/Task_18.md) |
| 19 | Numerical Optimization | [code/Task_19_optimization.py](code/Task_19_optimization.py) | [code/Task_19_modified.py](code/Task_19_modified.py) | [docs/Task_19.md](docs/Task_19.md) |
| 20 | Random Numbers and Monte Carlo Methods | [code/Task_20_monte_carlo.py](code/Task_20_monte_carlo.py) | [code/Task_20_modified.py](code/Task_20_modified.py) | [docs/Task_20.md](docs/Task_20.md) |

## How to run

```bash
python -m venv venv
source venv/Scripts/activate     # Git Bash on Windows (use venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
python code/Task_02_numpy_arrays.py
```

Programs that draw graphs open a Matplotlib window. The graphs in `docs/images/` were produced by running the same programs and saving each figure.

## Notes

- NumPy 2.0 or later is needed for `np.trapezoid` (Task 16).
- In Tasks 16 and 18 the long `print` lines were kept on a single line, because a line break inside an f-string is a syntax error.
- Data in the modified programs is synthetic or assumed unless stated otherwise, and each write-up lists its assumptions.
