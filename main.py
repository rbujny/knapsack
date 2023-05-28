from algo.bf import bfAlgorithm as bf
from algo.dy import dyAlgorithm as dy
from algo.gr import grAlgorithm as gr

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
            while data_error2:
                try:
                    r, w = map(int, input().split())
                    d[i + 1] = {
                        "r": r,
                        "w": w
                    }
                    data_error2 = False
                except:
                    print("Niepoprawnie wprowadzone dane")


    elif data_type == "2":
        error = False
        f = open("data.txt", 'r').read().split("\n")
        n, b = int(f[0].split(" ")[0]), int(f[0].split(" ")[1])
        del f[0]
        d = {}
        i = 0
        for line in f:
            i += 1
            d[i] = {
                "r": int(line.split(" ")[0]),
                "w": int(line.split(" ")[1])
            }

print("Algorytm programowania dynamicznego")
input()
print(dy())
input()
print("Algorytm zachłanny")
input()
print(gr())
input()
print("Algorytm siłowy")
input()
print(bf(n, b, d))
input()
print("Koniec programu")
