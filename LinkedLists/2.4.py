import unittest
from LinkedListImpl import Node 
from LinkedListImpl import LinkedList

def sumReversedLinkedLists(l1, l2):
	if l1 is None or l2 is None:
		return LinkedList(None)

	# initial computation to deal with annoying constructor
	curr1 = l1.getHead()
	curr2 = l2.getHead()
	ret = LinkedList(None)
	to_add = 0
	while curr1 is not None and curr2 is not None:
		val1 = curr1.getNodeVal()
		val2 = curr2.getNodeVal()

		if val1 + val2 + to_add >= 10:
			new_node = Node(val1 + val2 - 10)
			to_add = 1
		else:
			new_node = Node(val1 + val2 + to_add)
			to_add = 0

		ret.prepend(new_node)
		curr1 = curr1.getNext()
		curr2 = curr2.getNext()


	if curr1 is None and curr2 is not None:
		while curr2 is not None:
			val = curr2.getNodeVal()
			if val + to_add >= 10:
				new_node = Node(val + to_add - 10)
				to_add = 1
			else:
				new_node = Node(val + to_add)
				to_add = 0
			ret.prepend(new_node)
			curr2 = curr2.getNext()

	if curr1 is not None and curr2 is None:
		while curr1 is not None:
			val = curr1.getNodeVal()
			if val + to_add >= 10:
				new_node = Node(val + to_add - 10)
				to_add = 1
			else:
				new_node = Node(val + to_add)
				to_add = 0
			ret.prepend(new_node)
			curr1 = curr1.getNext()

	if to_add == 1:
		ret.prepend(Node(1))

	return ret


class TestCases(unittest.TestCase):

	def test_singleton(self):
		l1 = LinkedList(6)
		l2 = LinkedList(6)

		ret = LinkedList(2)
		ret.prepend(Node(1))
		
		self.assertTrue(ret.equals(sumReversedLinkedLists(l1, l2)))

	def test_unbalanced_l1(self):
		l1 = LinkedList(6)
		l1.addNode(Node(7))
		l2 = LinkedList(6)

		ret = LinkedList(2)
		ret.prepend(Node(8))
		
		self.assertTrue(ret.equals(sumReversedLinkedLists(l1, l2)))

	def test_book_sample(self):
		l1 = LinkedList(3)
		l1.addNode(Node(1))
		l1.addNode(Node(5))
		l2 = LinkedList(5)
		l2.addNode(Node(9))
		l2.addNode(Node(2))

		ret = LinkedList(8)
		ret.addNode(Node(0))
		ret.addNode(Node(8))

		self.assertTrue(ret.equals(sumReversedLinkedLists(l1, l2)))



if __name__ == '__main__':
    unittest.main()