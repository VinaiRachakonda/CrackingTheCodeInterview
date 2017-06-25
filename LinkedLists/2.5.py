import unittest
from LinkedListImpl import LinkedList
from LinkedListImpl import Node


def findHeadofCycle(input):

	p1 = input.getHead()
	p2 = input.getHead()

	while p2.hasNext():
		p1 = p1.getNext()
		p2 = p2.getNext().getNext()

		if p1.getNodeVal() == p2.getNodeVal():
			break

	p1 = input.getHead()

	while p1.getNodeVal() != p2.getNodeVal():
		p1 = p1.getNext()
		p2 = p2.getNext()


	return p1.getNodeVal()



class TestCases(unittest.TestCase):

	def test_self_loop_singleton(self):
		l = LinkedList(6)
		l.getHead().setNext(l.getHead())

		self.assertEquals(6, findHeadofCycle(l))

	def test_simple_cycle_from_head(self):
		l = LinkedList(6)
		l.addNode(Node(7))
		l.addNode(l.getHead())

		self.assertEquals(6, findHeadofCycle(l))

	def test_given_example(self):
		l = LinkedList(1)
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)
		n5 = Node(5)

		l.addNode(n2)
		l.addNode(n3)
		l.addNode(n4)
		l.addNode(n5)
		l.addNode(n3)


		self.assertEquals(3, findHeadofCycle(l))

if __name__ == '__main__':
    unittest.main()