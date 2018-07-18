# given two sorted arrays of equal length find the number of elements in common

# use 2 index pointers. if current elements are equal add to list
# if not, advance curr pointer until not curr is >= other.
# swap current pointer/list
# keep going until 1 pointer reaches the end
def find_common(a, b):
	ci = 0
	oi = 0 
	curr = a
	other = b
	ret = []
	while ci < len(a) - 1 or oi < len(a) - 1:
		if curr[ci] == other[oi]:
			ret.append(curr[ci])
			ci += 1
		else:
			while not curr[ci] >= other[oi]:
				ci += 1
		curr, other = other, curr
		ci, oi = oi, ci
	return ret

a = [13, 14, 17, 27, 35, 40, 49, 55, 59]
b = [17, 18, 19, 35, 39, 40, 55, 58, 60]
x = find_common(a, b)
print(x)