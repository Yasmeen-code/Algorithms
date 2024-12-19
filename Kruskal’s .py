class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def find_set(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find_set(parent, parent[x])
        return parent[x]

    def union(self, parent, rank, x, y):
        rootX = self.find_set(parent, x)
        rootY = self.find_set(parent, y)
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

    def kruskal(self):
        self.edges.sort(key=lambda edge: edge[2])
        parent = {i: i for i in range(self.vertices)}
        rank = {i: 0 for i in range(self.vertices)}
        mst = []
        mst_cost = 0
        for u, v, w in self.edges:
            if self.find_set(parent, u) != self.find_set(parent, v):
                mst.append((u, v, w))
                mst_cost += w
                self.union(parent, rank, u, v)
        return mst, mst_cost


# Taking input from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

g = Graph(num_vertices)

print("Enter the edges in the format (u, v, w):")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

mst, cost = g.kruskal()

print("\nEdges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print(f"Total cost of MST: {cost}")
