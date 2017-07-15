def reverseStringRecursive(string, l, r):
	if l <= r:
		x = list(string)
		temp = x[l]
		x[l] = x[r]
		x[r] = temp
		l += 1
		r -= 1
		return reverseStringRecursive("".join(x), l, r)
	else:
		return string

a = "123456789"
b = reverseStringRecursive(a, 0, len(a) - 1)
print(b)