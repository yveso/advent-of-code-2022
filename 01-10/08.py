#%%
use_test_data = False
grid = []
with open(f"./08_{'test' if use_test_data else 'input'}.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    for line in lines:
        grid.append([int(x) for x in list(line)])

grid

#%%
def is_visible(row, column, grid):
    current = grid[row][column]
    if row in [0, len(grid) - 1]:
        return True
    if column in [0, len(grid[0]) - 1]:
        return True
    # from left
    trees_to_the_left = grid[row][:column]
    max_left = max(trees_to_the_left)
    if max_left < current:
        return True
    # from right
    trees_to_the_right = grid[row][column + 1 :]
    max_right = max(trees_to_the_right)
    if max_right < current:
        return True
    # from top
    current_column = [grid[i][column] for i in range(len(grid))]
    trees_above = current_column[:row]
    max_above = max(trees_above)
    if max_above < current:
        return True
    # from below
    trees_below = current_column[row + 1 :]
    max_below = max(trees_below)
    if max_below < current:
        return True


count_visible_trees = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if is_visible(y, x, grid):
            count_visible_trees += 1

answer_part_one = count_visible_trees
answer_part_one

#%%
def count_trees(line_of_trees, current):
    count = 0
    for tree in line_of_trees:
        count += 1
        if tree >= current:
            break
    return count


def scenic_score(row, column, grid):
    current = grid[row][column]

    # from left
    current_row = grid[row]
    trees_to_the_left = current_row[:column]
    left = count_trees(trees_to_the_left[::-1], current)
    # from right
    trees_to_the_right = current_row[column + 1 :]
    right = count_trees(trees_to_the_right, current)
    # from above
    current_column = [grid[i][column] for i in range(len(grid))]
    trees_above = current_column[:row]
    above = count_trees(trees_above[::-1], current)
    # from below
    trees_below = current_column[row + 1 :]
    below = count_trees(trees_below, current)

    return left * right * above * below


highest_neighbour_count = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        n = scenic_score(y, x, grid)
        if n > highest_neighbour_count:
            highest_neighbour_count = n

answer_part_two = highest_neighbour_count
answer_part_two
