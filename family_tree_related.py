# given a family tree of people and two people
# return whether or not the two people are related.
# design of the family tree is up to you

# graph search problem
# design nodes to separate parents from children
# two people are related if they have an ancestor in common
from collections import deque

class Person():
	def __init__(self, name, parent1, parent2):
		self.name = name
		self.parents = [parent1, parent2]

	def __repr__(self):
		return self.name


# do a bidirectional BFS where you only add parents as adjacent nodes
def find_related(person1, person2):
	q1 = deque()
	q2 = deque()
	ancestors = set()
	q1.append(person1)
	q2.append(person2)
	cont_1 = cont_2 = True
	while cont_1 or cont_2:
		print(q1, q2, ancestors)
		if q1:
			curr_1 = q1.popleft()
			if curr_1 in ancestors:
				return True
			for p in curr_1.parents:
				if p: # guard against null parents
					if p in ancestors:
						return True
					else:
						ancestors.add(p)
						q1.append(p)
		else:
			cont_1 = False

		if q2:
			curr_2 = q2.popleft()
			if curr_2 in ancestors:
				return True
			for p in curr_2.parents:
				if p: # guard against null parents
					ancestors.add(p)
					q2.append(p)
		else:
			cont_2 = False
	return False


def test_find_related():
	A = Person('A', None, None)
	B = Person('B', None, None)
	C = Person('C', A, B)
	D = Person('D', A, B)
	E = Person('E', None, None)
	F = Person('F', D, E)
	print(find_related(C, F))
	print(find_related(B, E))

if __name__ == '__main__':
	test_find_related()