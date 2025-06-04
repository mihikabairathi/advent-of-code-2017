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
    seen = dict()
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    i = 0
    while i < times:
        programs = perform_dance(programs, instructions)
        prg_str = ''.join(programs)
        
        if prg_str in seen:
            diff = i - seen[prg_str]
            i += ((1000000000 - i)//diff)*diff + 1
        else:
            seen[''.join(programs)] = i
            i += 1

    return ''.join(programs)

if __name__ == "__main__":
    print(simulate_dances('day16.txt'))