from linked_list import LinkedList

def mergeLists(a, b):
	a_curr = a.head
	b_curr = b.head
	ret = LinkedList(None)
	if a_curr.data < b_curr.data:
		ret.head = a_curr
		a_curr = a_curr.next
	else:
		ret.head = b_curr
		b_curr = b_curr.next

	ret.head.next = None # since insertTail/Head doesn't work with current LL implementation

	while a_curr or b_curr:
		if not a_curr:
			ret.insertTail(b_curr)
			b_curr = b_curr.next
		elif not b_curr:
			ret.insertTail(a_curr)
			a_curr = a_curr.next
		elif a_curr.data < b_curr.data:
			ret.insertTail(a_curr)
			a_curr = a_curr.next
		elif b_curr.data < a_curr.data:
			ret.insertTail(b_curr)
			b_curr = b_curr.next	

	return ret


a = LinkedList.from_list(["a", "c", "e", "g"])
b = LinkedList.from_list(["b", "d", "f", "h", "z", "z", "z"])

merged = mergeLists(a, b)
print(merged)