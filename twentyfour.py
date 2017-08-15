# given 4 random numbers find whether or not they can be arranged
# with mathematical operators (+ - * /) to form an equation to 
# equal 24


# brute force solution that does not use extra space (generator for permuations)
# go through every permutation of the input
# apply every operator in every space left to right ignoring operator precedence
# complexity: 4! permuations * 4^3 operators = 1536 maximum operations
import itertools
from random import randrange

def twenty_four(nums):
	operators = ["+", "*", "-", "/"]
	for perm in itertools.permutations(nums):
		for op1 in operators:
			for op2 in operators:
				for op3 in operators:
					result = a_op(a_op(a_op(nums[0], nums[1], op1), nums[2], op2), nums[3], op3)
					if result == 24:
						print(nums[0], op1, nums[1], op2, nums[2], op3, nums[3])
						return True
	return False


def a_op(a, b, op):
	if op == "+":
		return a + b
	elif op == "*":
		return a * b
	elif op == "-":
		return a - b
	elif op == "/":
		return a / b


a = [randrange(1, 10) for _ in range(4)]
print(a)
b = twenty_four(a)
print(b)