import unittest


def isSubstring(s1, s2):
	return s2 in s1


def isRotation(s1, s2):

	if (len(s1) != len(s2)):
		return false

	ccat = s1 + s1

	return isSubstring(ccat, s2)


class TestCases(unittest.TestCase):
	def test_simple_no(self):
		self.assertFalse(isRotation("a", "b"))

	def test_simple_yes(self):
		self.assertTrue(isRotation("ab", "ba"))

	def test_complex_yes(self):
		self.assertTrue(isRotation("erbottlewat", "waterbottle"))

if __name__ == '__main__':
    unittest.main()
