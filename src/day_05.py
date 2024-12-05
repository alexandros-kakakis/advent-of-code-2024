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

def correct_update(update, rules, rule_regex):
    for rule in rules:
        first_number, second_number = rule.split('|')
        
        single_rule_regex = f"{second_number},.*{first_number}"
        replacement_string = f"{first_number},{second_number}"
        
        start_index = re.search(single_rule_regex, update).start() if re.search(single_rule_regex, update) else -1
        if start_index != -1:

            update = update.replace(
                f",{first_number}",
                ""
            )
            update = update.replace(
                second_number,
                replacement_string
            )

    if re.search(rule_regex, update):
        return correct_update(update, rules, rule_regex)
    else:
        return update

print(
    "Solution Part Two: ",
    sum(
        return_middle_number(
            correct_update(update, rules, rule_regex)
        ) for update in incorrect_updates
    )
)
