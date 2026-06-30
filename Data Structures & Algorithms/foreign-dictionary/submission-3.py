class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)  # Adjacency list
        in_degree = {char: 0 for word in words for char in word}  # Initialize in-degree

        # Step 2: Find letter order by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # If prefix is same but second word is shorter, order is invalid
            if word1[:min_length] == word2[:min_length] and len(word1) > len(word2):
                return ""

            for j in range(min_length):
                if word1[j] != word2[j]:  # Find first different character
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1  # Increase in-degree
                    break  # Stop after first difference

        # Step 3: Topological Sort (BFS - Kahn's Algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])  # Nodes with in-degree 0
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If order includes all unique letters, return it; otherwise, return ""
        return "".join(order) if len(order) == len(in_degree) else ""