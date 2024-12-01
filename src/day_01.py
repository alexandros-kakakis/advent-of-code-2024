FILEPATH = "./data/puzzle_input_day_01.txt"

with open(FILEPATH, 'r') as file:
    left_list, right_list = zip(*[map(int, line.strip().split()) for line in file])
    left_list, right_list = list(left_list), list(right_list)

    
print(
    "Solution Part One:",
    sum([abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list))])
)


print(
    "Solution Part Two:",
    sum([len([right for right in right_list if left == right]) * left for left in left_list])
)
