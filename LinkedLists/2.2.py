import unittest
from LinkedListImpl import Node 
from LinkedListImpl import LinkedList


def getNthLastElement(input, n):
	if n < 1:
		return None

	p1 = input.getHead()
	p2 = input.getHead()

	counter = 0
	while (counter < n - 1 and p2 is not None):
		p2 = p2.getNext()
		counter = counter + 1

	# n > lenght of list
	if p2 is None:
		return p1

	while p2.hasNext():
		p2 = p2.getNext()
		p1 = p1.getNext()


	return p1


class TestCases(unittest.TestCase):

	def test_singleton(self):
		l = LinkedList(6)
		self.assertEquals(None, getNthLastElement(l, 0))


	def test_middle_element(self):
		l = LinkedList(6)
		l.addNode(Node(7))
		l.addNode(Node(8))
		self.assertEquals(7, getNthLastElement(l, 2).getNodeVal())

	def test_last_element(self):
		l = LinkedList(6)
		l.addNode(Node(7))
		l.addNode(Node(8))
		l.addNode(Node(1212))
		self.assertEquals(1212, getNthLastElement(l, 1).getNodeVal())

	def test_long_list(self):
		l = LinkedList(1)
		for i in range(0, 11):
			l.addNode(Node(i))

		self.assertEquals(8, getNthLastElement(l, 3).getNodeVal())

	def test_big_n(self):
		l = LinkedList(1)
		for i in range(0, 10):
			l.addNode(Node(i))

		self.assertEquals(1, getNthLastElement(l, 1000).getNodeVal())


if __name__ == '__main__':
	unittest.main()