import networkx as nx
import matplotlib.pyplot as plt

numTestes = int(input())

for testes in range(0, numTestes):
    linha = input()

    G = nx.Graph()

    numCamisetas, numVoluntarios = linha.split(" ")
    numCamisetas = int(numCamisetas)
    numVoluntarios = int(numVoluntarios)

    for camisa in ["XXL", "XL", "L", "M", "S", "XS"]:
        for i in range(1, int(numCamisetas / 6) + 1):
            G.add_node((camisa + str(i)), bipartite = 0)

    for i in range(1, numVoluntarios + 1):
        linha = input()
        camisa1, camisa2 = linha.split(" ")

        for j in range(1, int(numCamisetas / 6) + 1):
            G.add_edge((camisa1 + str(j)), i)
            G.add_edge((camisa2 + str(j)), i)

    M = nx.maximal_matching(G)

    if len(M) == numVoluntarios:
        print("YES")
    else:
        print("NO")
