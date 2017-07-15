class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)


class LinkedList:
	def __init__(self, head):
		if(type(head) == "Node"):
			self.head = head
		else:
			h = Node(head)
			self.head = h

	@classmethod
	def from_list(cls, elems):
		head = Node(elems[-1])
		ret = cls(head)
		elems = elems[:-1]
		for x in reversed(elems):
			add = Node(x)
			ret.insertHead(add)
		return ret

	def __str__(self):
		iterate = self.head
		ret = ""
		while iterate:
			ret += str(iterate.data) + " "
			iterate = iterate.next
		return ret

	def insertHead(self, data):
		new = Node(data)
		new.next = self.head
		self.head = new

	def search(self, data):
		iterate = self.head
		while iterate:
			if iterate.data == data:
				return iterate
			iterate = iterate.next
