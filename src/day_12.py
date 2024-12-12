with open("data/puzzle_input_day_12.txt", "r") as file:
    map = {(i,j): char for i, line in enumerate(file) for j, char in enumerate(line.strip())}

def walk_map(map, starting_coordinate):
    area, perimeter, sides, visited, coordinates_to_check = 0, 0, 0, set(), [starting_coordinate]
    top_perimeter, left_perimeter, bottom_perimeter, right_perimeter = [], [], [], []

    while coordinates_to_check:
        current_coordinate = coordinates_to_check.pop(0)
        current_plant_type = map[current_coordinate]
            
        visited.add(current_coordinate)
        
        touching_plant_types = []

        top_coordinate = (current_coordinate[0] - 1, current_coordinate[1])
        if top_coordinate in map and map[top_coordinate] == current_plant_type:
            touching_plant_types.append(top_coordinate)
        else:
            top_perimeter.append(current_coordinate)
        
        left_coordinate = (current_coordinate[0], current_coordinate[1] - 1)
        if left_coordinate in map and map[left_coordinate] == current_plant_type:
            touching_plant_types.append(left_coordinate)
        else:
            left_perimeter.append(current_coordinate)
        
        bottom_coordinate = (current_coordinate[0] + 1, current_coordinate[1])
        if bottom_coordinate in map and map[bottom_coordinate] == current_plant_type:
            touching_plant_types.append(bottom_coordinate)
        else:
            bottom_perimeter.append(current_coordinate)
        
        right_coordinate = (current_coordinate[0], current_coordinate[1] + 1)
        if right_coordinate in map and map[right_coordinate] == current_plant_type:
            touching_plant_types.append(right_coordinate)
        else:
            right_perimeter.append(current_coordinate)

        next_coordinates = [
            coord for coord in touching_plant_types 
            if coord not in visited and coord not in coordinates_to_check
        ]
        
        coordinates_to_check.extend(next_coordinates)
        perimeter += 4 - len(touching_plant_types)
        area += 1
        
    sides = calculate_sides(top_perimeter, left_perimeter, bottom_perimeter, right_perimeter)
 
    return visited, area, perimeter, sides

def calculate_sides(top_perimeter, left_perimeter, bottom_perimeter, right_perimeter):
    return len(return_non_touching_perimeter(top_perimeter, position="top")) + \
        len(return_non_touching_perimeter(left_perimeter, position="left")) + \
        len(return_non_touching_perimeter(bottom_perimeter, position="bottom")) + \
        len(return_non_touching_perimeter(right_perimeter, position="right"))

def return_non_touching_perimeter(perimeters, position):
    if position in ["top", "bottom"]:
        touching_perimeters = [(perimeter[0], perimeter[1] + 1) for perimeter in perimeters]
        return [perimeter for perimeter in perimeters if perimeter not in touching_perimeters]
    else:
        touching_perimeters = [(perimeter[0] + 1, perimeter[1]) for perimeter in perimeters]
        return [perimeter for perimeter in perimeters if perimeter not in touching_perimeters]

total_price_part_one, total_price_part_two = 0, 0
coordinates_to_check = [coord for coord in map.keys()]

while coordinates_to_check:
    current_coordinate = coordinates_to_check.pop(0)
    visited, area, perimeter, sides = walk_map(map, current_coordinate)
    total_price_part_one += area * perimeter
    total_price_part_two += area * sides
    coordinates_to_check = [coord for coord in coordinates_to_check if coord not in visited]
    
print(
    "Solution Part One:",
    total_price_part_one
)
print(
    "Solution Part Two:",
    total_price_part_two
)