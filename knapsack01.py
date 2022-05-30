def wys(a):
    for i in a:
        print(i)
    print()



def knapSack(W, weight, val):
    """
    Rozwiązanie dyskretnego problemu plecakowego za pomocą programowania dynamicznego
    W - pojemność plecaka,
    weight - lista wag,
    val - lista kosztów.

    Funkcja zwraca:
    table[n][W] - kozt plecaka przy optymalnym rozwiązaniu,
    prod[n][W] - lista indeksów produktów, które są brane do plecaka przy optymalnym rozwiązaniu.
    """


    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    prod = [[[] for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            if i == 0 or j == 0:
                table[i][j] = 0

            elif weight[i - 1] <= j:

                if val[i - 1] + table[i - 1][j - weight[i - 1]] > table[i - 1][j]:

                    table[i][j] = val[i - 1] + table[i - 1][j - weight[i - 1]]
                    prod[i][j] = prod[i - 1][j - weight[i - 1]].copy()
                    prod[i][j].append(i-1)

                else:
                    table[i][j] = table[i - 1][j]
                    prod[i][j] = prod[i - 1][j].copy()

            else:
                table[i][j] = table[i - 1][j]
                prod[i][j] = prod[i - 1][j].copy()

    return table[n][W], prod[n][W]

def na_vector(vec, num):
    """Funkcja konwertuje listę indeksów produktów na listę 01 z całą listą produktów,
    gdzie 1 oznacza, że bierzemy produkt do plecaka, a 0 że nie
    vec - listę indeksów produktów, które są brane do plecaka
    num - pełna lista indeksów produktów

    Funkcja zwraca:
    vec_x - lista 01 wskazująca na produkty, które są brane do plecaka"""


    vec_x = []
    for i in range(num):
        if i in vec:
            vec_x.append(1)
        else:
            vec_x.append(0)
    return vec_x
