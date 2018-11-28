quantity = []
weight = []
flag = []
numToys = 0
bagWeight = 0

def init():
    global numToys
    global bagWeight
    quantity.clear()
    weight.clear()
    flag.clear()
    numToys = 0
    bagWeight = 0

def backtracking(n, p, f, t, bw):
    global numToys
    global bagWeight
    global flag
    for i in range(p, n):
        aux = False
        if f[i] == False:
            f[i] = True
            if bw + weight[i] <= 50:
                aux = True
                t = t + quantity[i]
                bw = bw + weight[i]

                if t > numToys:
                    numToys = t
                    bagWeight = bw
                    flag = f.copy()

        backtracking(n, i + 1, f, t, bw)
        if aux == True:
            t = t - quantity[i]
            bw = bw - weight[i]
        f[i] = False

numTests = int(input())
for i in range(0, numTests):
    init()
    numPack = int(input())

    for j in range(0, numPack):
        aux1, aux2 = input().split(" ")
        aux1 = int(aux1)
        aux2 = int(aux2)
        quantity.append(aux1)
        weight.append(aux2)

    f = []
    for i in range(0, numPack):
        f.append(False)

    backtracking(numPack, 0, f, 0, 0)

    print(str(numToys) + " brinquedos")
    print("Peso: " + str(bagWeight) + " kg")
    cont = 0
    for k in flag:
        if k == False:
            cont = cont + 1
    print("sobra(m) " + str(cont) + " pacote(s)")
    print()
