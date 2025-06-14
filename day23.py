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

def run_program(filename, registers={}):
    instructions = generate_instructions(filename)
    num_mult = 0

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
        elif operation == 'sub':
            registers[register] = registers.get(register, 0) - value
        elif operation == 'mul':
            registers[register] = registers.get(register, 0) * value
            num_mult += 1
        elif operation == 'jnz' and ((registers.get(register, 0) != 0) or (register.isnumeric() and int(register) != 0)):
            i += value - 1

        i += 1

    return num_mult

def run_program_simplified(a, c, k):
    h = 0
    for b in range(a, c, k):
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break
    return h

if __name__ == "__main__":
    print(run_program('day23.txt')) 
    print(run_program_simplified(101, 202, 2))