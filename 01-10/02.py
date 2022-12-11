#%%
from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def map_shapes(input: str) -> Shape:
    if input in ["A", "X"]:
        return Shape.ROCK
    elif input in ["B", "Y"]:
        return Shape.PAPER
    else:
        return Shape.SCISSORS


def score_of_round(opponent_shape: Shape, my_shape: Shape) -> int:
    score = my_shape.value
    if opponent_shape == my_shape:
        score += 3
    elif opponent_shape == Shape.ROCK:
        score += 6 if my_shape == Shape.PAPER else 0
    elif opponent_shape == Shape.PAPER:
        score += 6 if my_shape == Shape.SCISSORS else 0
    elif opponent_shape == Shape.SCISSORS:
        score += 6 if my_shape == Shape.ROCK else 0

    return score


def shape_to_choose(opponent_shape: Shape, result: str) -> Shape:
    if result == "X":  # Lose
        if opponent_shape == Shape.ROCK:
            return Shape.SCISSORS
        if opponent_shape == Shape.PAPER:
            return Shape.ROCK
        if opponent_shape == Shape.SCISSORS:
            return Shape.PAPER

    if result == "Y":  # Draw
        return opponent_shape

    if result == "Z":  # Win
        if opponent_shape == Shape.ROCK:
            return Shape.PAPER
        if opponent_shape == Shape.PAPER:
            return Shape.SCISSORS
        if opponent_shape == Shape.SCISSORS:
            return Shape.ROCK


with open("./02_input.txt", "r") as file:
    raw_rounds = file.readlines()

raw_rounds[:5]

#%%
rounds_part_one = [
    (map_shapes(opponent_shape), map_shapes(my_shape))
    for opponent_shape, my_shape in [
        raw_round.rstrip().split() for raw_round in raw_rounds
    ]
]
answer_part_one = 0

for current_round in rounds_part_one:
    opponent_shape, my_shape = current_round
    answer_part_one += score_of_round(opponent_shape, my_shape)

answer_part_one

#%%
rounds_part_two = [
    (map_shapes(opponent_shape), result)
    for opponent_shape, result in [
        raw_round.rstrip().split() for raw_round in raw_rounds
    ]
]
answer_part_two = 0

for current_round in rounds_part_two:
    opponent_shape = current_round[0]
    my_shape = shape_to_choose(opponent_shape, current_round[1])
    answer_part_two += score_of_round(opponent_shape, my_shape)

answer_part_two
