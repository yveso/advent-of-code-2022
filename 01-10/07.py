#%%
def full_path(prompt: list[str]) -> str:
    return "/" + "/".join(prompt[1:])


use_test_data = False
with open("./07_test.txt" if use_test_data else "./07_input.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

directories = {}
prompt = []
for line in lines:
    if line.startswith("$ cd"):
        *_, dir_name = line.split()
        if dir_name != "..":
            prompt.append(dir_name)
            full_name = full_path(prompt)
            if full_name not in directories.keys():
                directories[full_name] = 0
        else:
            prompt.pop()
    elif line == "$ ls" or line.startswith("dir"):
        continue
    else:
        size, name = line.split()
        for i, _ in enumerate(prompt):
            full_name = full_path(prompt[: i + 1])
            directories[full_name] += int(size)

directories

#%%
answer_part_one = sum([v for v in directories.values() if v < 100_000])
answer_part_one

#%%
total_disk_space = 70_000_000
currently_free_disk_space = total_disk_space - directories["/"]
total_space_needed = 30_000_000
still_needed_to_be_freed_up = total_space_needed - currently_free_disk_space

answer_part_two = min(
    [space for space in directories.values() if space > still_needed_to_be_freed_up]
)
answer_part_two
