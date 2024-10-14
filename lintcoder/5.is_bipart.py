
from collections import deque

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

    # We need to check every node because the graph may not be connected
    for start in range(n):
        if color[start] == -1:  # If the node is not yet colored
            # Start a BFS from this node
            queue = deque([start])
            color[start] = 0  # Assign the first color

            while queue:
                node = queue.popleft()

                # Try to color all neighbors with the opposite color
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Color the neighbor with the opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # If the neighbor has the same color, the graph is not bipartite
                        return False
    
    # If all components are bipartite, return True
    return True

# Example 1
graph1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(is_bipartite(graph1))  # Output: False

# Example 2
graph2 = [[1, 2, 3], [0, 2], [0, 1], [0]]
print(is_bipartite(graph2))  # Output: False

# Example 3
graph3 = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(is_bipartite(graph3))  # Output: True
