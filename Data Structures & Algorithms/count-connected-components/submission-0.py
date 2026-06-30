class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # A set to keep track of visited nodes
        visited = set()

        def dfs(node: int):
            # Mark the node as visited
            visited.add(node)
            # Visit all the neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Counter for the number of connected components
        components = 0

        # Iterate through all nodes
        for i in range(n):
            if i not in visited:
                # If a node hasn't been visited, it's a new component
                dfs(i)
                components += 1

        return components