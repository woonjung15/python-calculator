import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)# actual output vs expected output

    # Add the following test methods to the TestCalculator class:
    def test_add_negetive(self):
            self.assertEqual(self.calc.add(-2, 1), -1)
    
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)


    def test_sub_negetive(self):
        self.assertEqual(self.calc.subtract(-2, -1), -1)
    
    def test_sub_zero(self):
        self.assertEqual(self.calc.subtract(1, 0), 1)

    
    def test_mul_negetive(self):
        self.assertEqual(self.calc.multiply(-1, -2), 2)#สลับที่ไม่ได้
    
    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)


    def test_divide_negetive(self):
        self.assertEqual(self.calc.divide(18, 9), 2) 
    
    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(4, 4), 1)

    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

   
    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(2, 10), 2)
        

if __name__ == '__main__':
    unittest.main()