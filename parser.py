

# Basic Input
"""
x...
x...
xx..
n
x...
xx..
....
"""
class Parser():
	def parse(self, input):
		return  [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]





import unittest
class Test(unittest.TestCase):
	def test_parse(self):
		input = """x...
					x...
					....
					....
				"""
		result = [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
		self.assertEquals(result, Parser().parse(input))
	def test_parse_empty_layer(self):
		input = """
				....
				....
				....
				.... 
				"""


if __name__ == "__main__":
    unittest.main() 

