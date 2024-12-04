from collections import Counter

with open("data/puzzle_input_day_04.txt", "r") as file:
    word_grid = [list(line.strip()) for line in file]

def create_padded_word_grid(word_grid, padding_size):
    word_grid_size = len(word_grid)
    padded_word_grid = []

    for _ in range(padding_size):
        word_grid.insert(0, ['.'] * word_grid_size)

    for _ in range(padding_size):
        word_grid.append([ '.' ] * word_grid_size)

    for row in word_grid:
        padded_row = ['.'] * padding_size + row + ['.'] * padding_size
        padded_word_grid.append(padded_row)

    return padded_word_grid

padded_word_grid = create_padded_word_grid(word_grid, padding_size=3)
padded_word_grid_size = len(padded_word_grid)

x_location_list = [(i, j) for i in range(padded_word_grid_size) for j in range(padded_word_grid_size) if padded_word_grid[i][j] == 'X']
xmas_count = 0
word_to_check = "XMAS"

for x_location in x_location_list:  
    x, y = x_location

    ## unsure about correctness of directions
    word_length = len(word_to_check)

    xmas_count += "".join(padded_word_grid[x][y+1] for i in range(word_length)) == word_to_check ## right
    xmas_count += "".join(padded_word_grid[x][y-1] for i in range(word_length)) == word_to_check ## left
    xmas_count += "".join(padded_word_grid[x-i][y] for i in range(word_length)) == word_to_check ## top
    xmas_count += "".join(padded_word_grid[x+i][y] for i in range(word_length)) == word_to_check ## bottom

    xmas_count += "".join(padded_word_grid[x-i][y+i] for i in range(word_length)) == word_to_check ## top right
    xmas_count += "".join(padded_word_grid[x+i][y+i] for i in range(word_length)) == word_to_check ## bottom right
    xmas_count += "".join(padded_word_grid[x+i][y-i] for i in range(word_length)) == word_to_check ## top left
    xmas_count += "".join(padded_word_grid[x-i][y-i] for i in range(word_length)) == word_to_check ## bottom left

print("Solution Part One:", xmas_count)

m_location_list = [(i, j) for i in range(padded_word_grid_size) for j in range(padded_word_grid_size) if padded_word_grid[i][j] == 'M']
word_to_check = "MAS"

mas_center_locations = []

for m_location in m_location_list:  
    x, y = m_location

    word_length = len(word_to_check)

    word = "".join(padded_word_grid[x-i][y+i] for i in range(word_length))
    if word == word_to_check:
        mas_center_locations.append((x-1, y+1))

    word = "".join(padded_word_grid[x-i][y-i] for i in range(word_length))
    if word == word_to_check:
        mas_center_locations.append((x-1, y-1))

    word = "".join(padded_word_grid[x+i][y-i] for i in range(word_length))
    if word == word_to_check:
        mas_center_locations.append((x+1, y-1))

    word = "".join(padded_word_grid[x+i][y+i] for i in range(word_length))
    if word == word_to_check:
        mas_center_locations.append((x+1, y+1))

duplicates = Counter(mas_center_locations)
print("Solution Part Two:", sum(count - 1 for count in duplicates.values() if count > 1))
