from unittest import TestCase

from adventofcode.daytwo import puzzle_one, puzzle_two

test_input = """A Y
B X
C Z"""


class Test(TestCase):
    def test_puzzle_one(self):
        self.assertEqual(puzzle_one("A X"), 4)
        self.assertEqual(puzzle_one("A Y"), 8)
        self.assertEqual(puzzle_one("A Z"), 3)
        self.assertEqual(puzzle_one("B X"), 1)
        self.assertEqual(puzzle_one("B Y"), 5)
        self.assertEqual(puzzle_one("B Z"), 9)
        self.assertEqual(puzzle_one("C X"), 7)
        self.assertEqual(puzzle_one("C Y"), 2)
        self.assertEqual(puzzle_one("C Z"), 6)

    def test_puzzle_two(self):
        self.assertEqual(puzzle_two("A X"), 3)
        self.assertEqual(puzzle_two("A Y"), 4)
        self.assertEqual(puzzle_two("A Z"), 8)
        self.assertEqual(puzzle_two("B X"), 1)
        self.assertEqual(puzzle_two("B Y"), 5)
        self.assertEqual(puzzle_two("B Z"), 9)
        self.assertEqual(puzzle_two("C X"), 2)
        self.assertEqual(puzzle_two("C Y"), 6)
        self.assertEqual(puzzle_two("C Z"), 7)

