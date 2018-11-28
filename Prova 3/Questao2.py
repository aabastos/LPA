import networkx as nx

while True:
    try:
        str = input()

        G = nx.Graph()
        numRegions, numBridges = str.split(" ")
        numBridges = int(numBridges)

        for i in range(0, numBridges):
            r1, r2 = input().split(" ")
            G.add_edge(r1, r2)

        flag = False
        for node in G.nodes():
            if G.degree(node) == numBridges:
                flag = True

        if flag == True:
            print("S")
        else:
            print("N")

    except EOFError:
        break
