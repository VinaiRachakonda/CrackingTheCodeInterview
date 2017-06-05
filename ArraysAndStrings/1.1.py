import unittest


# part 1 
# This method employs hashing each char as a key. Collisions imply
# the string is not unique 
def hasUnqiueChars(input):
	dict = {}
	keyCounter = 0 # dummy value

	# now conver each string as character equiv
	for char in input:
		dict[ord(char)] = keyCounter
		keyCounter = keyCounter + 1

	return len(dict) == len(input)



# Test Cases
class TestCases(unittest.TestCase):
	def test_simple_yes(self):
		self.assertTrue(hasUnqiueChars('a'))

	def test_simple_no(self):
		self.assertFalse(hasUnqiueChars('aa'))

	def test_long_word(self):
		self.assertTrue(hasUnqiueChars('afsepq'))

	def test_long_word2(self):
		self.assertFalse(hasUnqiueChars('afsepqf'))

# part 2 using no additional data structures
# This method uses sorting of chars. Only a list is needed
def hasUniqueChars2(input):
	# convert input string to numbers
	newString = []
	for i in range(0, len(input)):
		newString.append(ord(input[i]))

	# sort the numbers 
	sorted2 = sorted(newString)

	before = sorted2[0]
	for j in range(1, len(sorted2)):
		if (before == sorted2[j]):
			return False
		before = sorted2[j]

	return True


class TestCases2(unittest.TestCase):
	def test_simple_yes2(self):
		self.assertTrue(hasUniqueChars2('a'))

	def test_simple_no2(self):
		self.assertFalse(hasUniqueChars2('aa'))

	def test_long_word2(self):
		self.assertTrue(hasUniqueChars2('afsepq'))

	def test_long_word22(self):
		self.assertFalse(hasUniqueChars2('afsepqf'))


if __name__ == '__main__':
    unittest.main()


# Analysis

# After reading the solution the better idea would have been to use a boolean array for each
# ascii character. Hashing would be too expensive on extremely long string. Need to consider such 
# simple array options in the future.











