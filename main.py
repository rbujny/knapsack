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


# siłowy
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
                elements.append(num - 1)
        if rx <= b:
            if wx > fmax:
                fmax = wx
                elmax = elements
                resSize = rx
    return [elmax[::-1], resSize, fmax]


# dynamiczny
def dyAlgorithm(c, n, W, V, t, total_weight):
    if n == 0 or c == 0:  # base case, jeśli pojemność jest zero lub liczba elementów do sprawdzenia to zero
        return 0, total_weight, []
    if t[n][c] != -1:  # sprawdzenie, czy subproblem został już rozwiązany
        return t[n][c], total_weight, []
    if W[
        n - 1] <= c:  # jeśli mieści się w plecaku, sprawdzamy rekurencyjnie maksimum uwzględniając i nieuwzględniając go
        include_val, include_weight, include_items = dyAlgorithm(c - W[n - 1], n - 1, W, V, t, total_weight + W[n - 1])
        exclude_val, exclude_weight, exclude_items = dyAlgorithm(c, n - 1, W, V, t, total_weight)
        if include_val + V[n - 1] > exclude_val:
            t[n][c] = include_val + V[n - 1]
            include_items.append(n - 1)
            return t[n][c], include_weight, include_items
        else:
            t[n][c] = exclude_val
            return t[n][c], exclude_weight, exclude_items
    elif W[n - 1] > c:  # jeśli waga jest większa niż pojemność, pomijamy ten przedmiot
        t[n][c], total_weight, exclude_items = dyAlgorithm(c, n - 1, W, V, t, total_weight)
        return t[n][c], total_weight, exclude_items


def add_item_indices(items, indices):
    items_with_indices = []
    for item, index in zip(items, indices):
        items_with_indices.append((item, index))
    return items_with_indices


def sort_lists_by_ratio(items):
    sorted_items = sorted(items, key=lambda x: x[0] / W[x[1]], reverse=True)
    sorted_V = [item[0] for item in sorted_items]
    sorted_indices = [item[1] for item in sorted_items]
    return sorted_V, sorted_indices


# zachłanny
def greedy(n, c, W, V):
    value = 0
    total_weight = 0
    items_in_bag = []
    i = 0
    while c > 0 and i < n:
        if W[i] <= c:
            value += V[i]
            total_weight += W[i]
            items_in_bag.append(sorted_indices[i])
            c -= W[i]
        i += 1

    return value, total_weight, items_in_bag


print("Algorytm programowania dynamicznego")
t = [[-1 for i in range(b + 1)] for j in range(n + 1)]
input()
max_value, total_weight, selected_items = dyAlgorithm(b, n, W, V, t, 0)
print("Elementy wybrane do plecaka:", [i for i in selected_items])
print("Sumaryczny rozmiar:", total_weight)
print("Wartość:", max_value)
input()
print("Algorytm zachłanny")
input()
items_with_indices = add_item_indices(V, list(range(n)))
sorted_V, sorted_indices = sort_lists_by_ratio(items_with_indices)
sorted_W = [W[i] for i in sorted_indices]
value, total_weight, items_in_bag = greedy(n, b, sorted_W, sorted_V)
print("Elementy wybrane do plecaka:", items_in_bag)
print("Sumaryczny rozmiar:", total_weight)
print("Wartość:", value)
input()
print("Algorytm siłowy")
input()
res = bfAlgorithm(n, b, d)
print("Elementy wybrane do plecaka:", res[0])
print("Sumaryczny rozmiar:", res[1])
print("Wartość:", res[2])
input()
print("Koniec programu")
