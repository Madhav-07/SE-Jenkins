import unittest
from program import summation

class TestSummation(unittest.TestCase):
  def test_Sum1(self):
    result1 = summation(2)
    self.assertEqual(result1,3)
  
  def test_Sum2(self):
    result2 = summation(0)
    self.assertEqual(result2,0)
    
  def test_Sum3(self):
    result3 = summation(5)
    self.assertEqual(result3,15)
    
if __name__ == "__main__":
  unittest.main()
