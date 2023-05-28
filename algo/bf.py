#Brute Force algorithm


def bfAlgorithm(n,b,d):
    fmax = 0
    for i in range(1, 2**n):
        bini = bin(i).replace("0b","")
        binil = n-len(bini)
        leading = "0"*binil
        bini = leading+bini
        rx = 0
        wx = 0
        for j in range(len(bini)):
            if bini[j] == "1":
                num = abs(j-n)
                rx += d[num]["r"]
                wx += d[num]["w"]
        if rx <= b:
            if wx > fmax:
                fmax = wx
    return fmax