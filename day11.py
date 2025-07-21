def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_instructions(filename):
    return read_file(filename).split(',')

def execute_instructions_with_max(filename, instructions=None):
    if instructions is None:
        instructions = generate_instructions(filename)
    max_steps_ever = 0

    positions_moved = {'n': 0, 's': 0, 'ne': 0, 'sw': 0, 'se': 0, 'nw': 0}
    for instruction in instructions:
        positions_moved[instruction] += 1

        changes_made = True
        while changes_made:
            changes_made = False

            s_nw_becomes_sw_count = min(positions_moved['s'], positions_moved['nw'])
            if s_nw_becomes_sw_count > 0:
                positions_moved['sw'] += s_nw_becomes_sw_count
                positions_moved['s'] -= s_nw_becomes_sw_count
                positions_moved['nw'] -= s_nw_becomes_sw_count
                changes_made = True

            s_ne_becomes_se_count = min(positions_moved['s'], positions_moved['ne'])
            if s_ne_becomes_se_count > 0:
                positions_moved['se'] += s_ne_becomes_se_count
                positions_moved['s'] -= s_ne_becomes_se_count
                positions_moved['ne'] -= s_ne_becomes_se_count
                changes_made = True

            s_n_count = min(positions_moved['s'], positions_moved['n'])
            if s_n_count > 0:
                positions_moved['n'] -= s_n_count
                positions_moved['s'] -= s_n_count
                changes_made = True

            n_sw_becomes_nw_count = min(positions_moved['n'], positions_moved['sw'])
            if n_sw_becomes_nw_count > 0:
                positions_moved['nw'] += n_sw_becomes_nw_count
                positions_moved['n'] -= n_sw_becomes_nw_count
                positions_moved['sw'] -= n_sw_becomes_nw_count
                changes_made = True

            n_se_becomes_ne_count = min(positions_moved['n'], positions_moved['se'])
            if n_se_becomes_ne_count > 0:
                positions_moved['ne'] += n_se_becomes_ne_count
                positions_moved['n'] -= n_se_becomes_ne_count
                positions_moved['se'] -= n_se_becomes_ne_count
                changes_made = True

            ne_sw_count = min(positions_moved['ne'], positions_moved['sw'])
            if ne_sw_count > 0:
                positions_moved['ne'] -= ne_sw_count
                positions_moved['sw'] -= ne_sw_count
                changes_made = True

            ne_nw_becomes_n_count = min(positions_moved['ne'], positions_moved['nw'])
            if ne_nw_becomes_n_count > 0:
                positions_moved['n'] += ne_nw_becomes_n_count
                positions_moved['ne'] -= ne_nw_becomes_n_count
                positions_moved['nw'] -= ne_nw_becomes_n_count
                changes_made = True

            se_sw_becomes_s_count = min(positions_moved['se'], positions_moved['sw'])
            if se_sw_becomes_s_count > 0:
                positions_moved['s'] += se_sw_becomes_s_count
                positions_moved['se'] -= se_sw_becomes_s_count
                positions_moved['sw'] -= se_sw_becomes_s_count
                changes_made = True

            se_nw_count = min(positions_moved['se'], positions_moved['nw'])
            if se_nw_count > 0:
                positions_moved['se'] -= se_nw_count
                positions_moved['nw'] -= se_nw_count
                changes_made = True
        
        max_steps_ever = max(max_steps_ever, sum(positions_moved.values()))
    return max_steps_ever

def execute_instructions(filename, instructions=None):
    if instructions is None:
        instructions = generate_instructions(filename)

    positions_moved = {'n': 0, 's': 0, 'ne': 0, 'sw': 0, 'se': 0, 'nw': 0}
    for instruction in instructions:
        positions_moved[instruction] += 1

    # Optimized movement calculation using vector math
    x = (positions_moved['ne'] + positions_moved['se'] -
         positions_moved['nw'] - positions_moved['sw'])
    y = (positions_moved['n'] + positions_moved['ne'] + positions_moved['nw'] -
         positions_moved['s'] - positions_moved['se'] - positions_moved['sw'])
    z = positions_moved['n'] + positions_moved['s']
    
    # Calculate distance using cube coordinates
    distance = (abs(x) + abs(y) + abs(z)) // 2
    return distance

if __name__ == "__main__":
    print(execute_instructions("whatever", ['ne', 'ne', 'ne']))
    print(execute_instructions("whatever", ['ne', 'ne', 'sw', 'sw']))
    print(execute_instructions("whatever", ['ne', 'ne', 's', 's']))
    print(execute_instructions("whatever", ['se', 'sw', 'se', 'sw', 'sw']))
    print(execute_instructions("day11.txt"))

    print(execute_instructions_with_max("whatever", ['ne', 'ne', 'ne']))
    print(execute_instructions_with_max("whatever", ['ne', 'ne', 'sw', 'sw']))
    print(execute_instructions_with_max("whatever", ['ne', 'ne', 's', 's']))
    print(execute_instructions_with_max("whatever", ['se', 'sw', 'se', 'sw', 'sw']))
    print(execute_instructions_with_max("day11.txt"))
