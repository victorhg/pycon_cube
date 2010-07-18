import pieces as init
from move import move_down, move_right, can_move_down, can_move_right

def create_moving_possibilities():
	result_pieces = []
	for piece in init.pieces:
		possibilities = [piece]
		actual_pos = piece
		for i in range(4):
			right_pos = actual_pos
			for j in range(4):
				if can_move_right(right_pos):
					right_pos = move_right(right_pos)
					possibilities.append(right_pos)
			if can_move_down(piece):
				actual_pos = move_down(actual_pos)
				possibilities.append(actual_pos)
		result_pieces.append(possibilities)
	return result_pieces
	
	

print create_moving_possibilities()
	
	
