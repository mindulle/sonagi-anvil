import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_permute(self):
        nums = [1, 2, 3]
        expected = [
            [1,2,3],[1,3,2],
            [2,1,3],[2,3,1],
            [3,1,2],[3,2,1]
        ]
        res = self.sol.permute(nums)
        # Sort both lists to compare regardless of order
        self.assertEqual(sorted(res), sorted(expected))

    def test_permute_two(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        res = self.sol.permute(nums)
        self.assertEqual(sorted(res), sorted(expected))

    def test_permute_one(self):
        nums = [1]
        expected = [[1]]
        res = self.sol.permute(nums)
        self.assertEqual(sorted(res), sorted(expected))

if __name__ == '__main__':
    unittest.main()
