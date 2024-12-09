with open("data/puzzle_input_day_09.txt", "r") as file:
    data = [int(x) for x in file.read().strip()]
    
    block_size_list = [data[x] for x in range(len(data)) if x % 2 == 0]
    free_space_list = [data[x] for x in range(len(data)) if x % 2 == 1] + [0]
    id_number_list = [str(x) for x in range(len(block_size_list))]

layout = []
for block_size, free_space, id_number in zip(block_size_list, free_space_list, id_number_list):
    layout += block_size * [id_number]
    layout += free_space * "."

last_non_dot = len(layout) - 1

i = 0
while i < last_non_dot:
    if layout[i] == '.':
        layout[i] = layout[last_non_dot]
        layout[last_non_dot] = '.'
        while last_non_dot > i and layout[last_non_dot] == '.':
            last_non_dot -= 1
    i += 1

print(
    "Solution Part One:",
    sum([i * int(x) for i, x in enumerate(layout) if x != "."])
)