from collections import deque
import heapq

def parse_graph_input():
    """
    Takes graph input from user in terminal.
    Format example:
    4
    1 2
    1 3
    2 4
    3 4
    (First line = number of nodes, next lines = edges u v)
    """
    graph = {}
    n = int(input().strip())

    for i in range(1, n+1):
        graph[i] = []

    print("Enter edges (u v). Type 'done' when finished:")

    while True:
        line = input().strip()
        if line.lower() == "done":
            break
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)  # remove this if you want directed graph

    return graph

def bfs_graph(adj, start):
    visited = set([start])
    order = []
    q = deque([start])

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order

def dfs_graph(adj, start):
    visited = set()
    order = []
    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                dfs(v)
    dfs(start)
    return order

def dijkstra_graph(adj, start):
    """
    For weighted graph input
    Expected format for adj:
    {1: [(2,4), (3,1)], 2:[(4,2)], 3:[(4,5)], 4:[]}
    """
    dist = {node: float('inf') for node in adj}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

# Example run
if __name__ == "__main__":
    g = parse_graph_input()
    print("Graph:", g)
    print("BFS:", bfs_graph(g, 1))
    print("DFS:", dfs_graph(g, 1))
