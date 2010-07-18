#!/usr/bin/env python

import unittest
import copy
import numpy

def rotate_x(n):
  """Rotates along the X axis, top side away."""
  response = (n[48:52]
            + n[32:36]
            + n[16:20]
            + n[0:4]

            + n[52:56]
            + n[36:40]
            + n[20:24]
            + n[4:8]
            
            + n[56:60]
            + n[40:44]
            + n[24:28]
            + n[8:12]

            + n[60:64]
            + n[44:48]
            + n[28:32]
            + n[12:16]
            )
  return response

class FooTest(unittest.TestCase):

  # ^ y
  # |
  #  --> x

  def setUp(self):
    # bottom layer of the cube
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

  def test_2(self):
    expected = copy.copy(self.data)
    expected[24] = 1
    self.data[20] = 1
    self.assertEqual(expected, rotate_x(self.data))


if __name__ == '__main__':
	unittest.main()
