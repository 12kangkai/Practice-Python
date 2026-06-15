import unittest

# 被测试的应用代码
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b


# 单元测试类
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """每个测试方法前执行"""
        self.calc = Calculator()
    
    def tearDown(self):
        """每个测试方法后执行"""
        pass
    
    def test_add(self):
        """测试加法"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtract(self):
        """测试减法"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
    
    def test_multiply(self):
        """测试乘法"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """测试除法"""
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        """测试除零异常"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()