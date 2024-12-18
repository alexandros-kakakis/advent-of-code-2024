from collections import deque

with open("data/puzzle_input_day_18.txt", "r") as f:
    list_of_byte_positions = [ tuple(map(int, i.split(","))) for i in f.read().splitlines()]


def find_shortest_path(list_of_byte_positions, grid_size):
    memory_space = {(x,y): '.' for x in range(grid_size + 1) for y in range(grid_size + 1)}
    for byte_position in list_of_byte_positions:
        memory_space[byte_position] = '#'
    
    start_position = (0,0)
    end_position = (grid_size,grid_size)
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    queue = deque([(start_position[0], start_position[1], [start_position])])
    
    visited = {start_position}
    
    while queue:
        row, col, path = queue.popleft()
        
        if (row, col) == end_position:
            return path
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            new_pos = (new_row, new_col)
            
            if (new_pos in memory_space and 
                memory_space[new_pos] == "." and 
                new_pos not in visited):
                
                visited.add(new_pos)
                new_path = path + [new_pos]
                queue.append((new_row, new_col, new_path))
    
    return []

print(
    "Solution Part One:",
    len(find_shortest_path(list_of_byte_positions[:1024], grid_size=70)) - 1
)

number_of_bytes = 1024
while find_shortest_path(list_of_byte_positions[:number_of_bytes], grid_size=70):
    number_of_bytes += 1

print(
    "Solution Part Two:",
    ",".join(map(str, list_of_byte_positions[number_of_bytes-1]))
)