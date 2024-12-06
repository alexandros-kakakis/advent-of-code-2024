with open("data/puzzle_input_day_06.txt", "r") as file:
    map = [list(line.strip()) for line in file]

def move_guard(direction, start_location, obstacle_locations, valid_locations):
    visited_locations = [start_location]
    visited_locations_with_direction = []
    
    while True:
    
        if direction == "up":
            visited_locations_with_direction.append((start_location, direction))
            new_location = (start_location[0] - 1, start_location[1])
            if (new_location, direction) in visited_locations_with_direction:
                return visited_locations, False
            elif new_location not in valid_locations:
                return visited_locations, True
            elif new_location in obstacle_locations:
                direction = "right"
            else:
                visited_locations.append(new_location)
                start_location = new_location
        
        elif direction == "right":
            visited_locations_with_direction.append((start_location, direction))
            new_location = (start_location[0], start_location[1] + 1)
            if (new_location, direction) in visited_locations_with_direction:
                return visited_locations, False
            elif new_location not in valid_locations:
                return visited_locations, True
            elif new_location in obstacle_locations:
                direction = "down"
            else:
                visited_locations.append(new_location)
                start_location = new_location

        elif direction == "down":
            visited_locations_with_direction.append((start_location, direction))
            new_location = (start_location[0] + 1, start_location[1])
            if (new_location, direction) in visited_locations_with_direction:
                return visited_locations, False
            elif new_location not in valid_locations:
                return visited_locations, True
            elif new_location in obstacle_locations:
                direction = "left"
            else:
                visited_locations.append(new_location)
                start_location = new_location

        elif direction == "left":
            visited_locations_with_direction.append((start_location, direction))
            new_location = (start_location[0], start_location[1] - 1)
            if (new_location, direction) in visited_locations_with_direction:
                return visited_locations, False
            elif new_location not in valid_locations:
                return visited_locations, True
            elif new_location in obstacle_locations:
                direction = "up"
            else:
                visited_locations.append(new_location)
                start_location = new_location

valid_locations = [(i, j) for i in range(len(map)) for j in range(len(map[0]))]
start_location = [(i, j) for i, row in enumerate(map) for j, val in enumerate(row) if val == '^'][0]
obstacle_locations = [(i, j) for i, row in enumerate(map) for j, val in enumerate(row) if val == '#']

original_path, _ = move_guard("up", start_location, obstacle_locations, valid_locations)
original_path_set = set(original_path)

print(
    "Solution Part One: ",
    len(original_path_set)
)

number_of_obstacles_that_cause_loop = 0
total_locations = len(original_path_set)

for idx, location in enumerate(original_path_set, 1):
    _, loop_detected = move_guard("up", start_location, obstacle_locations + [location], valid_locations)
    if not loop_detected:
        number_of_obstacles_that_cause_loop += 1
    # print(f"Processing location {idx}/{total_locations}", end="\n")
    
print(
    "Solution Part Two: ",
    number_of_obstacles_that_cause_loop
)
