with open("data/puzzle_input_day_10.txt", "r") as file:
    map = {(i,j): int(char) for i, line in enumerate(file) for j, char in enumerate(line.strip())}


def calculate_score(map, trailhead_coordinate, keep_going=False):
    coordinates_to_check = [trailhead_coordinate]
    score, visited = 0, set()
    while coordinates_to_check:
        current_coordinate = coordinates_to_check.pop(0)
        
        if current_coordinate in visited and not keep_going:
            continue
            
        current_height = map[current_coordinate]
        visited.add(current_coordinate)
        
        if current_height == 9:
            score += 1
            continue
            
        candidate_coordinates = [
            (current_coordinate[0] + dx, current_coordinate[1] + dy) 
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)] 
            if (current_coordinate[0] + dx, current_coordinate[1] + dy) in map
        ]
        candidate_coordinates = [
            coord for coord in candidate_coordinates 
            if map[coord] == (current_height + 1) and coord not in visited
        ]
        
        coordinates_to_check.extend(candidate_coordinates)
        
    return score

trailhead_coordinates = [key for key in map.keys() if map[key] == 0]

sum_of_scores, sum_of_ratings = 0, 0
for trailhead_coordinate in trailhead_coordinates:
    sum_of_scores += calculate_score(map, trailhead_coordinate)
    sum_of_ratings += calculate_score(map, trailhead_coordinate, keep_going=True)

print(
    "Solution Part One:",
    sum_of_scores
)

print(
    "Solution Part Two:",
    sum_of_ratings
)