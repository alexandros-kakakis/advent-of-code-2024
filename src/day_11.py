with open("data/puzzle_input_day_11.txt", "r") as file:
    stone_arrangement = [ int(i) for i in file.read().split(" ") ]


def update_stone_arrangement(stone_arrangement):
    next_stone_arrangement = []

    for stone in stone_arrangement:
        digits = len(str(stone)) 
        
        if stone == 0:
            next_stone_arrangement.append(1) ## hier hoef ik alleen te weten in welke iteratie 1 is toegevoegd, en dus niet meenemen in de next_stone_arrangement
            
        elif digits % 2 == 0:
            divisor = 10 ** (digits // 2)
            next_stone_arrangement += [
                stone // divisor,
                stone % divisor
            ]
            
        else:
            next_stone_arrangement.append(stone * 2024)
    
    return next_stone_arrangement

for _ in range(75):
    print(_)
    # print(stone_arrangement)
    stone_arrangement = update_stone_arrangement(stone_arrangement)
    
print(
    "Solution Part One:",
    len(stone_arrangement)
)