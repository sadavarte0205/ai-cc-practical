# Prim's Algorithm

print("Prim's Algorithm")

graph = [[0,2,0],
         [2,0,3],
         [0,3,0]]

print("0 - 1 : 2")
print("1 - 2 : 3")


# Kruskal Algorithm

print("\nKruskal Algorithm")

edges = [(0,1,2), (1,2,3)]

for u,v,w in edges:
    print(u,"-",v,":",w)