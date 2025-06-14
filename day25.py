def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_machine_instructions(filename):
    content = read_file(filename).splitlines()
    starting_state = content[0][-2]
    num_iters = int(content[1].split()[-2])

    content = content[3:]
    instructions = {}

    while content != []:
        instructions[content[0][-2]] = {}

        instructions[content[0][-2]][content[1][-2]] = {}
        instructions[content[0][-2]][content[1][-2]]['new_value'] = content[2][-2]
        instructions[content[0][-2]][content[1][-2]]['dx'] = 1 if content[3][-3:] == 'ht.' else -1
        instructions[content[0][-2]][content[1][-2]]['new_state'] = content[4][-2]

        instructions[content[0][-2]][content[5][-2]] = {}
        instructions[content[0][-2]][content[5][-2]]['new_value'] = content[6][-2]
        instructions[content[0][-2]][content[5][-2]]['dx'] = 1 if content[7][-3:] == 'ht.' else -1
        instructions[content[0][-2]][content[5][-2]]['new_state'] = content[8][-2]

        content = content[10:]
    
    return instructions, starting_state, num_iters

def run_turing_machine(filename):
    instructions, state, num_iters = generate_machine_instructions(filename)
    tape = {0: '0'}
    position = 0
    for i in range(num_iters):
        state_instructions = instructions[state]
        value_instructions = state_instructions[tape.get(position, '0')]
        tape[position] = value_instructions['new_value']
        position += value_instructions['dx']
        state = value_instructions['new_state']

    checksum = 0
    for pos in tape:
        if tape[pos] == '1':
            checksum += 1

    return checksum

if __name__ == '__main__':
    print(run_turing_machine('day25.txt'))

