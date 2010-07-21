#!/usr/bin/env python2.6

import optparse
import pieces
import pprint


def main():
  parser = optparse.OptionParser()
  parser.add_option("-s", "--show", dest="show",
      default=False, action="store_true",
      help="Show all the pieces.")
  options, args = parser.parse_args()
  if options.show:
    pieces.show(pieces.PIECES)
    list_pieces = pieces.make_list(pieces.PIECES)
    for i, piece in enumerate(list_pieces):
      print
      print "Piece %d:" % i
      pieces.visualize_piece(piece)


if __name__ == '__main__':
  main()
