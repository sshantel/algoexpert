import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))


def isValidSubsequence(array, sequence):
# create two pointers
    seq = 0
    for value in array:
        if seq == len(sequence):
            break
        if sequence[seq] == value:
            seq += 1

    return seq == len(sequence)



if __name__ == '__main__':
    unittest.main()