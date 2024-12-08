from itertools import combinations

antenna_positions = {}
feasible_map_positions = []

with open("./data/puzzle_input_day_08.txt", 'r') as file:
    for y, line in enumerate(line.strip() for line in file):
        for x, frequency in enumerate(line):
            feasible_map_positions.append((x, y))
            if frequency != '.' and frequency != '#':
                if frequency in antenna_positions:
                    antenna_positions[frequency].append((x, y))
                else:
                    antenna_positions[frequency] = [(x, y)]

antinode_positions = []
map_size = len(line)

for frequency_positions in antenna_positions.values():
    antenna_pairs = list(combinations(frequency_positions, 2))

    for antenna_pair in antenna_pairs:
        x_distance = (antenna_pair[1][0] - antenna_pair[0][0])
        y_distance = (antenna_pair[1][1] - antenna_pair[0][1])

        antinode_positions.append(
            (antenna_pair[1][0] + x_distance, antenna_pair[1][1] + y_distance)
        )

        x_distance = (antenna_pair[0][0] - antenna_pair[1][0])
        y_distance = (antenna_pair[0][1] - antenna_pair[1][1])

        antinode_positions.append(
            (antenna_pair[0][0] + x_distance, antenna_pair[0][1] + y_distance)
        )

antinode_positions = [pos for pos in antinode_positions if pos in feasible_map_positions]

print(
    "Solution Part One:",
    len(set(antinode_positions))
)

antinode_positions = []

for frequency_positions in antenna_positions.values():
    antenna_pairs = list(combinations(frequency_positions, 2))

    if len(frequency_positions) > 2:
        antinode_positions += frequency_positions

    for antenna_pair in antenna_pairs:
        x_distance = (antenna_pair[1][0] - antenna_pair[0][0])
        y_distance = (antenna_pair[1][1] - antenna_pair[0][1])

        for i in range(1, map_size):
            antinode_positions.append(
                (antenna_pair[1][0] + x_distance * i, antenna_pair[1][1] + y_distance * i)
            )

        x_distance = (antenna_pair[0][0] - antenna_pair[1][0])
        y_distance = (antenna_pair[0][1] - antenna_pair[1][1])

        for i in range(1, map_size):
            antinode_positions.append(
                (antenna_pair[0][0] + x_distance * i, antenna_pair[0][1] + y_distance * i)
            )

antinode_positions = [pos for pos in antinode_positions if pos in feasible_map_positions]

print(
    "Solution Part Two:",
    len(set(antinode_positions))
)