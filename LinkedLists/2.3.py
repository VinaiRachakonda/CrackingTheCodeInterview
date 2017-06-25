import unittest
from LinkedListImpl import Node 
from LinkedListImpl import LinkedList

def deleteGivenNode(node, l):
	if not node.hasNext():
		return l


	#Replace next nodes value with this node's value

	val = node.getNext().getNodeVal()
	new_next = node.getNext().getNext()

	node.setNodeVal(val)
	node.setNext(new_next)


class TestCases(unittest.TestCase):

	def test_singleton_does_nothing(self):
		l1 = LinkedList(6)
	
		ret = deleteGivenNode(l1.getHead(), l1)
		self.assertEquals(1, l1.getLength())
		

	def test_two_nodes(self):
		l1 = LinkedList(6)
		n = Node(7)
		l1.addNode(n)

		ret = deleteGivenNode(l1.getHead(), l1)
		self.assertEquals(1, l1.getLength())
		self.assertEqual(7, l1.getHead().getNodeVal())
		
	def test_three_nodes_middle(self):
		l1 = LinkedList(6)
		n = Node(7)
		n2 = Node(8)
		l1.addNode(n)
		l1.addNode(n2)

		ret = deleteGivenNode(l1.getHead().getNext(), l1)
		self.assertEquals(2, l1.getLength())
		self.assertEqual(6, l1.getHead().getNodeVal())
		self.assertEqual(8, l1.getHead().getNext().getNodeVal())



if __name__ == '__main__':
    unittest.main()