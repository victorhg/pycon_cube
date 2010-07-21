#!/usr/bin/env python2.6

import optparse
import pprint
import unittest
import sys
from rotate import Rotator
import re

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
        print '%d:' % (i+1), piece


def visualize_piece(piece):
  """Shows something that humans can interpret spacially."""
  s = ['X ' if x else '. ' for x in piece]
  for i in range(0, 16, 4):
    for j in range(0, 64, 16):
      print "".join(s[i+j:i+j+4]), " ",
      # print "%s:%s" % (i+j, i+j+4),
    print
  # print s[0:4], s[16:20], s[32:36], s[48:52]
  # print s[4:8], s[20:24], 


def make_binary(RAW_PIECES):
    pieces = []
    for piece in RAW_PIECES:
        val = 0L
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


class AllTheWays(object):

  def __init__(self):
    self.r = Rotator()

  def all_rotations(self, piece):
    """All rotations of a piece.  Accepts the list format.

    http://www.euclideanspace.com/maths/discrete/groups/categorise/finite/cube/index.htm
    """
    # This variable represents all the 24 rotations of a piece.
    data = """i x y xx  xy  yx  yy  xxx xxy xyx xyy yxx yyx yyy
    xxxy  xxyx  xxyy  xyxx xyyy  yxxx  yyyx  xxxyx xyxxx xyyyx"""
    rotation_defs = re.split(r"\s+", data)
    rotations = []
    functions = {
        'i': lambda x: x, # Identity
        'x': self.r.RotatePieceX,
        'y': self.r.RotatePieceY,
        'z': self.r.RotatePieceZ,
    }
    for rotation_def in rotation_defs:
      rotated = piece
      for rotation_dir in rotation_def:
      	rotated = functions[rotation_dir](rotated)
      rotations.append(tuple(rotated))
    return rotations

  def all_positions(self, piece):
    """All positions of a piece.  Accepts the list format.

    The algorithm:
    - move the piece near the (0, 0, 0) corner
    - while true # x
    	- while true # y
    		- while true # z
    			- record the position
          - if can move along z
          	- move
            - else break z
        - if can move along y
        	- move
          - else break y
      - if can move along x
      	- move
        - else break
    """
    pass



class MakeListUnitTest(unittest.TestCase):
  
  def testMakeList_1(self):
    pieces = [0L]
    self.assertEqual([[False] * 64], make_list(pieces))

  def testMakeList_2(self):
    pieces = [1L]
    self.assertEqual([[False] * 63 + [True]], make_list(pieces))


class AllTheWaysUnitTest(unittest.TestCase):

  def test_1(self):
    a = AllTheWays()
    piece = [0] * 64
    piece[0] = 1
    piece[1] = 1
    piece[2] = 1
    rotations = a.all_rotations(piece)
    self.assertEqual(24, len(set(rotations)))


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
