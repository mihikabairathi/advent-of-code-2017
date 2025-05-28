def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_instructions(filename):
    instructions = []
    for line in read_file(filename).splitlines():
        instruction = dict()
        line = line.split()

        instruction["register"] = line[0]
        if line[1] == "inc":
            instruction["to_add"] = int(line[2])
        else:
            instruction["to_add"] = -int(line[2])
        instruction["condition_register"] = line[4]
        instruction["condition"] = line[5]
        instruction["condition_value"] = int(line[6])

        instructions.append(instruction)

    return instructions

def condition_met(registers, instruction):
    register_value = registers.get(instruction['condition_register'], 0)
    if instruction['condition'] == '==':
        return register_value == instruction['condition_value']
    elif instruction['condition'] == '!=':
        return register_value != instruction['condition_value']
    elif instruction['condition'] == '<':
        return register_value < instruction['condition_value']
    elif instruction['condition'] == '<=':
        return register_value <= instruction['condition_value']
    elif instruction['condition'] == '>':
        return register_value > instruction['condition_value']
    elif instruction['condition'] == '>=':
        return register_value >= instruction['condition_value']

def execute_instructions(filename):
    instructions = generate_instructions(filename)
    registers = dict()
    max_value = 0

    for instruction in instructions:
        if condition_met(registers, instruction):
            registers[instruction['register']] = registers.get(instruction['register'], 0) + instruction['to_add']
            max_value = max(registers[instruction['register']], max_value)

    return max_value

if __name__ == "__main__":
    print(execute_instructions("day8.txt"))

