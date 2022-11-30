import unittest
from main import square
from main import cube

class Test(unittest.TestCase):
  def test_square(self):
    self.assertEqual(square(-2), 4)
    self.assertEqual(square(4), 16)
  
  def test_cube(self):
    self.assertEqual(cube(5), 125)
    self.assertEqual(cube(-2), -8)

def test_square():
  assert square(4)==16
  assert square(-2)==4

def test_cube():
  assert cube(5)==125
  assert cube(-2)==-8
