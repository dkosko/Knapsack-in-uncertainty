def wys(a):
    for i in a:
        print(i)
    print()


def knapSack(W, weight, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    prod = [[[] for x in range(W + 1)] for x in range(n + 1)]
    wys(prod)


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

    wys(table)
    print('rozwiązanie w ostatniej komórce')
    wys(prod)

    return table[n][W]


val = [3, 2, 1.5]
wt = [4, 3, 1]
W = 4

print(knapSack(W, wt, val))