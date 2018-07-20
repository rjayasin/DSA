# djikstra graph algorithm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

graph = {1: [2, 3, 6],
         2: [1, 3, 4],
         3: [1, 2, 4, 6],
         4: [2, 3, 5],
         5: [4, 6],
         6: [1, 3, 5]}

weights = {(1, 2): 7,
           (1, 3): 9,
           (1, 6): 14,
           (2, 3): 10,
           (2, 4): 15,
           (3, 4): 11,
           (3, 6): 2,
           (4, 5): 6,
           (5, 6): 9}

def weight(i):
    return weights.get((i[0], i[1])) if weights.get((i[0], i[1])) else weights.get((i[1], i[0]))

def djikstra(graph, weights, source, destination):
    # unvisited set
    Q = set()
    # distances to source
    dist = {}
    # previous node in optimal path
    prev = {}

    for node in graph:
        dist[node] = float('inf')
        prev[node] = None
        Q.add(node)

    dist[source] = 0
    curr = None

    while Q:
        m = float('inf')
        for q in Q:
            if dist[q] < m:
                curr = q
        print(Q, curr)
        Q.remove(curr)
        for adj in graph[curr]:
            alt = dist[curr] + weight((curr, adj))
            if alt < dist[adj]:
                dist[adj] = alt
                prev[adj] = curr

    return dist, prev

x, y = djikstra(graph, weights, 1, 5)
print(x, y)
