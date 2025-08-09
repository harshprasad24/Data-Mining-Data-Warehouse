def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

start_node = input("Enter the starting node: ")

visited = []
print("DFS traversal:")
dfs(visited, graph, start_node)