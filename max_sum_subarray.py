# given an array, find the subarray that will yield the maximum sum
# sometimes posed as when should you buy / sell a stock given a list of prices
import random

# using kandane's algorithm
def kandane(nums):
	deltas = []
	for x in range(1, len(nums)):
		deltas.append(nums[x] - nums[x - 1])
	print(deltas)

	maxSoFar = maxEndingHere = 0
	for x in range(len(deltas)):
		maxEndingHere += deltas[x]
		if maxEndingHere < 0:
			maxEndingHere = 0

		if maxSoFar < maxEndingHere:
			maxSoFar = maxEndingHere
			sell = x + 1

	return maxSoFar


a = [random.randrange(1, 20) for _ in range(10)]
print(a)
b = kandane(a)
print(b)