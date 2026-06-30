class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        
    

        if not words:
            return ""

        graph = defaultdict(set)
        in_degree = {}

        # Initialize in-degree for all unique characters.
        for word in words:
            for char in word:
                in_degree[char] = 0

        # Build the graph based on adjacent word comparisons.
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        visited = {}  # 0: unvisited, 1: visiting, 2: visited
        result = []

        def dfs(char):
            visited[char] = 1  # Visiting

            for neighbor in graph[char]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False  # Cycle detected
                elif visited[neighbor] == 1:
                    return False  # Cycle detected

            visited[char] = 2  # Visited
            result.append(char)
            return True

        for char in in_degree:
            if char not in visited:
                if not dfs(char):
                    return ""

        result.reverse()  # Reverse the result for correct order
        return "".join(result)
