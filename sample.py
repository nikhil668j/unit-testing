import unittest

# A simple function to demonstrate unit testing
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathFunctions(unittest.TestCase):
    
    def test_add(self):
        # Test case for add function
        self.assertEqual(add(3, 4), 7)  # 3 + 4 should equal 7
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 should equal 0
        self.assertEqual(add(-1, -1), -2)  # -1 + (-1) should equal -2
    
    def test_subtract(self):
        # Test case for subtract function
        self.assertEqual(subtract(10, 5), 5)  # 10 - 5 should equal 5
        self.assertEqual(subtract(0, 0), 0)  # 0 - 0 should equal 0
        self.assertEqual(subtract(-1, -1), 0)  # -1 - (-1) should equal 0

if __name__ == '__main__':
    unittest.main()
