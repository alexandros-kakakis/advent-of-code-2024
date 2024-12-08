from itertools import product

with open("data/puzzle_input_day_07.txt", "r") as f:
    list_of_test_values, list_of_numbers = zip(*[line.split(":") for line in f.readlines()])

list_of_test_values = [int(i) for i in list_of_test_values]
list_of_numbers = [list(map(int, i.split())) for i in list_of_numbers]

def calculate(operator, numbers):
    assert len(numbers) == 2, "Only two numbers are supported"
    operations = {
        'mul': lambda x, y: x * y,
        'add': lambda x, y: x + y,
        'concat': lambda x, y: int(str(x) + str(y)),
    }        
    return operations[operator](numbers[0], numbers[1])

def generate_operator_combinations(n, list_of_operators):
    return list(product(list_of_operators, repeat=n))

total_calibration_result = 0

for test_value, numbers in zip(list_of_test_values, list_of_numbers):
    operator_combinations = generate_operator_combinations(len(numbers)-1, ["mul", "add"])

    for operator_combination in operator_combinations:
        current_number = numbers[0]
        for number, operator in zip(numbers[1:], operator_combination):
            current_number = calculate(operator, [current_number, number])
            if current_number > test_value:
                break
        if current_number == test_value:
            total_calibration_result += test_value
            break

print(
    "Solution Part One:",
    total_calibration_result
)

total_calibration_result = 0

for test_value, numbers in zip(list_of_test_values, list_of_numbers):
    operator_combinations = generate_operator_combinations(len(numbers)-1, ["concat", "mul", "add"])

    for operator_combination in operator_combinations:
        current_number = numbers[0]
        for number, operator in zip(numbers[1:], operator_combination):
            current_number = calculate(operator, [current_number, number])
            if current_number > test_value:
                break
        if current_number == test_value:
            total_calibration_result += test_value
            break

print(
    "Solution Part Two:",
    total_calibration_result
)