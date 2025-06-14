import day10

def row_binary_count_used(input_string, row_num):
    row_string = f'{input_string}-{row_num}'
    hex_hash = day10.create_hash(row_string)
    binary_string = ""
    for h in hex_hash:
        new_string = bin(int(h, 16))[2:]
        new_string = '0'*(4 - len(new_string)) + new_string
        binary_string += new_string

    return binary_string.count('1')

def count_used(input_string):
    total_used = 0
    for i in range(128):
        total_used += row_binary_count_used(input_string, i)
    return total_used

def find_group(grid, pos, seen):
    x, y = pos
    if grid[x][y] != '1':
        return 
    
    seen.add(pos)
    grid[x][y] = '0'
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        new_pos = (x + dx, y + dy)
        if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and new_pos not in seen:
            find_group(grid, new_pos, seen)

def create_grid(input_string):
    grid = []
    for i in range(128):
        row_string = f'{input_string}-{i}'
        hex_hash = day10.create_hash(row_string)
        binary_list = []
        for h in hex_hash:
            new_string = bin(int(h, 16))[2:]
            new_string = '0'*(4 - len(new_string)) + new_string
            binary_list.extend(list(new_string))
        grid.append(binary_list)

    return grid

def count_groups(input_string):
    grid = create_grid(input_string)
    seen = set()
    group_count = 0
    for i in range(128):
        for j in range(128):
            if (i, j) not in seen and grid[i][j] == '1':
                find_group(grid, (i, j), seen)
                group_count += 1

    return group_count
    
if __name__ == "__main__":
    print(count_used("flqrgnkx"))
    print(count_groups("flqrgnkx"))
