class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

    # 1. Build the graph (adjacency list) and in-degree count.
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
                    break  # Only the first differing character matters.
            else: # if the for loop completes without breaking
                if len(word1) > len(word2):
                    return "" # invalid order. "abc", "ab" is not possible

        # 2. Topological sort using Kahn's algorithm.
        queue = [char for char in in_degree if in_degree[char] == 0]
        result = []

        while queue:
            char = queue.pop(0)
            result.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 3. Check for cycles (invalid order).
        if len(result) != len(in_degree):
            return ""  # Cycle detected.

        return "".join(result)