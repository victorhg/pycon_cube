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

def show():
    for i, piece in enumerate(pieces):
        print '%d:' % (i+1)
        print

pieces = []

def make_binary():
    for piece in raw_pieces:
        val = 0;
        for i, char in enumerate(piece):
            if char == 'x':
                val += 2**(64-i)
        pieces.append(val)

make_binary()

if __name__ == '__main__':
    print pieces