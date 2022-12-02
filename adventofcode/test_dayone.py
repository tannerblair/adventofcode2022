from unittest import TestCase

from adventofcode.dayone import puzzle_one, puzzle_two

test_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

class Test(TestCase):
    def test_puzzle_one(self):
        self.assertEqual(puzzle_one(test_input), 24000)



    def test_puzzle_two(self):
        self.assertEqual(puzzle_two(test_input), 45000)
