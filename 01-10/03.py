#%%
with open("./03_input.txt", "r") as file:
    rucksacks = [line.rstrip() for line in file.readlines()]


def priority_of_item(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


#%%
def item_that_appears_in_both_compartments(
    first_compartment: str, second_compartment: str
) -> str:
    for item in first_compartment:
        if item in second_compartment:
            return item


rucksack_as_compartments = []
for rucksack in rucksacks:
    number_of_items = len(rucksack)
    rucksack_as_compartments.append(
        (rucksack[: number_of_items // 2], rucksack[number_of_items // 2 :])
    )

answer_part_one = 0
for rucksack in rucksack_as_compartments:
    first, second = rucksack
    answer_part_one += priority_of_item(
        item_that_appears_in_both_compartments(first, second)
    )

answer_part_one

#%%
def item_that_appears_in_all_rucksacks(group_of_three: list[str]) -> str:
    one, two, three = group_of_three
    for item in one:
        if item in two and item in three:
            return item


groups_of_three = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

answer_part_two = sum(
    priority_of_item(item_that_appears_in_all_rucksacks(group))
    for group in groups_of_three
)

answer_part_two
