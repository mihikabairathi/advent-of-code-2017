def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_tower(filename):
    tower = dict()
    for line in read_file(filename).splitlines():
        line_list = line.split()
        name = line_list[0]
        weight = int(line_list[1][1:-1])
        tower[name] = {'weight': weight, 'children': []}

        if len(line_list) > 2:
            children = line_list[3:]
            children = [child.strip(',') for child in children]
            tower[name]['children'] = children

    return tower

def calculate_bottom_disk(tower):
    bottom_name = None
    bottom_weight = None
    potential_bottoms = set()
    for name in tower:
        if tower[name]['children'] != []:
            potential_bottoms.add(name)

    while len(potential_bottoms) != 1:
        for name in tower:
            for child in tower[name]['children']:
                potential_bottoms.discard(child)

    return potential_bottoms.pop()

def calculate_weight(tower, name):
    weight = tower[name]['weight']
    for child in tower[name]['children']:
        weight += calculate_weight(tower, child)
    return weight

def correct_weight(tower, bottom, expected_weight=None):
    if tower[bottom]['children'] == []:
        return expected_weight

    weights = dict()
    for child in tower[bottom]['children']:
        child_weight = calculate_weight(tower, child)
        weights[child_weight] = weights.get(child_weight, []) + [child]
    
    odd_child = None
    new_expected_weight = None
    for weight in weights:
        if len(weights[weight]) == 1:
            odd_child = weights[weight][0]
        if len(weights[weight]) > 1:
            new_expected_weight = weight

    if new_expected_weight is None:
        child1 = tower[bottom]['children'][0]
        child2 = tower[bottom]['children'][1]
        return correct_weight(tower, child1, calculate_weight(tower, child2)) or correct_weight(tower, child2, calculate_weight(tower, child1))
    elif odd_child is None:
        return expected_weight - new_expected_weight*len(tower[bottom]['children'])
    else:
        return correct_weight(tower, odd_child, new_expected_weight)
    
if __name__ == "__main__":
    tower = generate_tower("day7.txt")
    print(correct_weight(tower, calculate_bottom_disk(tower)))