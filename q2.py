from sympy import *

# Cubic Spline method
x = [1, 2, 3, 4]
y = [1, 5, 11, 8]
X0 = 1.5

h = x[1] - x[0]
n = len(x) - 1
X = symbols('X')
m = symbols('m0:%d' % (n + 1))
M = {0: 0, n: 0}
expr = []

for i in range(1, n):
    expr.append(m[i - 1] + 4 * m[i] + m[i + 1] - 6 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2)
    for j in M:
        expr[i - 1] = expr[i - 1].subs(m[j], M[j])

sol = solve(tuple(expr), tuple(m))

for i in range(len(sol)):
    M[i + 1] = sol[m[i + 1]]

ind = 0
for ind in range(n + 1):
    if X0 <= x[ind]:
        break

Y = (x[ind] - X0) ** 3 * M[ind - 1] / (6 * h) + (X0 - x[ind - 1]) ** 3 * M[ind] / (6 * h) + (x[ind] - X0) / h * (y[ind - 1] - (h ** 2 * M[ind - 1]) / 6) + (X0 - x[ind - 1]) / h * (y[ind] - h ** 2 * M[ind] / 6)
print(Y)



#Lagranges interpolation
x = [300, 304, 305, 307]
y = [2.4771, 2.4829, 2.4843, 2.4871]
X = 301

Y = 0

for i in range(len(x)):
    numerator = 1
    denominator = 1
    for j in range(len(x)):
        if j != i:
            numerator *= (X - x[j])
            denominator *= (x[i] - x[j])
    Y += numerator * y[i] / denominator

print(Y)



#lagranges iverse interpolation
x = [168, 120, 72, 63]
y = [3, 7, 9, 10]
X = 6

Y = 0

for i in range(len(y)):
    numerator = 1
    denominator = 1
    for j in range(len(y)):
        if j != i:
            numerator *= (X - y[j])
            denominator *= (y[i] - y[j])
    Y += numerator * x[i] / denominator

print(Y)



#Newton's Divided Difference Interpolation
x = [300, 304, 305, 307]
y = [2.4771, 2.4829, 2.4843, 2.4871]
X = 301

n = len(x)
table = []
table.append(y)

for i in range(n - 1):
    values = []
    for j in range(len(table[i]) - 1):
        value = (table[i][j + 1] - table[i][j]) / (x[j + i + 1] - x[j])
        values.append(value)
    table.append(values)

Y = 0

for i in range(len(table)):
    prod = 1
    for j in range(i):
        prod *= (X - x[j])
    Y += prod * table[i][0]

print(Y)