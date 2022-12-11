#%%
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Instruction:
    quantity: int
    from_stack: int
    to_stack: int


drawing_lines = []
instruction_lines = []
with open("./05_input.txt", "r") as file:
    while line := file.readline()[:-1]:
        drawing_lines.append(line)

    instruction_lines = file.readlines()

*drawing_lines, last_drawing_line = drawing_lines
number_of_stacks = int(last_drawing_line.split()[-1])
stacks = [[] for _ in range(number_of_stacks)]


for line in reversed(drawing_lines):
    for i in range(number_of_stacks):
        magic_index = i * 3 + 1 + i
        crate = line[magic_index]
        if crate != " ":
            stacks[i].append(crate)


instructions: list[Instruction] = []
for instruction in instruction_lines:
    qty, fr_st, to_st = [int(x) for x in instruction.split() if x.isnumeric()]
    instructions.append(Instruction(qty, fr_st, to_st))

#%%
stacks_part_one = deepcopy(stacks)
for instruction in instructions:
    for quantity in range(instruction.quantity):
        crate = stacks_part_one[instruction.from_stack - 1].pop()
        stacks_part_one[instruction.to_stack - 1].append(crate)

answer_part_one = "".join(stack[-1] for stack in stacks_part_one)
answer_part_one

#%%
stacks_part_two = deepcopy(stacks)
for instruction in instructions:
    stacks_part_two[instruction.from_stack - 1], crates = (
        stacks_part_two[instruction.from_stack - 1][: -1 * instruction.quantity],
        stacks_part_two[instruction.from_stack - 1][-1 * instruction.quantity :],
    )
    stacks_part_two[instruction.to_stack - 1].extend(crates)

answer_part_two = "".join(stack[-1] for stack in stacks_part_two)
answer_part_two
