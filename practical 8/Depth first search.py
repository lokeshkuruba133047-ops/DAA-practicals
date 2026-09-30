import time


n = int(input("Enter number of vertices: "))


graph = [[] for _ in range(n)]


e = int(input("Enter number of edges: "))


print("Enter edges (u v):")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  
start = int(input("Enter starting vertex: "))

visited = [False] * n
dfs_result = []

def dfs(vertex):
    visited[vertex] = True
    dfs_result.append(vertex)

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs(neighbour)

start_time = time.perf_counter()

dfs(start)

end_time = time.perf_counter()

print("DFS Traversal:", dfs_result)
print("Execution Time:", end_time - start_time, "seconds")
print("Time Complexity: O(V + E)")
