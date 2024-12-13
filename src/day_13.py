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

total_tokens = 0
for claw_machine in claw_machines:
    button_a, button_b, prize_location = claw_machine
    solution = np.linalg.solve(
        np.column_stack((button_a, button_b)),
        prize_location
    )
    if not np.all(np.isclose(solution, np.round(solution))):
        continue
    total_tokens += int(3 * solution[0] + 1 * solution[1])

print(total_tokens)