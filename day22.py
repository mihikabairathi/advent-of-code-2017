def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_initial_grid(filename):
    grid = dict()
    content = read_file(filename).splitlines()
    for i in range(len(content)):
        for j in range(len(content[i])):
            grid[(i, j)] = content[i][j]

    return grid, len(content) // 2, len(content[0]) // 2

def simulate_bursts(num_bursts, filename):
    grid, x, y = generate_initial_grid(filename)
    left_mapping = {(1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (-1, 0), (0, -1): (1, 0)}
    right_mapping = {(0, 1): (1, 0), (0, -1): (-1, 0), (-1, 0): (0, 1), (1, 0): (0, -1)}
    direction = (-1, 0)
    infected_bursts = 0

    for _ in range(num_bursts):
        grid[(x, y)] = grid.get((x, y), '.')
        direction = left_mapping[direction] if grid[(x, y)] == '.' else right_mapping[direction]
        grid[(x, y)] = '#' if grid[(x, y)] == '.' else '.'
        if grid[(x, y)] == '#':
            infected_bursts += 1

        (x, y) = (direction[0] + x, direction[1] + y)

    return infected_bursts

def simulate_bursts_evolved(num_bursts, filename):
    grid, x, y = generate_initial_grid(filename)
    left_mapping = {(1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (-1, 0), (0, -1): (1, 0)}
    right_mapping = {(0, 1): (1, 0), (0, -1): (-1, 0), (-1, 0): (0, 1), (1, 0): (0, -1)}
    direction = (-1, 0)
    infected_bursts = 0

    for _ in range(num_bursts):
        grid[(x, y)] = grid.get((x, y), '.')
        if grid[(x, y)] == '.':
            direction = left_mapping[direction]
        elif grid[(x, y)] == '#':
            direction = right_mapping[direction]
        elif grid[(x, y)] == 'F':
            direction = left_mapping[left_mapping[direction]]

        state_mapping = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}
        grid[(x, y)] = state_mapping[grid[(x, y)]]
        if grid[(x, y)] == '#':
            infected_bursts += 1

        (x, y) = (direction[0] + x, direction[1] + y)

    return infected_bursts

if __name__ == '__main__':
    print(simulate_bursts(10000, 'day22.txt'))
    print(simulate_bursts_evolved(10000000, 'day22.txt'))

        

    