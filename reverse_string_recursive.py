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

# keep taking characters off
# add our first char to end of string
def rev_string(string):
	print(string)
	if len(string) == 1:
		return string
	return rev_string(string[1:]) + string[0]

a = "abcd"
b = rev_string(a)
print(b)