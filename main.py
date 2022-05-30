from random import randint
import numpy as np
from knapsack01 import knapSack as ks
from knapsack01 import na_vector as nw
from statistics import fmean

import matplotlib.pyplot as plt


# warunki początkowe:
p_intervals = [(2, 5), (3, 9), (1, 8), (3, 5), (5, 12), (6, 9), (2, 8), (1, 5), (2, 8), (6, 9)] #przdziały kosztów dla każdego z produktów
p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # początkowe rozwiązanie - nic nie jest brano do plecaka
w = [1, 3, 4, 7, 5, 8, 2, 3, 2, 3]  # wagi dla każdego z produktów
C = 20  # pojemność plecaka





def losuj_wagi():  #funkca losująca wagi, zwraca listę wag losowanych z przedziału [1,10)
    wynik = []
    for i in range(10):
        wynik.append(randint(1, 10))
    return wynik


def losuj_koszty():  #funkcja losująca przdziały kosztów dla każdego z produktów
    price_list = []
    for i in range(10):
        dol = randint(0, 12)
        gora = randint(dol, 15)
        price_list.append((dol, gora))

    return price_list


""" Symulacja rozwiązania dla losowych kosztów produktów oraz dla różnych pojemności plecaka
W celu przeprowadzenia analizy skuteczności rozwiązania przeprowadziliśmy symulacje dla 10 różnych pojemnośći
plecaka, wraz ze zwiększeniem pojemności plecaka dodawaliśmy też nowe produkty do wyboru losowane za pomocą wyżej 
zaimplemetowanych funkcji"""

sr_zal = []
for m in range(10):

    # obliczam optymalne rozwiązanie dla najgorszej możliwości - dolne granicy kosztów
    koszt, rozwiazanie = ks(C, w, [x[0] for x in p_intervals])
    rozwiazanie = nw(rozwiazanie, len(p))

    # scenariusze
    ilosc_scen = 50
    S = [[] for i in range(ilosc_scen)]

    # losowanie scenariuszy
    for i in range(ilosc_scen):
        for j in p_intervals:
            S[i].append(randint(j[0], j[1]))

    # obliczanie KS wartosci dla kazdego scenariusza
    zale = []
    wartosci = []
    for i in S:
        wart_plecaka, opt_rozw = ks(C, w, i)
        opt_rozw = nw(opt_rozw, len(p_intervals))
        wartosci.append(wart_plecaka)
        z = wart_plecaka - np.dot(rozwiazanie, i)
        zale.append(z)


    print('sredni zal', fmean(zale))
    print('srednia wartosc plecaka', fmean(wartosci))
    sr_zal.append(fmean(zale) / wart_plecaka)
    print('maksymalny zal', max(zale))

    # zwiększa się pojemność plecaka i dodawane są kolejne produkty do wyboru
    C += 20
    p_intervals += losuj_koszty()
    w += losuj_wagi()
    p = [0 for n in range(len(w))]
    print(p_intervals)

print(sr_zal)
cc = [x * 20 for x in range(1, 11)]
plt.plot(cc, sr_zal)
plt.xlabel('Pojemność plecaka')
plt.ylabel('Srednim zal / Opt_rozwiazanie')
plt.show()