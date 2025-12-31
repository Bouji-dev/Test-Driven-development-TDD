import unittest
from math_utils import multiply, is_even, divide

class testMultiply(unittest.TestCase):
    def test_multiply_two_numbers(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_multiply_with_none(self):
        with self.assertRaises(ValueError):
            multiply(None, 3)


class testIsEven(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))

    def test_is_odd(self):   
        self.assertFalse(is_even(5))

    def test_invalid_inputs(self):
        invalid_inputs = ["4", None, 2.2]
        for i in invalid_inputs:
            with self.subTest(value=i):
                with self.assertRaises(TypeError):
                    is_even(i)    

class testDivide(unittest.TestCase):
    def test_divide_two_numbers_should_return_result(self):
        self.assertEqual(divide(10, 2), 5)
        
    def test_divide_by_zero_should_raise_zero_devision_error(self):    
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
    
    def test_divide_with_non_numeric_input_should_raise_type_error(self):
        with self.assertRaises(TypeError):
            divide(10, "2")















if __name__ == '__main__':
    unittest.main()            