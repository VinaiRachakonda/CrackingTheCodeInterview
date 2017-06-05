import unittest

# take the last element each time and recurively to front


def reverseHelper(input):
	if len(input) == 1:
		return input

	return input[len(input)-1:len(input)] + reverseHelper(input[0:len(input)-1])


def reverseCString(input):
	if len(input) == 1:
		return input

	remainder = input[0:len(input)-1]

	return reverseHelper(remainder) + "\0"



class testCases(unittest.TestCase):

	def test_singleton(self):
		self.assertEquals("\0", reverseCString("\0"))

	def test_len2(self):
		self.assertEquals("c\0", reverseCString("c\0"))

	def test_long(self):
		self.assertEquals("cba\0", reverseCString("abc\0"))

if __name__ == '__main__':
    unittest.main()


#Analysis

# I think this is a solid solution. O(n) complexitiy. 
# Written recursivley for eleganc/ But definitely this
# isn't my cleanest code
#
#