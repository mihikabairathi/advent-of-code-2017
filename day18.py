def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_instructions(filename):
    instructions = []
    for line in read_file(filename).splitlines():
        line = line.split()
        instruction = dict()
        instruction['instruction'] = line[0]
        instruction['register'] = line[1]
        if len(line) == 3:
            instruction['value'] = line[2]
        instructions.append(instruction)

    return instructions

def update_program(instructions, i, registers, incoming, outgoing):
    instruction = instructions[i]
    operation = instruction['instruction']
    register = instruction['register']
    sent_value = False

    value = instruction.get('value', None)
    if value and value.isalpha():
        value = registers.get(value, 0)
    elif value:
        value = int(value)

    if operation == 'set':
        registers[register] = value
    elif operation == 'add':
        registers[register] = registers.get(register, 0) + value
    elif operation == 'mul':
        registers[register] = registers.get(register, 0) * value
    elif operation == 'mod':
        registers[register] = registers.get(register, 0) % max(1, value)
    elif operation == 'snd':
        outgoing.insert(0, registers.get(register, 0))
        sent_value = True
    elif operation == 'rcv':
        if incoming == []:
            return i, sent_value
        else:
            registers[register] = incoming.pop()
    elif operation == 'jgz' and ((registers.get(register, 0) > 0) or (register.isnumeric() and int(register) > 0)):
        i += value - 1

    return i + 1, sent_value

def real_duet(filename):
    instructions = generate_instructions(filename)
    registers_one = {'p': 0}
    registers_two = {'p': 1}
    incoming_one = []
    outgoing_one = []
    i = 0
    j = 0
    new_i = 0
    new_j = 0
    send_count_one = 0
    send_count_two = 0

    while (i >= 0 and i < len(instructions)) or (j >= 0 and j < len(instructions)):
        sent_value_one = False
        sent_value_two = False

        if i >= 0 and i < len(instructions):
            new_i, sent_value_one = update_program(instructions, i, registers_one, incoming_one, outgoing_one)
        if j >= 0 and j < len(instructions):
            new_j, sent_value_two = update_program(instructions, j, registers_two, outgoing_one, incoming_one)

        if i == new_i and j == new_j:
            break
        i = new_i
        j = new_j

        if sent_value_one:
            send_count_one += 1
        if sent_value_two:
            send_count_two += 1

    return send_count_two


def duet(filename):
    instructions = generate_instructions(filename)
    registers = {}
    last_played = 0

    i = 0
    while i < len(instructions) and i >= 0:
        instruction = instructions[i]
        operation = instruction['instruction']
        register = instruction['register']
        value = instruction.get('value', None)
        if value and value.isalpha():
            value = registers.get(value, 0)
        elif value:
            value = int(value)

        if operation == 'set':
            registers[register] = value
        elif operation == 'add':
            registers[register] = registers.get(register, 0) + value
        elif operation == 'mul':
            registers[register] = registers.get(register, 0) * value
        elif operation == 'mod':
            registers[register] = registers.get(register, 0) % max(1, value)
        elif operation == 'snd':
            last_played = registers.get(register, 0)
        elif operation == 'rcv' and registers.get(register, 0) != 0:
            return last_played
        elif operation == 'jgz' and (registers.get(register, 0) > 0):
            i += value - 1

        i += 1

    return last_played

if __name__ == "__main__":
    print(duet('day18.txt')) 
    print(real_duet('day18.txt'))
