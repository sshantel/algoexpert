import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10) 
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)


def twoNumberSum(array, targetSum): 
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return array[i], array[j]
    return []


if __name__ == '__main__':
    unittest.main()