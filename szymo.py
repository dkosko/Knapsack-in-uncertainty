from random import randint
import itertools
import numpy as np
from knapsack01 import knapSack as ks
from knapsack01 import na_vector as nw


p_intervals = [(2, 5), (3, 9), (1, 8), (3, 5), (5, 12), (6, 9), (2, 8), (1, 5)]
p = [0, 0, 0, 0, 0, 0, 0, 0]
w = [1, 3, 4, 7, 5, 8, 2, 3]
C = 20

#obliczam najgorsza mozliwosc
value, sol = ks(C, w, [x[0] for x in p_intervals])
sol = nw(sol, len(p))
print("F*: najslabsza mozliwosc")
print(value, sol)

#scenariusze
ilosc_scen = 40
S = [[] for i in range(ilosc_scen)]

#losowanie scenariuszy
for i in range(40):
    for j in p_intervals:
        S[i].append(randint(j[0], j[1]))

#obliczanie KS wartosci dla kazdego scenariusza
for i in S:
    print("najlepsza wartosc dla danego scenariusza")
    print(ks(C, w, i))

