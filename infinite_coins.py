# given an infinite number of coins (quarters nickels dimes pennies)
# count the number of ways you can make n cents

# recursively subtract all denominations from n
# if N == 0 increment counter
from collections import Counter
def wrapper(n):
	def infinite_coins(n, coins):
		# base case TODO
		print(n)
		if n == 0:
			infinite_coins.counter += 1
			infinite_coins.ways.append(coins)
			infinite_coins.memo[n]
			return
		elif n < 0:
			return
		elif n in infinite_coins.memo:
			return infinite_coins.memo[n]
		for coin in [25, 10, 5, 1]:
			infinite_coins(n - coin, coins + [coin])
	infinite_coins.counter = 0
	infinite_coins.ways = []
	infinite_coins.memo = {}
	infinite_coins(n, [])
	return infinite_coins.counter, infinite_coins.ways

def dedup_ways(ways):
	counts = [Counter(x) for x in ways]
	no_dupes = [a for a in counts if a not in no_dupes]

a = 17
x, ways = wrapper(a)
print(x, ways)
# dedup_ways(ways)
