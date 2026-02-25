#Newton-Raphson Method

import sympy as sp

x = sp.symbols('x')

x_val = float(input("Enter the variable x you would like to start with: "))

n = int(input("Enter the number of iterations you would like to run: "))

f = x**2 - x + 1
df = sp.diff(f, x)

for i in range(n):
    x_old = x_val
    a = f.subs(x, x_val)      
    b = df.subs(x, x_val)     
    x_val = x_val - a/b
    print("The current x value is:", x_old)
    print("The value of the slope is:", b)
    print("The new x is:", x_val, "and it jumped by", x_val - x_old)