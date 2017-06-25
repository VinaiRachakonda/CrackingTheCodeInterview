import unittest

def rotate(matrix, n):

	# Step 1 transpose

	for i in range(0, n):
		for j in range(i, n):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp



	# Step 2 flip 

	for i in range(0, n):
		for j in range(0, n/2):
			temp = matrix[i][j]
			matrix[i][j] = matrix[i][n-1-j]
			matrix[i][n-1-j] = temp

	return matrix

class TestCase(unittest.TestCase):

	def test_two_by_two(self):
		input = [[1, 2],
				[3, 4]]
		output = [[3, 1],
				  [4, 2]]

	  	self.assertEquals(output, rotate(input, 2))

  	def test_three_by_three(self):
  		input = [[1, 2, 3],
  				 [4, 5, 6],
  				 [7, 8, 9]]
		output = [[7, 4, 1],
				  [8, 5, 2],
				  [9, 6, 3]]
	  	self.assertEquals(output, rotate(input, 3))


if __name__ == '__main__':
    unittest.main()

