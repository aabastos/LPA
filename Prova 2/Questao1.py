import networkx as nx

linha = input()

while linha != "0 0 0":
    G = nx.Graph()

    n, m, t = linha.split(" ")
    n = int(n)
    m = int(m)
    t = int(t)

    for i in range(0, n):
        G.add_node(i + 1)

    for i in range(0, m):
        linha = input()
        a, b, c = linha.split(" ")

        G.add_edge(int(a), int(b), weight = int(c))

    custo = []

    for i in range(0, n):
        custo.append(int(input()))

    if(nx.has_path(G, source = 1, target = n) == True):
        path = nx.shortest_path(G, source = 1, target = n)

        tamPath = len(path)
        custoTotal = 0
        for i in range(0, tamPath - 1):
            t = t - (G[path[i]][path[i+1]]['weight'])
            custoTotal = custoTotal + (t * custo[i+1])

        print(custoTotal)

    else:
        print(-1)

    linha = input()
