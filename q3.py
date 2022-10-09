from sympy import *


#Newton's Forward Difference Interpolation
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

x = [1891, 1901, 1911, 1921, 1931]
y = [46, 66, 81, 93, 101]
X = 1895

h = x[1] - x[0]
p = (X - x[0]) / h

table = []
table.append(y)
for i in range(len(x) - 1):
    column = []
    for j in range(1, len(table[i])):
        column.append(table[i][j] - table[i][j - 1])
    table.append(column)

Y = 0

for i in range(len(table)):
    prod = 1
    for j in range(i):
        prod *= (p - j)
    Y += prod * table[i][0] / fact(i)

print(Y)



#Newton's Backward Difference Interpolation
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

x = [1891, 1901, 1911, 1921, 1931]
y = [46, 66, 81, 93, 101]
X = 1925

h = x[1] - x[0]
p = (X - x[len(x) - 1]) / h

table = []
table.append(y)
for i in range(len(x) - 1):
    column = []
    for j in range(1, len(table[i])):
        column.append(table[i][j] - table[i][j - 1])
    table.append(column)

Y = 0

for i in range(len(table)):
    prod = 1
    for j in range(i):
        prod *= (p + j)
    Y += prod * table[i][-1] / fact(i)

print(Y)



#Newtons forward Difference Differentiation
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

x = [0.0, 0.1, 0.2, 0.3, 0.4]
y = [1.0000, 0.9975, 0.9900, 0.9776, 0.8604]
X = 0

h = x[1] - x[0]
p = (X - x[0]) / h

table = []
table.append(y)
for i in range(len(x) - 1):
    column = []
    for j in range(1, len(table[i])):
        column.append(table[i][j] - table[i][j - 1])
    table.append(column)

Y = 0
t = symbols('t')

for i in range(len(table)):
    temp = table[i][0]
    for j in range(i):
        temp *= (t - j)
    temp /= fact(i)
    Y += temp

dydx = diff(Y, t).subs(t, p) / h
dy2dx2 = diff(diff(Y, t), t).subs(t, p) / h ** 2

print(dydx)
print(dy2dx2)