graph = {1 : [2, 3],
		 2 : [1, 4],
		 3 : [1, 5],
		 4 : [2],
		 5 : [3, 6],
		 6 : [5]}


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


def dfs(node, dest, path, visited=set()):
	print(node)
	visited.add(node)
	path.append(node)
	if node == dest:
		print(path)
		return
	else:
		for adj in graph.get(node):
			if adj not in visited:
				dfs(adj, dest, path, visited)
				path.pop()


dfs(1, 6, [])