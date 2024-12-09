from collections import Counter
import re

with open("data/puzzle_input_day_09.txt", "r") as file:
    data = [int(x) for x in file.read().strip()]
    
    block_size_list = [data[x] for x in range(len(data)) if x % 2 == 0]
    free_space_list = [data[x] for x in range(len(data)) if x % 2 == 1] + [0]
    id_number_list = [str(x) for x in range(len(block_size_list))]

layout = []
for block_size, free_space, id_number in zip(block_size_list, free_space_list, id_number_list):
    layout += block_size * [id_number]
    layout += free_space * "."

new_layout = layout.copy()
last_non_dot = len(new_layout) - 1

i = 0
while i < last_non_dot:
    if new_layout[i] == '.':
        new_layout[i] = new_layout[last_non_dot]
        new_layout[last_non_dot] = '.'
        while last_non_dot > i and new_layout[last_non_dot] == '.':
            last_non_dot -= 1
    i += 1

print(
    "Solution Part One:",
    sum([i * int(x) for i, x in enumerate(new_layout) if x != "."])
)

new_layout = layout.copy()

file_sizes = Counter(int(x) for x in new_layout if x != '.')
file_sizes = dict(sorted(file_sizes.items(), reverse=True))

for file_id, file_size in file_sizes.items():
    file_id_str = str(file_id)
    
    start_idx = -1
    count = 0
    for i, val in enumerate(new_layout):
        if val == file_id_str:
            if count == 0:
                start_idx = i
            count += 1
            if count == file_size:
                break
        else:
            count = 0
            start_idx = -1
    
    dot_start = -1
    dot_count = 0
    for i, val in enumerate(new_layout):
        if val == '.':
            if dot_count == 0:
                dot_start = i
            dot_count += 1
            if dot_count == file_size:
                break
        else:
            dot_count = 0
            dot_start = -1
    
    if start_idx != -1 and dot_start != -1 and dot_count == file_size and dot_start < start_idx:
        new_layout[start_idx:start_idx + file_size] = ['.'] * file_size
        new_layout[dot_start:dot_start + file_size] = [file_id_str] * file_size

print(
    "Solution Part Two:",
    sum([i * int(x) for i, x in enumerate(new_layout) if x != "."])
)
