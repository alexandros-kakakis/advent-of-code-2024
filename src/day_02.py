with open("./data/puzzle_input_day_02.txt", "r") as file:
    list_of_reports = [list(map(int, l.split())) for l in file.readlines()]


def report_is_safe(report: list[int]) -> bool:
    differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]
    
    check_same_direction = all(d <= 0 for d in differences) or all(d >= 0 for d in differences)
    check_differences = all(1 <= abs(i) <= 3 for i in differences)
    return check_same_direction and check_differences

def remove_level_from_report(report, level_index):
    return report[:level_index] + report[level_index + 1 :]

print("Solution Part One: ", sum([report_is_safe(r) for r in list_of_reports]))

print("Solution Part Two: ", sum([
    any(
        [report_is_safe(remove_level_from_report(report, i)) for i in range(len(report))]
    )
    for report in list_of_reports
    ]
))
