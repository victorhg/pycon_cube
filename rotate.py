#!/usr/bin/env python2.6

import unittest
import copy
import itertools
import pprint
import math

class Rotator(object):
  
  OFFSET = 1.5

  def __init__(self, mapping_size=4):
    self.idx_by_dim, self.dim_by_idx = self.Mappings(mapping_size)
    self.x_rot_map = None
    self.y_rot_map = None
    self.z_rot_map = None

  def Mappings(self, size):
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

  def RotateCoordsX(self, x, y, z):
    # p = numpy.array([x, y, z])
    # x' = x cos f - y sin f
    # y' = y cos f + x sin f
    # The dimensions at play are: y, z
    my_cos = 0
    my_sin = 1
    x -= self.OFFSET
    y -= self.OFFSET
    z -= self.OFFSET
    new_x = x
    new_y = y * my_cos - z * my_sin
    new_z = z * my_cos + y * my_sin
    new_x += self.OFFSET
    new_y += self.OFFSET
    new_z += self.OFFSET
    return (int(new_x), int(new_y), int(new_z))

  def RotateCoordsY(self, x, y, z):
    """Rotating topside left."""
    # p = numpy.array([x, y, z])
    # x' = x cos f - y sin f
    # y' = y cos f + x sin f
    # The dimensions at play are: x, z
    my_cos = 0
    my_sin = 1
    x -= self.OFFSET
    y -= self.OFFSET
    z -= self.OFFSET
    new_x = x * my_cos - z * my_sin
    new_y = y
    new_z = z * my_cos + x * my_sin
    new_x += self.OFFSET
    new_y += self.OFFSET
    new_z += self.OFFSET
    return (int(new_x), int(new_y), int(new_z))

  def RotateCoordsZ(self, x, y, z):
    """Rotating clockwise."""
    # p = numpy.array([x, y, z])
    # x' = x cos f - y sin f
    # y' = y cos f + x sin f
    # The dimensions at play are: x, z
    my_cos = 0
    my_sin = -1
    x -= self.OFFSET
    y -= self.OFFSET
    z -= self.OFFSET
    new_x = x * my_cos - y * my_sin
    new_y = y * my_cos + x * my_sin
    new_z = z
    new_x += self.OFFSET
    new_y += self.OFFSET
    new_z += self.OFFSET
    return (int(new_x), int(new_y), int(new_z))

  def _GetRotationMapping(self, function):
    mapping = {}
    for dim in self.idx_by_dim:
      old_idx = self.idx_by_dim[dim]
      new_dim = function(*dim)
      new_idx = self.idx_by_dim[new_dim]
      mapping[old_idx] = new_idx
    return mapping

  def GetRotationMappingX(self):
    if not self.x_rot_map:
      self.x_rot_map = self._GetRotationMapping(self.RotateCoordsX)
    return self.x_rot_map

  def GetRotationMappingY(self):
    if not self.y_rot_map:
      self.y_rot_map = self._GetRotationMapping(self.RotateCoordsY)
    return self.y_rot_map

  def GetRotationMappingZ(self):
    if not self.z_rot_map:
      self.z_rot_map = self._GetRotationMapping(self.RotateCoordsZ)
    return self.z_rot_map

  def RotatePieceX(self, n):
    assert len(n) == 64, "n has the wrong length."
    mapping = self.GetRotationMappingX()
    new = range(64)
    for i in range(64):
      new[mapping[i]] = n[i]
    return new

  def RotatePieceY(self, n):
    assert len(n) == 64, "n has the wrong length."
    mapping = self.GetRotationMappingY()
    new = range(64)
    for i in range(64):
      new[mapping[i]] = n[i]
    return new

  def RotatePieceZ(self, n):
    assert len(n) == 64, "n has the wrong length."
    mapping = self.GetRotationMappingZ()
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
    self.data = [0, 0, 0, 0, #  0
                 0, 0, 0, 0, #  4
                 0, 0, 0, 0, #  8
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
    self.r = Rotator()
    self.r2 = Rotator(2)

  def test_1(self):
    expected = copy.copy(self.data)
    expected[12] = 1
    self.data[0] = 1
    self.assertEqual(expected, self.r.RotatePieceX(self.data))

  def test_2(self):
    expected = copy.copy(self.data)
    expected[24] = 1
    self.data[20] = 1
    self.assertEqual(expected, self.r.RotatePieceX(self.data))

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
    self.assertEqual(expected, self.r.RotatePieceX(data))

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
    self.assertEqual(expected, self.r.RotatePieceX(data))

  def testRotateCoordsY(self):
    dim = (0, 0, 0)
    expected = (3, 0, 0)
    self.assertEqual(expected, self.r.RotateCoordsY(*dim))

  def testY_1(self):
    expected = copy.copy(self.data)
    expected[38] = 1
    data = copy.copy(self.data)
    data[22] = 1
    self.assertEqual(expected, self.r.RotatePieceY(data))

  def testY_2(self):
    data = (list('a' * 16)
          + list('b' * 16)
          + list('c' * 16)
          + list('d' * 16))
    expected = list("dcba") * 16
    self.assertEqual(expected, self.r.RotatePieceY(data))

  def testRotateCoordsZ(self):
    dim = (0, 0, 0)
    expected = (0, 3, 0)
    self.assertEqual(expected, self.r.RotateCoordsZ(*dim))

  def testRotateCoordsZ_leftTop(self):
    dim = (0, 3, 0)
    expected = (3, 3, 0)
    self.assertEqual(expected, self.r.RotateCoordsZ(*dim))

  def test_mappings_1(self):
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
    self.assertEqual(expected, self.r2.idx_by_dim)

  def test_mappings_2(self):
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
    self.assertEqual(expected, self.r2.dim_by_idx)

  def testGetRotationMappingX(self):
    rot_mapping = self.r.GetRotationMappingX()
    self.assertEqual(64, len(rot_mapping.keys()))
    self.assertEqual(64, len(set(rot_mapping.values())))

  def testGetRotationMappingY(self):
    """All the keys and the values have to keep unique after the
    transformation."""
    rot_mapping = self.r.GetRotationMappingY()
    self.assertEqual(64, len(rot_mapping.keys()))
    self.assertEqual(64, len(set(rot_mapping.values())))

  def testGetRotationMappingZ(self):
    """All the keys and the values have to keep unique after the
    transformation."""
    rot_mapping = self.r.GetRotationMappingZ()
    self.assertEqual(64, len(rot_mapping.keys()))
    self.assertEqual(64, len(set(rot_mapping.values())))


if __name__ == '__main__':
  unittest.main()
