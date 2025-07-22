def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def get_instructions(filename):
    return read_file(filename).split(',')

def perform_dance(programs, instructions):
    for instruction in instructions:
        if instruction[0] == 's':
            size = int(instruction[1:])
            programs = programs[-size:] + programs[:-size]
        elif instruction[0] == 'x':
            moves = instruction[1:].split('/')
            pos1, pos2 = int(moves[0]), int(moves[1])
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        elif instruction[0] == 'p':
            moves = instruction[1:].split('/')
            p1, p2 = moves[0], moves[1]
            pos1, pos2 = programs.index(p1), programs.index(p2)
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]

    return programs

def simulate_dances(filename, times=1000000000):
    instructions = get_instructions(filename)
    seen = {}
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    MAX_ITERATIONS = 1000000  # Safety limit

    i = 0
    while i < times and i < MAX_ITERATIONS:
        programs = perform_dance(programs, instructions)
        prg_tuple = tuple(programs)
        
        if prg_tuple in seen:
            cycle_length = i - seen[prg_tuple]
            remaining = times - i - 1
            if cycle_length > 0:
                # Skip full cycles
                i += (remaining // cycle_length) * cycle_length
        else:
            seen[prg_tuple] = i

        i += 1

    if i >= MAX_ITERATIONS:
        raise Exception(f"Exceeded maximum iterations ({MAX_ITERATIONS}) without completing simulation")

    return ''.join(programs)

if __name__ == "__main__":
    print(simulate_dances('day16.txt'))
