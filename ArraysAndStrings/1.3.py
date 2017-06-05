# First idea is to hash while iterating and removing if key is seen
# Hashing would be O(1) time. Total O(n). 

# From problem 1.1 the ascii array seems like a more efficient idea

import unittest


def removeDuplicates(input):
	boolA = [False] * 256

	ret = ""
	for i in range(0, len(input)):
		if (not boolA[ord(input[i])]):
			boolA[ord(input[i])] = True
			ret = ret + input[i]
			
	return ret

class TestCases(unittest.TestCase):
	def test_no_change(self):
		self.assertEquals('vina', removeDuplicates('vina'))

	def test_last_letter(self):
		self.assertEquals('vina', removeDuplicates('vinai'))

	def test_very_long(self):
		self.assertEquals('ban', removeDuplicates('banana'))

	def test_very_empty(self):
		self.assertEquals('', removeDuplicates(''))

	def test_singleton(self):
		self.assertEquals('s', removeDuplicates('s'))

	def test_odd_symbols(self):
		self.assertEquals('s!&8', removeDuplicates('s!!&8&'))

if __name__ == '__main__':
    unittest.main()