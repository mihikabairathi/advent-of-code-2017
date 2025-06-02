def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def calculate_score(filename):
    input = read_file(filename)

    if input.count('{') == 1 and input.count('}') == 1:
        return 1
    
    # process ! marks
    new_input = ""
    i = 0
    while i < len(input):
        if input[i] != '!':
            new_input += input[i]
        else:
            i += 1
        i += 1
    input = new_input

    # delete garbage
    new_input = ""
    canceled_characters = 0
    i = 0
    processing_garbage = False
    while i < len(input):
        if input[i] != '<' and input[i] != '>' and not processing_garbage:
            new_input += input[i]
        elif input[i] == '<' and not processing_garbage:
            processing_garbage = True
        elif input[i] == '>' and processing_garbage:
            processing_garbage = False
        else:
            canceled_characters += 1
        i += 1
    input = new_input

    # compute score
    level_score = 0
    total_score = 0

    for c in input:
        if c == '{':
            level_score += 1
            total_score += level_score
        elif c == '}':
            level_score -= 1
    
    return total_score, canceled_characters

if __name__ == "__main__":
    print(calculate_score('day9.txt'))




