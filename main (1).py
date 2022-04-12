from random import randint
import itertools
import numpy as np


def knapSack(W, w, c, x):
    if np.dot(w, x) <= W:
        return np.dot(c, x)
    else:
        return 0


def f_gwiazdka(profits, x):
    suma = 0
    for i in range(len(profits)):
        suma += profits[i][0] * x[i]
    return suma


c_intervals = [(2, 5), (3, 9), (1, 8), (3, 5), (5, 12), (6, 9), (2, 8), (1, 5)]
c = [0, 0, 0, 0, 0, 0, 0, 0]
w = [1, 3, 4, 7, 5, 8, 2, 3]
W = 20
lst = list(itertools.product([0, 1], repeat=8))

results = []
for x in lst:
    sum = 0
    n = 100
    for i in range(n):
        for i in range(len(c)):
            c[i] = randint(c_intervals[i][0], c_intervals[i][1])
        sum += knapSack(W, w, c, x)
        avg = sum / n
    results.append(avg)

max_i = results.index(max(results))
print(max(results))
print(lst[max_i])