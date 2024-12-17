with open("data/puzzle_input_day_15.txt", "r") as f:
    original_map, moves = f.read().split('\n\n')

moves = [move for move in moves if move != '\n']

map = {
    (x, y): char 
    for y, line in enumerate(original_map.split('\n'))
    for x, char in enumerate(line.strip())
}

def move(map, x, y, direction):
    dx, dy = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }[direction]
    
    next_x, next_y = x + dx, y + dy
    
    if (next_x, next_y) not in map or map[(next_x, next_y)] == '#':
        return x, y
        
    if map[(next_x, next_y)] == '.':
        return next_x, next_y
        
    curr_x, curr_y = next_x, next_y
    while (curr_x + dx, curr_y + dy) in map:
        if map[(curr_x + dx, curr_y + dy)] == '#':
            break
        if map[(curr_x + dx, curr_y + dy)] == '.':
            map[(curr_x + dx, curr_y + dy)] = 'O'
            map[(next_x, next_y)] = '.'
            return next_x, next_y
        curr_x += dx
        curr_y += dy
    
    return x, y

def print_map(map):
    max_y = max(coord[1] for coord in map.keys())
    max_x = max(coord[0] for coord in map.keys())
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            line += map.get((x,y), " ")
        print(line)

x, y = [i for i in map if map[i] == '@'][0]
map[(x, y)] = '.'  # Remove robot from map

for move_direction in moves:

    new_x, new_y = move(map, x, y, move_direction)
    x, y = new_x, new_y

box_locations = [i for i in map if map[i] == 'O']
gps_coordinates = [100* y + x for x, y in box_locations]

print(
    "Solution Part One:",
    sum(gps_coordinates)
)

### Part Two ###

with open("data/puzzle_input_day_15.txt", "r") as f:
    map, moves = f.read().split('\n\n')

_widened_map = {
    (x, y): char_pair 
    for y, line in enumerate(original_map.split('\n'))
    for x, char in enumerate(line.strip())
    for x, char_pair in [(x*2, '#' * 2 if char == '#' else '..' if char == '.' else '[]' if char == 'O' else '@.')]
}

widened_map = {}
for (x, y), char_pair in _widened_map.items():
    widened_map[(x, y)] = char_pair[0]
    widened_map[(x+1, y)] = char_pair[1]

def move_widened_map(map, x, y, direction):
    dx, dy = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }[direction]
    
    next_x, next_y = x + dx, y + dy
    
    if (next_x, next_y) not in map or map[(next_x, next_y)] == '#':
        return x, y
        
    if map[(next_x, next_y)] == '.':
        return next_x, next_y
        
    ## TODO: adjust for widened map
    curr_x, curr_y = next_x, next_y
    while (curr_x + dx, curr_y + dy) in map:
        if map[(curr_x + dx, curr_y + dy)] == '#':
            break
        if map[(curr_x + dx, curr_y + dy)] == '.':
            map[(curr_x + dx, curr_y + dy)] = 'O'
            map[(next_x, next_y)] = '.'
            return next_x, next_y
        curr_x += dx
        curr_y += dy
    
    return x, y

x, y = [i for i in widened_map if widened_map[i] == '@'][0]
print("\nInitial state:")
print_map(widened_map)  # Print initial state
widened_map[(x, y)] = '.'  # Remove robot from map

for move_direction in moves:
    print(f"\nAfter moving {move_direction}:")
    new_x, new_y = move_widened_map(widened_map, x, y, move_direction)
    # Add robot position to map temporarily for visualization
    widened_map[(x, y)] = '@'
    print_map(widened_map)
    # Remove robot position again
    widened_map[(x, y)] = '.'
    x, y = new_x, new_y

box_locations = [i for i in widened_map if widened_map[i] == 'O']
gps_coordinates = [100* y + x for x, y in box_locations]

print(
    "\nSolution Part Two:",
    sum(gps_coordinates)
)