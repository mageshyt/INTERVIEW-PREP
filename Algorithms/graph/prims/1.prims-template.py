
import heapq
def minimumSpanningTree( edges: list[list[int]], n: int) -> int:
    visited = set()  

    graph={i:[] for i in range(1,n+1)}
    for src,dst in edges:
        graph[src].append([dst,1])
        graph[dst].append([src,1])

    heap = [] # (weight,src,dst)
    mst = []
    for neighbor,weight in graph[1]:
        heapq.heappush(heap,(weight,1,neighbor)) # (weight,src,dst)

    visited.add(1) # start from node 1

    while heap:
        weight,src,dst = heapq.heappop(heap)
        if dst in visited:
            continue
        visited.add(dst)
        mst.append((src,dst,weight)) # add the edge to the mst

        for neighbor,weight in graph[dst]:
            if neighbor not in visited:
                heapq.heappush(heap,(weight,dst,neighbor))
    print(mst)
    return sum([weight for src,dst,weight in mst])


# Time complexity : O(ElogV) where E is the number of edges and V is the number of vertices
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges

print("TEST CASE")
edges = [[1,2],[2,3],[3,4],[4,1]]
n = 4
print(minimumSpanningTree(edges,n)) # 6


