quantity = []
weight = []
flag = []
numEnfeites = 0
weightTree = 0

#inicializador das variaveis globais
def init():
    global numEnfeites
    global weightTree
    numEnfeites = 0
    weightTree = 0

    quantity.clear()
    weight.clear()
    flag.clear()


# n  = numero de pacotes totais
# p  = numero de pacotes colocados no galho
# c  = capacidade do galho da arvore
# f  = vetor flag que identifica quais pacotes estao no galho
# t  = quantidade de enfeites no galho
# tw = peso do galho
def backtracking(n, p, c, f, t, tw):
    global numEnfeites
    global weightTree
    global flag
    for i in range(p, n):
        aux = False
        if f[i] == False:
            f[i] = True
            if tw + weight[i] <= c:
                aux = True
                t = t + quantity[i]
                tw = tw + weight[i]

                if t > numEnfeites:
                    numEnfeites = t
                    weightTree = tw
                    flag = f.copy()

        backtracking(n, i + 1, c, f, t, tw)
        if aux == True:
            t = t - quantity[i]
            tw = tw - weight[i]
        f[i] = False

#
#inicio do programa
#
numTests = int(input())

for i in range(0, numTests):
    numPack = int(input())
    capacity = int(input())

    init()
    for j in range(0, numPack):
        aux1, aux2 = input().split(" ")
        aux1 = int(aux1)
        aux2 = int(aux2)
        quantity.append(aux1)
        weight.append(aux2)

    f = []
    for j in range(0, numPack):
        f.append(False)

    backtracking(numPack, 0, capacity, f, 0, 0)

    print("Galho " + str(i + 1) + ": ")
    print("Numero total de enfeites: " + str(numEnfeites))
    print()
