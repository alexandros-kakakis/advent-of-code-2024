import re

with open("data/puzzle_input_day_03.txt", "r") as file:
    memory = file.read()


mul_pattern = r"mul\(([0-9]+),([0-9]+)\)"
mul_outcomes = [
    (i.start(), int(i.group(1)) * int(i.group(2)))
    for i in re.finditer(mul_pattern, memory)
]

print(
    "Solution Part One: ",
    sum([i[1] for i in mul_outcomes]),
)

conditional_pattern = r"(don?'?t?)"
conditional_instructions = [
    (i.start(), i.group(0))
    for i in re.finditer(conditional_pattern, memory)
]

current_index = 0
current_instruction = "do"
sum_of_mul_outcomes = 0

for index, instruction in conditional_instructions + [(len(memory), "")]:
    if current_instruction == "do":
        sum_of_mul_outcomes += sum(
            i[1] for i in mul_outcomes if current_index < i[0] < index
        )

    current_instruction = instruction
    current_index = index

print("Solution Part Two: ", sum_of_mul_outcomes)
