#%%
with open("./06_input.txt", "r") as file:
    signal = file.readline().rstrip()

signal

#%%
for i in range(len(signal) - 3):
    subset = signal[i : i + 4]
    if len(set(subset)) == 4:
        answer_part_one = i + 4
        break

answer_part_one

#%%
for i in range(len(signal) - 13):
    subset = signal[i : i + 14]
    if len(set(subset)) == 14:
        answer_part_two = i + 14
        break

answer_part_two
