
class Matcher

	def solution(self):
		return (2 ** 64 - 1)

	def match(self, possibility):
		sum = 0b00
		for piece in possibility.pieces
			sum += piece	
		return sum == solution()
	
	def evaluate(self, possibility):
		areTheyfitting(possibility.pieces[0], possibility.piece[0])

	def areTheyFitting(self, piece1, piece2):
		piece1 = str(bin(piece1)).replace("0b", "")[::-1]
		piece2 = str(bin(piece2)).replace("0b", "")[::-1]
		for i in range(0, len(piece1))
			if (len(str(bin(piece1[i]) + bin(piece2[i])).replace("0b", "")) != 1 )
				return false
		return true

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
			

class Possibility

	def __init__(self, pieces):
		self.pieces = pieces
		self.empty_space = 0
		self.pieces_fitted = 0
		

			
		

