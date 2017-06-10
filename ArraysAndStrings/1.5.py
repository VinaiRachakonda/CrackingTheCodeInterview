import unittest


def replaceSpace(input):
	return input.replace(' ', "%20")


class TestCases(unittest.TestCase):
	def test_simple_case(self):
		self.assertEqual("h%20l", replaceSpace("h l"))


	def test_multiple_spaces(self):
		self.assertEqual("p%20%20%20p", replaceSpace("p   p"))

if __name__ == '__main__':
    unittest.main()

