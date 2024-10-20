
# bfs tempalte

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited = set()
    visited.add(start)

    while queue:
        node = queue.pop(0)
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing work


# dfs template

def dfs(node, visited):
    if node in visited:
        return

    visited.add(node)

    # process current node here
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)

    
