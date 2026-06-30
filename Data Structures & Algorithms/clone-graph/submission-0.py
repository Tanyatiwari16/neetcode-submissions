"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None  # If input graph is empty, return None

        # Dictionary to store original node -> cloned node mapping
        cloned_nodes = {}

        # Initialize queue for BFS traversal
        queue = deque([node])

        # Create a copy of the first node
        cloned_nodes[node] = Node(node.val)

        # Start BFS traversal
        while queue:
            # Get the current node
            curr = queue.popleft()

            # Iterate through the neighbors of the current node
            for neighbor in curr.neighbors:

                if neighbor not in cloned_nodes:

                    # Clone the neighbor if not already cloned
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    # Add original neighbor to queue for processing
                    queue.append(neighbor)

                # Connect the cloned node to its cloned neighbors
                cloned_nodes[curr].neighbors.append(cloned_nodes[neighbor])

        return cloned_nodes[node] 