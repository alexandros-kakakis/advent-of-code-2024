import numpy as np
import re

with open("data/puzzle_input_day_13.txt", "r") as file:
    claw_machines = file.read().split('\n\n')

claw_machines = [
    (lambda nums: (
        np.array([nums[0], nums[1]]),
        np.array([nums[2], nums[3]]),
        np.array([nums[4], nums[5]])
    ))([int(num) for num in re.findall(r'\d+', claw_machine)])
    for claw_machine in claw_machines
]

def calculate_total_tokens(claw_machines, prize_offset=0):
    total_tokens = 0
    for claw_machine in claw_machines:
        button_a, button_b, prize_location = claw_machine
        prize_location += prize_offset
        solution = np.linalg.solve(
            np.column_stack((button_a, button_b)),
            prize_location
        )
        if np.all(np.isclose(solution, np.round(solution), rtol=1e-14, atol=1e-8)):
            total_tokens += int(3 * round(solution[0]) + 1 * round(solution[1]))
    return total_tokens

print(
    "Solution Part One:",
    calculate_total_tokens(claw_machines)
)

print(
    "Solution Part Two:",
    calculate_total_tokens(claw_machines, prize_offset=10000000000000)
)