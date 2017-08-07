graph = {1 : [2, 3],
		 2 : [1, 4],
		 3 : [1, 4, 5],
		 4 : [2, 3, 6],
		 5 : [3, 6, 7],
		 6 : [4, 5],
		 7 : [5]}


def bfs(start):
	q = []
	visited = set()
	q.append(start)
	visited.add(start)
	while(q):
		curr = q.pop(0)
		print(curr)
		for adj in graph.get(curr):
			if(adj not in visited):
				q.append(adj)
				visited.add(adj) # mark current as visited


def dfs(node, visited=set()):
	print(node)
	visited.add(node)
	for adj in graph.get(node):
		if adj not in visited:
			dfs(adj, visited)


bfs(1)
dfs(1)