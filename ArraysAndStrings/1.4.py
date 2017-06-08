# Write a maethod to decide if two strings are anagrams or not

# The idea here is to keep a counter of the number of times a character has been
# seen in both strings. For each character, if the # of times they've
# been seen is the same then they must be anagrams.null=

# I assume we are only using ASCII Characters. So hashing will not
# be necessary
import unittest


def isAnagram(str1, str2):
	arr1 = [0] * 256
	arr2 = [0] * 256

	for c in str1:
		arr1[ord(c)] = arr1[ord(c)] + 1


	for c2 in str2:
		arr2[ord(c2)] = arr2[ord(c2)] + 1 


	for i in range(0, len(arr1)):
		if (arr1[i] != arr2[i]):
			return False	


	return True



class TestCases(unittest.TestCase):
	def test_simple_case(self):
		self.assertTrue(isAnagram("a", "a"))


	def test_simple_false_case(self):
		self.assertFalse(isAnagram("a", "b"))

	def test_longer(self):
		self.assertTrue(isAnagram("abc", "cba"))

	def test_longer_false(self):
		self.assertFalse(isAnagram("banana", "ananaab"))

if __name__ == '__main__':
    unittest.main()