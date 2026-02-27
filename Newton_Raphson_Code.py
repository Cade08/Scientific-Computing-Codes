#Newton-Raphson Method

import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')

x_val = float(input("Enter the variable x you would like to start with: "))

n = int(input("Enter the number of iterations you would like to run: "))

f = x**2 - 2 
df = sp.diff(f, x)   

errors = []

for i in range(n):
    x_old = x_val
    a = f.subs(x, x_val)     
    b = df.subs(x, x_val) 
    x_val = x_val - a/b
    print("\nIteration", i)
    print("x_n =", x_old)
    print("Slope =", b)
    print("New x =", x_val, " Jump =", x_val - x_old)
    
    errors.append(abs(float(f.subs(x, x_val))))
    
plt.semilogy(errors, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Absolute value of f(x_n)")
plt.title("Newton Convergence")
plt.grid(True)
plt.show()
