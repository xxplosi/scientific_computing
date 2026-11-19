"""Task 16 (modified): Total water volume from a river-flow sensor.
Assumption: flow rate (m^3/s) recorded every 3 hours for a day (9 readings, synthetic).
Volume = integral of flow rate over time. Compare trapezoid and Simpson."""
import numpy as np
from scipy.integrate import simpson

t_hours = np.arange(0, 25, 3, dtype=float)
flow = np.array([4.0, 3.6, 3.9, 6.5, 9.8, 8.2, 5.6, 4.5, 4.1])   # m^3/s

t_sec = t_hours * 3600
vol_trap = np.trapezoid(flow, t_sec)
vol_simp = simpson(flow, x=t_sec)

print(f"Volume (trapezoid): {vol_trap:,.0f} m^3  = {vol_trap/1e6:.3f} million m^3")
print(f"Volume (Simpson)  : {vol_simp:,.0f} m^3  = {vol_simp/1e6:.3f} million m^3")
print(f"Difference        : {abs(vol_simp-vol_trap):,.0f} m^3 ({abs(vol_simp-vol_trap)/vol_simp:.2%})")
print(f"Average flow over the day: {vol_simp/86400:.3f} m^3/s")
