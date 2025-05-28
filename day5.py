def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_maze(filename):
    maze = []
    for step in read_file(filename).splitlines():
        maze.append(int(step))

    return maze

def steps_in_maze(filename):
    maze = generate_maze(filename)

    position = 0
    num_steps = 0

    while True:
        if position >= len(maze):
            return num_steps
        
        new_position = position + maze[position]
        num_steps += 1
        if maze[position] >= 3:
            maze[position] -= 1
        else:
            maze[position] += 1

        position = new_position

if __name__ == "__main__":
    print(steps_in_maze("day5.txt"))
        

