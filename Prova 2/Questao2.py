import networkx as nx
import matplotlib.pyplot as plt

n = int(input())

while n != 0:
    G = nx.Graph()

    for i in range(0, n):
        p = int(input())
        a = input().split(" ")

        tamA = len(a)
        for j in range(0, tamA):
            G.add_edge(i+1, int(a[j]))

    if(nx.is_bipartite(G) == True):
        print("SIM")
    else:
        print("NÃO")

    n = int(input())
