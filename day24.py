import copy

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_mappings(filename):
    mappings = {}
    for component in read_file(filename).splitlines():
        ends = component.split('/')
        first_end, second_end = int(ends[0]), int(ends[1])
        mappings[first_end] = mappings.get(first_end, set())
        mappings[first_end].add(second_end)
        mappings[second_end] = mappings.get(second_end, set())
        mappings[second_end].add(first_end)

    return mappings

def create_longest_bridge(mappings, starting_port):
    if starting_port not in mappings or len(mappings[starting_port]) == 0:
        return 0, ''
    elif len(mappings[starting_port]) == 1:
        last_comp = mappings[starting_port].pop()
        mappings[last_comp].discard(starting_port)
        new_strength, new_bridge = create_longest_bridge(mappings, last_comp)
        if new_bridge != '':
            new_bridge = '--' + new_bridge
        return starting_port + last_comp + new_strength, f'{starting_port}/{last_comp}{new_bridge}'
    else:
        max_strength = None
        max_bridge = None
        max_mappings = dict()
        max_component = None
        for next_component in mappings[starting_port]:
            new_mappings = copy.deepcopy(mappings)
            new_mappings[starting_port].remove(next_component)
            new_mappings[next_component].discard(starting_port)
            potential_strength, potential_bridge = create_longest_bridge(new_mappings, next_component)

            if max_strength == None or (potential_bridge.count('--') > max_bridge.count('--')) or (potential_bridge.count('--') == max_bridge.count('--') and potential_strength > max_strength):
                max_strength = potential_strength
                if potential_bridge != '':
                    potential_bridge = '--' + potential_bridge
                max_bridge = f'{starting_port}/{next_component}{potential_bridge}'
                max_mappings = new_mappings
                max_component = next_component

        for m in mappings:
            mappings[m] = max_mappings.get(m, set())

        return max_strength + starting_port + max_component, max_bridge

def create_strongest_bridge(mappings, starting_port):
    if starting_port not in mappings or len(mappings[starting_port]) == 0:
        return 0, ''
    elif len(mappings[starting_port]) == 1:
        last_comp = mappings[starting_port].pop()
        mappings[last_comp].discard(starting_port)
        new_strength, new_bridge = create_strongest_bridge(mappings, last_comp)
        if new_bridge != '':
            new_bridge = '--' + new_bridge
        return starting_port + last_comp + new_strength, f'{starting_port}/{last_comp}{new_bridge}'
    else:
        max_strength = None
        max_bridge = None
        max_mappings = dict()
        max_component = None
        for next_component in mappings[starting_port]:
            new_mappings = copy.deepcopy(mappings)
            new_mappings[starting_port].remove(next_component)
            new_mappings[next_component].discard(starting_port)
            potential_strength, potential_bridge = create_strongest_bridge(new_mappings, next_component)

            if max_strength == None or potential_strength > max_strength:
                max_strength = potential_strength
                if potential_bridge != '':
                    potential_bridge = '--' + potential_bridge
                max_bridge = f'{starting_port}/{next_component}--{potential_bridge}'
                max_mappings = new_mappings
                max_component = next_component

        for m in mappings:
            mappings[m] = max_mappings.get(m, set())

        return max_strength + starting_port + max_component, max_bridge
    
def find_strongest_bridge(filename):
    mappings = generate_mappings(filename)
    return create_strongest_bridge(mappings, 0)

def find_longest_bridge(filename):
    mappings = generate_mappings(filename)
    return create_longest_bridge(mappings, 0)
    
if __name__ == "__main__":
    print(find_strongest_bridge("day24.txt"))
    print(find_longest_bridge("day24.txt"))