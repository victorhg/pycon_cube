#!/usr/bin/env python

import unittest
import copy
import numpy
import itertools
import pprint
import math

def mappings(size):
  """Calculates mappings between coordinates and indexes."""
  dim_by_idx = {}
  idx_by_dim = {}
  count = itertools.count()
  for z in range(size):
    for y in range(size):
      for x in range(size):
        idx = count.next()
        dim = (x, y, z)
        idx_by_dim[dim] = idx
        dim_by_idx[idx] = dim
  return idx_by_dim, dim_by_idx


def rotate_dim_x(x, y, z):
  # p = numpy.array([x, y, z])
  # x' = x cos f - y sin f
  # y' = y cos f + x sin f
  # The dimensions at play are: y, z
  offset = 1.5
  my_cos = 0
  my_sin = 1
  x -= offset
  y -= offset
  z -= offset
  new_x = x
  new_y = y * my_cos - z * my_sin
  new_z = z * my_cos + y * my_sin
  new_x += offset
  new_y += offset
  new_z += offset
  return (int(new_x), int(new_y), int(new_z))


def x_rotation_mapping():
  """Rotates along the X axis, top side forward."""
  idx_by_dim, dim_by_idx = mappings(4)
  x_rot = {}
  for dim in idx_by_dim:
    old_idx = idx_by_dim[dim]
    new_dim = rotate_dim_x(*dim)
    new_idx = idx_by_dim[new_dim]
    x_rot[old_idx] = new_idx
  return x_rot


def rotate_x(n):
  assert len(n) == 64, "n has the wrong length."
  mapping = x_rotation_mapping()
  new = range(64)
  for i in range(64):
    new[mapping[i]] = n[i]
  return new


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
  # top layer of the cube

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

  def testX_3(self):
    data = range(64)
    # This documents the function, but isn't necessarily right.
    expected = [48, 49, 50, 51,
                32, 33, 34, 35,
                16, 17, 18, 19,
                 0,  1,  2,  3,

                52, 53, 54, 55,
                36, 37, 38, 39,
                20, 21, 22, 23,
                 4,  5,  6,  7,

                56, 57, 58, 59,
                40, 41, 42, 43,
                24, 25, 26, 27,
                 8,  9, 10, 11,

                60, 61, 62, 63,
                44, 45, 46, 47,
                28, 29, 30, 31,
                12, 13, 14, 15]
    self.assertEqual(expected, rotate_x(data))

  def testX_4(self):
    data = (list('a' * 16)
          + list('b' * 16)
          + list('c' * 16)
          + list('d' * 16))
    expected = ['d', 'd', 'd', 'd',
                'c', 'c', 'c', 'c',
                'b', 'b', 'b', 'b',
                'a', 'a', 'a', 'a',

                'd', 'd', 'd', 'd',
                'c', 'c', 'c', 'c',
                'b', 'b', 'b', 'b',
                'a', 'a', 'a', 'a',

                'd', 'd', 'd', 'd',
                'c', 'c', 'c', 'c',
                'b', 'b', 'b', 'b',
                'a', 'a', 'a', 'a',

                'd', 'd', 'd', 'd',
                'c', 'c', 'c', 'c',
                'b', 'b', 'b', 'b',
                'a', 'a', 'a', 'a']
    self.assertEqual(expected, rotate_x(data))

  def disabled_testY_1(self):
    expected = copy.copy(self.data)
    expected[36] = 1
    self.data[37] = 1
    self.assertEqual(expected, rotate_y(self.data))

  def disabled_testY_2(self):
    data = (list('a' * 16)
          + list('b' * 16)
          + list('c' * 16)
          + list('d' * 16))
    expected = list("dcba") * 16
    self.assertEqual(expected, rotate_y(data))

  def test_mappings_1(self):
    idx_by_dim, dim_by_idx = mappings(2)
    expected = {
        (0, 0, 0): 0,
        (1, 0, 0): 1,
        (0, 1, 0): 2,
        (1, 1, 0): 3,
        (0, 0, 1): 4,
        (1, 0, 1): 5,
        (0, 1, 1): 6,
        (1, 1, 1): 7,
    }
    self.assertEqual(expected, idx_by_dim)

  def test_mappings_2(self):
    idx_by_dim, dim_by_idx = mappings(2)
    expected = {
        0: (0, 0, 0),
        1: (1, 0, 0),
        2: (0, 1, 0),
        3: (1, 1, 0),
        4: (0, 0, 1),
        5: (1, 0, 1),
        6: (0, 1, 1),
        7: (1, 1, 1)
    }
    self.assertEqual(expected, dim_by_idx)

if __name__ == '__main__':
  unittest.main()
