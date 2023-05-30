error = True

while error:
    data_type = input("Wybierz opcje:?\n"
                      "1.Wczytanie danych z klawiatury.\n"
                      "2.Wczytanie danych z pliku.\n").upper()
    if data_type == "1":
        error = False
        data_error = True
        print("Wprowadź liczbę wierzchołków i krawędzi grafu (v, e)")
        while data_error:
            try:
                n, b = map(int, input().split())
                data_error = False
            except:
                print("Niepoprawnie wprowadzone dane")
        for i in range(n):
            data_error2 = True
            d = {}
            W = []
            V = []
            while data_error2:
                try:
                    r, w = map(int, input().split())
                    d[i + 1] = {
                        "r": r,
                        "w": w
                    }
                    W.append(r)
                    V.append(w)
                    data_error2 = False
                except:
                    print("Niepoprawnie wprowadzone dane")


    elif data_type == "2":
        error = False
        f = open("data.txt", 'r').read().split("\n")
        n, b = int(f[0].split(" ")[0]), int(f[0].split(" ")[1])
        W = []
        V = []
        del f[0]
        d = {}
        i = 0
        for line in f:
            i += 1
            d[i] = {
                "r": int(line.split(" ")[0]),
                "w": int(line.split(" ")[1])
            }
            W.append(int(line.split(" ")[0]))
            V.append(int(line.split(" ")[1]))


def bfAlgorithm(n, b, d):
    fmax = 0
    resSize = 0
    elmax = []
    for i in range(1, 2 ** n):
        bini = bin(i).replace("0b", "")
        binil = n - len(bini)
        leading = "0" * binil
        bini = leading + bini
        rx = 0
        wx = 0
        elements = []
        for j in range(len(bini)):
            if bini[j] == "1":
                num = abs(j - n)
                rx += d[num]["r"]
                wx += d[num]["w"]
                elements.append(num)
        if rx <= b:
            if wx > fmax:
                fmax = wx
                elmax = elements
                resSize = rx
    return [elmax[::-1], resSize, fmax]


def dyAlgorithm(c, n, W, V):
    if n == 0 or c == 0:  # base case, jak capacity jest zero, lub liczba elementow ktore zostaly do sprawdzenia to zero
        return 0
    if t[n][c] != -1:  # sprawdzanie czy jest już taki subproblem rozwiązany
        return t[n][c]
    if W[n - 1] <= c:  # jesli sie miesci w plecaku , to sprawdzamy rekurencyjnie max z, uwzgledn. i nie
        t[n][c] = max(V[n - 1] + dyAlgorithm(c - W[n - 1], n - 1, W, V), dyAlgorithm(c, n - 1, W, V))
        return t[n][c]
    elif W[n - 1] > c:  # jak waga jest większa niż capacity to pomijamy
        t[n][c] = dyAlgorithm(c, n - 1, W, V)
        return t[n][c]


def sort_lists_by_ratio(V, W):
    ratios = [v / w for v, w in zip(V, W)]
    sorted_indices = sorted(range(len(ratios)), key=lambda k: ratios[k], reverse=True)
    sorted_V = [V[i] for i in sorted_indices]
    sorted_W = [W[i] for i in sorted_indices]
    return sorted_V, sorted_W


def greedy(n, c, W, V):
    value = 0
    i = 0
    while c > 0 and i < n:
        if W[i] <= c:
            value += V[i]
            c -= W[i]
        i += 1

    return value


print("Algorytm programowania dynamicznego")
t = [[-1 for i in range(b + 1)] for j in range(n + 1)]
input()
print(dyAlgorithm(b, n, W, V))
input()
print("Algorytm zachłanny")
input()
sorted_V, sorted_W = sort_lists_by_ratio(V, W)
print(greedy(n, b, sorted_W, sorted_V))
input()
print("Algorytm siłowy")
input()
res = bfAlgorithm(n, b, d)
print("Elementy wybrane do plecaka", res[0])
print("Sumaryczny rozmiar", res[1])
print("Wartość", res[2])
input()
print("Koniec programu")
