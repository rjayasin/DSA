from collections import deque

graph = {1 : [2, 3],
		 2 : [1, 4],
		 3 : [1, 5],
		 4 : [2],
		 5 : [3, 6],
		 6 : [5]}


def bfs(start, end):
	q = deque()
	visited = set()
	q.append((start, [start]))
	visited.add(start)
	while(q):
		curr = q.popleft()
		print(curr)
		if curr[0] == end:
			return curr[1]
		for adj in graph.get(curr[0]):
			if(adj not in visited):
				q.append((adj, curr[1] + [adj]))
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


if __name__ == '__main__':
	# dfs(1, 6, [])
	a = bfs(1, 6)
	print(a)