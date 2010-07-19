from possibility import Possibility

class Matcher(object):

	def __init__(self):
		self.solution = (2 ** 64 - 1)

	def match(self, possibility):
		sum = 0b00
		for piece in possibility.pieces:
			sum ^= piece
		return sum == self.solution
	
	def areTheyFitting(self, piece1, piece2):
		return (piece1 & piece2) == 0

	def evaluate(self, possibility):
		best_fit = {}
		for piece in possibility.pieces:
			best_fit[piece] = [piece]
			for test in possibility.pieces:
				if (self.areTheyFitting(piece, test) and self.doesItFitWithGroup(test, best_fit[piece])):
					best_fit[piece].append(test)
								
		the_best = max([len(s) for s in best_fit.values()])
		possibility.pieces_fitted = [s for x, y in best_fit.items() if the_best == len(y)][0]	

	def doesItFitWithGroup(self, piece, group): 			
		for item in group:
			if not self.areTheyFitting(item, piece):
				return False
		return True

	"""

		1 2 3 4 5 6
		

	def merge(self, data):
		for i in range()
			Possibility(data[0][i], 
				    data[1][i], 
			 	    data[2][i],
				    data[3][i],
				    data[4][i],
				    data[5][i], 
				    data[6][i], 
				    data[7][i],
				    data[8][i],
				    data[9][i],
				    data[10][i],
				    data[11][i], 
				    data[12][i])
			
	"""
