class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        indegree = [0]*numCourses

        for dest,src in prerequisites:
            adj[src].append(dest)
            indegree[dest] +=1

        q = collections.deque([])

        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        
        processed = 0

        while q:

            course = q.popleft()
            processed+=1
            for neighbour in adj[course]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)

        return True if processed==numCourses else False
            
        