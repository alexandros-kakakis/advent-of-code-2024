from collections import defaultdict

with open("data/puzzle_input_day_11.txt", "r") as file:
    stone_arrangement = [ int(i) for i in file.read().split(" ") ]

def process_stone(stone):
    digits = len(str(stone))
    if stone == 0:
        return [1]
        
    elif digits % 2 == 0:
        divisor = 10 ** (digits // 2)
        return [
            stone // divisor,
            stone % divisor
        ]
        
    else:
        return [stone * 2024]


def blink(stone_dict):
    new_stone_dict = defaultdict(int)
    for stone, count in stone_dict.items():
        new_stones = process_stone(stone)
        for new_stone in new_stones:
            new_stone_dict[new_stone] += count

    return new_stone_dict

stone_dict = defaultdict(int)

for stone in stone_arrangement:
    stone_dict[int(stone)] += 1

for i in range(75):
    stone_dict = blink(stone_dict)

    if i == 24:
        print(
            "Solution Part One:",
            sum(stone_dict.values())
        )

print(
    "Solution Part Two:",
    sum(stone_dict.values())
)
