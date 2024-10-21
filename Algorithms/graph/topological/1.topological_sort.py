

from collections import defaultdict
def topologicalSort(edges,n):
    adj=defaultdict(list)

    for src,dst in edges:
        adj[src].append(dst)


    visited=set() # to make sure we are not visiting the same node again
    top_order=[]

    for i in range(1,n+1):
        dfs(i,adj,visited,top_order)

    top_order.reverse()

    return top_order


def dfs(src,adj,visited,top_order):
    if src in visited:
        return

    visited.add(src)

    for dst in adj[src]: # go through all the neighbours of the src
        dfs(dst,adj,visited,top_order)

    top_order.append(src)

def find_indegree(graph):
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree

from collections import deque
def topo_sort(edges):

    graph = defaultdict(list)

    for src,dst in edges:
        graph[src].append(dst)



    res = []
    q = deque()
    indegree = find_indegree(graph)
    print(indegree)
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    print()
    return res if len(graph) == len(res) else None

def main():
    n=6
    edges=[[1,2],[1,3],[2,4],[2,5],[3,4],[3,6],[4,6],[5,6]]
    print(topologicalSort(edges,n))
    print(topo_sort(edges))

main()
