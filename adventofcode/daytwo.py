from __future__ import annotations
from enum import Enum
from typing import List


class RockPaperScissorsMove(Enum):
    ROCK = (1, 'AX')
    PAPER = (2, 'BY')
    SCISSORS = (3, 'CZ')

    def beats(self, other: RockPaperScissorsMove):
        if self is RockPaperScissorsMove.ROCK and other is RockPaperScissorsMove.SCISSORS: return True
        if self is RockPaperScissorsMove.PAPER and other is RockPaperScissorsMove.ROCK: return True
        if self is RockPaperScissorsMove.SCISSORS and other is RockPaperScissorsMove.PAPER: return True
        return False

    def loses_to(self):
        if self is RockPaperScissorsMove.ROCK: return RockPaperScissorsMove.PAPER
        if self is RockPaperScissorsMove.PAPER: return RockPaperScissorsMove.SCISSORS
        if self is RockPaperScissorsMove.SCISSORS: return RockPaperScissorsMove.ROCK

    def wins_against(self):
        if self is RockPaperScissorsMove.ROCK: return RockPaperScissorsMove.SCISSORS
        if self is RockPaperScissorsMove.PAPER: return RockPaperScissorsMove.ROCK
        if self is RockPaperScissorsMove.SCISSORS: return RockPaperScissorsMove.PAPER

    @staticmethod
    def from_value(value: str) -> RockPaperScissorsMove:
        for move in RockPaperScissorsMove:
            if value in move.value[1]:
                return move
        raise ValueError(value)


def puzzle_one(puzzle_input: str) -> int:
    puzzle_input = process_puzzle_input(puzzle_input)
    score = 0
    for match in puzzle_input:
        opponent_move = RockPaperScissorsMove.from_value(match[0])
        player_move = RockPaperScissorsMove.from_value(match[1])
        if player_move == opponent_move:
            score += 3
        elif player_move.beats(opponent_move):
            score += 6
        score += player_move.value[0]
    return score

def puzzle_two(puzzle_input: str):
    puzzle_input = process_puzzle_input(puzzle_input)
    score = 0
    for match in puzzle_input:
        opponent_move = RockPaperScissorsMove.from_value(match[0])
        player_move = opponent_move.wins_against()  # outcome X, loss
        desired_outcome = match[1]
        if desired_outcome == "Y":  # draw
            score += 3
            player_move = opponent_move
        if desired_outcome == "Z":
            score += 6
            player_move = opponent_move.loses_to()
        score += player_move.value[0]
    return score

def process_puzzle_input(input_string: str) -> List[List[str]]:
    return [[value for value in row.split(" ")] for row in input_string.split("\n")]
