# sum of a list that can contain nested lists
def nested_sum(a):
	sumSoFar = 0
	for x in a:
		if(isinstance(x, list)):
			sumSoFar += nested_sum(x)
		else:
			sumSoFar += x;
	return sumSoFar


x = [1, [1, 1], 1, [[1, 1], 1]]
print(nested_sum(x))