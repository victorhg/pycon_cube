#0000000000000000 0000000000000000 0000000000000000 0000000000000000

#0000 0000 0000 0000

raw_pieces = [
    'x...xx...xx.....',
    '.xx.xx..............x...........',
    '.x..xxx..........x..............',
    '.....xx..........x..xx..........',
    '.x..xxx.............x...........',
    'x...xxx.............x...........',
    'x...xxx.........x...............',
    '.x..xxx..x......',
    'xx..x...............x...........',
    '..x.xxx.............x...........',
    '.x..xxx..............x..........',
    '.xx..x..............xx..........',
    '.x..xxx.x.......'
]

def show(pieces):
    """
    Take in raw pieces and represent them as x's and dots.
    """
    for i, piece in enumerate(pieces):
        print '%d:' % (i+1)
        print

def make_binary(raw_pieces):
    pieces = []
    for piece in raw_pieces:
        val = 0
        for i, char in enumerate(piece):
            if char == 'x':
                val += 2**(64-i)
        pieces.append(val)
    return pieces

def make_list(pieces):
    listpieces = []
    for i, piece in enumerate(pieces):
        listpieces.append([])
        str_piece = bin(piece)[2:]
        for char in str_piece:
            listpieces[i].append(bool(char))
    return listpieces

pieces = make_binary(raw_pieces)
list_pieces = make_list(pieces)
