#!/usr/bin/env python

import unittest
import copy

# Layers listed from bottom up.

# all_data = [
#     [n1, n2, n3, n4, n5, ... ],  # p1
#     [n1, n2, n3, n4, n5, ... ],  # p2
# ]

def rotate_x(n):
  return n

class FooTest(unittest.TestCase):

  # ^ y
  # |
  #  --> x

  def setUp(self):
    self.data = [0, 0, 0, 0, # 0
                 0, 0, 0, 0, # 4
                 0, 0, 0, 0, # 8
                 0, 0, 0, 0, # 12

                 0, 0, 0, 0, # 16
                 0, 0, 0, 0, # 20
                 0, 0, 0, 0, # 24
                 0, 0, 0, 0, # 28

                 0, 0, 0, 0, # 32
                 0, 0, 0, 0, # 36
                 0, 0, 0, 0, # 40
                 0, 0, 0, 0, # 44

                 0, 0, 0, 0, # 48
                 0, 0, 0, 0, # 52
                 0, 0, 0, 0, # 56
                 0, 0, 0, 0,] # 60

  def test_1(self):
    expected = copy.copy(self.data)
    expected[12] = 1
    self.data[0] = 1
    self.assertEqual(expected, rotate_x(self.data))


if __name__ == '__main__':
	unittest.main()
