from mpmath import zetazero as z
import matplotlib.pyplot as p
from numpy import array as a

non_trivial_zeros = []
## Change the range values for more zeros
for i in range(1, 10):
    non_trivial_zeros.append(float(str(z(i)).strip("(0.5 + ").strip(")").strip("j")))

non_trivial_zeros = a(non_trivial_zeros)
y = non_trivial_zeros * 0 + 0.5
  
_, ax = p.subplots(figsize=(10, 10))
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

p.plot(y, non_trivial_zeros, linestyle='--', marker='x', color='b')
p.axvspan(0, 0.999999, color='red', alpha=0.5)
p.title("Visualization of non-trivial zeros of the Riemann zeta function")
p.xlabel("Real Axis")
p.ylabel("Imaginary axis (i)")
ax.set_xlim(-3, 3)
ax.set_ylim(0, 60)
p.show() 