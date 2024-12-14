import re
from collections import defaultdict
import math

with open("data/puzzle_input_day_14.txt", "r") as f:
    robots = f.read().splitlines()

ROOM_WIDTH = 101
ROOM_HEIGHT = 103

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

        self.room_width = ROOM_WIDTH
        self.room_height = ROOM_HEIGHT
        self.quadrant = self.determine_quadrant()

    def move(self, n_seconds):
        self.position = (
            (self.velocity[0] * n_seconds + self.position[0]) % self.room_width,
            (self.velocity[1] * n_seconds + self.position[1]) % self.room_height
        )
        self.quadrant = self.determine_quadrant()

    def determine_quadrant(self):
        return "".join([
            "X" if self.position[0] == self.room_width // 2 else "0" if self.position[0] < self.room_width // 2 else "1",
            "X" if self.position[1] == self.room_height // 2 else "0" if self.position[1] < self.room_height // 2 else "1",
        ])

list_of_robots = [
    Robot(
        position=(nums[0], nums[1]),
        velocity=(nums[2], nums[3])
    ) for nums in [
        [int(num) for num in re.findall(r'-?\d+', robot)]
        for robot in robots
    ]
]

def print_grid(coordinates, width=ROOM_WIDTH, height=ROOM_HEIGHT):
    grid = [['.'] * width for _ in range(height)]

    for x, y in coordinates:
        grid[y][x] = '#'
    
    for y in range(height):
        print(''.join(grid[y]))

def group_horizontal_adjacents(coordinates):
    sorted_coords = sorted(coordinates, key=lambda p: (p[1], p[0]))
    
    groups = []
    current_group = []
    
    for i in range(len(sorted_coords)):
        current = sorted_coords[i]
        
        if not current_group:
            current_group.append(current)
        else:
            last = current_group[-1]
            if (last[1] == current[1] and  abs(last[0] - current[0]) == 1):
                current_group.append(current)
            else:
                groups.append(current_group)
                current_group = [current]
    
    return groups

quadrant_counts = defaultdict(int)

for robot in list_of_robots:
    robot.move(100)
    quadrant_counts[robot.quadrant] += 1
            
print(
    "Solution Part One:",
    math.prod([
        quadrant_counts[quadrant]
        for quadrant in ["00", "01", "10", "11"]
    ])
)

for n_seconds in range(101, 10000):
    for robot in list_of_robots:
        robot.move(1)

    coords = [ r.position for r in list_of_robots ]
    groups = group_horizontal_adjacents(coords)
    groups = [ group for group in groups if len(group) > 10 ]

    if len(groups) > 10:
        print(
            "Solution Part Two:",
            n_seconds
        )
        print_grid(coords)
        break

    

