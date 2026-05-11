class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])

        print("Edges in MST")

        for u, v, w in self.graph:
            print("%d -- %d == %d" % (u, v, w))

g = Graph(4)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)

g.kruskal()