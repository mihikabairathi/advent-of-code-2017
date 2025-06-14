def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def flip_mapping(input):
    new_input = [[0]*len(input) for i in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input)):
            new_input[i][len(input) - j - 1] = input[i][j]

    return new_input

def rotate_mapping(input):
    new_input = [[0]*len(input) for i in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input)):
            new_input[j][len(input) - 1 - i] = input[i][j]

    return new_input
    
def generate_variations(input):
    all_inputs = []
    for i in range(4):
        all_inputs.append(input)
        all_inputs.append(flip_mapping(input))
        input = rotate_mapping(input)

    return all_inputs

def compact_mapping(input):
    input_compact = ""
    for row in input:
        input_compact += ''.join(row) + '/'

    return input_compact[:-1]

def expand_mapping(input_string):
    input = []
    for row in input_string.split('/'):
        input.append(list(row))

    return input
    
def generate_mappings(filename):
    mappings = dict()
    for line in read_file(filename).splitlines():
        split_line = line.split(" => ")
        original_input_compact, output = split_line[0], split_line[1]

        original_input = expand_mapping(original_input_compact)

        all_inputs = generate_variations(original_input)
        for input in all_inputs:
            mappings[compact_mapping(input)] = output

    return mappings

def create_fractal(filename, num_iters):
    mappings = generate_mappings(filename)
    input = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]

    for i in range(num_iters):
        div_num = 2 if len(input) % 2 == 0 else 3

        num_new_squares = len(input) // div_num
        new_length = num_new_squares * (div_num + 1)
        new_input = [[0]*new_length for i in range(new_length)]

        for j in range(num_new_squares):
            for k in range(num_new_squares):
                block = [input[(j*div_num) + n][k * div_num: (k+1) * div_num ] for n in range(div_num)]
                block_compact = compact_mapping(block)
                output_compact = mappings[block_compact]
                output_block = expand_mapping(output_compact)
                for a in range(len(output_block)):
                    for b in range(len(output_block)):
                        new_input[j * (div_num+1) + a][k * (div_num+1) + b] = output_block[a][b]

        input = new_input

    count = 0
    for row in input:
        for col in row:
            if col == '#':
                count += 1

    return count

if __name__ == '__main__':
    print(create_fractal('day21.txt', 18))