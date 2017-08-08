# find the largest integer k for a given list such that there are at least
# k elements in the list >= k

def largest_k(arr):
	size = max(arr)
	if size == 0:
		return 0
	a = [0 for _ in range(size + 1)]
	b = [0 for _ in range(size + 1)]
	for x in arr:
		a[x] += 1

	b[-1] = a[-1]
	for x in range(len(b) - 2, -1, -1):
		b[x] = a[x] + b[x + 1]

	for x in range(len(b) - 1, -1, -1):
		if x <= b[x]:
			print(a, b)
			return x

b = [0, 1]
print(largest_k(b))

# time & space complexity: O(k), where k is the greatest element in list