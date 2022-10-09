from sympy import *
x = symbols('x')

# ************************************ Trapezoidal rule ***********************************************
eq = log(x)
limits = [4, 5.2]

h = 0.1
X = []
Y = []
ind = limits[0]

while ind <= limits[1]:
    X.append(ind)
    Y.append(eq.subs(x, ind))
    ind += h

value = (h / 2) * (Y[0] + 2 * sum(Y[1:-1]) + Y[-1])

print(N(value))


# *************************************** Simpsons 1/3 ************************************************
eq = log(x)
limits = [4, 5.2]

h = 0.1
X = []
Y = []
ind = limits[0]

while ind <= limits[1]:
    X.append(ind)
    Y.append(eq.subs(x, ind))
    ind += h

value = (h / 3) * (Y[0] + 4 * sum(Y[1:-1:2]) + 2 * sum(Y[2:-1:2]) + Y[-1])

print(N(value))



# *********************************************** Simpsons 3/8 ****************************************************************
eq = log(x)
limits = [4, 5.2]

h = 0.1
X = []
Y = []
ind = limits[0]

while ind <= limits[1]:
    X.append(ind)
    Y.append(eq.subs(x, ind))
    ind += h

total = 0
total3 = 0
for i in range(1, len(Y) - 1):
    if i % 3 != 0:
        total += Y[i]
    else:
        total3 += Y[i]


value = (3 * h / 8) * (Y[0] + 2 * total3 + 3 * total + Y[-1])

print(N(value))
