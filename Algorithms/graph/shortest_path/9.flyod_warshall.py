"""
The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix. mat[i][j] denotes the weight of the edge from i to j. If mat[i][j] = -1, it means there is no edge from i to j.
Note: Modify the distances for every pair in place.


"""
class Solution:
    # time complexity O(n^3) | space complexity O(n^2)
    def shortest_distance(self, matrix):
        n=len(matrix)
        rows,cols=len(matrix),len(matrix[0])
        # relace -1 with infinity and [x][x] with 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==-1:
                    matrix[row][col]=float('inf')
                if row==col:
                    # to reach the same node it will take 0 time
                    matrix[row][col]=0

        # floyd warshall algorithm (go via every vertex and compute the shortest path)

        for via in range(n):
            for src in range(n):
                for dst in range(n):
                    # matrix[src][via] + matrix[via][dst] is the distance from src to dst via the vertex via
                    distance=matrix[src][via]+matrix[via][dst]
                    matrix[src][dst]=min(matrix[src][dst],distance)
        
        # negative cycles
        for i in range(n):
            if matrix[i][i]<0:
                print("Negative cycle detected")
        # replace infinity with -1
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==float('inf'):
                    matrix[row][col]=-1

        return matrix



s=Solution()
matrix = [[0, 5, -1, 10],
          [-1, 0, 3, -1],
          [-1, -1, 0, 1],
          [-1, -1, -1, 0]]
print(s.shortest_distance(matrix)) # [[0, 5, 8, 9], [-1, 0, 3, 4], [1000000000, 1000000000, 0, 1], [1000000000, 1000000000, 1000000000, 0]]

mat = [[0, 25], [-1, 0]]
print(s.shortest_distance(mat)) # [[0, 25], [-1, 0]]
