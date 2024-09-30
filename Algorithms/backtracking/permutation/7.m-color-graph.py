def graphColoring(graph, m, N):
    color = [0] * N
    if solve(0,color,m,graph,N) :
        return True
    return False

def isSafe(node,color,graph,n,col):
    # check if the node is connected to any other node with the same color
    for i in range(n):
        if graph[node][i] == 1 and color[i] == col:
            return False

    return True

def solve(node,color,m,graph,n):
    if node==n:
        return True

    # Try all colors 
    for i in range(1,m+1):
        if isSafe(node,color,graph,n,i):
            # assign the color and move to the next node
            color[node]=i
            if solve(node+1,color,m,graph,n):
                return True
            # backtrack
            color[node]=0

    return False
# Test cases
