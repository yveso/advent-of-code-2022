#%%
with open("./01_input.txt", "r") as file:
    file_as_str = file.read()

groups = [group.split("\n") for group in file_as_str.split("\n\n")]

summed_up_calories = []
for group in groups:
    summed_up_calories.append(sum(int(calory) for calory in group if calory))

sorted_sums = sorted(summed_up_calories, reverse=True)

#%%
answer_part_one = sorted_sums[0]
answer_part_one

#%%
answer_part_two = sum(sorted_sums[:3])
answer_part_two
