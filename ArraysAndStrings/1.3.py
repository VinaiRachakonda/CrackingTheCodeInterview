import unittest

def removeDuplicatesWithBuffer(input):
	boolA = [False] * 256

	ret = ""
	for i in range(0, len(input)):
		if (not boolA[ord(input[i])]):
			boolA[ord(input[i])] = True
			ret = ret + input[i]
		
	return ret

class TestCases(unittest.TestCase):
	def test_no_change(self):
		self.assertEquals('vina', removeDuplicatesWithBuffer('vina'))

	def test_last_letter(self):
		self.assertEquals('vina', removeDuplicatesWithBuffer('vinai'))

	def test_very_long(self):
		self.assertEquals('ban', removeDuplicatesWithBuffer('banana'))

	def test_very_empty(self):
		self.assertEquals('', removeDuplicatesWithBuffer(''))

	def test_singleton(self):
		self.assertEquals('s', removeDuplicatesWithBuffer('s'))

	def test_odd_symbols(self):
		self.assertEquals('s!&8', removeDuplicatesWithBuffer('s!!&8&'))

if __name__ == '__main__':
    unittest.main()