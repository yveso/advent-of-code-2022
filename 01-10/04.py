#%%
from dataclasses import dataclass


@dataclass
class Assignment:
    start: int
    end: int


with open("./04_input.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

list_of_assignment_pairs = []
for line in lines:
    assignments = []
    for single_assignment in line.split(","):
        start, end = [int(x) for x in single_assignment.split("-")]
        assignments.append(Assignment(start, end))
    list_of_assignment_pairs.append(assignments)

#%%
answer_part_one = 0
for first, second in list_of_assignment_pairs:
    longer_assignment, shorter_asignment = (
        (first, second)
        if (first.end - first.start) >= (second.end - second.start)
        else (second, first)
    )
    if (
        longer_assignment.start <= shorter_asignment.start <= longer_assignment.end
    ) and (longer_assignment.start <= shorter_asignment.end <= longer_assignment.end):
        answer_part_one += 1

answer_part_one

#%%
answer_part_two = 0
for first, second in list_of_assignment_pairs:
    longer_assignment, shorter_asignment = (
        (first, second)
        if (first.end - first.start) >= (second.end - second.start)
        else (second, first)
    )
    if (
        longer_assignment.start <= shorter_asignment.start <= longer_assignment.end
    ) or (longer_assignment.start <= shorter_asignment.end <= longer_assignment.end):
        answer_part_two += 1

answer_part_two
