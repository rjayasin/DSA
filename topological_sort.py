# Topological sort
from collections import deque

GRAPH = {
	'A': {'C'},
	'B': {'C', 'D'},
	'C': {'E'},
	'D': {'F'},
	'E': {'F', 'H'},
	'F': {'G'},
	'G': {},
	'H': {}
}

def topo_sort(graph):
	stack = []
	visited = set()
	for node in graph:
		if node not in visited:
			dfs(graph, node, visited, stack)
	return list(reversed(stack))

def dfs(graph, node, visited, stack):
	visited.add(node)
	for adj in graph[node]:
		if adj not in visited:
			dfs(graph, adj, visited, stack)
	stack.append(node)

if __name__ == '__main__':
	a = topo_sort(GRAPH)
	print(a)