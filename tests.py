import unittest
from main import square
from main import cube
from main import quad
from main import weather

class Test(unittest.TestCase):
  def test_square(self):
    self.assertEqual(square(-2), 4)
    self.assertEqual(square(4), 16)
  
  def test_cube(self):
    self.assertEqual(cube(5), 125)
    self.assertEqual(cube(-2), -8)
    
   def test_quad(self):
    self.assertEqual(quad(3), 81)
    self.assertEqual(quad(-2), -)

def test_square():
  assert square(4)==16
  assert square(-2)==4

def test_cube():
  assert cube(5)==125
  assert cube(-2)==-8
  
 def test_quad():
  assert quad(3)== 81
  assert quad(-2)==-

def test_weather(capsys):
  weather(25)
  captured = capsys.readouterr()
  assert captured.out == "it's cold outside\n"
  weather(55)
  captured = capsys.readouterr()
  assert captured.out == "it's nice outside\n"
  weather(75)
  captured = capsys.readouterr()
  assert captured.out == "it's hot outside\n"
