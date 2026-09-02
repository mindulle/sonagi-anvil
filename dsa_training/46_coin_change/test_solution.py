import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_coinChange(self):
        self.assertEqual(self.sol.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(self.sol.coinChange([2], 3), -1)
        self.assertEqual(self.sol.coinChange([1], 0), 0)

if __name__ == '__main__':
    unittest.main()
