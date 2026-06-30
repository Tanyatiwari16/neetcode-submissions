class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [1]*n
        components = n

        def find(node):
            while node!=parent[node]:
                #path compression to grand parent
                parent[node]=parent[parent[node]]
                node = parent[node]
            return node

        def union(n1,n2):
            nonlocal components
            root1 = find(n1)
            root2 = find(n2)

            if root1!=root2:
                if rank[root1]>rank[root2]:
                    parent[root2] = root1
                elif rank[root2]>rank[root1]:
                    parent[root1] = root2

                else:
                    parent[root2] = root1
                    rank[root1]+=1
                components-=1
            

        
        for n1,n2 in edges:

            union(n1,n2)

        return components
