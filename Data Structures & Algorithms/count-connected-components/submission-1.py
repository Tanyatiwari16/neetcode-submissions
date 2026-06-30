class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = list(range(n))  # Each node is its own parent initially
        rank = [1] * n           # Rank array to optimize union operation
        count = n                # Initial number of components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            nonlocal count  # Since we modify count inside this function
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                count -= 1  # Reduce the number of connected components

        for u, v in edges:
            union(u, v)

        return count











        