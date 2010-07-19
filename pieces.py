#!/usr/bin/env python2.6

import optparse
import pprint
import unittest
import sys

# Module data in uppercase
RAW_PIECES = [
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

def make_binary(RAW_PIECES):
    pieces = []
    for piece in RAW_PIECES:
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
        if len(str_piece) < 64:
        	str_piece = '0' * (64 - len(str_piece)) + str_piece
        for char in str_piece:
            listpieces[i].append(bool(int(char)))
    return listpieces

PIECES = make_binary(RAW_PIECES)
collision = lambda x, y: x & y

def total_collision_count(pieces):
    """
    Loop over pieces and return a total collision count.
    """
    cube = 0
    collision_count = 0
    for i, piece in enumerate(pieces):
        c = bin(collision(cube, piece)).count('1')
        if c:
            print "%d has %d collisions" % (i+1, c)
            collision_count += c
        cube |= piece
    return collision_count


class MakeListUnitTest(unittest.TestCase):
  
  def testMakeList_1(self):
    pieces = [0L]
    self.assertEqual([[False] * 64], make_list(pieces))

  def testMakeList_2(self):
    pieces = [1L]
    self.assertEqual([[False] * 63 + [True]], make_list(pieces))


def main():
  """Can be substituted for unittest.main() to run other things."""
  parser = optparse.OptionParser()
  parser.add_option("-s", "--show", dest="show",
                    default=False, action="store_true",
                    help="Show the pieces")
  parser.add_option("-c", "--collisions", dest="collisions",
                    default=False, action="store_true",
                    help="Show the collisions")
  parser.add_option("-t", "--test", dest="test",
                    default=False, action="store_true",
                    help="Run tests")
  options, args = parser.parse_args()
  if options.show:
    pprint.pprint(make_list(PIECES))
    show(PIECES)
  if options.collisions:
    list_pieces = make_list(PIECES)
    print "Total collisions: %d" % total_collision_count(pieces)


if __name__ == '__main__':
  unittest.main()
