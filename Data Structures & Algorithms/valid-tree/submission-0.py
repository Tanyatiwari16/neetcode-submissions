class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if (n - 1)!=len(edges): return False

        parent = [i for i in range(n)]
        rank = [1]*n
        # components = n

        def find(node):
            while parent[node]!=node:
                parent[node]=parent[parent[node]]
                node = parent[node]
            return node

        def union(n1,n2):

            global components

            root1 = find(n1)
            root2 = find(n2)

            if root1==root2:
                return False
            else:
                if rank[root1]>rank[root2]:
                    parent[root2]=root1
                elif rank[root2]>rank[root1]:
                    parent[root1]=root2
                else:
                    parent[root2] = root1

                    rank[root1]+=1
                # components = components -1

            return True

        for n1,n2 in edges:
            if not union(n1,n2):

                return False
        return True
