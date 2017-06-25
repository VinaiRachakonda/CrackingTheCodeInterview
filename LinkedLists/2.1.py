import unittest
from LinkedListImpl import Node 
from LinkedListImpl import LinkedList

def removeDuplicatedWithoutBuffer(input):
	curr = input.getHead()

	while curr != None:
		val = curr.getNodeVal()
		prev = curr
		explorer = curr.getNext()
		while (explorer != None):
			if explorer.getNodeVal() == val:
				prev.setNext(explorer.getNext())
			else:
				prev = explorer
			explorer = explorer.getNext()
		curr = curr.getNext()

	return input



class TestCases2(unittest.TestCase):

	def test_noChange(self):
		l = LinkedList(6)
		n1 = Node(7)

		l.addNode(n1)

		self.assertTrue(l.equals(removeDuplicatedWithoutBuffer(l)))

	def test_list_all_same(self):
		l = LinkedList(6)
		n1 = Node(6)
		n2 = Node(6)

		l.addNode(n1)
		l.addNode(n2)

		self.assertEquals(1, removeDuplicatedWithoutBuffer(l).getLength())

	def test_list_one_repeat(self):
		l = LinkedList(6)
		n1 = Node(7)
		n2 = Node(6)

		l.addNode(n1)
		l.addNode(n2)	
		ans = removeDuplicatedWithoutBuffer(l)
		self.assertEquals(2, ans.getLength())
		arr = [6, 7]

		head = ans.getHead()
		i = 0
		while head.hasNext():
			self.assertEquals(arr[i], head.getNodeVal())
			i = i + 1
			head = head.getNext()


def removeDuplicatesWithBuffer(input):
	seen = {}
	kVal = 'SEEN'

	curr = input.getHead()
	prev = None

	while curr != None:
		# in case we've seen
		val = curr.getNodeVal()
		if val in seen:
			prev.setNext(curr.getNext())
		else:
			seen[val] = kVal
			prev = curr

		curr = curr.getNext()

	return input


class TestCases(unittest.TestCase):

	def test_noChange(self):
		l = LinkedList(6)
		n1 = Node(7)

		l.addNode(n1)

		self.assertTrue(l.equals(removeDuplicatesWithBuffer(l)))

	def test_list_all_same(self):
		l = LinkedList(6)
		n1 = Node(6)
		n2 = Node(6)

		l.addNode(n1)
		l.addNode(n2)

		self.assertEquals(1, removeDuplicatesWithBuffer(l).getLength())

if __name__ == '__main__':
    unittest.main()