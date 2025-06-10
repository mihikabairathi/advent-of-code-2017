def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_grid(filename):
    grid = []
    for line in read_file(filename).splitlines():
        grid_line = []
        for c in line:
            grid_line.append(c)

        grid.append(grid_line)

    return grid

def find_path(filename):
    grid = generate_grid(filename)
    x, y = 0, grid[0].index('|')
    path = []
    dx, dy = 1, 0 # going downwards
    steps = 0

    while True:
        if grid[x][y].isalpha():
            path.append(grid[x][y])
            x += dx
            y += dy
        elif grid[x][y] in ['|', '-']:
            x += dx
            y += dy
        else:
            possible_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            found_path = False
            for dir in possible_dirs:
                if (x + dir[0], y + dir[1]) == (x - dx, y - dy):
                    continue
                elif 0 > x + dir[0] or len(grid) <= x + dir[0] or 0 > y + dir[1] or len(grid[0]) <= y + dir[1]:
                    continue
                elif grid[x + dir[0]][y + dir[1]] == ' ':
                    continue
                elif grid[x + dir[0]][y + dir[1]] == '|':
                    found_path = True
                    dx, dy = dir
                    break
                elif grid[x + dir[0]][y + dir[1]] == '-':
                    found_path = True
                    dx, dy = dir
                    break
            if not found_path:
                break

            x += dx
            y += dy
        steps += 1

    return ''.join(path), steps

if __name__ == "__main__":
    print(find_path('day19.txt'))