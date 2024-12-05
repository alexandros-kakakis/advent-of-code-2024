import re

with open("data/puzzle_input_day_05.txt", "r") as f:
    rules, updates = f.read().split('\n\n')

rules = rules.split('\n')
updates = updates.split('\n')

rule_regex = "|".join([ f"({r},.*{l})" for l, r in [rule.split('|') for rule in rules]])

correct_updates = [
    update for update in updates if not bool(re.search(rule_regex, update))
]

def return_middle_number(update):
    return int(update.split(',')[len(update.split(',')) // 2])

print(
    "Solution Part One: ",
    sum(return_middle_number(update) for update in correct_updates)
)

incorrect_updates = [
    update for update in updates if bool(re.search(rule_regex, update))
]

"""
TODO: replace each incorrect occurance with the correct rule
- Iterate over rules: create regex, create replacement string, find index of rule violation, replace, update rule
- Check if updated rules pass rule_regex
- Get middle number of updated rules
"""

for rule in rules:
    single_rule_regex = ""
    print(rule)
    break