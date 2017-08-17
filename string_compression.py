# given a string return a compressed version
# e.g. aabbbcddd -> a2b3c1d3

# walk through string keeping track of current character
# and the current count
# when next char is different from prev char, end that segment, start new
def compress(string):
	ret = []
	count = 1
	curr = string[0]
	for ind in range(1, len(string)):
		if string[ind] == curr:
			count += 1
			if ind == len(string) - 1:
				ret.append(curr)
				ret.append(str(count))
		elif string[ind] != curr:
			ret.append(curr)
			ret.append(str(count))
			count = 1
			curr = string[ind]
	return "".join(ret)

x = compress("aabbbcddd")
print(x)
