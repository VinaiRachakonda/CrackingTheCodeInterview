import unittest

class Node(object):
	
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

	def getNodeVal(self):
		return self.val

	def setNodeVal(self, val):
		self.val = val

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setNext(self, node):
		self.next = node

	def setPrev(self, node):
		self.prev = node

	def hasNext(self):
		return self.next is not None

	def hasPrev(self):
		return self.prev is not None


class LinkedList(object):

	def __init__(self, val):
		if val == None:
			self.head = None
		else:
			self.head = Node(val)

	def addNode(self, node):
		if self.head is None:
			self.head = node
			return 

		curr = self.head
		while curr.hasNext():
			curr = curr.getNext()
		curr.setNext(node)

	def prepend(self, node):
		if self.head is None:
			self.head = node
			return 

		self.head.setPrev(node)
		node.setNext(self.head)
		self.head = self.head.getPrev()

	def getLength(self):
		curr = self.head
		c = 0
		while curr != None:
			curr = curr.getNext()
			c = c + 1
		return c

	def getHead(self):
		return self.head

	def equals(self, l2):
		if self.getLength() != l2.getLength():
			return False	
		else:
			c = self.head
			c1 = l2.getHead()

			while c.hasNext() and c1.hasNext():
				if c.getNodeVal() != c1.getNodeVal():
					return False	
				c = c.getNext()
				c1 = c1.getNext()
		return True

class TestCases(unittest.TestCase):
	def test_create(self):
		n = Node(5)
		l = LinkedList(6)
		self.assertEqual(5, n.getNodeVal())


	def test_simple_length(self):
		l = LinkedList(6)
		self.assertEqual(1, l.getLength())


	def test_append(self):
		n = Node(5)
		l = LinkedList(6)
		l.addNode(n)
		self.assertEqual(2, l.getLength())


if __name__ == '__main__':
    unittest.main()




